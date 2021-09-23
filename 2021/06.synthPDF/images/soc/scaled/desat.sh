for i in *
do
  convert -modulate 100,30 $i ../$i
done
