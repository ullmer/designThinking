import yaml
fn = 'ex01.yaml'
f  = open(fn, 'rt')
yd = yaml.safe_load(f)
print(yd)
