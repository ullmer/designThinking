wget 'https://en.wikipedia.org/wiki/Classification_of_the_Indigenous_peoples_of_the_Americas'
grep '^<link' Class* > class-link.html
grep wiki class-link.html | sed 's/^.*href="\/wiki.//;s/".*$//'|grep -v '^<' > class-links.url

