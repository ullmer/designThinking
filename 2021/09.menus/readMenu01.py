import yaml

yfn = 'smna-m4.yaml'
yf  = open(yfn, 'r+t')
yd  = yaml.safe_load(yf)

print(yd)

### end ### 

