for i in A B C D E F G H
 do
   for j in 0 1 2 3 4 5 6 7 8
   do
     coord=$i$j
     echo git mv cc77g-$coord.png $coord.png
   done
 done

