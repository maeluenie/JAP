import requests
import json
import numpy as np
import pandas as pd
import pymysql
import re

import warnings
warnings.filterwarnings('ignore')

# connection to database
conn = pymysql.connect(host='host',port=int('port_number'),
                        user='user',passwd='password',db='schema')

questions_table = pd.read_sql_query("SELECT * FROM questions", conn)
skills_table = pd.read_sql_query("SELECT * FROM skills", conn)

df = pd.read_csv('skills_extraction.csv')
df = df.drop(labels='Unnamed: 0', axis =1)
df['SkillName'] = df.SkillName.apply(lambda x: x[1:-1].split(','))



for index, row in df.iterrows():
    # print(row['FileName'])
    temp_list = []
    for i in row['SkillName']:
        newi = i.replace("'","")
        # print(newi)        
        temp_list.append(newi)
        row['SkillName'] = temp_list

temp = ""
name = []
final =[]
# NewtextFile = open("path_to_textfile", 'a', encoding='utf-8')

def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

# store only questions where it is not empty and delete duplicate questions
for i, r in df.iterrows():
    # sep = ' - '
    # newname = r['FileName'].split(sep, 1)[0]
    questions = []
    # NewtextFile.write("\n"+str(r['FileName']))
    for n in r['SkillName']:
        # print(n)
        temp = pd.read_sql_query("SELECT questions.id FROM questions WHERE questions.keywords LIKE '%" + n + "%'", conn)
        print(temp)
        if len(temp) != 0:
            new = temp['id'].to_list()
            for x in range(len(new)):
                questions.append(new[x])
            # NewtextFile.write(n+"\n"+str(temp)+"\n")
            # NewtextFile.close()
            if checkIfDuplicates_1(questions) == True:
                # print('duplicate in list')
                questions = list(dict.fromkeys(questions))
    name.append(r['FileName'])          
    final.append(questions) 

data = {
    "FileName" : name,
    "Questions": final
}
table = pd. DataFrame(data)
# table.to_csv('init_questions.csv')        


