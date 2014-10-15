#!/bin/bash
echo "Deleting old output directory"
hdfs dfs -rm -r nytouts

# Term frequency operations:
echo "Starting term frequency job"
hadoop jar $HADOOP_LIB/hadoop-streaming-2.5.1.jar \
-mapper  mapper.py                                \
-reducer tf_reducer.py                            \
-input   articles_sample.csv                      \
-output  nytouts
rm ../../data/tf_vectors.tsv
hdfs dfs -get nytouts/part-00000 ../../data/tf_vectors.tsv

echo "Deleting old TF vectors in hadoop file system"
hdfs dfs -rm /user/lnunno/tf_vectors.tsv
hdfs dfs -put ../../data/tf_vectors.tsv /user/lnunno/tf_vectors.tsv

echo "Deleting old output directory for tf-idf"
hdfs dfs -rm -r nytouts/tf_idf

echo "Starting tf-idf job"
hadoop jar $HADOOP_LIB/hadoop-streaming-2.5.1.jar     \
-mapper  tf_idf_mapper.py                             \
-reducer org.apache.hadoop.mapred.lib.IdentityReducer \
-input   /user/lnunno/tf_vectors.tsv                  \
-output  nytouts/tf_idf

rm ../../data/tf_idf_vectors.tsv
hdfs dfs -get nytouts/tf_idf/part-00000 ../../data/tf_idf_vectors.tsv
