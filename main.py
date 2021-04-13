from PyPDF2 import PdfFileMerger
from os import listdir
import os

input_dir = "{}/".format(os.path.dirname(os.path.realpath(__file__)))
print(input_dir)
merge_list = []

for x in listdir(input_dir):
    if not x.endswith('.pdf'):
        continue
    merge_list.append(input_dir + x)

merger = PdfFileMerger(strict=False)

for pdf in merge_list:
    merger.append(pdf)

merger.write("merged_pdf.pdf") #your output directory
merger.close()