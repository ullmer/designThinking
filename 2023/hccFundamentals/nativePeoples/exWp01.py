# Wikipedia retrieval example
# Brygg Ullmer, Clemson University
# Begun 2023-11-22

import sys, traceback 
import wikipediaapi

#https://github.com/martin-majlis/Wikipedia-API

projNameFn = 'wp-projname.txt'; projNameF = open(projNameFn, 'rt')
projName = projNameF.readlines()[0].rstrip() #first line
print("Using %s as Wikipedia user-agent" % projName)

ww=wikipediaapi.Wikipedia(user_agent=projName, language='en', 
                          extract_format=wikipediaapi.ExtractFormat.HTML)

#wpPagen = "Classification_of_the_Indigenous_peoples_of_the_Americas"
wpPagen = "Classification of the Indigenous peoples of the Americas"
wpPage  = ww.page(wpPagen)

links = wpPage.links
print("Links:", str(links))

wpText = wpPage.text #wpPage.images
print("Text:", wpText)

### end ###
