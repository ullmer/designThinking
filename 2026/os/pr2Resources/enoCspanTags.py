import yaml

fn='cspan-tags.yaml'
f =open(fn, 'rt')
yd=yaml.safe_load(f)

tags = yd['tags']
print("Tags:", tags)

### end ###
