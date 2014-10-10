#!/usr/bin/env python3
'''
Created on Oct 9, 2014

@author: lnunno
'''
import sys
from collections import defaultdict
import numpy as np
import pandas as pd

class NYTReducer(object):
    
    def __init__(self):
        self.number_of_articles = 0
        self.word_count = 0 # Not used currently.

def main():
    reducer = NYTReducer()
    last_url = None
    
    # article_vectors[URL][WORD] = WORD frequency in URL.
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
            reducer.word_count += value
        else:
            reducer.number_of_articles += 1
            reducer.word_count = value 
            last_url = url
    
    # We know the number of articles present here.
    
    # Create a DataFrame from the dictionary.
    freq_matrix = pd.DataFrame.from_dict(article_vectors)
    freq_matrix = freq_matrix.fillna(0) # Fill NaN values with a 0.
    
    print('===Freq matrix===\n',freq_matrix)
    
    # Calculate the number of documents that each term appears in.
    df_vector = freq_matrix.apply(lambda a: np.nonzero(a)[0].size, axis=1)
    print('===Doc freq vector===\n',df_vector)
    
    idf_vector = np.log(reducer.number_of_articles/df_vector)
    print('===IDF vector===\n',idf_vector)
    
    # Normalizes the DataFrame with the "augmented" term-frequency.
    norm_freq_matrix = freq_matrix + 0.5 + ((0.5 * freq_matrix)/freq_matrix.max())
    print(norm_freq_matrix)
    
    tf_idf_matrix = norm_freq_matrix.mul(idf_vector, axis=0)
    
    print('===TF-IDF Matrix===\n',tf_idf_matrix)
    

    
    
    
if __name__ == '__main__':
    main()