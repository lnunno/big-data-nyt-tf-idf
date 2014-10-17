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
from argparse import ArgumentParser

NONZERO_ONLY = True

def main():
    parser = ArgumentParser()
    parser.add_argument('--spark', dest='spark', action='store_true', default=False)
    args = parser.parse_args()
    
    doc_freq = read_json('../../data/doc_freq.json', typ='series')
    N = doc_freq['TOTAL_DOCS']
    idf_vector = np.log10(N / doc_freq)
    for line in sys.stdin:
        url, tf_vector = line.split()
        tf_vector = read_json(tf_vector, typ='series')
        
        # Calculate tf-idf from tf vector and doc_freq vector 
        tf_idf_vector = tf_vector.multiply(idf_vector, fill_value=0)
        
        # Normalize the tf-idf vector, this is important for the clustering done
        # later on.
        tf_idf_vector = tf_idf_vector / tf_idf_vector.sum() # Normalize the tf-idf vector.
        
        if NONZERO_ONLY:
            # tf_idf terms where these terms actually exist in this document, since
            # this is going to be a sparse vector.
            output_vector = tf_idf_vector[tf_idf_vector.nonzero()[0]]
        else:
            output_vector = tf_idf_vector
            
        s = StringIO()
        
        output_vector.to_json(s)
        if args.spark:
            indices_zip = list(zip(tf_idf_vector.nonzero()[0].tolist(),output_vector.tolist()))
            print('%s\t%s' % (url,indices_zip))
        else:
            print('%s\t%s' % (url, s.getvalue()))
        
if __name__ == '__main__':
    main()
