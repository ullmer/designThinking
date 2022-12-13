for i in *.png
do
  echo $i
  convert -modulate 100,22,100 $i ds/$i
done
