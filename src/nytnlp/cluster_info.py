#!/usr/bin/env python3
'''
Output information on the clusters output by Apache Spark.

Created on Oct 17, 2014

@author: lnunno
'''
import pandas as pd
from pandas.io.json import read_json

NUM_TERMS = 20

class ClusterComponent(object):
    
    def __init__(self, word, index, score):
        self.word = word
        self.index = index
        self.score = score

if __name__ == '__main__':
    doc_freq = read_json('../../data/doc_freq.json', typ='series')
    doc_freq_index = doc_freq.index
    df = pd.DataFrame.from_csv('../../data/raw_clusters.txt', header=None, index_col=None)
    word_clusters = []
    for index, row in df.iterrows():
        t = row.nlargest(NUM_TERMS)
        w_words = pd.Series()
        for item_index, item_value in t.iteritems():
            word = doc_freq_index[item_index]
            w_words[word] = item_value
        word_clusters.append(w_words)
    print(word_clusters)
    
