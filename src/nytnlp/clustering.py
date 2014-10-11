'''
Created on Oct 11, 2014

@author: lnunno
'''
import pandas as pd
# from nltk.cluster.kmeans import KMeansClusterer

def main():
    # Load the pickled matrix. This is produced from reducer.py
    tf_idf_matrix = pd.read_pickle('../../data/tf_idf_matrix.pkl')
    print(tf_idf_matrix)
    
if __name__ == '__main__':
    main()