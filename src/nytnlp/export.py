'''
Combines and exports the JSON files produced by get_data.py to a format friendly
to Hadoop.

Created on Sep 24, 2014

@author: lnunno
'''
import os
import json
import csv
from nytnlp.get_data import DATA_DIR

def combine(files, output_file):
    '''
    @param files: A list of JSON file paths
    
    @param output_file: A file path of the destination file.  
    '''
    pass

def export(input_path, export_path):
    '''
    '''
    input_file = open(input_path)
    json_file = json.load(input_file)
    input_file.close()
    
    output_file = open(export_path, 'w', encoding='utf-8')
    file_writer = csv.writer(output_file)
    
    doc_list = json_file['docs']
    docid = 0
    url_set = set()
    for doc in doc_list:
        url = doc['url']
        abstract = doc['abstract']
        if not url.startswith('http'):
            print('EXPECTED BAD URL: %s' %(url))
        if url in url_set:
            print('WARNING: The article with URL %s has already been added, skipping...' %(url) )
            continue
        row = [docid, abstract, url]
        file_writer.writerow(row)
        url_set.add(url)
        docid += 1
    output_file.close()
    
if __name__ == '__main__':
    input_file_name = 'articles_40000.json'
    export_file_name = 'articles.csv'
    input_path = os.path.join(DATA_DIR,input_file_name)
    export_path = os.path.join(DATA_DIR,export_file_name)
    export(input_path, export_path)