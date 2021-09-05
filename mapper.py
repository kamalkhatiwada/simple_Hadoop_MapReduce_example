#!/usr/bin/env python
import sys
import string

stop_words = ['the', 'and']

#mapping punctuation to whitespace
#https://stackoverflow.com/questions/34860982/replace-the-punctuation-with-whitespace
translator = string.maketrans(string.punctuation, ' '*len(string.punctuation))

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()
 #   line = line.translate(translator)
    line = line.translate(translator)
    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
#    stopWords = set (['the', 'and'])
    for word in words:
        if word not in stop_words:
           print '%s\t%s' % (word, "1")
