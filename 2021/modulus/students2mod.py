fn = "students2.txt"
f  = open(fn, "r+t")

def name2initials(fullname):
  result = ""
  splitname = fullname.split()
  for name in splitname:
    result += name[0]
  return result

def id2mod(id):
  lastDigits = int(id[-2:])
  mod = lastDigits % 16 + 1
  return mod

rawlines = f.readlines()
for rawline in rawlines:
  student, email, id = rawline.rstrip().split("\t")
  initials = name2initials(student)
  modId    = id2mod(id)
    
  print(initials, modId)

### end ###
