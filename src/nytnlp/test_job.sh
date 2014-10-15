#!/bin/bash
DATA="../../data/articles_sample.csv"
head -n 5 $DATA | ./mapper.py | sort | ./tf_reducer.py | ./tf_idf_mapper.py
