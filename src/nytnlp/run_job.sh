#!/bin/bash
echo "Deleting old output directory"
hdfs dfs -rm -r nytouts

echo "Starting job"
hadoop jar $HADOOP_LIB/hadoop-streaming-2.5.1.jar \
-mapper  mapper.py                                \
-reducer tf_reducer.py                            \
-input   articles.csv                             \
-output  nytouts

rm ../../data/tf_vectors.tsv

hdfs dfs -get nytouts/part-00000 ../../data/tf_vectors.tsv

echo "Deleting old TF vectors"
hdfs dfs -rm /user/lnunno/tf_vectors.csv
hdfs dfs -put ../../data/tf_vectors.csv /user/lnunno/tf_vectors.csv
