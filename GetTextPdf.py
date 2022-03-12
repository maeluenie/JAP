#Template for text extraction from pdf

from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

import os
import glob

path = '/Users/maeluenie/Documents/GitHub/JAP/resume/'
count =0
for filename in glob.glob(os.path.join(path,'*.pdf')):
    count +=1
    with open(os.path.join(os.getcwd(), filename), 'rb') as f:
        output_string = StringIO()
        #with open(filename, 'rb') as in_file:
        parser = PDFParser(f)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
        print(output_string.getvalue())
        print('-----------------------------------------', count)