#Progressive intersections of example Matplotlib/pyplot code and COVID datasets
#Brygg Ullmer, Clemson University
#Begun 2021-09-07
#https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

import csv, sys, traceback, matplotlib.pyplot as plt

covidF        = open('procHospital9.csv')
dataReader    = csv.reader(covidF, delimiter=',');

names = []; values = []
for row in dataReader:
  try:
    state, city, date, d1, d2, d3, d4 = row
    names.append(city); values.append(d1)
  except: pass

plt.figure(); plt.bar(names, values); plt.show()

### end ###

