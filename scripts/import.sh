for i in `ls ./data`;do
cat ./data/$i|zcat|python3 ./import.py
done
