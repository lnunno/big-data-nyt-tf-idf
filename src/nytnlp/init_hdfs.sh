#!/bin/bash
hdfs dfs -mkdir -p /user/lnunno
hdfs dfs -put ../../data/articles.csv /user/lnunno/articles.csv
hdfs dfs -put ../../data/articles_sample.csv /user/lnunno/articles_sample.csv
hdfs dfs -put ../../data/tf_vectors.tsv /user/lnunno/tf_vectors.tsv
