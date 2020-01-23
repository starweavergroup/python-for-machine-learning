#!/usr/bin/env python3

import sys
import csv


filename = sys.argv[1]  # Grab Filename

print("Opening file: " + filename)

# TODO: Process the file

with open(filename, 'r') as myfile:
    for line in myfile:
        print(line)
