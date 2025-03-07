'''
Downloads articles as JSON and combines the results into a single JSON file to
be processed later.

@see: export.py 

Created on Sep 23, 2014

@author: lnunno
'''
import os
import requests
import json
import time
from nytnlp.secret import API_KEY, API_KEY2

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(THIS_DIR,'..','..','data'))

VERSION = 'v3'
BASE_URL = 'http://api.nytimes.com/svc/news/%s/content/all/all.json' % (VERSION)

def main(DEBUG=False):
    initial_offset = 40000
    requests_per_second = 8
    sleep_time = 1/requests_per_second
    offset = 0 + initial_offset
    num_results = 100 if DEBUG else 50000
    print('Going to collect %5d articles.' %(num_results))
    input_file_name = 'articles_sample.json' if DEBUG else 'articles.json'
    file_path = os.path.join(DATA_DIR,input_file_name)
    assert os.path.isdir(DATA_DIR)
    params = {
              'api-key': API_KEY,
              'offset' :  offset
              }
    results = []
    while num_results > 0:
        print('Current offset = %d' %(offset))
        params['offset'] = offset
        r = requests.get(BASE_URL, params=params)
        if not r.status_code == requests.codes.ok: # @UndefinedVariable
            print('HTTP Error code %d returned, trying again in %f seconds...' %(r.status_code, sleep_time))
            # Sleep a little bit and then try again.
            time.sleep(sleep_time)
            continue
        json_response = r.json()
        results += json_response['results']
        offset += 20
        num_results -= 20
        num_collected = offset - initial_offset 
        print('Collected %5d results' % (num_collected))
        if (num_collected % 1000) == 0:
            td = {'docs': results}
            tfp = os.path.join(DATA_DIR,'articles_older_%d.json' % (num_collected))
            with open(tfp,'wb') as f:
                json.dump(td,f)
                print('Saved temp results to %s' %(tfp))
        time.sleep(sleep_time) # Wait a little bit so we don't get banned.
    d = {'docs': results }
    with open(file_path, 'wb') as f:
        json.dump(d,f)
        print('Dumped results to %s' %(file_path))

if __name__ == '__main__':
    main()