# Processing of panel metadata: imbibe .yaml, express .pdf
# By Brygg Ullmer and Aika Washington, Clemson University
# Begun 2021-09-15

import yaml
#from reportlab.pdfgen import canvas
#from PyPDF2 import PdfFileWriter, PdfFileReader

sourceYFn = "descriptives.yaml"
sourceYF  = open(sourceYFn, "r+t")
sourceYD  = yaml.safe_load(sourceYF)

#print(sourceYD)

yearsStruct = sourceYD['scgssm-alumni-awards']['years']
years = yearsStruct.keys()
print("years:", years)

sampleYear = 2011
syStruct = yearsStruct[sampleYear]
syName   = syStruct['name']

print("2011:", str(syStruct))
print("2011 name:", str(syName))


### end ###
