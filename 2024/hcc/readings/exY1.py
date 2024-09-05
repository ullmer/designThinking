import yaml
fn = 'index.yaml'
f  = open(fn, 'rt')
yd = yaml.safe_load(f)
print(yd)
