# Process Clemson School of Computing research areas
# Brygg Ullmer, Clemson University, 2021-09-16

import yaml

yfn = 'soc-research-categories.yaml'
yf  = open(yfn, 'r+t')
yd  = yaml.safe_load(yf)  #yd: yaml data

#print(yd)
categories = yd.keys()
personHash = {}

print("<table>"); row = 1
headerColor = ['cccccc', 'aaaaaa']; bodyColor = ['ffffff', 'eeeeee']

for category in categories:
  fields    = yd[category]
  numFields = len(fields)
  print("<tr><td width=200 height=40 bgcolor=%s><b>%s</b></td><td bgcolor=%s>" \
     % (headerColor[row%2], category, bodyColor[row%2]))

  print(' | '.join(fields))
  print("</td></tr>"); row += 1

print("</table>")

### end ###
