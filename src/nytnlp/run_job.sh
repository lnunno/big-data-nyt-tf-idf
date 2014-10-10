#!/bin/bash
echo "Deleting old output directory"
hdfs dfs -rm -r nytouts

echo "Starting job"
hadoop jar $HADOOP_LIB/hadoop-streaming-2.5.1.jar \
-mapper  mapper.py                                \
-reducer reducer.py                               \
-input   articles_sample.csv                      \
-output  nytouts

hdfs dfs -cat nytouts/part-00000
