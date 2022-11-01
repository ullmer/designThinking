import yaml

yfn = 'dkdc01.yaml'
yf  = open(yfn, 'rt')
y   = yaml.safe_load(yf)

print(y)

categories = y['categories']
print('categories:', categories)

### end ####
