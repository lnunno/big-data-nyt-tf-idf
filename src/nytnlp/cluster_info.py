#!/usr/bin/env python3
'''
Output information on the clusters output by Apache Spark.

Created on Oct 17, 2014

@author: lnunno
'''
import pandas as pd
from pandas.io.json import read_json

if __name__ == '__main__':
    doc_freq = read_json('../../data/doc_freq.json', typ='series')
    df = pd.DataFrame.from_csv('../../data/raw_clusters.txt', header=None, index_col=None)
#     print(df)
    def calc_largest(series):
        ret_val = series.nlargest(3)
        return ret_val
    largest = df.apply(calc_largest,axis=1)
    print(largest)
