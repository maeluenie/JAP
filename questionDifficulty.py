from hashlib import new
import os
import re
import requests
import json
import pandas as pd
from pandas import json_normalize
import warnings
warnings.filterwarnings("ignore")
import pymysql
import time, glob
import shutil

Headerlist = ['SKILLS','SKILL','Skill','Skills','EXPERIENCES','EXPERIENCE','AboutMe','Experience','Experiences', 'Work History','WORK HISTORY','Project','Projects','PROJECTS','PROJECT','Internship','INTERNSHIP','PROFILE','ABOUT ME','ABOUTME','Aboutme','About me','Profile','Interests','INTERESTS','Interest','INTEREST','ACTIVITY','ACTIVITIES','Activity','Activities','Achivement','ACHIVEMENT','Achivements','ACHIVEMENTS']

TxtCleaned = '/root/Filesys/TxtQuesCleaned/'
destination_path = '/root/Filesys/ApplicantFolder/'
CsvPath = '/root/Filesys/Scores/'

SkillsGroup = ['SKILLS','SKILL','PROJECTS','Skill','Skills','Project','Projects','PROJECT','Interests','INTERESTS','Interest','INTEREST','ACTIVITY','ACTIVITIES','Activity','Activities']
ExperiencesGroup =['EXPERIENCES','EXPERIENCE','INTERNSHIP','Experience','Experiences','Internship', 'Work History','WORK HISTORY','Achivement','ACHIVEMENT','Achivements','ACHIVEMENTS']
ProfileGroup = ['PROFILE','ABOUT ME','ABOUTME','Profile','About Me','Aboutme','AboutMe']

auth_endpoint = "https://auth.emsicloud.com/connect/token" # auth endpoint
client_id = "your_client_id" # replace 'your_client_id' with your client id from your api invite email
client_secret = "your_client_secret" # replace 'your_client_secret' with your client secret from your api invite email
scope = "emsi_open" # ok to leave as is, this is the scope we will used

payload = "client_id=" + client_id + "&client_secret=" + client_secret + "&grant_type=client_credentials&scope=" + scope # set credentials and scope
headers = {'content-type': 'application/x-www-form-urlencoded'} # headers for the response
access_token = json.loads((requests.request("POST", auth_endpoint, data=payload, headers=headers)).text)['access_token']

URL = 'https://api.job-application.duckdns.org/pairSelectedQuestions'

def extract_skills_from_document(text):
    tempList = []
    skills_from_doc_endpoint = "https://emsiservices.com/skills/versions/latest/extract"
    payload = "{ \"text\": \"... " + text + " ...\",  \"confidenceThreshold\": 0.7 }"

    headers = {
        'authorization': "Bearer " + access_token,
        'content-type': "text/plain"
        }

    response = requests.request("POST", skills_from_doc_endpoint, data= payload.encode('utf-8'), headers=headers)
    skills_found_in_document_df = pd.DataFrame(json_normalize(response.json()['data']));
    if  'skill.name' in skills_found_in_document_df :
        skills_list = skills_found_in_document_df['skill.name'].to_list()
        return skills_list
    else: 
        return tempList

file_size = -1

while True:
    textFile = glob.glob(os.path.join(TxtCleaned,'*.txt'))
    time.sleep(1)
    if len(textFile) != 0:
        file = textFile[0]
        while file_size != os.path.getsize(file):
            file_size = os.path.getsize(file)
            time.sleep(1)
        file_size = -1

        file_name = os.path.basename(file)
        data = file_name.split('_')
        apID = data[0]
        print(apID)


        #temp info should be the position he applied for
        # user_input = filename/applicant id
        conn = pymysql.connect(host='host',
                                port=int(port_number),
                                user='user',
                                passwd='password',
                                db='defaultdb')

        with conn:
            with conn.cursor() as cursor:
                sql = """SELECT organization_information.department, organization_information.position
                            FROM application
                            JOIN job_information ON application.job_id = job_information.job_id
                            JOIN organization_information ON job_information.position_id = organization_information.position_id
                            WHERE application.applicant_id = %s;"""
                cursor.execute(sql, (str(apID)))
                query = cursor.fetchone()
                position = query[1]

                sql2 = """select skills_map from organization_information where organization_information.position = %s"""
                cursor.execute(sql2, (position))
                query2 = cursor.fetchone()

        # print(query2, type(query2), position)

        pos_skills = query2[0]
        # print(pos_skills, type(pos_skills))
        pos_skills = pos_skills.split(',')
        # pos_skills['skills_map'] = pos_skills.skills_map.apply(lambda x: x[1:-1].split(','))                                   
        # positionSkill = pos_skills.iat[0,0]
        requiredSkills = []
        # # print(positionSkill,type(positionSkill))
        for j in pos_skills:
            j = j.replace("'",'')
            j = j.replace("[",'')
            j = j.replace("]",'')
            j = j.strip()
            print(j)
            requiredSkills.append(j)
        # print(requiredSkills)


        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()


        stat = ''
        mydict = {}
        newdict = {}
        fname = []
        cat = [] 
        skills = []
        checkPopList = [] 
        popList = []
        temp = []


        if len(content) > 0 :
            text = re.split(r'\W+',content)

            #extract text from location according to header list
            for i in text:
                if i in Headerlist:
                    stat = i
                    mydict[stat] = []
                elif i not in Headerlist and stat != '':
                    mydict[stat] += [i]
                else:
                    pass

            #remove values that cannot be used to extract skills       
            for k, v in mydict.items():
                if len(v) <= 5:
                    checkPopList.append(k)
            for i in checkPopList:
                mydict.pop(i)

            #change list to one string for function input
            for k, v in mydict.items():
                # print(k,v)
                temp = ' '.join(str(e) for e in v)
                # print(temp)
                newdict[k]= temp

        # print(newdict)

            #removing key that have an empty values
            for k,v in newdict.items():
                if v == '':
                    popList.append(k)
            for i in popList:
                newdict.pop(i)

            #extract skills from key values
            for key, values in newdict.items():
                skill_val = extract_skills_from_document(values)
                
                fname.append(apID)
                cat.append(key)
                skills.append(skill_val)
                
            data = {
                'name': fname,
                'category': cat,
                'skills': skills
            }

            table = pd.DataFrame(data)
            # table.to_csv('temp.csv')
            print(table)

        stat = ''
        mydict = {}
        newdict = {}
        fname.clear()
        cat.clear()
        skills.clear()
        popList.clear()
        checkPopList.clear()
        f.close()

        sk = 0
        ex = 0
        pr = 0
        sk_temp = []
        ex_temp = []
        pr_temp = []
        NewList = []
        level1 = []
        level2 = []
        level3 = []
        finalAP = []
        finalPos = []
        finalname = []
        finalscore = []

        for i in table['category']:
            # print(i)
            if i in SkillsGroup:
                sk += 1
                sk_temp.append(i)
            if i in ExperiencesGroup:
                ex += 1
                ex_temp.append(i)
            elif i in ProfileGroup:
                pr +=1
                pr_temp.append(i)


        for i in ex_temp:
            # print(i)
            row = table.loc[table['category'] == i]
            
            for n in row['skills']:
                check = type(n) == str
                # print(check)
                if check == True:
                    row['skills'] = row.skills.apply(lambda x: x[1:-1].split(','))
                else:
                    break
            
            for j in row['skills']:
                # print(len(j))
                for k in j:
                    k = k.replace("'",'')
                    k = k.strip()
                    # print(k)
                    level3.append(k)

            level3 = list(dict.fromkeys(level3))


        for i in sk_temp:
            # print(i)
            row = table.loc[table['category'] == i]
            
            for n in row['skills']:
                check = type(n) == str
                # print(check)
                if check == True:
                    row['skills'] = row.skills.apply(lambda x: x[1:-1].split(','))
                else:
                    break
            
            for j in row['skills']:
                # print(len(j))
                for k in j:
                    k = k.replace("'",'')
                    k = k.strip()
                    # print(k)
                    level2.append(k)
                
            level2 = list(dict.fromkeys(level2))               


        for i in pr_temp:
            # print(i)
            row = table.loc[table['category'] == i]
            
            for n in row['skills']:
                check = type(n) == str
                # print(check)
                if check == True:
                    row['skills'] = row.skills.apply(lambda x: x[1:-1].split(','))
                else:
                    break
            
            for j in row['skills']:
                # print(len(j))
                for k in j:
                    k = k.replace("'",'')
                    k = k.strip()
                    # print(k)
                    level1.append(k)

            level1 = list(dict.fromkeys(level1))

        print('Profile:',level1)
        print('Skills:',level2)
        print('Experiences:',level3)

        requiredSkills = set(requiredSkills)
        lv1 = set(level1) 
        lv2 = set(level2)
        lv3 = set(level3)

        foundlv1 = requiredSkills.intersection(lv1)
        foundlv2 = requiredSkills.intersection(lv2)
        foundlv3 = requiredSkills.intersection(lv3)

        duplicateSklExp = foundlv3 & foundlv2
        for i in duplicateSklExp:
            if i in foundlv2:
                foundlv2.remove(i)
        # print(foundlv2)

        duplicatePrfExp = foundlv3 & foundlv1
        for i in duplicatePrfExp:
            if i in foundlv1:
                foundlv1.remove(i)
        # print(foundlv1)

        duplicatePrfSkl = foundlv2 & foundlv1
        for i in duplicatePrfSkl:
            if i in foundlv1:
                foundlv1.remove(i)
        # print(foundlv1)

        print(foundlv1)
        print(foundlv2)
        print(foundlv3)
            
        for i in foundlv3:
            finalAP.append(apID)
            finalPos.append(position)
            finalname.append(i)
            finalscore.append(3)

        for i in foundlv2:
            finalAP.append(apID)    
            finalPos.append(position)
            finalname.append(i)
            finalscore.append(2)

        for i in foundlv1:
            finalAP.append(apID)
            finalPos.append(position)
            finalname.append(i)
            finalscore.append(1)

        print(finalname)
        print(finalscore)

        finaldata = {
                'name':finalAP,
                'position':finalPos,
                'skills': finalname,
                'difficulty': finalscore
            }

        finaltable = pd.DataFrame(finaldata)
        print(finaltable)
        # finaltable.to_csv('finaltable.csv')

        ques_id = []
        ques_ques = []
        ques_key = []
        skill_input = []

        final_quesid = []

        conn2 = pymysql.connect(host='host',
                                port=int(port_number),
                                user='user',
                                passwd='password',
                                db='defaultdb')

        with conn2:
            with conn2.cursor() as cursor2:
                for index, row in finaltable.iterrows():
                        keys_temp = []
                        pos_input = row['position']
                        dif_input = row['difficulty']
                        ski_input = row['skills']

                        sql = """SELECT questions.question_id, questions.question, questions.question_keywords FROM questions 
                                WHERE questions.question_position = %s and questions.question_difficulty = %s;"""
                        cursor2.execute(sql, (pos_input, dif_input))
                        query = cursor2.fetchone()  
                        ques_id.append(query[0])
                        ques_ques.append(query[1])
                        keys = query[2].split(',')

                        for j in keys:
                                j = j.strip()
                                print(j)
                                keys_temp.append(j)
                        ques_key.append(keys_temp)
                        skill_input.append(ski_input)
                keys_temp.clear()
                print(ques_key)
                map_data = {
                        'qid': ques_id,
                        'qname': ques_ques,
                        'qkey': ques_key
                }
                map_table = pd.DataFrame(map_data)
                map_table = map_table.drop_duplicates(subset=["qid"], keep='first')
            print(map_table)

            for index, row in map_table.iterrows():
                    for t in row['qkey']:
                            for i in skill_input:
                                    if t == i:
                                            # print(i, t)
                                            # print('found duplicate -------')
                                            final_quesid.append(row['qid'])
            final_quesid = list(set(final_quesid))
            print('After filter the questions id are:' ,final_quesid)

        shutil.move(file, destination_path+apID+'/'+file_name+'_Questioned.txt')

        score_table = pd.read_csv(CsvPath + apID + '_Score.csv')

        val = score_table[score_table['position'] == position]
        score = val.iloc[0]['score']

        top3Department = score_table.iloc[:3]['department']
        top3Position = score_table.iloc[:3]['position']
        top3Score = score_table.iloc[:3]['score']

        suitedDepartment = []
        suitedPosition = []
        suitedScore = []
        for i in top3Department:
            suitedDepartment.append(i)

        for i in top3Position:
            suitedPosition.append(i)

        for i in top3Score:
            suitedScore.append(i)

        print(suitedScore)
        print(suitedPosition)
        print(suitedDepartment)

        shutil.move(CsvPath + apID + '_Score.csv', destination_path+apID+'/'+apID+'_Scored.csv')

        send_data = {
            'applicant_id' : apID,
            'q_id' : final_quesid,
            'applied_score' : 12,
            'suited_dept' : suitedDepartment,
            'suited_pos' : suitedPosition,
            'score' : suitedScore
        }

        print(send_data)

        json_send_data = json.dumps(send_data)
        load_send_data = json.loads(json_send_data)

        print(load_send_data, type(load_send_data))

        r = requests.post(URL, json = load_send_data)

        print(r)
        pastebin_url = r.text
        print("Response:%s"%pastebin_url)
        print('Sent email')


