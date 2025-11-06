import yaml

fn='essay-cites-01a.yaml'
f = open(fn, 'rt')
y = yaml.safe_load(f)
print(y)
