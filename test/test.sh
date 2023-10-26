#!/bash

wc -l test.csv
wc -l <(uniq test.csv)
uniq -d test.csv
wc -l <(uniq <(sort test.csv))