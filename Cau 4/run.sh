#!/bin/bash

# Loop from 1 to 5
for i in {1..5}
do
   echo "Running test case $i..."
   python "src/main.py" "input/input$i.txt"
done

