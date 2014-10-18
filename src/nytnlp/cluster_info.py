#!/usr/bin/env python3
'''
Output information on the clusters output by Apache Spark.

Created on Oct 17, 2014

@author: lnunno
'''
import pandas as pd
from pandas.io.json import read_json
import matplotlib.pyplot as plt
import os
from matplotlib import rcParams

NUM_TERMS = 20
NUM_CLUSTERS = 20

class ClusterComponent(object):
    
    def __init__(self, word, index, score):
        self.word = word
        self.index = index
        self.score = score

if __name__ == '__main__':
    rcParams.update({'figure.autolayout':True})
    doc_freq = read_json('../../data/doc_freq.json', typ='series')
    doc_freq_index = doc_freq.index
    n = NUM_CLUSTERS
    cluster_ls = []
    average_cluster_length_ls = []
    while n >= 2:
        df = pd.DataFrame.from_csv('../../data/clusters_%d.txt' %(n), header=None, index_col=None)
        # Create a new directory.
        dir_name_path = '../../data/clusters/%d' % (n)
        os.makedirs(dir_name_path, exist_ok=True)
        word_clusters = []
        for index, row in df.iterrows():
            t = row.nlargest(NUM_TERMS)
            w_words = pd.Series()
            for item_index, item_value in t.iteritems():
                word = doc_freq_index[item_index]
                w_words[word] = item_value
            word_clusters.append(w_words)
        with open('../../data/top_terms_%d_clusters.txt' % (n),'w') as f:
            i = 0
            sum_acc = 0
            for wc in word_clusters:
                f.write('CLUSTER %d\t' % (i))
                wc.to_json(f)
                f.write('\n')
                i += 1
                sum_acc += wc.sum()
                # Create the graph for this cluster.
                wc = wc[wc.nonzero()[0]]
                plt.figure()
                wc.plot(kind='bar')
                plt.xlabel('word')
                plt.ylabel('tf-idf score')
                plt.title('Cluster %d of %d' % (i,n))
                plt.savefig(os.path.join(dir_name_path,'cluster_%d.png' % (i)))
                plt.close()
            average_cluster_length = sum_acc/len(word_clusters)
            print('Wrote top terms for n = %d' % (n) )
            print('Average cluster length = %f' % (average_cluster_length))
            cluster_ls.append(n)
            average_cluster_length_ls.append(average_cluster_length)
        n -= 2
    # Create the cluster length graph.
    plt.figure()
    plt.plot(cluster_ls,average_cluster_length_ls)
    plt.xlabel('Number of clusters')
    plt.ylabel('Average tf-idf score')
    plt.title('Effect of number of clusters on average tf-idf score')
    plt.savefig('../../data/cluster_effect.png')