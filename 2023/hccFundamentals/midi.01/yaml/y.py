import yaml
yfn = 'numark-mt3-midi.yaml'
yf  = open(yfn, 'rt')
y   = yaml.safe_load(yf)
print(y)

