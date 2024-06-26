from calendar import month
from cgi import test
from email.mime import application
from lib2to3.pgen2 import token
import re
import smtplib
import os
from email.message import EmailMessage
from requests import session
from sqlalchemy.orm import load_only
import os
from flask import Flask, request, jsonify, make_response , render_template
import sqlalchemy as db
from sqlalchemy import engine_from_config, insert, null, text, update
import jwt
import ssl
import datetime
import os
import json
from prettytable import PrettyTable
from functools import wraps
import bcrypt
from password_generator import PasswordGenerator
import datetime
import time
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# CROSS-ORIGIN RESOURCE SHARING must be provided to allow different domains to pass data to each other.
CORS(app, resources={r"*": {"origins": "*"}})

# import "the secret key" for jwt.token encode/decode procedures.
app.config['SECRET_KEY'] = os.environ.get('JAP_API_SECRET_KEY')

# provide the email and password for the system's automated email
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')  

# this is used initially to test for the email targeted
EMAIL_ADMIN_RECEIVER = os.environ.get('EMAIL_ADMIN_RECEIVER')
EMAIL_APPLICANT_RECEIVER = os.environ.get('EMAIL_APPLICANT_RECEIVER')

# the directory path for the resume files to be submitted via HTTP POST Request.
upload_path = os.environ.get('RESUME_UPLOAD_PATH')

# create the engine to prepare and call specify the database where it will get from.
# the variable in db.create_engine must be mysql://<username>:<password>@<hostname>:<port_number>/<schema_name>
engine = db.create_engine(os.environ.get('JAP_DB_URL'))

# use to generate randomized password
pwo = PasswordGenerator()
pwo.excludeschars = "$%^ " 
pwo.minlen = 8
pwo.maxlen = 12

# this is the middleware for the API to prevent users without credentials to interact with the data.
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({'Message':'Token is missing'}), 401

        conn = engine.connect()
        metadata = db.MetaData()

        blacklisted_table = db.Table('jwt_blacklist', metadata, autoload=True, autoload_with=engine)
        blacklisted_token = conn.execute(db.select(blacklisted_table).where(blacklisted_table.columns.blacklisted==token)).fetchall()

        if blacklisted_token: 
            return jsonify({'Message':'Token is invalid, please re-login into the system to continue.'}), 401

        applicants = db.Table('applicant_information', metadata, autoload=True, autoload_with=engine)

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"])
            current_user = conn.execute(db.select(applicants).where(applicants.columns.applicant_id==data['applicant_id'])).fetchall()
        except:
            conn.close()
            return jsonify({'Message':'Token is invalid'}), 401

        conn.close()
        return f(current_user,*args, **kwargs)

    return decorated

# rechecked
@app.route('/login', methods=['POST'])
def login():

    data = { 'username': request.json['username'], 'password': request.json['password']}    # get the information from front-end login section.

    # print('This is the data submitted from front-end', data)

    conn = engine.connect()
    metadata = db.MetaData()
    # print(data,flush=True)
    # applicants = db.Table('applicant_information', metadata, autoload=True, autoload_with=engine)

    if data == None or not data['username'] or not data['password']:   
        conn.close()
        return make_response('Could not verify due to lack of username and password information', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
    
    applicants = db.Table('applicant_information', metadata, autoload=True, autoload_with=engine)

    new_user = conn.execute(db.select(applicants).where(applicants.columns.username == data['username']))
    # new_user = conn.execute("SELECT * FROM applicant_information WHERE username = '"+str(data['username'])+"'").fetchall()
    # print(new_user)
    print(new_user,flush=True)

    if not new_user:
        conn.close()
        return make_response('Could not verify as there are no selected user within the database', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    for user in new_user:   # these information can instead be retrieved using foreign key relationships in the database, some fields can be removed.
        user_data = {}
        user_data['applicant_id'] = user.applicant_id
        user_data['applicant_fullname'] = user.fullname
        user_data['username'] = user.username
        user_data['password'] = user.password
        user_data['email'] = user.email
        user_data['role'] = user.role
    
    applications = db.Table('application', metadata, autoload=True, autoload_with=engine)
    specific_application = conn.execute(db.select(applications).where(applications.columns.applicant_id == user_data['applicant_id']))

    if specific_application != None:
        for i in specific_application:
            user_data['application_id'] = i.application_id
    else:
        user_data['application_id'] = 0

    try:    
        if bcrypt.checkpw(bytes(data['password'],'utf-8'),bytes(user_data['password'],'utf-8')):     
            token = jwt.encode( { 'application_id':user_data['application_id'], 'applicant_id':user_data['applicant_id'], 'fullname':user_data['applicant_fullname'], 'user':user_data['username'], 'role':user_data['role'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=3) } , app.config['SECRET_KEY'] )

        # print("Token =",token)

        conn.close()

        response = jsonify( { 'accessToken' : token } )
        response.headers.add("Access-Control-Allow-Origin","*")
        
        return response

    except:
        conn.close()

        response = jsonify( { 'Response' : 'Could not verify as there are no selected user within the database, 401'} )
        response.headers.add("Access-Control-Allow-Origin","*")
        # print(response)

        return response
    
# rechecked
@app.route('/logout', methods=['DELETE'])
@token_required
def logout(current_user):

    if 'Authorization' in request.headers:
            token = request.headers['Authorization']

    conn = engine.connect()
    metadata = db.MetaData()

    blacklisted_table = db.Table('jwt_blacklist', metadata, autoload=True, autoload_with=engine)
    
    values = {}
    values['blacklisted'] = token
    query = db.insert(blacklisted_table)
    conn.execute(query,values)

    response = jsonify({'Message':'You have successfully logged out'})
    response.headers.add("Access-Control-Allow-Origin","*")

    return response

# rechecked
@app.route('/userinfo', methods=['GET'])
@token_required
def userinfo(current_user):

    if 'Authorization' in request.headers:
            token = request.headers['Authorization']

    if not token:
        return make_response("Token is not being provided",401)

    # print("Token =" ,token)

    data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"])

    # print("Data =",data)

    response =  jsonify(data)
    response.headers.add("Access-Control-Allow-Origin","*")

    # print(response)

    return response


# rechecked
@app.route('/getAllApplicants', methods=['GET'])
@token_required
def getAllApplicants(current_user):

    for i in current_user:
        if i.role != 'admin':
            response = jsonify({ 'response':'Unauthorized, 401' })
            response.headers.add("Access-Control-Allow-Origin","*")
            return response

    conn = engine.connect()
    # establish the connection to the database as declared.

    selection_query = """
    SELECT application.application_id, application.applicant_id, application.job_id, application.validation, 
    application.validated_time, application.sent_offer, application.question_progress,
    applicant_information.fullname, applicant_information.contact_number, applicant_information.email,
    job_information.rolename, job_information.department, job_information.working_location, job_information.application_deadline
    """
    from_query = """FROM application 
    LEFT JOIN applicant_information ON application.applicant_id = applicant_information.applicant_id 
    LEFT JOIN job_information ON application.job_id = job_information.job_id
    WHERE applicant_information.role != 'admin'"""
    
    test_string = selection_query + from_query
    
    all_values = conn.execute(test_string).fetchall()

    # for conn.execute function, you can provide the queries as usable in MySQL Workbench.
    # or either, this example from the /userinfo function.
    # 
    # This below line notates the declaration of database table name before being used to search in the conn.execute() function.
    # applicants = db.Table('applicant_information', metadata, autoload=True, autoload_with=engine)
    # 
    # On line 243, will select things from the table declared as "applicants" and the .where method is used to select the criteria.           
    # On line 243, applicants.columns.username is to specify the username column in the "applicants" table declared.
    #
    # ----> new_user = conn.execute(db.select(applicants).where(applicants.columns.username == data['username']))

    # however, the conn.execute(query) will result in a LegacyRow object, of which, getting fetchall() method will get those rows into
    # a list of dictionary pairs 

    # for instance, the conn.execute(query).fetchall() will get [ ( 1 , 2 , 3 , 4 , 5 , 6 ) ] where accessing the data by using .field_name
    # such as
    #       fullname_of_app_id_of_123 = conn.execute("SELECT * FROM application WHERE application_id = 123").fetchall()[0].fullname
    #       ( This will get the data where application_id is 123 as the query, getting a LegacyRow with one element.
    #         Then, fetchall() will get the LegacyRow in list of object type "Row" so [0] will access the first element ( Row object )
    #         after getting that row object , providing .fullname in the end, will get only the data in the field "fullname"
    #       )

    # for more documentations, search SQLAlchemy conn or either search about LegacyRow.




    # output = []
    # metadata = db.MetaData()
    # application = db.Table('application', metadata, autoload=True, autoload_with=engine)

    # application_data = conn.execute(db.select(application))

    # for i in application_data:
    #     #print(i)
    #     data = {}
    #     data['application_id'] = i.application_id
    #     data['applicant_id'] = i.applicant_id
    #     data['job_id'] = i.job_id
    #     data['validation'] = i.validation
    #     data['validated_time'] = i.validated_time
    #     data['sent_offer'] = i.sent_offer
    #     data['question_progress'] = i.question_progress

    #     applicant = db.Table('applicant_information', metadata, autoload=True, autoload_with=engine)
    #     applicant_data = conn.execute(db.select(applicant).where(applicant.columns.applicant_id == data['applicant_id']))
        
    #     for i in applicant_data:
    #         data['applicant_fullname'] = i.fullname
    #         data['contact_number'] = i.contact_number
    #         data['email'] = i.email

    #     job = db.Table('job_information', metadata, autoload=True, autoload_with=engine)
    #     job_data = conn.execute(db.select(job).where(job.columns.job_id == data['job_id']))

    #     for j in job_data:
    #         data['position'] = j.position
    #         data['department'] = j.department
    #         data['working_location'] = j.working_location
    #         data['application_deadline'] = j.application_deadline

    #     output.insert(0,data)

    conn.close()
    # we have to close the established connection too.

    response = jsonify([dict(row) for row in all_values]) # making those Row objects into dictionary datatype and placing those dictionary into lists so it can jsonify.
    response.headers.add("Access-Control-Allow-Origin","*")

    return response


# for the <application_id> in the app.route, it tells where take the parameters in the URL endpoints in front-end at the same specific position.
# for instance https://<api_web_url>/getApplication/42 will get 42 to passed into this function.

@app.route('/getApplication/<application_id>', methods=['GET'])  
@token_required
def getApplication(current_user, application_id):

    for i in current_user:
        if i.role != 'admin':
            response = jsonify({ 'response':'Unauthorized, 401' })
            response.headers.add("Access-Control-Allow-Origin","*")
            return response

    conn = engine.connect()
    metadata = db.MetaData()

    application = db.Table('application', metadata, autoload=True, autoload_with=engine)
    application_data = conn.execute(db.select(application).where(application.columns.application_id == application_id))

    set_application_data = {}
    set_applicant_data = {}
    set_partner_data = {}
    set_emergency_data = {}
    set_skill_data = {}
    set_employee_data = {}
    set_organization_data = {}
    set_job_data = {}
    set_answered_questions = []

    for i in application_data:
        set_application_data['application_id'] = i.application_id
        set_application_data['applicant_id'] = i.applicant_id
        set_application_data['job_id'] = i.job_id
        set_application_data['validation'] = i.validation
        set_application_data['sent_offer'] = i.sent_offer
        set_application_data['question_progress'] = i.question_progress
        ## add PERCENTAGE OF SUITABILITY.

    applicant = db.Table('applicant_information', metadata, autoload=True, autoload_with=engine)
    applicant_data = conn.execute(db.select(applicant).where(applicant.columns.applicant_id == set_application_data['applicant_id']))
    
    for j in applicant_data:
        set_applicant_data['application_id'] = i.application_id
        set_applicant_data['applicant_id'] = set_application_data['applicant_id']
        set_applicant_data['fullname'] = j.fullname
        set_applicant_data['citizen_id'] = j.citizen_id
        set_applicant_data['contact_number'] = j.contact_number
        set_applicant_data['email'] = j.email
        set_applicant_data['age'] = j.age
        set_applicant_data['DOB'] = j.DOB
        set_applicant_data['nationality'] = j.nationality
        set_applicant_data['religion'] = j.religion
        set_applicant_data['university'] = j.university
        set_applicant_data['degree'] = j.degree
        set_applicant_data['GPA'] = j.GPA
        set_applicant_data['address'] = j.address
        set_applicant_data['gender'] = j.gender
        set_applicant_data['marital_status'] = j.marital_status
        set_applicant_data['military_status'] = j.military_status
        set_applicant_data['append_date'] = j.append_date
        set_applicant_data['working_experience_id'] = j.workingexp_id
        set_applicant_data['emergencycont_id'] = j.emergencycont_id
        set_applicant_data['partnerinfo_id'] = j.partnerinfo_id

    working_experience = db.Table('working_experiences', metadata, autoload=True, autoload_with=engine)
    working_experience_data = conn.execute(db.select(working_experience).where(working_experience.columns.workingexp_id == set_applicant_data['working_experience_id']))   

    for k in working_experience_data:
        set_skill_data['working_experience_id'] = set_applicant_data['working_experience_id']
        set_skill_data['statement_of_purpose'] = k.statement_of_purpose
        set_skill_data['driving_license'] = k.driving_license
        set_skill_data['car_possession'] = k.car_possession
        set_skill_data['pc_possession'] = k.pc_possession
        set_skill_data['foreign_language'] = k.foreign_language
        set_skill_data['proficiency'] = k.proficiency
        set_skill_data['special_ability'] = k.special_ability

    partner = db.Table('partner_information', metadata, autoload=True, autoload_with=engine)
    partner_data = conn.execute(db.select(partner).where(partner.columns.partnerinfo_id == set_applicant_data['partnerinfo_id']))

    for i in partner_data:
        set_partner_data['partner_id'] = set_applicant_data['partnerinfo_id']
        set_partner_data['partner_fullname'] = i.fullname
        set_partner_data['partner_occupation'] = i.contact_number
        set_partner_data['partner_company'] = i.company
        set_partner_data['number_of_children'] = i.number_of_children
        set_partner_data['partner_contact_number'] = i.contact_number
        set_partner_data['partner_email'] = i.email
        set_partner_data['partner_address'] = i.address

    emergency_contact = db.Table('emergency_contact', metadata, autoload=True, autoload_with=engine)
    emergency_contact_data = conn.execute(db.select(emergency_contact).where(emergency_contact.columns.emergencycont_id == set_applicant_data['emergencycont_id']))

    for j in emergency_contact_data:
        set_emergency_data['emergencycont_id'] = set_applicant_data['emergencycont_id']
        set_emergency_data['emergencycont_fullname'] = j.fullname
        set_emergency_data['emergencycont_contact_number'] = j.contact_number
        set_emergency_data['emergencycont_relationship'] = j.relationship
        set_emergency_data['emergencycont_additional_fullname'] = j.additional_fullname
        set_emergency_data['emergencycont_contact_number'] = j.contact_number
        set_emergency_data['emergencycont_relationship'] = j.relationship


    job_applied = db.Table('job_information', metadata, autoload=True, autoload_with=engine)
    job_applied_data = conn.execute(db.select(job_applied).where(job_applied.columns.job_id == set_application_data['job_id']))

    for i in job_applied_data:
        set_job_data['job_id'] = i.job_id
        set_job_data['rolename'] = i.rolename
        set_job_data['position_id'] = i.position_id
        set_job_data['approx_salary'] = i.approx_salary
        set_job_data['number_of_applicants'] = i.number_of_applicants
        set_job_data['start_date'] = i.start_date
        set_job_data['application_deadline'] = i.application_deadline
        set_job_data['line_manager_id'] = i.line_manager_id
        set_job_data['working_location'] = i.working_location
        set_job_data['educational_degree_required'] = i.educational_degree_required
        set_job_data['required_experiences'] = i.required_experiences
        set_job_data['required_skills'] = i.required_skills
        set_job_data['status'] = i.status
        set_job_data['working_time_details'] = i.working_time_details
        set_job_data['job_description'] = i.job_description
        set_job_data['accommodations'] = i.accommodations
        set_job_data['bonus'] = i.bonus
        set_job_data['transportation'] = i.transportation
        set_job_data['transportation_allowances'] = i.transportation_allowances
        set_job_data['ot_per_hour'] = i.ot_per_hour
        set_job_data['leave_quota'] = i.leave_quota
        set_job_data['laptop_provision'] = i.laptop_provision
        set_job_data['other_provision'] = i.other_provision
        set_job_data['insurance_provision'] = i.insurance_provision
        set_job_data['insurance_level'] = i.insurance_level
        set_job_data['additional_benefits_welfare'] = i.additional_benefits_welfare

    organization_info = db.Table('organization_information', metadata, autoload=True, autoload_with=engine)
    organization_info_data = conn.execute(db.select(organization_info).where(organization_info.columns.position_id == set_job_data['position_id']))

    for i in organization_info_data:
        set_organization_data['position_id'] = set_job_data['position_id']
        set_organization_data['department'] = i.department
        set_organization_data['position'] = i.position
        set_organization_data['competencies'] = i.competencies

    employee_info = db.Table('employee_information', metadata, autoload=True, autoload_with=engine)
    employee_info_data = conn.execute(db.select(employee_info).where(employee_info.columns.employee_id == set_job_data['line_manager_id']))

    for i in employee_info_data:
        set_employee_data['manager_id'] = set_job_data['line_manager_id']
        set_employee_data['manager_fullname'] = i.employee_fullname
        set_employee_data['manager_role'] = i.role

    # answered_questions = db.Table('questions_answered', metadata, autoload=True, autoload_with=engine)

    answered_questions_data = conn.execute("""
    SELECT questions_answered.question_id, questions_answered.answer, questions.question FROM questions_answered 
    JOIN questions ON questions_answered.question_id = questions.question_id
    WHERE questions.question_type = 'general' and application_id = """ +str(application_id)
    )


    # answered_questions_data = conn.execute(db.select(answered_questions).where(answered_questions.columns.application_id == application_id))
    # questions = db.Table('questions', metadata, autoload=True, autoload_with=engine)
    
    if answered_questions_data:
        for j in answered_questions_data:
            dummy_data = {}
            question_data = conn.execute("SELECT * FROM questions WHERE question_type = 'general' and question_id = "+str(j.question_id)).fetchall()
            # question_data = conn.execute(db.select(questions).where(questions.columns.question_id == j.question_id))
            for k in question_data:
                dummy_data['q_id'] = k.question_id
                dummy_data['questions'] = k.question
            dummy_data['answer'] = j.answer
            set_answered_questions.append(dummy_data)
    else:
        set_answered_questions = None

    conn.close()
    
    response = jsonify( {'Application': set_application_data , 'Applicant':set_applicant_data,'Emergency':set_emergency_data,'Skill':set_skill_data, 'Partner': set_partner_data, 'Job':set_job_data,'Manager':set_employee_data,'Organization':set_organization_data, 'Questions':set_answered_questions})
    response.headers.add("Access-Control-Allow-Origin","*")
    return response


# rechecked
@app.route('/uploadApplication', methods=['GET','POST'])
def uploadApplication(): 

    conn = engine.connect()
    metadata = db.MetaData()

    data = request.form.to_dict()
    print(data, flush=True)
    print(data['applicant_fullname'], flush=True)

    check_query = "SELECT number_of_applicants FROM job_information WHERE job_id = " + str(data['job_id'])
    num_of_applicant_check = conn.execute(check_query).fetchall()[0].number_of_applicants 
     
    if not data:
        response = jsonify({'Action': 'No Data Available' })
        response.headers.add("Access-Control-Allow-Origin","*")
        return response

    partner = db.Table('partner_information', metadata, autoload=True, autoload_with=engine)
    last_partner_id = engine.execute(text("select partnerinfo_id from partner_information ORDER BY time_registered DESC LIMIT 1;")).fetchall()

    if last_partner_id == []:
        new_partner_id = 'PN1'
    else:
        string_last_partner_id = last_partner_id[0].partnerinfo_id
        dummy_id = ''
        for char in string_last_partner_id[2::]: 
            if char.isdigit():
                dummy_id += char  
            else:
                break
        
        new_partner_id = 'PN' + str(int(dummy_id) + 1)

    partner_values = {
        'partnerinfo_id' : new_partner_id,
        'fullname': data['partner_fullname'],
        'company' : data['partner_company'],
        'occupation' : data['partner_occupation'],
        'number_of_children' : data['number_of_children'],
        'contact_number' : data['partner_contact_number'],
        'email' : data['partner_email'],
        'address' : data['partner_address'],
        'time_registered' : time.strftime('%Y-%m-%d %H:%M:%S')
    }
    print(partner_values, flush=True)
    partner_query = db.insert(partner)
    conn.execute(partner_query,partner_values)

    emergency = db.Table('emergency_contact', metadata, autoload=True, autoload_with=engine)
    last_emerg_cont_id = engine.execute(text("select emergencycont_id from emergency_contact ORDER BY time_registered DESC LIMIT 1;")).fetchall()

    if last_emerg_cont_id == []:
        new_emerg_cont_id = 'EC1'

    else:
        string_last_emerg_cont_id = last_emerg_cont_id[0].emergencycont_id
        dummy_id = ''
        for char in string_last_emerg_cont_id[2::]:
            if char.isdigit():
                dummy_id += char  
            else:
                break
        new_emerg_cont_id = 'EC' + str(int(dummy_id) + 1)

    emergcont_values = {
        'emergencycont_id' : new_emerg_cont_id,
        'fullname': data['emergency_fullname'],
        'contact_number' : data['emergency_contact_number'],
        'relationship' : data['emergency_relationship'],
        'time_registered' : time.strftime('%Y-%m-%d %H:%M:%S')
    }

    if data['additional_fullname'] :
        emergcont_values['additional_fullname'] = data['additional_fullname'] 

    if data['additional_contact_number'] :
        emergcont_values['additional_contact_number'] = data['additional_contact_number']

    if data['additional_relationship'] :
        emergcont_values['additional_relationship'] = data['additional_relationship']

    emergency_query = db.insert(emergency)
    conn.execute(emergency_query,emergcont_values)
    
    workexp = db.Table('working_experiences', metadata, autoload=True, autoload_with=engine)
    last_workexp_id = engine.execute(text("select workingexp_id from working_experiences ORDER BY time_registered DESC LIMIT 1;")).fetchall()
    
    if last_workexp_id == []:
        new_workexp_id = 'WE1'
    else:
        string_last_workexp_id = last_workexp_id[0].workingexp_id
        dummy_id = ''
        for char in string_last_workexp_id[2::]: 
            if char.isdigit():
                dummy_id += char  
            else:
                break
        
        new_workexp_id = 'WE' + str(int(dummy_id) + 1)

    workexp_values = {
        'workingexp_id' : new_workexp_id,
        'document_path': 'Specified in the system',
        'statement_of_purpose' : data['statement_of_purpose'],
        'driving_license' : data['driving_license'],
        'car_possession' : data['car_possession'],
        'pc_possession' : data['pc_possession'],
        'foreign_language' : data['foreign_language'],
        'proficiency' : data['proficiency'],
        'special_ability' : data['special_ability'],
        'time_registered' : time.strftime('%Y-%m-%d %H:%M:%S')
    }
    print(workexp_values, flush=True)
    workexp_query = db.insert(workexp)
    conn.execute(workexp_query,workexp_values)

    applicants = db.Table('applicant_information', metadata, autoload=True, autoload_with=engine)
    last_app_id = engine.execute(text("select applicant_id from applicant_information ORDER BY append_date DESC LIMIT 1;")).fetchall()
    
    if last_app_id == []:
        new_id = 'AP1'
    else:
        string_last_id = last_app_id[0].applicant_id
        dummy_id = ''
        for char in string_last_id[2::]: 
            if char.isdigit():
                dummy_id += char  
            else:
                break
        
        new_id = 'AP' + str(int(dummy_id) + 1)

    generated_username = new_id + data['applicant_fullname'].replace(" ","").upper()

    rand_pw = pwo.generate()
    hashed_pw = bcrypt.hashpw(bytes(str(rand_pw),'utf-8'),bcrypt.gensalt(12)) 

    applicant_values = {
        'applicant_id' : new_id,
        'fullname' : data['applicant_fullname'],
        'citizen_id' : data['applicant_citizen_id'],
        'contact_number' : data['applicant_contact_number'],
        'email' : data['applicant_email'],
        'age' : data['age'],
        'DOB' :  data['DOB'],
        'username': generated_username,
        'password': hashed_pw,
        'nationality':data['nationality'],
        'religion':  data['religion'],
        'university': data['university'],
        'degree': data['degree'], 
        'GPA': data['GPA'],
        'address':data['address'],
        'gender':data['gender'],
        'marital_status': data['marital_status'],
        'military_status': data['military_status'],
        'workingexp_id': new_workexp_id,
        'emergencycont_id': new_emerg_cont_id,
        'partnerinfo_id': new_partner_id,
        'append_date': time.strftime('%Y-%m-%d %H:%M:%S'),
        'role': str('applicant')
    }
    print(applicant_values, flush=True)
    applicants_query = db.insert(applicants)
    conn.execute(applicants_query,applicant_values)

    application = db.Table('application', metadata, autoload=True, autoload_with=engine)

    application_values = {
        'applicant_id': applicant_values['applicant_id'],
        'job_id': data['job_id'],
        'registered_datetime': time.strftime('%Y-%m-%d %H:%M:%S'),
        'validation': 0,
        'sent_offer': 0,
        'offer_acceptance': 0,
        'question_progress' : 'Preparing'
    }
    print(application_values, flush=True)
    application_query = db.insert(application)
    conn.execute(application_query,application_values)

    job = db.Table('job_information', metadata, autoload=True, autoload_with=engine)
    job_data = conn.execute(db.select(job).where(job.columns.job_id == data['job_id']))

    for i in job_data:
        pos_id = i.position_id
        application_deadline = i.application_deadline
        job_role_applied = i.rolename
        num_of_applicant = i.number_of_applicants - 1
        line_manager_id = i.line_manager_id

    stmt = " UPDATE job_information SET number_of_applicants = " + str(num_of_applicant) + " WHERE job_id = " + str(data['job_id'])
    conn.execute(stmt)
    
    application_id = engine.execute(text("select application_id from application ORDER BY registered_datetime DESC LIMIT 1;")).fetchall()[0].application_id

    answers = db.Table('questions_answered', metadata, autoload=True, autoload_with=engine)
    
    
    list_of_q_and_a = json.loads(data['all_questions'])

    print(list_of_q_and_a,flush=True)
    print(type(list_of_q_and_a),flush=True)

    for k in list_of_q_and_a:
        print(i,flush=True)
        answer_values = {}
        answer_values['application_id'] = application_id
        answer_values['selected'] = 1
        answer_values['question_id'] = k['question_id']
        answer_values['answer'] =  k['answer']
        target_table = db.insert(answers)
        conn.execute(target_table,answer_values)


    position_name = conn.execute("SELECT position FROM organization_information WHERE position_id = " + str(pos_id)).fetchall()[0].position
    department_name = conn.execute("SELECT department FROM organization_information WHERE position_id = " + str(pos_id)).fetchall()[0].department

    resume = request.files['pdf'] 

    resume.filename = new_id + '.pdf'
    resume.save(os.path.join(upload_path,resume.filename))

    applicant_email = applicant_values['email']

    applicant_inform_email = EmailMessage()
    applicant_inform_email['Subject'] = "Company A Online Application : Personalized Evaluation Test"
    applicant_inform_email['From'] = EMAIL_ADDRESS    
    applicant_inform_email['To'] = applicant_email

    content = open("applicant_email.html").read().format(applicant_name=applicant_values['fullname'], 
                                            job_role=job_role_applied, 
                                            app_deadline=application_deadline,
                                            position=position_name,
                                            department=department_name,
                                            username=generated_username,
                                            password=rand_pw)
    applicant_inform_email.set_content(content,subtype="html")

    employee_information = db.Table('employee_information', metadata, autoload=True, autoload_with=engine)
    manager_name = conn.execute(db.select(employee_information).where(employee_information.columns.employee_id == line_manager_id)).fetchall()[0].employee_fullname
    manager_email = conn.execute(db.select(employee_information).where(employee_information.columns.employee_id == line_manager_id)).fetchall()[0].employee_email

    organization_inform_email = EmailMessage()
    organization_inform_email['Subject'] = "Company A Online Application : New Application Submitted"
    organization_inform_email['From'] = EMAIL_ADDRESS    # jobapplicationplatform@gmail.com
    organization_inform_email['To'] = manager_email 
    org_content = open("manager_email.html").read().format( manager_name= manager_name,
                                            position= position_name,
                                            applicant_name=applicant_values['fullname'], 
                                            job_role=job_role_applied, 
                                            app_deadline=application_deadline,
                                            )
    organization_inform_email.set_content(org_content,subtype="html")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:   # to the actual email, required smtp.ehlo() and smtp.starttls() code

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(applicant_inform_email)
        smtp.send_message(organization_inform_email)

    print("A information email has been sent to", applicant_values['email'], "( via SSL Connection ) while the questions selection emails are being submmitted to", manager_email )
    
    conn.close()


    response = jsonify({'Action': 'An application has been uploaded into the system, please check your email for more details.' })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response


# rechecked
@app.route('/getAllJobs', methods=['GET'])
def getAllJobs():

    conn = engine.connect()
    selection_query = """
    SELECT job_information.job_id, job_information.rolename, job_information.position_id, job_information.approx_salary, job_information.number_of_applicants,
    job_information.start_date, job_information.application_deadline, job_information.educational_degree_required,
    job_information.required_experiences, job_information.required_skills, job_information.status, job_information.working_time_details,
    job_information.job_description, job_information.job_description, job_information.working_location, job_information.accommodations, job_information.bonus,
    job_information.transportation, job_information.transportation_allowances, job_information.ot_per_hour, job_information.leave_quota,
    job_information.laptop_provision, job_information.other_provision, job_information.insurance_provision, job_information.insurance_provision,
    job_information.insurance_level,job_information.additional_benefits_welfare, organization_information.department,
    organization_information.position, organization_information.competencies,employee_information.employee_fullname,employee_information.role
    """


    from_query = """FROM job_information
    JOIN organization_information ON job_information.position_id = organization_information.position_id
    JOIN employee_information ON job_information.line_manager_id = employee_information.employee_id"""
    
    test_string = selection_query + from_query
    # print(test_string)
    all_values = conn.execute(test_string).fetchall()
    test = [dict(row) for row in all_values][-2]
    # print(test)


    test2 = []
    for row in all_values:
        test2.append(dict(row))
    
    for i in test2:
        i['required_skills'] = list(i['required_skills'][1:-1].split(","))
        # print(i['required_skills'], end="\n")

    # metadata = db.MetaData()

    # job_applied = db.Table('job_information', metadata, autoload=True, autoload_with=engine)
    # job_applied_data = conn.execute(db.select(job_applied))

    # whole_data = []
    
    # for i in job_applied_data:
    #     data = {}
    #     data['job_id'] = i.job_id
    #     data['position_id'] = i.position_id
    #     data['approx_salary'] = i.approx_salary
    #     data['number_of_applicants'] = i.number_of_applicants
    #     data['start_date'] = i.start_date
    #     data['application_deadline'] = i.application_deadline
    #     data['line_manager_id'] = i.line_manager_id
    #     data['working_location'] = i.working_location
    #     data['educational_degree_required'] = i.educational_degree_required
    #     data['required_experiences'] = i.required_experiences
    #     data['required_skills'] = i.required_skills      

    #     # for the best possible way, get the data into this form in the json data submitted.    
    #     # "required_skills": [
    #     #     "Human-Centred Design",
    #     #     "Customer Psychology",
    #     #     "User Experience Theorie"
    #     # ],        

    #     data['status'] = i.status
    #     data['working_time_details'] = i.working_time_details
    #     data['job_description'] = i.job_description
    #     data['accommodations'] = i.accommodations
    #     data['bonus'] = i.bonus
    #     data['transportation'] = i.transportation
    #     data['transportation_allowances'] = i.transportation_allowances
    #     data['ot_per_hour'] = i.ot_per_hour
    #     data['leave_quota'] = i.leave_quota
    #     data['laptop_provision'] = i.laptop_provision
    #     data['other_provision'] = i.other_provision
    #     data['insurance_provision'] = i.insurance_provision
    #     data['insurance_level'] = i.insurance_level
    #     data['additional_benefits_welfare'] = i.additional_benefits_welfare

    #     organization_info = db.Table('organization_information', metadata, autoload=True, autoload_with=engine)
    #     organization_info_data = conn.execute(db.select(organization_info).where(organization_info.columns.position_id == data['position_id']))

    #     for i in organization_info_data:
    #         data['position_id'] = data['job_id']
    #         data['department'] = i.department
    #         data['position'] = i.position
    #         data['competencies'] = i.competencies

    #     employee_info = db.Table('employee_information', metadata, autoload=True, autoload_with=engine)
    #     employee_info_data = conn.execute(db.select(employee_info).where(employee_info.columns.employee_id == data['line_manager_id']))

    #     for i in employee_info_data:
    #         data['manager_id'] = data['line_manager_id']
    #         data['manager_fullname'] = i.employee_fullname
    #         data['manager_role'] = i.role

    #     whole_data.append(data)

    conn.close()

    response = jsonify(test2)
    # response = jsonify(whole_data)
    response.headers.add("Access-Control-Allow-Origin","*")
    return response


@app.route('/getSingleJob/<job_id>', methods=['GET'])
def getSingleJob(job_id):

    conn = engine.connect()
    # list(i.required_skills[1:-1].split(","))
    metadata = db.MetaData()
    # print("getSingleJob job_id   ", job_id , flush=True)
    job_applied = db.Table('job_information', metadata, autoload=True, autoload_with=engine)
    
    job_applied_data = conn.execute(db.select(job_applied).where(job_applied.columns.job_id == job_id))
    # print("getSingleJob get_job_applied_data    " , job_applied_data , flush=True)

    data = {}
    for i in job_applied_data:
        data['job_id'] = i.job_id
        data['rolename'] = i.rolename
        data['position_id'] = i.position_id
        data['approx_salary'] = i.approx_salary
        data['number_of_applicants'] = i.number_of_applicants
        data['start_date'] = i.start_date
        data['application_deadline'] = i.application_deadline
        data['line_manager_id'] = i.line_manager_id
        data['working_location'] = i.working_location
        data['educational_degree_required'] = i.educational_degree_required
        data['required_experiences'] = i.required_experiences
        data['required_skills'] = list(i.required_skills[1:-1].split(","))
        data['status'] = i.status
        data['working_time_details'] = i.working_time_details
        data['job_description'] = i.job_description
        data['accommodations'] = i.accommodations
        data['bonus'] = i.bonus
        data['transportation'] = i.transportation
        data['transportation_allowances'] = i.transportation_allowances
        data['ot_per_hour'] = i.ot_per_hour
        data['leave_quota'] = i.leave_quota
        data['laptop_provision'] = i.laptop_provision
        data['other_provision'] = i.other_provision
        data['insurance_provision'] = i.insurance_provision
        data['insurance_level'] = i.insurance_level
        data['additional_benefits_welfare'] = i.additional_benefits_welfare


    # pending questions and stuff.
    query = "SELECT * FROM job_questions WHERE job_id = " + str(job_id)
    all_job_q_id = conn.execute(query).fetchall() 

    questions_set = []

    for j in all_job_q_id:
        #print(j.question_id)

        query = "SELECT * FROM questions WHERE question_id = " + str(j.question_id)
        questions_data = conn.execute(query)  
            
        list_of_questions = {}
            
        for i in questions_data:
            list_of_questions['q_id'] = i.question_id
            list_of_questions['question'] = i.question
        
        questions_set.append(list_of_questions)


    if data == {}:

        response = jsonify({'Response': 'No question with this ID in the database'})
        response.headers.add("Access-Control-Allow-Origin","*")
        return response

    data['list_of_questions'] = questions_set


    organization_info = db.Table('organization_information', metadata, autoload=True, autoload_with=engine)
    organization_info_data = conn.execute(db.select(organization_info).where(organization_info.columns.position_id == data['position_id']))

    for i in organization_info_data:
        data['position_id'] = data['job_id']
        data['department'] = i.department
        data['position'] = i.position
        data['competencies'] = i.competencies

    employee_info = db.Table('employee_information', metadata, autoload=True, autoload_with=engine)
    employee_info_data = conn.execute(db.select(employee_info).where(employee_info.columns.employee_id == data['line_manager_id']))

    for i in employee_info_data:
        data['manager_id'] = data['line_manager_id']
        data['manager_fullname'] = i.employee_fullname
        data['manager_role'] = i.role

    # print("getSingleJob single_job_data_json    " , data , flush=True)

    conn.close()

    response = jsonify({'Jobs': data })
    response.headers.add("Access-Control-Allow-Origin","*")
    # print(response)
    return response


# rechecked
@app.route('/addNewJob', methods=['POST'])  
@token_required
def addNewJob(current_user):

    for i in current_user:
        if i.role != 'admin':
            response = jsonify({ 'response':'Unauthorized, 401' })
            response.headers.add("Access-Control-Allow-Origin","*")
            return response

    data = request.json

    conn = engine.connect()
    metadata = db.MetaData()

    str_cat = "["
    for i in data['required_skills']:
        str_cat += str(i)
        str_cat += ','
    str_cat = str_cat[0:-1]+"]"
    # print(str_cat)


    line_manager_id = conn.execute("SELECT employee_id FROM employee_information WHERE employee_fullname = '"+data['manager_name'] + "'").fetchall()[0].employee_id


    values = {
                'rolename' : data['role_name'],    # this role_name go into job_information position field.
                'approx_salary' : data['approx_salary'],
                'number_of_applicants': data['number_of_applicants'],
                'start_date': data['start_date'],
                'application_deadline' : data['application_deadline'],
                'line_manager_id' : line_manager_id,     # will be taken from the input from front-end after providing the manager dropdown both their id and names, ( controversial )
                'working_location' : data['working_location'],
                'educational_degree_required': data['educational_degree_required'],
                'required_experiences': data['required_experiences'],
                'required_skills': str_cat , # pending , hoping for an array in the end.
                'status': data['status'],
                'working_time_details' : data['working_time_details'],
                'job_description': data['job_description'],
                'accommodations' : data['accommodations'],   # the data here will 
                'bonus': data['bonus'],
                'transportation' : data['transportation'],
                'transportation_allowances' : data['transportation_allowances'],
                'ot_per_hour' : data['ot_per_hour'],
                'leave_quota' : data['leave_quota'],
                'laptop_provision' : data['laptop_provision'],
                'other_provision' : data['other_provision'],
                'insurance_provision' : data['other_provision'],
                'insurance_level' : data['insurance_level'],
                'additional_benefits_welfare': data['additional_benefits_welfare'],
                'time_registered' : time.strftime('%Y-%m-%d %H:%M:%S')
              }


    organization_info_data = conn.execute("SELECT position_id, department FROM organization_information WHERE position = '" + str(data['position']) + "'").fetchall()
   
    if organization_info_data != None:
        for i in organization_info_data:
            values['position_id'] = i.position_id  # will be taken from the input from front-end after providing the manager dropdown both their id and names, ( controversial )
            values['department'] = i.department
    else: 
        return make_response('No position available', 404)

    job = db.Table('job_information', metadata, autoload=True, autoload_with=engine)
    query = db.insert(job)
    conn.execute(query,values)  # execute to add new job, next to the questions  

    list_of_questions = list( str(data['question_array'])[1:-1].split(",") )
    questions = db.Table('questions', metadata, autoload=True, autoload_with=engine)
    job_questions = db.Table('job_questions', metadata, autoload=True, autoload_with=engine)

    recent_q_id_list = []

    for i in list_of_questions:
        new_question_values = {
                'question' : i[1:-1].translate({ ord("'"): None }),
                'question_type' : 'general',
                'question_category': 'category A',
                'question_difficulty': 'general',
                'question_position' : values['department'],
                'question_keywords' : str_cat,     
        }
        add_question_query = db.insert(questions)
        conn.execute(add_question_query,new_question_values)
        
        latest_job_id = conn.execute("SELECT job_id FROM job_information ORDER BY job_id DESC LIMIT 1").fetchall()[0].job_id
        latest_q_id = conn.execute("SELECT question_id FROM questions ORDER BY question_id DESC LIMIT 1").fetchall()[0].question_id

        recent_q_id_list.append(latest_q_id)

        question_job_link = {
            'job_id' : latest_job_id,
            'question_id' : latest_q_id
        }

        # print('this is the question job link variable',question_job_link)
        job_questions_query = db.insert(job_questions)
        conn.execute(job_questions_query,question_job_link)


    # questions will be submitted in an array of strings for tagun to add it into db first, then get it linked together.


    # job_questions = db.Table('job_questions', metadata, autoload=True, autoload_with=engine)
    # query = db.insert(job_questions)
    # last_job_id = engine.execute(text("select job_id from job_information ORDER BY time_registered DESC LIMIT 1;")).fetchall()[0].job_id

    # for q_id in data['selected_questions_id']:   # accepting [1,2,3,4,5,6] without any spaces between integers or the brackets at all.
    #     jq_values = {
    #             'question_id' : q_id,
    #             'job_id' : last_job_id  
    #     }
    #     conn.execute(query,jq_values)

    conn.close()


    result_text = str(data['role_name']) + ' has been added into the database and questions with the ID of ' + str(recent_q_id_list) + ' are added into the system'

    response = jsonify({'Message':result_text})
    response.headers.add("Access-Control-Allow-Origin","*")
    return response



@app.route('/editJob/<job_id>', methods=['POST']) 
@token_required
def editJob(current_user,job_id):

    for i in current_user:
        if i.role != 'admin':
            response = jsonify({ 'response':'Unauthorized, 401' })
            response.headers.add("Access-Control-Allow-Origin","*")
            return response

    data = request.json

    keys = list(data.keys())
    # print("This is keys in the dict from data requested",keys)
    conn = engine.connect()
    metadata = db.MetaData() 
 

    job_information = db.Table('job_information', metadata, autoload=True, autoload_with=engine)
    job_data = conn.execute(db.select(job_information).where(job_information.columns.job_id == job_id)).fetchall()[0]

    for i in keys:
        # print("This is each keys while looping in the dict from data requested",i)
        if i in ['department']:
            continue

        elif i == 'position':


            query = "SELECT position_id, department FROM organization_information WHERE position = '" + str(data['position']) + "'"
            # print(query, 'position query')
            # print(data['position'], type(data['position']),flush=True)

            organization_information = db.Table('organization_information', metadata, autoload=True, autoload_with=engine)
            organization_info_data = conn.execute(db.select(organization_information).where(organization_information.columns.position == data['position'])).fetchall()
            # organization_info_data = conn.execute("SELECT position_id, department FROM organization_information WHERE position = '" + str(data['position']) + "'").fetchall()

            # print("This is organization_info_data ",organization_info_data, flush=True)
        

            new_pos_id = organization_info_data[0].position_id
            # print("this is new position_id ",new_pos_id, flush=True)
            new_department = organization_info_data[0].department
            # print("this is new_department ",new_department, flush=True)

            posid_update_query = "UPDATE job_information SET position_id = " + str(new_pos_id) +  " WHERE job_id = " + str(job_id)
            dept_update_query = "UPDATE job_information SET department = '" + new_department + "'" + " WHERE job_id = " + str(job_id)
                
            conn.execute(posid_update_query)  
            conn.execute(dept_update_query)  
            

        elif i == 'required_skills':

            prev_skills_before_conv = conn.execute("SELECT required_skills FROM job_information WHERE job_id = " + str(job_id)).fetchall()[0].required_skills
            # print("Original Data Taken from the DB is ", prev_skills_before_conv,type(prev_skills_before_conv))
            prev_skills = conn.execute("SELECT required_skills FROM job_information WHERE job_id = " + str(job_id)).fetchall()[0].required_skills[1:-1].split(",")
            # print("Converted Data from the DB is ",prev_skills,type(prev_skills))

            if data['required_skills'] != prev_skills:
                
                str_cat = "["
                for i in data['required_skills']:
                    str_cat += str(i)
                    str_cat += ','
                str_cat = str_cat[0:-1]+"]"

                # print(str_cat,type(str_cat))
                skills_update_query = "UPDATE job_information SET required_skills = '" + str(str_cat) + "' WHERE job_id = " + str(job_id)

                # print(skills_update_query)
                conn.execute(skills_update_query)

        elif i == 'prev_questions':
            if len(data["prev_questions"]) >= 0:
                questions = db.Table('questions', metadata, autoload=True, autoload_with=engine)
                job_questions_table = db.Table('job_questions', metadata, autoload=True, autoload_with=engine)

                job_question_query = '''
                SELECT job_questions.question_id, questions.question
                FROM job_questions
                JOIN questions ON job_questions.question_id = questions.question_id
                WHERE job_questions.job_id =
                ''' + str(job_id)

                job_questions_from_db = conn.execute(job_question_query).fetchall()
                    
                question_arr_from_db = [dict(row) for row in job_questions_from_db]
                q_id_arr_from_db = [dict(row)["question_id"] for row in job_questions_from_db]

                requested_questions = [p for p in data["prev_questions"]]
                q_id_arr_from_requested = [k["q_id"] for k in data["prev_questions"]]

                # print(question_arr_from_db)
                # print(q_id_arr_from_db)

                # print(requested_questions)
                # print(q_id_arr_from_requested)

                for m in requested_questions:
                    question_record_in_db = conn.execute(db.select(questions).where(questions.columns.question_id==m['q_id'])).fetchall()[0].question
                    if m['question'] != question_record_in_db:
                        question_update_query = "UPDATE questions SET question = '" + m['question'] + "' WHERE question_id = " + str(m['q_id'])
                        conn.execute(question_update_query)
                        # print("Question with the ID", m['q_id'], 'has been updated')


            # Deleting the disappeared question from the front-end
            for q in question_arr_from_db:
                if q["question_id"] not in q_id_arr_from_requested:
                    # print("Successfully DELETE questions with the job_id of "+str(job_id)+" AND question_id = "+str(q["question_id"]))
                    conn.execute("DELETE FROM job_questions WHERE job_id = "+str(job_id)+" AND question_id = "+str(q["question_id"]))

        
        elif i == "new_questions":

            if len(data["new_questions"]) >= 0:
                arr_new_questions = data["new_questions"]  
                for b in arr_new_questions:
                    new_question_values = {
                            'question' : b,
                            'question_type' : 'general',
                            'question_category': 'category A',
                            'question_difficulty': 'general',
                            'question_position' : conn.execute("SELECT required_skills FROM job_information WHERE job_id = "+ str(job_id)).fetchall()[0].required_skills,
                            'question_keywords' : 'test',     
                    }

                    add_question_query = db.insert(questions)
                    conn.execute(add_question_query,new_question_values)
                        
                    latest_q_id = conn.execute("SELECT question_id FROM questions ORDER BY question_id DESC LIMIT 1").fetchall()[0].question_id
                    new_question_link = {
                            'job_id' : job_id,
                            'question_id' : latest_q_id
                    }

                    # print('this is the question job link variable',new_question_link)
                    conn.execute(db.insert(job_questions_table),new_question_link)

        else:
            # print("This is the current key of this iteration",i, flush=True)
            # print(data[i])
            # print(job_data[i])
            if data[i] != job_data[i]:
                if isinstance(job_data[i], int):
                    int_query = "UPDATE job_information SET " + str(i) + " = " + str(data[i]) + " WHERE job_id = " + str(job_id)
                    conn.execute(int_query)
                elif isinstance(job_data[i], str):
                    str_query = 'UPDATE job_information SET ' + str(i) + " = '" + str(data[i]) + "' WHERE job_id = " + str(job_id)
                    conn.execute(str_query)
                    
    conn.close()
    response = jsonify({'Message':'The job has been updated specifically'})
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

# rechecked
@app.route('/addNewQuestion', methods=['POST'])
@token_required
def addNewQuestion(current_user):

    for i in current_user:
        if i.role != 'admin':
            response = jsonify({ 'response':'Unauthorized, 401' })
            response.headers.add("Access-Control-Allow-Origin","*")
            return response

    data = request.json

    conn = engine.connect()
    metadata = db.MetaData()

    questions = db.Table('questions', metadata, autoload=True, autoload_with=engine)

    values = {
                'question' : data['question'],
                'question_type' : data['question_type'].lower(),
                'question_category': data['question_category'].lower(),
                'question_difficulty': data['question_difficulty'],
                'question_position' : data['question_position'],
                'question_keywords' : data['question_keywords'],     
    }

    questions = db.Table('questions', metadata, autoload=True, autoload_with=engine)
    query = db.insert(questions)

    conn.execute(query,values)
    conn.close()
    
    response = jsonify({'Jobs': 'New Question Added' })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response



@app.route('/postSpecificQuestions', methods=['POST'])  # this is for applicants to answer their personalized
@token_required
def postSpecificQuestions(current_user):

    if 'Authorization' in request.headers:
            token = request.headers['Authorization']

    if not token:
        return make_response("Token is not being provided",401)

    data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"])  # get the application_id.

    conn = engine.connect()
    answers = request.json['list_of_answers']
    # # print(answers, type(answers))

    table = PrettyTable()
    table.field_names = ["Question ID","Question","Answer"]

    for i in answers:
        question_for_disp = conn.execute("SELECT question FROM questions WHERE question_id = "+str(i['q_id'])).fetchall()[0].question
        table.add_row([ i['q_id'] , question_for_disp , i['answer'] ])
        query = "UPDATE questions_answered SET answer = '" + str(i['answer']) + "' WHERE application_id = " + str(data['application_id']) + " and question_id = " + str(i['q_id']) + ""
        conn.execute(query)

    query_for_info = '''
    SELECT application.application_id, application.job_id, applicant_information.fullname, applicant_information.email, job_information.rolename, organization_information.position, 
    job_information.department, job_information.line_manager_id, employee_information.employee_fullname, employee_information.employee_email
    FROM application
    INNER JOIN applicant_information ON application.applicant_id = applicant_information.applicant_id
    INNER JOIN job_information ON application.job_id = job_information.job_id
    INNER JOIN organization_information ON job_information.position_id = organization_information.position_id
    INNER JOIN employee_information ON job_information.line_manager_id = employee_information.employee_id
    WHERE application_id = ''' + str(data['application_id'])

    data_for_email = conn.execute(query_for_info).fetchall()[0]

    applicant_inform_email = EmailMessage()
    applicant_inform_email['Subject'] = "Company A Online Application : Thank you for your application"
    applicant_inform_email['From'] = EMAIL_ADDRESS    
    applicant_inform_email['To'] = data_for_email.email

    content_for_applicant = open("thank_applicant_for_applying.html").read().format(
                                            applicant_name=data_for_email.fullname, 
                                            job_role=data_for_email.rolename, 
                                            position=data_for_email.position,
                                            department=data_for_email.department,
                                            )
    applicant_inform_email.set_content(content_for_applicant,subtype="html")

    manager_inform_email = EmailMessage()
    manager_inform_email['Subject'] = "Company A Online Application : Application Consideration"
    manager_inform_email['From'] = EMAIL_ADDRESS    
    manager_inform_email['To'] = data_for_email.employee_email

    content_for_manager = open("inform_employee_for_completed_questionaire.html").read().format(
                                            manager_name=data_for_email.employee_fullname,
                                            applicant_name=data_for_email.fullname,
                                            applicant_email=data_for_email.email, 
                                            job_role=data_for_email.rolename, 
                                            position=data_for_email.position,
                                            department=data_for_email.department,
                                            answer_disp=table.get_html_string()
                                            )

    manager_inform_email.set_content(content_for_manager,subtype="html")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(applicant_inform_email)
        smtp.send_message(manager_inform_email)

    response = jsonify({'Jobs': 'Answers submitted successfully, emails have been submitted to involved people' })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response



@app.route('/getAllQuestions/<question_category>/<question_difficulty>', methods=['GET'])
@token_required
def getAllQuestions(current_user,question_category,question_difficulty):

    for i in current_user:
        if i.role != 'admin':
            response = jsonify({ 'response':'Unauthorized, 401' })
            response.headers.add("Access-Control-Allow-Origin","*")
            return response

    conn = engine.connect()
    metadata = db.MetaData()

    #all_questions = db.Table('questions', metadata, autoload=True, autoload_with=engine)
    
    output = []

    if question_category not in [ 'general' , 'specific' ]:
        return make_response('The first parameter provided is incorrect, it only accepts "general" or "specific"', 401)

    if question_difficulty not in [ 'Beginner' , 'Intermed' , 'Expert' ]:
        return make_response('The second parameter provided is incorrect, it only accepts "beginner","intermediate" or "expert"', 401)

    query = "SELECT * FROM questions WHERE question_category = '" + str(question_category) + "' and question_difficulty = '" + str(question_difficulty) + "'"

    questions_data = conn.execute(query)  
    

    for i in questions_data:
        data = {}
        data['question_id'] = i.question_id
        data['question'] = i.question
        data['question_type'] = i.question_type
        data['question_category'] = i.question_category
        data['question_difficulty'] = i.question_difficulty
        data['question_position'] = i.question_position
        data['question_keywords'] = i.question_keywords

        output.append(data)

    conn.close()

    response = jsonify({'Applicants':output})
    response.headers.add("Access-Control-Allow-Origin","*")
    return response



@app.route('/getAllGeneralQuestions', methods=['GET'])
@token_required
def getGeneralQuestions(current_user):

    for i in current_user:
        if i.role != 'admin':
            response = jsonify({ 'response':'Unauthorized, 401' })
            response.headers.add("Access-Control-Allow-Origin","*")
            return response

    conn = engine.connect()
    metadata = db.MetaData()

    #all_questions = db.Table('questions', metadata, autoload=True, autoload_with=engine)
    
    output = []

    questions_query = db.Table('questions', metadata, autoload=True, autoload_with=engine)
    questions_data = conn.execute(db.select(questions_query))

    for i in questions_data:
        data = {}
        data['question_id'] = i.question_id
        data['question'] = i.question
        data['question_type'] = i.question_type
        data['question_category'] = i.question_category
        data['question_difficulty'] = i.question_difficulty
        data['question_position'] = i.question_position
        data['question_keywords'] = i.question_keywords

        output.append(data)

    conn.close()

    response = jsonify(output)
    response.headers.add("Access-Control-Allow-Origin","*")
    return response
    


@app.route('/getSingleQuestion/<question_id>', methods=['GET'])
@token_required
def getSingleQuestions(current_user, question_id):

    for i in current_user:
        if i.role != 'admin':
            response = jsonify({ 'response':'Unauthorized, 401' })
            response.headers.add("Access-Control-Allow-Origin","*")
            return response

    conn = engine.connect()
    #all_questions = db.Table('questions', metadata, autoload=True, autoload_with=engine)
    
    query = "SELECT * FROM questions WHERE question_id = " + str(question_id)

    questions_data = conn.execute(query)  
        
    data = {}
        
    for i in questions_data:
        data['question_id'] = i.question_id
        data['question'] = i.question
        data['question_type'] = i.question_type
        data['question_category'] = i.question_category
        data['question_difficulty'] = i.question_difficulty
        data['question_position'] = i.question_position
        data['question_keywords'] = i.question_keywords

    conn.close()
    
    if data == {}:
        response = jsonify({'Response':'No question with this ID in the database'})
        response.headers.add("Access-Control-Allow-Origin","*")
        return response

    response = jsonify({'Question':data})
    response.headers.add("Access-Control-Allow-Origin","*")
    return response



@app.route('/getSetOfJobQuestions/<job_id>', methods=['GET'])  
def getQuestionsAccordingToJobs(job_id):

    conn = engine.connect()
    query = "SELECT * FROM job_questions WHERE job_id = " + str(job_id)
    all_job_q_id = conn.execute(query).fetchall() 

    questions_set = []

    for j in all_job_q_id:

        query = "SELECT * FROM questions WHERE question_id = " + str(j.question_id)
        questions_data = conn.execute(query)  
            
        data = {}
            
        for i in questions_data:
            data['question_id'] = i.question_id
            data['question'] = i.question
            data['question_type'] = i.question_type
            data['question_category'] = i.question_category
            data['question_difficulty'] = i.question_difficulty
            data['question_position'] = i.question_position
            data['question_keywords'] = i.question_keywords

        questions_set.append(data)

    conn.close()

    response = jsonify(questions_set)
    response.headers.add("Access-Control-Allow-Origin","*")
    return response



@app.route('/pairSelectedQuestions', methods=['POST'])  
def pairSelectedQuestions():

    conn = engine.connect()
    metadata = db.MetaData()

    # print(request.json, type(request.json), flush=True)
# 
    q_id_json = request.json['q_id']

    a_id_json = request.json['applicant_id']

    # pending validation with data analytics section.
    first_suitable_dep = request.json['suited_dept'][0]
    second_suitable_dep = request.json['suited_dept'][1]
    third_suitable_dep = request.json['suited_dept'][2]

    first_suitable_pos = request.json['suited_pos'][0]
    second_suitable_pos = request.json['suited_pos'][1]
    third_suitable_pos = request.json['suited_pos'][2]

    first_score = request.json['score'][0]
    second_score = request.json['score'][1]
    third_score = request.json['score'][2]

    suitability_score = request.json['applied_score']

    application_values_query = """
    SELECT application.application_id, application.applicant_id, application.job_id, applicant_information.fullname, job_information.rolename, 
    job_information.position_id, job_information.department, job_information.application_deadline, organization_information.position, job_information.line_manager_id,
    employee_information.employee_fullname, employee_information.role, employee_information.employee_email
    FROM application
    INNER JOIN applicant_information ON application.applicant_id = applicant_information.applicant_id
    INNER JOIN job_information ON application.job_id = job_information.job_id
    INNER JOIN organization_information ON job_information.position_id = organization_information.position_id
    INNER JOIN employee_information ON job_information.line_manager_id = employee_information.employee_id
    WHERE application.applicant_id = '""" + str(a_id_json) + "'"

    # print(application_values_query, flush=True)

    application_data = conn.execute(application_values_query).fetchall()

    # print(application_data, flush=True)
    
    application_data = application_data[0]

    if type(q_id_json) == int:
        q_id_json = list(q_id_json)

    elif type(q_id_json) == str:
        q_id_json = list(q_id_json[1:-1].split(","))

    if len(q_id_json) != 0:

        questions_set = []

        for i in q_id_json:

            dummy_data = {}
            dummy_data['application_id'] = application_data.application_id

            questions_answered = db.Table('questions_answered', metadata, autoload=True, autoload_with=engine)
                        
            dummy_data['question_id'] = int(i)
            dummy_data['selected'] = 0
                
            query = db.insert(questions_answered)
            conn.execute(query,dummy_data)
            
            questions_set.append(dummy_data)

    else:

        all_ques_for_pos = conn.execute("SELECT question_id FROM questions WHERE question_position = '" + str(application_data.position) + "'").fetchall()

        questions_set = []

        for i in all_ques_for_pos:

            dummy_data = {}
            dummy_data['application_id'] = application_data.application_id

            questions_answered = db.Table('questions_answered', metadata, autoload=True, autoload_with=engine)
                        
            dummy_data['question_id'] = int(i.question_id)
            dummy_data['selected'] = 0
                
            query = db.insert(questions_answered)
            conn.execute(query,dummy_data)
            
            questions_set.append(dummy_data)

    update_q_progress_query = "UPDATE application SET question_progress = 'Ready' WHERE application_id = " + str(application_data.application_id)
    conn.execute(update_q_progress_query)

    organization_inform_email = EmailMessage()
    organization_inform_email['Subject'] = "Company A Online Application : Questions ready to be selected in the system"
    organization_inform_email['From'] = EMAIL_ADDRESS   
    organization_inform_email['To'] = application_data.employee_email
    org_content = open("questions_ready_to_be_selected.html").read().format( 
                                            manager_name= application_data.employee_fullname,
                                            applicant_name= application_data.fullname, 
                                            job_role = application_data.rolename,
                                            position = application_data.position,
                                            department = application_data.department,
                                            app_deadline = application_data.application_deadline,
                                            suitability_score = suitability_score,

                                            first_suitable_pos = first_suitable_pos,
                                            second_suitable_pos = second_suitable_pos,
                                            third_suitable_pos = third_suitable_pos,

                                            first_suitable_dep = first_suitable_dep,
                                            second_suitable_dep = second_suitable_dep,
                                            third_suitable_dep = third_suitable_dep,

                                            first_score = first_score,
                                            second_score = second_score,
                                            third_score = third_score
                                            )

    organization_inform_email.set_content(org_content,subtype="html")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:   # to the actual email, required smtp.ehlo() and smtp.starttls() code

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        smtp.send_message(organization_inform_email)

        print("An email has been sent to while the questions selection emails are being submmitted to", application_data.employee_email )
    
    conn.close()
    
    if dummy_data == {}:
        response = jsonify({'Response': 'No question with this ID in the database' } )
        response.headers.add("Access-Control-Allow-Origin","*")
        return response

    response = jsonify({'Response': 'The suggested questions are being recorded, pending selection' } )
    response.headers.add("Access-Control-Allow-Origin","*")
    return response



@app.route('/displayAllSpecificQuestions/<application_id>', methods=['GET'])
@token_required
def displaySpecificQuestions(current_user,application_id):

    for i in current_user:
        if i.role != 'admin':
            response = jsonify({ 'response':'Unauthorized, 401' })
            response.headers.add("Access-Control-Allow-Origin","*")
            return response

    conn = engine.connect()

    query = "SELECT question_id FROM questions_answered WHERE application_id = " + str(application_id)
    all_q_id = conn.execute(query).fetchall()

    specific_q_id = []
    output = []

    for i in all_q_id:
        query = "SELECT * FROM questions WHERE question_id = " + str(i.question_id)
        question_data = conn.execute(query).fetchall()[0]
        question_type = question_data.question_type
        if question_type == 'specific':
            specific_q_id.append(i.question_id)

    for j in specific_q_id:
        data = {}
        query2 = "SELECT question FROM questions WHERE question_id = " + str(j)
        data['q_id'] = j
        data['question'] = conn.execute(query2).fetchall()[0].question
        output.append(data)

    response = jsonify(output)
    response.headers.add("Access-Control-Allow-Origin","*")
    return response



@app.route('/selectSpecificQuestions/<application_id>', methods=['POST'])  
@token_required
def selectQuestions(current_user,application_id):

    for i in current_user:
        if i.role != 'admin':
            response = jsonify({ 'response':'Unauthorized, 401' })
            response.headers.add("Access-Control-Allow-Origin","*")
            return response

    selection = request.json['selected_q_id']   # 2 and 7
    conn = engine.connect()

    query = "SELECT question_id FROM questions_answered WHERE application_id = " + str(application_id)
    all_q_id = conn.execute(query).fetchall()

    specific_q_id = []
    output = []

    for i in all_q_id:
        query = "SELECT * FROM questions WHERE question_id = " + str(i.question_id)
        question_data = conn.execute(query).fetchall()[0]
        question_type = question_data.question_type
        if question_type == 'specific':
            specific_q_id.append(i.question_id)

    # specific_q_id will be 2 and 7

    for j in specific_q_id:
        if j in selection:
            query2 = "UPDATE questions_answered SET selected = 1 WHERE question_id = " + str(j) + " and application_id = " + str(application_id)
            conn.execute(query2)
            output.append(j)

        # UPDATE questions_answered SET answer = 'test2' WHERE application_id not in (2,3) and question_id = '2';
        # SELECT * FROM questions_answered WHERE application_id = 99 and selected != 1;

    query_for_all_questions = "SELECT question_id FROM questions_answered WHERE application_id = " + str(application_id) + " and selected != 1"
    all_q_a_to_del = conn.execute(query_for_all_questions).fetchall()

    del_id  = []
    for k in all_q_a_to_del:
        if k not in del_id:
            del_id.append(k[0])

    for i in del_id:
        conn.execute("DELETE FROM questions_answered WHERE application_id = " + str(application_id) + " and selected != 1 and question_id in "+ str(i) )     
       
    application_query = "SELECT * FROM application WHERE application_id = " + str(application_id)

    job_id = conn.execute(application_query).fetchall()[0].job_id  
    applicant_id = conn.execute(application_query).fetchall()[0].applicant_id

    applicant_query = "SELECT * FROM applicant_information WHERE applicant_id = '" + str(applicant_id) + "'"
    applicant_name = conn.execute(applicant_query).fetchall()[0].fullname
    applicant_email = conn.execute(applicant_query).fetchall()[0].email

    job_query = "SELECT * FROM job_information WHERE job_id = " + str(job_id)
    job_role_applied = conn.execute(job_query).fetchall()[0].rolename
    application_deadline = conn.execute(job_query).fetchall()[0].application_deadline

    applicant_inform_email = EmailMessage()
    applicant_inform_email['Subject'] = "Company A Online Application : Personalized Evaluation Test Ready"
    applicant_inform_email['From'] = EMAIL_ADDRESS    # jobapplicationplatform@gmail.com
    applicant_inform_email['To'] = applicant_email
            # retrieved from the database ( the applicant's email )
    content = open("inform_applicant_for_questions.html").read().format(applicant_name=applicant_name, 
                                                        job_role=job_role_applied, 
                                                        app_deadline=application_deadline)

    applicant_inform_email.set_content(content,subtype="html")


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:   # to the actual email, required smtp.ehlo() and smtp.starttls() code

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(applicant_inform_email)
        # print("A confirmation email has been sent to", applicant_name, "( via SSL Connection ) ")
            
    stmt = " UPDATE application SET question_progress = 'Submitted' WHERE application_id = " + str(application_id)
    conn.execute(stmt)

    conn.close()
    response = jsonify({ 'Response': 'Questions has been informed to the applicant in Application ' + str(application_id) , 'q_id selected for application '+ str(application_id) : output  })
    response.headers.add("Access-Control-Allow-Origin","*")

    return response
    

@app.route('/displaySelectedQuestions', methods=['GET'])  
@token_required
def displaySelectedSpecificQuestions(current_user):

    if 'Authorization' in request.headers:
        token = request.headers['Authorization']

    if not token:
        return jsonify({'Message':'Token is missing'}), 401

    user_data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"])


    application_id = user_data['application_id']

    conn = engine.connect()

    query_for_selected_q = """SELECT questions_answered.question_id, questions.question FROM questions_answered 
    JOIN questions ON questions_answered.question_id = questions.question_id 
    WHERE questions.question_type = 'specific' and questions_answered.selected = 1 and questions_answered.application_id = """ + str(application_id)

    spec_ques_for_application = conn.execute(query_for_selected_q).fetchall()
    print(spec_ques_for_application[0])

    output = []

    for i in spec_ques_for_application:
        pair_of_q_and_q_id = {
            'q_id' : i.question_id,
            'question' : i.question
        }
        print(pair_of_q_and_q_id)
        output.append(pair_of_q_and_q_id)

    print( output , flush=True)
    response = jsonify({'questions': output } )
    response.headers.add("Access-Control-Allow-Origin","*")

    return response


@app.route('/validation/<application_id>', methods=['POST'])  
@token_required
def validation(current_user,application_id):

    for i in current_user:
        if i.role != 'admin':
            response = jsonify({ 'response':'Unauthorized, 401' })
            response.headers.add("Access-Control-Allow-Origin","*")
            return response

    conn = engine.connect()

    check_query = "SELECT validation FROM application WHERE application_id = " + str(application_id)
    validation_check = conn.execute(check_query).fetchall()[0].validation
    if validation_check != 1 :
        stmt = " UPDATE application SET validation = 1 WHERE application_id = " + str(application_id)
        conn.execute(stmt)
        stmt2 =  " UPDATE application SET validated_time = '" + str(time.strftime('%Y-%m-%d %H:%M:%S')) + "' WHERE application_id = " + str(application_id) 
        conn.execute(stmt2)
    else:
        response = jsonify({ 'Response': 'This application is already validated' })
        response.headers.add("Access-Control-Allow-Origin","*")
        return response

    response = jsonify({ 'Response': 'Application ' + str(application_id) + ' is now validated' })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response



@app.route('/devalidation/<application_id>', methods=['POST'])   
@token_required
def devalidation(current_user, application_id):

    for i in current_user:
        if i.role != 'admin':
            response = jsonify({ 'response':'Unauthorized, 401' })
            response.headers.add("Access-Control-Allow-Origin","*")
            return response

    conn = engine.connect()

    check_query = "SELECT validation FROM application WHERE application_id = " + str(application_id)
    validation_check = conn.execute(check_query).fetchall()[0].validation
    if validation_check == 1 :
        stmt = " UPDATE application SET validation = 0 WHERE application_id = " + str(application_id)
        conn.execute(stmt)
        response = jsonify({ 'Response': 'Application ' + str(application_id) + ' is now devalidated' })
        response.headers.add("Access-Control-Allow-Origin","*")
        return response
        
    else:
        response = jsonify({ 'Response': 'This application has not yet been validated' })
        response.headers.add("Access-Control-Allow-Origin","*")
        return response



@app.route('/sent_offer/<application_id>', methods=['POST']) 
@token_required 
def sentOffer(current_user, application_id):

    for i in current_user:
        if i.role != 'admin':
            response = jsonify({ 'Response': 'Unauthorized, 401' })
            response.headers.add("Access-Control-Allow-Origin","*")
            return response

    conn = engine.connect()

    application_query = "SELECT * FROM application WHERE application_id = " + str(application_id)
    offered_check = conn.execute(application_query).fetchall()[0].sent_offer



    if offered_check != 1 : 

        job_id = conn.execute(application_query).fetchall()[0].job_id  
        applicant_id = conn.execute(application_query).fetchall()[0].applicant_id

        applicant_query = "SELECT * FROM applicant_information WHERE applicant_id = '" + str(applicant_id) + "'"
        applicant_name = conn.execute(applicant_query).fetchall()[0].fullname
        applicant_email = conn.execute(applicant_query).fetchall()[0].email

        job_query = "SELECT position_id , rolename FROM job_information WHERE job_id = " + str(job_id)

        job_details = conn.execute(job_query).fetchall()[0]

        pos_query = "SELECT position FROM organization_information WHERE position_id = " + str(job_details.position_id)

        pos_details = conn.execute()
            
        applicant_inform_email = EmailMessage()
        applicant_inform_email['Subject'] = "Company A Online Application : Job Offer"
        applicant_inform_email['From'] = EMAIL_ADDRESS    # jobapplicationplatform@gmail.com
        applicant_inform_email['To'] = applicant_email
        content = open("job_offer_email.html").read().format(applicant_name=applicant_name, 
                                                    job_role=job_details.rolename,
                                                    position=pos_details.position
                                                    )
        applicant_inform_email.set_content(content,subtype="html")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:   # to the actual email, required smtp.ehlo() and smtp.starttls() code

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(applicant_inform_email)

            print("A confirmation email has been sent to", applicant_name, "( via SSL Connection ) ")
        
        stmt = " UPDATE application SET sent_offer = 1 WHERE application_id = " + str(application_id)
        conn.execute(stmt)

        conn.close()
        response = jsonify({ 'Response': 'Offer has been sent to the applicant in Application ' + str(application_id) })
        response.headers.add("Access-Control-Allow-Origin","*")
        return response





@app.route('/sentQuestions/<application_id>', methods=['POST'])  
@token_required
def sentQuestion(current_user,application_id):

    for i in current_user:
        if i.role != 'admin':
            response = jsonify({ 'Response': 'Unauthorized, 401' })
            response.headers.add("Access-Control-Allow-Origin","*")
            return response

    conn = engine.connect()

    application_query = "SELECT * FROM application WHERE application_id = " + str(application_id)
    question_progress = conn.execute(application_query).fetchall()[0].question_progress


    if question_progress == 'Submitted':
        response = jsonify({ 'Response': 'Questions has already been informed to the applicant in Application ' + str(application_id) })
        response.headers.add("Access-Control-Allow-Origin","*")
        return response
       
    elif question_progress == 'Preparing':
        response = jsonify({ 'Response': 'Questions are currently being prepared' + str(application_id) })
        response.headers.add("Access-Control-Allow-Origin","*")
        return response
        
    elif question_progress == 'Ready':
        job_id = conn.execute(application_query).fetchall()[0].job_id  
        applicant_id = conn.execute(application_query).fetchall()[0].applicant_id

        applicant_query = "SELECT * FROM applicant_information WHERE applicant_id = '" + str(applicant_id) + "'"
        applicant_name = conn.execute(applicant_query).fetchall()[0].fullname
        applicant_email = conn.execute(applicant_query).fetchall()[0].email

        job_query = "SELECT * FROM job_information WHERE job_id = " + str(job_id)
        job_role_applied = conn.execute(job_query).fetchall()[0].rolename
        application_deadline = conn.execute(job_query).fetchall()[0].application_deadline

        applicant_inform_email = EmailMessage()
        applicant_inform_email['Subject'] = "Company A Online Application : Question Inform"
        applicant_inform_email['From'] = EMAIL_ADDRESS    # jobapplicationplatform@gmail.com
        applicant_inform_email['To'] = applicant_email
                # retrieved from the database ( the applicant's email )
        content = open("inform_applicant_for_questions.html").read().format(applicant_name=applicant_name, 
                                                            job_role=job_role_applied, 
                                                            app_deadline=application_deadline)

        applicant_inform_email.set_content(content,subtype="html")


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:   # to the actual email, required smtp.ehlo() and smtp.starttls() code

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(applicant_inform_email)
            print("A confirmation email has been sent to", applicant_name, "( via SSL Connection ) ")

    response = jsonify({ 'Response': 'Questions has been informed to the applicant in Application ' + str(application_id)})
    response.headers.add("Access-Control-Allow-Origin","*")
    return response


if __name__ == "__main__":
    app.run(debug=True)




