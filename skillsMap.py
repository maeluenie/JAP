from cgitb import text
from distutils import filelist
from io import StringIO
import re
import os
import glob
import shutil
import time
from pathlib import Path
import requests
import json
import numpy as np
import pandas as pd
import pymysql
from pandas import json_normalize


"""THIS FILE NEED TO:
  1. GET SKILLS LIST FROM APPLICANT
  2. MAPPING APPLICANT SKILLS LIST TO EVERY POSSIBLE POSITION IN THE COMPANY
  3. CALCULATE THE MATCHING PERCENTAGE
  4. SAVE AS CSV FOR EACH APPLICANT"""

Cleanedpath = '/root/Filesys/TxtMapCleaned/'
csv_path = '/root/Filesys/Scores/'
ApplicantFolder = '/root/Filesys/ApplicantFolder/'
TempStation = '/root/Filesys/TempStation/'
InboundTesseract = '/root/Filesys/InboundTesseract/'


auth_endpoint = "https://auth.emsicloud.com/connect/token" # auth endpoint
client_id = "your_client_id" # replace 'your_client_id' with your client id from your api invite email
client_secret = "your_client_secret" # replace 'your_client_secret' with your client secret from your api invite email
scope = "emsi_open" # the scope we will used


payload = "client_id=" + client_id + "&client_secret=" + client_secret + "&grant_type=client_credentials&scope=" + scope # set credentials and scope
headers = {'content-type': 'application/x-www-form-urlencoded'} # headers for the response
access_token = json.loads((requests.request("POST", auth_endpoint, data=payload, headers=headers)).text)['access_token'] # grabs request's text and loads as JSON, then pulls the access token from that


# CONNECTION TO DATABASE
conn = pymysql.connect(host='host',
                        port=int(port_number),
                        user='user',
                        passwd='password',
                        db='defaultdb')



def extract_skills_list():
  all_skills_endpoint = "https://emsiservices.com/skills/versions/latest/skills" # List of all skills endpoint
  auth = "Authorization: Bearer " + access_token # Auth string including access token from above
  headers = {'authorization': auth} # headers
  response = requests.request("GET", all_skills_endpoint, headers=headers) # response
  response = response.json()['data'] # the data

  all_skills_df = pd.DataFrame(json_normalize(response)); # Where response is a JSON object drilled down to the level of 'data' key
  print(all_skills_df, type(all_skills_df))
  all_skills_df.to_csv('skills.csv')
  return all_skills_df
  

def find_id_by_skill_name(name_substring):
  all_skills_df = extract_skills_list() # pull all skills into a DF
  return all_skills_df[all_skills_df['name'].str.contains(name_substring)] # Filter that DF by substring


def extract_skills_from_document(text):
  skills_from_doc_endpoint = "https://emsiservices.com/skills/versions/latest/extract"
  payload = "{ \"text\": \"... " + text + " ...\",  \"confidenceThreshold\": 0.7 }"

  headers = {
      'authorization': "Bearer " + access_token,
      'content-type': "text/plain"
      }

  response = requests.request("POST", skills_from_doc_endpoint, data= payload.encode('utf-8'), headers=headers)
  skills_found_in_document_df = pd.DataFrame(json_normalize(response.json()['data']));
  skills_list = skills_found_in_document_df['skill.name'].to_list()
  return skills_list
                                 
  

def find_related_skills():
  url = "https://emsiservices.com/skills/versions/latest/related"

  # payload = "{ \"ids\": [ \"KS125LS6N7WP4S6SFTCK\", \"KSGWPO6DSN70GRY20JFT\" ] }"  
  payload = "{ \"ids\": [ \"KS122R865B9T68GPYPF2\" ] }"

  headers = {
      'authorization': "Bearer " + access_token,
      'content-type': "application/json"
      }

  response = requests.request("POST", url, data=payload, headers=headers)
  related_skills_df = pd.DataFrame(json_normalize(response.json()['data']))
  print(related_skills_df)


import re
import ast
def cleanup(txt):
    re_pattern = re.compile(r"[^a-z, ()]", re.I)
    return re.sub(re_pattern, "", txt).replace("  ", " ").strip()


AppId = []
skillList = []

file_size = -1

while True:

  # CHECK IF ANY FILES IN DIRECTORY
  Cleaned_file = glob.glob(os.path.join(Cleanedpath,'*.txt'))
  time.sleep(1)
  if len(Cleaned_file) != 0:
    file = Cleaned_file[0]
    while file_size != os.path.getsize(file):
        file_size = os.path.getsize(file)
        time.sleep(1)
    file_size = -1


    # OPEN THE FIRST FILE - GET SKILLS - STORE IN DATAFRAME
    with open(file, 'r', encoding='utf-8') as f:

      # GET APPLICANT ID
      basename = os.path.basename(file)
      data = basename.split('_')
      APid = data[0]
      print(APid)
      content = f.read()

      # EXTRACT SKILLS
      skills = extract_skills_from_document(content)
      AppId.append(APid)
      skillList.append(skills)
      applicant_df = pd.DataFrame({
        'AppID': AppId,
        'SkillName': skillList
      })

    f.close()

    # SKILLS MAPPING 
    with conn:
        with conn.cursor() as cursor:        
          sql = """SELECT * FROM organization_information;"""
          cursor.execute(sql)
          query = cursor.fetchall() 
          pos_skills = pd.DataFrame(query, columns=['position_id', 'department', 'position','competencies','skills','skills_map'])

          sql2 = """SELECT organization_information.department, organization_information.position
                    FROM application
                    JOIN job_information ON application.job_id = job_information.job_id
                    JOIN organization_information ON job_information.position_id = organization_information.position_id
                    WHERE application.applicant_id = %s;"""
          cursor.execute(sql2, (str(APid)))
          query2 = cursor.fetchone()
          position = query2[1]
          print(position,"position")

    pos_skills['skills_map'] = pos_skills['skills_map'].apply(cleanup)
    pos_skills['skills_map'] = pos_skills['skills_map'].str.split(',')

    for i in pos_skills['skills_map']:
      for j in range(len(i)):
          i[j] = i[j].strip()

    column_names =['appID','department', 'position', 'score', 'skills_found']
    appInfo = pd.DataFrame(columns = column_names)
    appInfo

    print(applicant_df)

    for index, row in applicant_df.iterrows():
      items = set(row['SkillName'])
      for i, r in pos_skills.iterrows():
          sk = set(r['skills_map'])
          found = sk.intersection(items)
          score = ( (0.8 * ( (len(sk.intersection(items))) / (len(items)) )) + (0.2 * ( (len(sk.intersection(items))) / (len(sk)) )) ) * 100 
          appInfo.loc[len(appInfo.index)] = [row['AppID'], r['department'],r['position'], score, found]
    
    rowPos = appInfo.loc[appInfo['position'] == position]

    appInfo = appInfo.sort_values(by='score', ascending=False)
    appInfo = appInfo.head(3)

    rows = rowPos.iloc[:1]
    appInfo = appInfo.append(rows, ignore_index=True)
    print(appInfo)

    appInfo.to_csv(csv_path+APid+'_Score.csv')  

    newPath = os.path.join(ApplicantFolder+APid+'/'+APid+'_Mapped.txt')
    shutil.move(Cleanedpath+basename, newPath)

    newPath2 = os.path.join(InboundTesseract+APid+'.pdf') 
    shutil.move(TempStation+APid+'.pdf', newPath2)

    print('done')
    # cursor.close()
    # conn.close()
  else:
    pass