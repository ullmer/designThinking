for i in CA NM AZ NY UT ID LA MA SC NC 
do
  echo $i `grep $i *yaml|wc -l`
done
