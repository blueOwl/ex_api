for i in `ls data`;do

#cat data/$i |zcat|python3 import.py &> logs/$i.log
cat data/$i |zcat|python3 import.py 

done
