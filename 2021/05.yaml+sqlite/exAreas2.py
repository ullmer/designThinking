# Process Clemson School of Computing research areas
# Brygg Ullmer, Clemson University, 2021-09-16

import yaml

yfn = 'soc-research-categories.yaml'
yf  = open(yfn, 'r+t')
yd  = yaml.safe_load(yf)  #yd: yaml data
#print(yd)

categories = yd.keys(); personHash = {}; numColumns = 3
print("<table>")

for category in categories:
  fields    = yd[category]
  numFields = len(fields)
  print("<tr><td bgcolor=cccccc colspan=%i><b>%s</b></td></tr> <tr>" % \
    (numColumns, category))

  idx = 1 
  for field in fields:
    numPeople = len(fields[field])
    print("<td>%s (%i)</td>" % (field, numPeople))
    if idx % numColumns == 0: print("</tr><tr>")
    idx += 1

  print("</tr>")
print("</table>")

### end ###
