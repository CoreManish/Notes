## 1. Explain a NLP processing pipeline with different steps involved in the process
##Answer:
NLP(Natural Language processing) means working/finding insights from human language. 
Most common task in NLP are - 
* text classification (example- email is spam or ham), 
* sentiment analysis
* Parts of speech tagging
* etc

Depending on task, pipeline may differ, however here is the list of common steps invloved in NLP taks-

1. Data Collection : First we collect desired data in raw form from source.
Data may be available inside html page (beautiful soup is used), pdf (tabula), spreadsheet (pandas is common framework), image (pytesseract), audio etc.
Sometimes collected data may not be enough to train algorithm, then we generate fake data called data augmentation.

2. Text cleaning: Collected text may contain emoji, spelling mistake, html tags, special characters, extra spaces etc.
If spelling mistakes - we correct them
If emoji - emoji may carry semantic of sentence, so we should not remove them, rather we will convert into machine readable text using an encoding.
3. Text preprocessing: 


## 2. “You shall know a word by the company it keeps.”. Mark all the text representations techniques which implement this adage? 2M
a. Bag of words
b. TF-IDF
c. One-hot-encodings
d. Word2vec

## 3. Why do we convert text into its numerical representations? [2M]
Model can't be trained directly using text data, so we convert them into numerical representation using techniques like one-hot encoding, Bag of words, n-gram, TF-IDF.

## 4. Your corpus consists of following 3 sentences: 2M
i. I am studying BSc Degree in IIT Madras.
ii. There are many interesting courses here.
iii. Studying NLP is really awesome.


#### Using the above corpus, write down the following
a. Vocabulary
b. Bag of words vector for each sentence
c. TF-IDF representation for sentences.

### Answer
a. The vocabulary is the set of unique words present in the corpus.
Vocabulary: {I, am, studying, BSc, Degree, in, IIT, Madras, There, are, many, interesting, courses, here, Studying, NLP, is, really, awesome}