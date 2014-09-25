big-data-nyt-tf-idf
===================

Document analysis and natural language processing using the New York Times API Newswire API.

The goal is to cluster the abstracts of some articles from the New York Times newspaper.

## PART 1: Data acquisition

Part 1 of this homework consists on downloading data using an API. The NY Times API is available at http://developer.nytimes.com. It provides access to various articles, both historic and new. For this assignment we are interested in the Times NewswireAPI, which provides access to articles, blogs, and so on, as they are being produced. For each article we can obtain directly from the API its URL and its abstract, among other information. Your tasks for this section of the problem are the following:


1. Downloading the data (5 pts)

- Study the API, download 50,000 different articles from the Times Newswire API.

- For each of them save the URL and the abstract. Note that because articles are created continually, you may end up downloading some articles multiple times; you should make sure that you do not store each article more than once. 

- For each article assign a unique docID. Note that this part is not completely trivial because often the API does not return the expected document, so you need to catch the exceptions thrown, put the right delays, and retry, for some steps.


## PART 2: Preprocessing, tf-idf


Review: The map function takes four parameters which by default correspond to:

a. WritableComparable key - the byte-offset of the current line in the file

b. Writable value - the line from the file

c. OutputCollector - output - this has the .collect method to output a <key, value> pair

d. Reporter reporter - allows us to retrieve some information about the job (like the current filename) 


 2. Preprocessing of the abstracts. (10 pts)

- Your map function should extract individual words from the input it is given, and output the word as the key, and the current filename as the value. Thus, the map function (or one of them) should output <"word", "filename"> pairs. 

- Remove all punctuation and numbers, and keep only the words. 

- Convert each word to lowercase, remove stopwords.

- Extra credit (+2 pts): perform word stemming (see for example Porter’s stemmer or the NLTK python package)


Hints:

* Since in this example we want to output <"word", "filename"> pairs, the types will both be Text.

* The word count program had an example of extracting individual words from a line

* To get the current filename, use the following code snippet:

    FileSplit fileSplit = (FileSplit)reporter.getInputSplit();

    String fileName = fileSplit.getPath().getName();



3. TF-IDF (5 pts)

- For each document compute its tf-idf vector as explained in *******

- Extra credit (+2 pts): Normalize with respect to document length

* Note that to accomplish this section of the homework you might need to perform a series of MR jobs and not just a single job


## PART 3: Clustering

Perform clustering using as features the vector space produced by tf-idf

4. Use a clustering algorithm of your choice (10 pts)

- Explain why did you chose that particular algorithm, what are pros and cons

- Explain design decisions with respect to the number of clusters (if applicable)

- Extra credit (+2 pts): use a quantitative approach to select the ‘best’ number of clusters (if applicable)



5. Perform a statistical analysis about the top 20 most discriminative terms per cluster (5 pts)

- Use tf-idf scores to find most discriminative terms per cluster



6. Present a visualization of clusters and term frequencies (5 pts)

- Use any graphic/visualization program of your choice

- Be creative and present useful graphs



7. Submit a presentation explaining/describing/showing clearly each of the previous 6 points. After submission, no further changes to your presentation will be allowed



Total: 40 points + 6 extra credit proportional to 23 points of your final grade
