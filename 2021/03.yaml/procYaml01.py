# YAML working examples
# Brygg Ullmer, Clemson University, 2021-09-09

import yaml

yfn   = 'hospital-fields-pediatric.yaml'; yf = open(yfn, 'r')
ydata = yaml.safe_load(yf)
print("full dump of yaml parsing:", str(ydata))

L1 = ydata['fields'][0]['L']
print("Line number of first field:", L1)

### end ###
