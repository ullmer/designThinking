import yaml

fn='essay-cites-01a.yaml'
f = open(fn, 'rt', encoding='utf-8')
y = yaml.safe_load(f)
print(y)
