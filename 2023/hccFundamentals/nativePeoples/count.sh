for i in SC NC CA UT ID NY LA
do
  echo $i `grep $i *yaml|wc -l`
done
