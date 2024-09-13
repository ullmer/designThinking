#basapparhearavandur.yaml:possibleProjectThemeName: How Culture impacts Human-AI Interaction
#beckerstephen.yaml:possibleProjectThemeName: MCI & AI Smartphone Systems
#childerslaythonthomas.yaml:possibleProjectThemeName: Technology assisting disabled users

import sys
lines = sys.stdin.readlines()

for line in lines:
  nameLetters  = line[:5] #extract the first five letters
  idx          = line.find(": ") #find the ": " as a demarcation
  themeName    = line[idx:]
  themeLetters = themeName.strip()[:5]
  print(nameLetters, ':', themeLetters, ';', end='')

