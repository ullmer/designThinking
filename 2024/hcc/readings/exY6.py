# Example parsing class reading li
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

import yaml, traceback
from hccReadingsYaml import *

readings = Readings()
readings.loadYaml()
readings.printReadingAbbrevs()

### end ###
