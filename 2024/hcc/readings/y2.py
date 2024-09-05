import yaml
fn = 'ex01.yaml'
f  = open(fn, 'rt')
yd = yaml.safe_load(f)
print(yd)

y2 = yd['class']['08-29']
print("y2:", y2)
