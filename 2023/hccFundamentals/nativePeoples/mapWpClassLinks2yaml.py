# Hacky mapping of Wikipedia class links to yaml using sdow.db3
# Brygg Ullmer, Clemson University
# Begun 2023-11-22

sourceFn = 'class-links.url' #list of category page titles
sourceF  = open(sourceFn, 'rt')
rawlines = sourceF.readlines()

for rawline in rawlines:
  cleanling = rawline.rstrip()

### end ###
