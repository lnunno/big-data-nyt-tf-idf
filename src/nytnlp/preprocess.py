'''
Text preprocessing utility functions.

Created on Sep 29, 2014

@author: lnunno
'''
import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

remove_pattern = re.compile(r'[,.;&#!\-\'"\(\)\|0-9]')

stemmer = PorterStemmer()

stopword_set = set(stopwords.words('english'))

def clean_text(text):
    '''
    Clean the line of text completely.
    '''
    text_lower     = text.lower()
    sanitized_text = remove_punctuation_and_numbers(text_lower)
    stopped_text   = remove_stopwords(sanitized_text)
    stemmed_text   = word_stem(stopped_text)
    return stemmed_text

def remove_stopwords(text):
    words    = text.split()
    new_ls   = [w for w in words if w not in stopword_set]
    new_text = ' '.join(new_ls)
    return new_text 
    
def remove_punctuation_and_numbers(text):
    '''
    Remove all punctuation and numbers from a line of text.
    
    @return: The sanitized string.
    '''
    return re.sub(remove_pattern,'',text)

def word_stem(text):
    '''
    Stem all the words in the line of text.
    @return: 
    '''
    words = text.split()
    stemmed_words_ls = [stemmer.stem(w) for w in words]
    stemmed_text = ' '.join(stemmed_words_ls) 
    return stemmed_text

if __name__ == '__main__':
    print(clean_text("&#8220;People are crying out for protection from greed and inequality,&#8221; Ban Ki-Moon, the secretary general said Wednesday. &#8220;The United Nations must answer the call.&#8221;"))

