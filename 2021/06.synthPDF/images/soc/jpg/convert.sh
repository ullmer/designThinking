for i in *
do 
  bn=`basename $i .jpg`
  convert $i ../$bn.png
done
