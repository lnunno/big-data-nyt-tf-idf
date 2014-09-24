'''
Created on Sep 23, 2014

@author: lnunno
'''
import os
import requests
import json
import time
from nytnlp.secret import API_KEY

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(THIS_DIR,'..','..','data'))

VERSION = 'v3'
BASE_URL = 'http://api.nytimes.com/svc/news/%s/content/all/all.json' % (VERSION)

def main(DEBUG=False):
    requests_per_second = 8
    sleep_time = 1/requests_per_second
    offset = 0
    num_results = 100 if DEBUG else 50000
    print('Going to collect %5d articles.' %(num_results))
    file_name = 'articles_sample.json' if DEBUG else 'articles.json'
    file_path = os.path.join(DATA_DIR,file_name)
    assert os.path.isdir(DATA_DIR)
    params = {
              'api-key': API_KEY,
              'limit':num_results,
              'offset':offset
              }
    results = []
    while num_results > 0:
        params['offset'] = offset
        r = requests.get(BASE_URL, params=params)
        if not r.status_code == requests.codes.ok: # @UndefinedVariable
            print('HTTP Error code returned, trying again in %f seconds...' %(sleep_time))
            # Sleep a little bit and then try again.
            time.sleep(sleep_time)
            continue
        json_response = r.json()
        results += json_response['results']
        offset += 20
        num_results -= 20
        print('Collected %5d results' %(offset))
        time.sleep(sleep_time) # Wait a little bit so we don't get banned.
    d = {'docs': results }
    with open(file_path, 'wb') as f:
        json.dump(d,f)
        print('Dumped results to %s' %(file_path))

if __name__ == '__main__':
    main()