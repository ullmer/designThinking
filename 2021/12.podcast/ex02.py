# https://podcastparser.readthedocs.io/en/latest/

import podcastparser
import urllib.request
import datetime

feedurl = 'https://www.southcarolinapublicradio.org/podcast/making-it-grow/rss.xml'

parsed = podcastparser.parse(feedurl, urllib.request.urlopen(feedurl))

# parsed is a dict
#import pprint
#pprint.pprint(parsed)

for entry in parsed['episodes']:
  #episode = entry[0]['episode']
  #print(len(episode))
  title, date1, link = [entry['title'], entry['published'], entry['link']]
  date2 = datetime.datetime.fromtimestamp(date1).strftime('%Y-%m-%d')

  print('%s | %s | %s...' % (title, date2, link[:15]))

### end ###
