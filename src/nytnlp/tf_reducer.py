#!/usr/bin/env python3
'''
Reduce to term frequency vectors.

Output URL, tf-vector

Created on Oct 14, 2014

@author: lnunno
'''
import sys
import pandas as pd

def main():
    N = 0
    last_url = None
    
    doc_freq = pd.Series()
    
    # word_series[WORD] = WORD frequency in URL.
    word_series = pd.Series()
    
    for line in sys.stdin:
        # Example:
        # http://www.nyt/whatever,foo,2
        url, word, value = line.split()
        value = int(value)
        word_series[word] = value
        if word not in doc_freq.index:
            doc_freq[word] = 1
        else:
            doc_freq[word] += 1 # Every word only appears once here so this is ok.
        if last_url == url:
            # Accumulating
            # Same as the last url.
            pass
        else:
            if last_url:
                # Emit the output.
                # URL, term frequency vector (JSON).
                word_series = word_series / word_series.sum() # Normalize with respect to doc length.
                print('%s\t%s' % (last_url, word_series.to_json()))
            word_series = pd.Series()
            N += 1
            last_url = url
    
    # Emit the last one.
    word_series = word_series / word_series.sum() # Normalize with respect to doc length.
    print('%s\t%s' % (url, word_series.to_json()))
    
    doc_freq['TOTAL_DOCS'] = N
    doc_freq.to_json('../../data/doc_freq.json')    
    
if __name__ == '__main__':
    main()
