# Processing of panel metadata: imbibe .yaml, express .pdf
# By Brygg Ullmer and Aika Washington, Clemson University
# Begun 2021-09-15

import yaml
#from reportlab.pdfgen import canvas
#from PyPDF2 import PdfFileWriter, PdfFileReader

sourceYFn = "descriptives.yaml"
sourceYF  = open(sourceYFn, "r+t")
sourceYD  = yaml.safe_load(sourceYF)

print(sourceYD)

### end ###
