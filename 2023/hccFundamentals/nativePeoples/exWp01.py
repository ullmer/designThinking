# Wikipedia retrieval example
# Brygg Ullmer, Clemson University
# Begun 2023-11-22

import wikipediaapi
#https://github.com/martin-majlis/Wikipedia-API

projNameFn = 'wp-projname.txt'; projNameF = open(projNameFn, 'rt')
projName = projNameFn.readlines[0].rstrip() #first line
print("Using %s as Wikipedia user-agent" % projName)
sys.exit(-1)

ww=wikipediaapi.Wikipedia(user_agent=projName, language='en')

wpPagen = "Classification of the Indigenous peoples of the Americas"
wpPage  = ww.page(wpPagen)

wpText = wpPage.text #wpPage.images
print(wpText)

### end ###
