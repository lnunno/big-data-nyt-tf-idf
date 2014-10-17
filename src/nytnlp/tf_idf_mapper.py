#!/usr/bin/env python3
'''
Calculate the *normalized* tf-idf vector for each document.

Created on Oct 15, 2014

@author: lnunno
'''
import sys
import pandas as pd
import numpy as np
from pandas.io.json import read_json
from _io import StringIO

def main():
    doc_freq = read_json('../../data/doc_freq.json', typ='series')
    N = doc_freq['TOTAL_DOCS']
    idf_vector = np.log10(N / doc_freq)
    for line in sys.stdin:
        url, tf_vector = line.split()
        tf_vector = read_json(tf_vector, typ='series')
        
        # Calculate tf-idf from tf vector and doc_freq vector 
        tf_idf_vector = tf_vector.multiply(idf_vector, fill_value=0)
        
        # tf_idf terms where these terms actually exist in this document, since
        # this is going to be a sparse vector.
        tf_idf_nonzero_vector = tf_idf_vector[tf_idf_vector.nonzero()[0]]
        
        # Normalize the tf-idf vector, this is important for the clustering done
        # later on.
        tf_idf_norm_vector = tf_idf_nonzero_vector / tf_idf_nonzero_vector.sum() 
        
        s = StringIO()
        tf_idf_norm_vector.to_json(s)
        print('%s\t%s' % (url, s.getvalue()))  # The tf-idf vector.
        
if __name__ == '__main__':
    main()
