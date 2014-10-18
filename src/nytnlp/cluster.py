'''
Cluster the results of the tf-idf vectors.

Run through: 

    spark-submit cluster.py

Created on Oct 17, 2014

@author: lnunno
'''
import numpy as np
from pyspark import SparkContext
from pyspark.mllib.linalg import SparseVector
from pyspark.mllib.clustering import KMeans

TOTAL_DOCS = 39944
NUM_CLUSTERS = 20

def parseVector(line):
    _,indices_tuple_ls = line.split('\t')
    indices_tuple_ls = eval(indices_tuple_ls) # Convert to a real python list.
    return SparseVector(TOTAL_DOCS,indices_tuple_ls)
    
if __name__ == '__main__':
    sc = SparkContext(appName="KMeans")
    lines = sc.textFile('../../data/spark_tf_idf_vectors.tsv')
    data = lines.map(parseVector)
    np.set_printoptions(threshold='nan')
    n = NUM_CLUSTERS
    while n >= 2:
        model = KMeans.train(data,n)
        centers = model.clusterCenters
        with open('../../data/clusters_%d.txt' % (n),'w') as f:
            for c in centers:
                # Format in exponential notation.
                s = ','.join([('%e' % x) for x in c])
                f.write('%s\n'% (s))
        n -= 2