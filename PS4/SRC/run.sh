#!/bin/bash

# Navigate to the directory where the test cases are stored
cd INPUT

# Loop over each .txt file in the directory
for file in *.txt
do
   echo "Running test case $file..."
   python "../main.py" "$file"
done

# Navigate back to the original directory
cd -
