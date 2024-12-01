#!/bin/bash
echo $1
mkdir day$1
touch day$1/day$1.py day$1/readme.txt day$1/source.txt  day$1/test_source.txt
cp shared.py day$1/shared.py 
curl https://adventofcode.com/2024/day/$1 | sed -n "/<main>/,/<\/main>/p" | sed -e 's/<[^>]*>//g' >> day$1/readme.txt
echo "import shared" >> day$1/day$1.py
echo >> day$1/day$1.py
echo "lines = shared.read_file(\"test_source.txt\")" >> day$1/day$1.py