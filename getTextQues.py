import os
import glob
# import cv2
from PIL import Image
from pathlib import Path
from pdf2image import convert_from_path
import pytesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
import time
import shutil

resume_files_path = '/root/Filesys/InboundTesseract/'
applicant_folder_path = '/root/Filesys/ApplicantFolder/'
resume_txt_path = '/root/Filesys/TxtQuesUncleaned/'
resume_images_path = '/root/Filesys/TxtQuesImage/'


file_size = -1
img_size = -1
while True:
    textFile = glob.glob(os.path.join(resume_files_path,'*.pdf'))
    time.sleep(1)
    if len(textFile) != 0:
        file = textFile[0]
        while file_size != os.path.getsize(file):
            file_size = os.path.getsize(file)
            time.sleep(1)
        file_size = -1

        print(file)
        fname = str(Path(file).stem)
        pages = convert_from_path(file)
    #     print(pages)
        for page in pages:
            image_name = resume_images_path + fname + ".jpg"  
    #         print(image_name)
            if os.path.exists(image_name):
                data = os.path.splitext(image_name)
                only_name = data[0]
                extension = data[1]
    #             print(only_name)
                new_base = only_name + '_2' + extension
                page.save(new_base, "JPEG")
    #             print('back page added')
            else:
                page.save(image_name, "JPEG")
    #             print('page 1')

        shutil.move(file, applicant_folder_path+fname+'/'+fname+'.pdf')

        while img_size != os.path.getsize(image_name):
            img_size = os.path.getsize(image_name)
            time.sleep(1)
        img_size = -1


        img = str(Path(image_name).stem)
        length = len(img)
        last_char = img[length -2:]
        
        content = pytesseract.image_to_string(Image.open(image_name))
        if content != "":
            if last_char == '_2':
                new_txt_file = resume_txt_path + img[:-2] + '.txt'
                text_file = open(new_txt_file, 'a')
            else:
                new_txt_file = resume_txt_path + img + '.txt'
                text_file = open(new_txt_file, 'a')

            n = text_file.write(content)
            text_file.close()
        else:
            print('No content')

        shutil.move(image_name, applicant_folder_path+fname+'/'+fname+'.jpg')
