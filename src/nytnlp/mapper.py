#!/usr/bin/env python3
'''
Mapper function for NYTNLP.

Created on Oct 9, 2014

@author: lnunno
'''
from nytnlp.preprocess import clean_text
import sys
from _io import StringIO
import csv
from argparse import ArgumentParser
from collections import Counter

separator = '\t'


def helper(line):
    counter = Counter()
    try:
        docid, abstract, url_str = parse_csv_string(line)
    except Exception as e:
#         print('FAIL ON:',line,e)
        return
    cleaned = clean_text(abstract)
    for word in cleaned.split():
        # Count all the words.
        counter[word] += 1
    # Output the collected counts. 
    for k,v in counter.items():
        print('%100s\t%20s\t%5d' % (url_str,k,v))

def main():
    for line in sys.stdin:
        helper(line)

def parse_csv_string(s):
    f = StringIO(s)
    reader = csv.reader(f,delimiter=',', dialect=csv.excel_tab)
    ls = []
    for row in reader:
        ls.append(row)
    return ls[0]
        
def test():
    s1 = '0,"The premium-priced phone makes a strong case to make the switch, but its size and difficult to use keyboard are among its drawbacks.",http://www.nytimes.com/2014/09/25/technology/personaltech/blackberry-passport-review.html'
    s2 = '1,The three men turned themselves in to the French authorities after a mix-up allowed them to walk free.,http://www.nytimes.com/2014/09/25/world/europe/french-islamic-militant-suspects-expelled-by-turkey.html'
    print('---s1---')
    helper(s1)
    print('---s2---')
    helper(s2)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--test', dest='test', action='store_true', default=False)
    args = parser.parse_args()
    if args.test:
        test()
    else:
        main()
