import yaml

fn='cspan-tags.yaml'
f =open(fn, 'rt')
yd=yaml.safe_load(f)

tags = yd['tags']
#print("Tags:", tags)

hashstr = '#' * 10

for tag in tags:
  try:
    taggedList    = tags[tag]
    taggedListLen = len(taggedList)
    catName       = taggedList[0]['catName']

    print(hashstr, tag, ':', catName, hashstr)
  except: print(">> ignoring error on tag", tag)

### end ###
