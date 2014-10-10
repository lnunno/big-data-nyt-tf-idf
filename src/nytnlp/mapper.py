#!/usr/bin/env python3
'''
Mapper function for NYTNLP.

Created on Oct 9, 2014

@author: lnunno
'''
from nytnlp.preprocess import clean_text
import sys

separator = '\t'

def main():
    for line in sys.stdin:
        print(clean_text(line),separator,1)

if __name__ == '__main__':
    main()