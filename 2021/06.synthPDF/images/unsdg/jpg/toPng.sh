for i in *jpg
do
  bn=`basename $i .jpg`
  convert $i ../$bn.png
done
