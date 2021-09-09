# YAML working examples
# Brygg Ullmer, Clemson University, 2021-09-09

import yaml

yfn   = 'hospital-fields-pediatric.yaml'; yf = open(yfn, 'r')
ydata = yaml.safe_load(yf)
print(ydata)

### end ###
