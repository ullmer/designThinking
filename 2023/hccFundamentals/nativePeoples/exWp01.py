import wikipediaapi

ww=wikipediaapi.Wikipedia('en')

wpPagen = "Classification of the Indigenous peoples of the Americas"
wpPage  = ww.page(wpPagen)

wpText = wpPage.text #wpPage.images
print(wpText)

### end ###
