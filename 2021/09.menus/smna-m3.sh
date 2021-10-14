mkdir tmp
sed -n '320,1062 p' < menus.asp | egrep '^<h3>|^<th>|^<p> *&nbsp;' > tmp/m1
cat tmp/m1 | sed 's/^<h3>/ - /;s/<\/h3>$//'              > tmp/m2
cat tmp/m2 | sed 's/^<th><cite>/   - /; s/<\/cite>.*$//' > tmp/m3
cat tmp/m3 | sed 's/^<p>.*nbsp;/      - /; s/<\/p>//;'   > tmp/m4
