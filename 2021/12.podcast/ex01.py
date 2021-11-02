# https://podcastparser.readthedocs.io/en/latest/

import podcastparser
import urllib.request

feedurl = 'https://www.southcarolinapublicradio.org/podcast/making-it-grow/rss.xml'

parsed = podcastparser.parse(feedurl, urllib.request.urlopen(feedurl))

# parsed is a dict
import pprint
pprint.pprint(parsed)

### end ###
