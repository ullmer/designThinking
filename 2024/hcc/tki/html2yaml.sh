for i in *html
do 
  bn=`basename $i .html`
  echo $bn
  html2text $i > yaml/$bn.yaml
done
