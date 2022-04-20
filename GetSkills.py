from cgitb import text
from io import StringIO

import os
import glob
import nltk
#solve nltk can't download needed files
# import ssl
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

import requests
import json
import numpy as np
import pandas as pd
import pymysql
from pandas import json_normalize # easy JSON -> pd.DataFrame

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# nltk.download('stopwords')

path = '/Users/maeluenie/Desktop/capstone project/processed text files/'

auth_endpoint = "https://auth.emsicloud.com/connect/token" # auth endpoint
client_id = "your_client_id" # replace 'your_client_id' with your client id from your api invite email
client_secret = "your_client_secret" # replace 'your_client_secret' with your client secret from your api invite email
scope = "emsi_open" # ok to leave as is, this is the scope we will used

payload = "client_id=" + client_id + "&client_secret=" + client_secret + "&grant_type=client_credentials&scope=" + scope # set credentials and scope
headers = {'content-type': 'application/x-www-form-urlencoded'} # headers for the response
access_token = json.loads((requests.request("POST", auth_endpoint, data=payload, headers=headers)).text)['access_token'] # grabs request's text and loads as JSON, then pulls the access token from that

# connection to database
conn = pymysql.connect(host='host',port=int('port_number'),
                        user='user',passwd='password',db='schema')


def extract_skills_list():
  all_skills_endpoint = "https://emsiservices.com/skills/versions/latest/skills" # List of all skills endpoint
  auth = "Authorization: Bearer " + access_token
  headers = {'authorization': auth} # headers
  response = requests.request("GET", all_skills_endpoint, headers=headers) # response
  response = response.json()['data'] # data

  all_skills_df = pd.DataFrame(json_normalize(response));
  print(all_skills_df, type(all_skills_df))
#   all_skills_df.to_csv('skills.csv')
  return all_skills_df
  
# extract_skills_list()

def find_id_by_skill_name(name_substring):
  all_skills_df = extract_skills_list() # pull all skills into a DF

  return all_skills_df[all_skills_df['name'].str.contains(name_substring)] # Filter that DF by substring

# find_id_by_skill_name("Python")

def extract_skills_from_document(text):
  skills_from_doc_endpoint = "https://emsiservices.com/skills/versions/latest/extract"
  # confidence_interval = str(0.4)
  payload = "{ \"text\": \"... " + text + " ...\",  \"confidenceThreshold\": 0.4 }"

  headers = {
      'authorization': "Bearer " + access_token,
      'content-type': "text/plain"
      }

  # data = payload.encode('utf-8')
  print(payload)
  print('----------------------------')
  response = requests.request("POST", skills_from_doc_endpoint, data= payload, headers=headers)
  skills_found_in_document_df = pd.DataFrame(json_normalize(response.json()['data'])); # response is a JSON object
  print(skills_found_in_document_df[["skill.name"]])  
  # skills_found_in_document_df.to_csv('skills_found.csv')                                   
  # print(skills_found_in_document_df)
  # return skills_found_in_document_df
  
# extract_skills_from_document()

def find_related_skills(payload):
  url = "https://emsiservices.com/skills/versions/latest/related"

  payload = "{ \"ids\": [ \"KS125LS6N7WP4S6SFTCK\", \"KSGWPO6DSN70GRY20JFT\" ] }"
  headers = {
      'authorization': "Bearer " + access_token,
      'content-type': "application/json"
      }

  response = requests.request("POST", url, data=payload, headers=headers)
  related_skills_df = pd.DataFrame(json_normalize(response.json()['data']))
  print(related_skills_df)



for filename in glob.glob(os.path.join(path,'*.txt')):
    with open(filename, 'r') as f:
      content = f.read()

      extract_skills_from_document(content)

    f.close()
    print('done')







