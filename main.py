""" 
Page2Setup main file.
Author: Eric Greenhalgh
Created: 5/20/2020
The purpose of this program is to take a proeprty list from an excel sheet, open each 
property's service contract and extract the billing methods. The active billing methods 
for the property will then be pulled from a seperate excel file that has the billing 
methodology for each property. A comparison will then be made between the methods and 
show what matches and what varies from the service contract. The results will then be 
saved in another excel file.
"""
import pdfminer

# Open the service agreement PDF
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 2
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

pdf = convert_pdf_to_txt(
    'files\wm66 Waterstone at Moorpark RUBS Billing Agreement (2).pdf'
)
# print(pdf)

from tabula import read_pdf

df = read_pdf(
    "files\wm66 Waterstone at Moorpark RUBS Billing Agreement (2).pdf",
    pages = "all",
    multiple_tables = True
)

print(df)

# Read the service agreement PDF
# Extract the billing methods from the service agreementPDF

