# Takeaway sheet: Text Vectorization

## Practice

```python
# NLTK: getting list of lemmatized words for a text

# you may have to download the wordnet files for the first time
# import nltk
# nltk.download('wordnet')  # https://wordnet.princeton.edu/

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer  = WordNetLemmatizer()

text = "All models are wrong, but some are useful."

tokens = word_tokenize(text.lower())
lemmas = [lemmatizer.lemmatize(token) for token in tokens]

# printing as a single line
print(" ".join(lemmas))
```

```python
# spaCy: getting list of lemmatized words for a text

# you may have to download a spaCy model for the first time with
# python -m spacy download en

import spacy

nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

doc = nlp(text.lower())

lemmas = [token.lemma_ for token in doc]

print(" ".join(lemmas))
```

```python
# pattern - check for the syntax at https://docs.python.org/3.7/library/re.html
# substitution — what each pattern match should be substituted with
# text — the text which the function scans for pattern matches

import re
re.sub(pattern, replacement, text)
```

```python
# getting stop words for English

from nltk.corpus import stopwords

stop_words = set(stopwords.words('English'))
```

```python
# constructing a bag-of-words, a simple model for vectorizing texts
# stopwords - list of stop words

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

stop_words = set(stopwords.words('english'))
count_vect = CountVectorizer(stop_words=stop_words)

bow = count_vect.fit_transform(corpus)

# dictionary of unique words
words = count_vect.get_feature_names()

# printing a bag-of-words array
print(bow.toarray())
```

```python
# constructing a bag-of-words of n-gramms (without stop words)
# min_n - min value for n
# max_n - max value for n

from sklearn.feature_extraction.text import CountVectorizer

count_vect = CountVectorizer(ngram_range=(min_n, max_n))

bow = count_vect.fit_transform(corpus)

# dictionary of n-gramms
words = count_vect.get_feature_names()

# printing a bag-of-words array
print(bow.toarray())
```

```python
# Constructing TF-IDF for a corpus

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

stop_words = set(stopwords.words('english'))

tfidf_vectorizer = TfidfVectorizer(stop_words=stop_words)
tfidf = tfidf_vectorizer.fit_transform(corpus)
```

```python
# Constructing TF-IDF for n-gramms of a corpus
# min_n - min value for n
# max_n - max value for n

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

stop_words = set(stopwords.words('english'))

tfidf_vectorizer = TfidfVectorizer(stop_words=stop_words, ngram_range=(min_n, max_n))
tfidf = tfidf_vectorizer.fit_transform(corpus)
```

## Theory

**Tokenization** — dividing text into **tokens**: separate phrases, words, and symbols. 

**Lemmatization** — reducing a word to its root form (**lemma**).

**Corpus** — set of texts, usually thematically associated with each other. 

**Regular expression** — a sequence of characters that defines a search pattern, one pattern is usually used for finding different occurrences confirming to this pattern, e.g. one pattern can describe different phone numbers, email addresses, and so on.

**Bag-of-words** — a simple model to convert texts into vectors regardless the order of words in texts and their importance.

**TFIDF** — a simple model to convert texts into vectors without considering word order but with respect to their importance.

***N*-gramm** — a sequence of N tokens.

**Sentiment Analysis** — an NLP task used to identify tonality of a text (document).