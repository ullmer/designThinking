#Progressive intersections of example Matplotlib/pyplot code and COVID datasets
#Brygg Ullmer, Clemson University
#Begun 2021-09-07
#https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

import csv, sys, traceback, matplotlib.pyplot as plt

covidF        = open('procHospital8a.csv')
dataReader    = csv.reader(covidF, delimiter=',');

names = []; values = []
for row in dataReader:
  try:
    state, city, date, pAdultBedsCovid, pAdultBedsFull, pICUcovid, pICUfull = row
    names.append(city); values.append(pICUfull)
  except: pass

plt.figure(); subplot = plt.subplot(); subplot.invert_yaxis()
plt.barh(names, values); plt.show()

### end ###

