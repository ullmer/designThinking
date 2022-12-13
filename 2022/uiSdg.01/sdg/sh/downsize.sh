for i in *.png
do
  echo $i
  convert -geometry x150 $i ../$i
done
