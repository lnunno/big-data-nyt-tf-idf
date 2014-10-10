#!/bin/bash
DATA="../../data/articles_sample.csv"
SM_DATA=$(head -n 5 $DATA)
cat $DATA | ./mapper.py 
