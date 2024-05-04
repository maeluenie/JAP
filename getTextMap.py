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
import time

"""THIS FILE NEED TO:
    1. GET TEXT FROM PDF FILES THEN MOVE TEXT FILES TO TxtMapUncleaned DIRECTORY
    2. MOVE PDF FILES TO TEMP STATION DIRECTORY
    3. CREATE DIRECTORY FOR EACH APPLICANT"""

parent_dir = '/root/Filesys/ApplicantFolder/'
init_path = '/root/Filesys/InboundResume/'
txt_path = '/root/Filesys/TxtMapUncleaned'
temp_path = '/root/Filesys/TempStation'

# Check if there's any file in the folder
file_size = -1


while True:
    files_name = glob.glob(init_path+'*.pdf')
    if len(files_name) != 0:
        file = files_name[0]
        while file_size != os.path.getsize(file):
            file_size = os.path.getsize(file)
            time.sleep(1)
        file_size = -1
        print(file)


        # CREATE APPLICANT DIRECTORY
        fname = str(Path(file).stem)
        file_name = os.path.basename(file)
        dir_app = os.path.join(parent_dir, fname)
        if os.path.exists(dir_app):
            # print('Applicant directory existed')
            pass
        else:
            os.mkdir(dir_app)
            # print('Applicant directory created')


        # GET TEXT FROM PDF
        with open(os.path.join(os.getcwd(), file), 'rb') as f:

            output_string = StringIO()
            parser = PDFParser(f)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)

            content = output_string.getvalue()
        # print(content)    


        # WRITE TO TEXT FILE   
        complete_name = os.path.join(txt_path, fname+"_Map.txt")
        text_file = open(complete_name, 'w')
        n = text_file.write(content)
        text_file.close()
        

        # MOVE PDF FILE TO TempStation DIRECTORY
        new_name = os.path.join(temp_path, file_name)
        shutil.move(init_path + file_name, new_name)
        print('DONE')
            
    else:
        pass
