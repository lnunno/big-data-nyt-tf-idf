#!/bin/bash

echo "This script creates the tf-idf vectors for spark consumption."
echo "Deleting old output directory for spark"
hdfs dfs -rm -r nytouts/spark

echo "Starting spark job"
hadoop jar $HADOOP_LIB/hadoop-streaming-2.5.1.jar     \
-mapper  'tf_idf_mapper.py --spark'                   \
-reducer org.apache.hadoop.mapred.lib.IdentityReducer \
-input   /user/lnunno/tf_vectors.tsv                  \
-output  nytouts/spark

rm ../../data/spark_tf_idf_vectors.tsv
hdfs dfs -get nytouts/spark/part-00000 ../../data/spark_tf_idf_vectors.tsv
