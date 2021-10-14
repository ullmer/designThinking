sed -n '320,1062 p' < menus.asp | egrep '^<h3>|^<th>|^<p>          &nbsp;' > m1
cat m1 | sed 's/^<h3>/ - /;s/<\/h3>$//' > m2
cat m2 | sed 's/^<th><cite>/   - /; s/<\/cite>.*$//' > m3
