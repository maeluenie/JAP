from cgitb import text
from io import StringIO
from pathlib import Path

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

import os
from os import path
import shutil
import glob
import numpy as np
import pandas as pd
from pandas import json_normalize # easy JSON -> pd.DataFrame

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# nltk.download('stopwords')

# Logic - get applicant name - create applicant's dir - get text - store in text folders separately - move processed resume to applicant dir
parent_dir = '/Users/maeluenie/Desktop/capstone project/'
init_path = '/Users/maeluenie/Desktop/capstone project/unprocessed resume/'
txt_path = '/Users/maeluenie/Desktop/capstone project/resume text files/'

# Check if there's any file in the folder
files_count = len(next(os.walk(init_path))[2])

temp_input = {
    'applicant_id':'id', 
    'fullname':'name', 
    'citizen_id':'citizen id', 
    'contact_number':'number', 
    'email':'email', 
    'age': 22, 
    'DOB':'datetime',
    'nationality':'nationality',
    'religion':'religion', 
    'degree':'degree',
    'GPA':'gpa',
    'address':'address', 
    'gender':'gender',
    'martial_status':'status',
    'military_status':'status' 
}

# print(files_count)
if files_count != 0:
    print('Files exist')
    # Check if this resume have been processed before
    for file in glob.glob(os.path.join(init_path,'*.pdf')):
        file_name = os.path.basename(file)
        print(file_name)
        # print(temp_input['fullname'])
        dir_app = os.path.join(parent_dir, temp_input['fullname'])
        if os.path.exists(dir_app):
            print('Applicant directory existed')
        else:
            os.mkdir(dir_app)
            print('Applicant directory created')

        # extract text from pdf files
        with open(os.path.join(os.getcwd(), file), 'rb') as f:

            output_string = StringIO()
            # with open(filename, 'rb') as in_file:
            parser = PDFParser(f)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)

            content = output_string.getvalue()
        
        fname = str(Path(file).stem)
        complete_name = os.path.join(txt_path, fname+".txt")
        text_file = open(complete_name, 'w')
        n = text_file.write(content)
        # for line in text_file:
        #     if not line.isspace():
        #             text_file.write(line)
        text_file.close()
        

        # move processed PDF file to the applicants folder
        # check if file exist in destination
        app_res = os.path.join(dir_app, file_name)
        print(app_res)
        if os.path.exists(app_res):
            # Split name and extension
            data = os.path.splitext(file_name)
            only_name = data[0]
            extension = data[1]
            # Adding the new name
            new_base = only_name + '_new' + extension
            # construct full file path
            new_name = os.path.join(dir_app, new_base)
            # move file
            print(new_name)
            shutil.move(init_path + file_name, new_name)
        else:
            print(app_res)
            shutil.move(init_path + file_name, app_res)
        print('All done')
    
else:
    print('no file exist')
