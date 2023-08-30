### Clemson Elevate evolving interactive instance ###
# Brygg Ullmer, Clemson University
# Begun 2023-08-30

import yaml

yfn = 'elevateMap01.yaml'
yf  = open(yfn, 'rt')
y   = yaml.safe_load(yfn)

bgFn = y['backdropFn']

### end ###
