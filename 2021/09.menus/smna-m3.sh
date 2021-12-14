mkdir tmp
sed -n '320,1062 p' < menus.asp | egrep '^<h3>|^<th>|^<p> *&nbsp;' > tmp/m1
cat tmp/m1 | sed 's/^<h3>/ - /;s/<\/h3>$//'                 > tmp/m2
cat tmp/m2 | sed 's/^<th><cite>/   - {main: /'              > tmp/m3
cat tmp/m3 | sed 's/<\/cite>&nbsp;/, sides: /; s/<\/th>/}/' > tmp/m4
cat tmp/m4 | sed 's/^<p>.*nbsp;/      - /; s/<\/p>//;'      > tmp/m5
cat tmp/m5 | sed 's/\&amp\;/ & /g;'                         > tmp/m6

