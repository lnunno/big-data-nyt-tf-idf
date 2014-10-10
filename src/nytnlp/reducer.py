#!/usr/bin/env python3
'''
Created on Oct 9, 2014

@author: lnunno
'''
import sys
from collections import defaultdict

def main():
    number_of_articles = 0
    last_url = None
    word_count = 0
    article_vectors = defaultdict(lambda: defaultdict(int))
    for line in sys.stdin:
        # Example:
        # http://www.nyt/whatever,foo,2
        url, word, value = line.split()
        value = int(value)
        article_vectors[url][word] = value
        if last_url == url:
            # Accumulating
            # Same as the last url.
            word_count += value
        else:
            if last_url:
                print('%100s\t%d' %(last_url,word_count))
            number_of_articles += 1
            word_count = value 
            last_url = url
    # Last entry
    print('%100s\t%d' %(last_url,word_count))
    print('Number of articles = %d' %(number_of_articles))
    
if __name__ == '__main__':
    main()