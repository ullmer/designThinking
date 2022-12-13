for i in *
do
  echo $i
  cat $i | sed 's/^.*modules.//; s/.index.cnxml:/ /;' > ../$i
done
