#!/bin/bash

# Loop from 1 to 5
for i in {1..5}
do
   echo "Running test case $i..."
   python "SRC/main.py" "SRC/INPUT/input_$i.txt"
done

