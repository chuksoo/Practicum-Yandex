# Chapter Summary: Text Vectorization

## Lemmatization

Here are the steps for text preprocessing:

1. **Tokenization:** you'll need to divide the text into tokens (separate phrases, words, and symbols); 
2. **Lemmatization:** you'll need to reduce the words to their root forms (lemma).

You can use these libraries for both tokenization and lemmatization:

- Natural Language Toolkit (NLTK)
- spaCy

Import the tokenization function and create a lemmatization object:

```python
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer  = WordNetLemmatizer()
```

Pass the text "All models are wrong, but some are useful" as separate tokens to the `lemmatize()` function:

```python
text = "All models are wrong, but some are useful."

tokens = word_tokenize(text.lower())

lemmas = [lemmatizer.lemmatize(token) for token in tokens]
```

The `word_tokenize()` function splits a text into tokens, and the `lemmatize()` function returns the lemma for a token passed to it. Because we're interested in lemmatizing a sentence, the result is usually presented as a list of lemmatized tokens.

```python
['all', 'model', 'be', 'wrong', ',', 'but', 'some', 'be', 'useful', '.']

```

We've also converted the text to lowercase because that's required by the NLTK lemmatizer. 

Use the `join()` function to convert the list of processed tokens back into a text line, separating the elements with an optional space:

```python
" ".join(lemmas)

```

We get:

```python
'all model be wrong , but some be useful .'

```

A set of texts is collectively called a corpus. It's usually necessary to define a corpus for a text analysis task (for example, to build a dictionary or a vector space based on it). Each text record is treated by a machine learning algorithm according to its "position" in a corpus. Don’t worry, we’ll look into all this in greater detail in the next few lessons.

Create a corpus from the reviews. Convert the `review` column into a list of texts.

```python
corpus = data['review']
```

## Regular expressions

A regular expression is an instrument for finding complex patterns in texts. These patterns can then be manipulated to your liking (extracted, replaced, etc.) Regular expressions are powerful tools that used almost everywhere that text appears!  

Python has a built-in module for working with regular expressions: **`re`** (Regular Expressions):

```python
import re
```

Take a look at the `re.sub()` function. It finds all the parts of the text that match the given pattern and then substitutes them with the chosen text.

```python
# pattern
# substitution — what each pattern match should be substituted with
# text — the text which the function scans for pattern matches
re.sub(pattern, substitution, text)

```

We only need to keep letters and spaces in these lemmatized review texts, so let's write a regular expression to find them.

The expression starts with *r* and is followed by square brackets in quotation marks:

```python
r'[]'
```

All the letters that match the pattern are listed in square brackets without spaces and can be placed in any order. Let's find the letters from "a" to "z." If we assume they can be in both lowercase and uppercase, then the code should be written as follows:

```python
# a range of letters is indicated by a hyphen:
# a-z = abcdefghijklmnopqrstuvwxyz
r'[a-zA-Z]'

```

Let's take one of the reviews from the dataset. We need to keep all Latin letters, spaces, and apostrophes, so our pattern will need to correctly identify them. If we call `re.sub()`, they will be substituted for spaces. To indicate the characters that don't match the pattern, put a caret (^) in front of the sequence:

```python
# review text
text = """
I liked this show from the first episode I saw, which was the "Rhapsody in Blue" episode (for those that don't know what that is, the Zan going insane and becoming pau lvl 10 ep). Best visuals and special effects I've seen on a television series, nothing like it anywhere.
"""
re.sub(r'[^a-zA-Z\']', ' ', text)

```

```python
" I liked this show from the first episode I saw  which was the  Rhapsody in Blue  episode  for those that don't know what that is  the Zan going insane and becoming pau lvl    ep   Best visuals and special effects I've seen on a television series  nothing like it anywhere  "

```

Now we only have Latin letters and spaces left. In the next step, let's get rid of the extra spaces. They hinder the analysis, but we can eliminate them by using the combination of the functions `join()` and `split()`.

Let's take a look at the example of a text with extra spaces in the middle, beginning, and end of the line. Use the `split()` method to convert it into a list. If we call `split()` without any arguments, it splits the text by spaces or groups of spaces:

```python
text = "            I   liked   this   show   "
text.split()

```

The result is a list without spaces:

```python
['I', 'liked', 'this', 'show']

```

Using the `join()` method, combine these elements into a line with spaces:

```python
" ".join(['I', 'liked', 'this', 'show'])

```

So we get a line with no extra spaces:

```python
'I liked this show'

```

## Bag-of-words and n-gram

Let's learn how we can convert text data into numeric data, which is a much more suitable type of data for computers. The conversion is usually done so that a word or sentence becomes a numerical vector.

One common technique for converting text is called the bag-of-words model. It transforms texts into vectors without considering word order, and that's why it's called a bag.

Let's take a famous proverb:

```
For want of a nail the shoe was lost.
For want of a shoe the horse was lost.
For want of a horse the rider was lost.
```

If we get rid of uppercase letters and lemmatize it with spaCy, we get this:

```
for want of a nail the shoe be lose 
for want of a shoe the horse be lose 
for want of a horse the rider be lose
```

Let's count how many times each word occurs:

- "for," "want," "of," "a," "the," "be," "lose" — 3;
- "shoe," "horse" — 2;
- "nail," "rider" — 1.

![Chapter%20Summary%20Text%20Vectorization%20c02ed14b7fa44f07a874ef72a6f4997e/ananas.jpg](Chapter%20Summary%20Text%20Vectorization%20c02ed14b7fa44f07a874ef72a6f4997e/ananas.jpg)

Here's the vector for this text:

```python
[2, 2, 2, 1, 1, 1, 1, 1]
```

If there are several texts, then the bag-of-words transforms them into a matrix. The rows represent texts and the columns represent unique words from all the texts in the corpus. The numbers at their intersections represent occurrences of each unique word.

The bag-of-words counts every unique word. But the word order and connections between words are not taken into account. Look at this lemmatized text, for example:

```
Peter travel from Tuscon to Vegas

```

Here's the list of words: "Peter," "travel," "from," "Tuscon," to "Vegas." So where does Peter go? To answer the question, let's look at the phrases, or **N-grams.**

An n-gram is a sequence of several words. *N* indicates the number of elements and is arbitrary. For instance if N=1, we have separate words or **unigrams**. If N=2, we have two-word phrases or **bigrams**. N=3 produces **trigrams**. You get the idea, right?

Let's find all the the trigrams for the sentence "Sunset raged like a beautiful bonfire."

![Chapter%20Summary%20Text%20Vectorization%20c02ed14b7fa44f07a874ef72a6f4997e/v140.jpg](Chapter%20Summary%20Text%20Vectorization%20c02ed14b7fa44f07a874ef72a6f4997e/v140.jpg)

We have four trigrams: "Sunset raged like," "raged like a," "like a beautiful," "a beautiful bonfire." The word "beautiful" cannot start a trigram because there's only one word left after it, and we need two.

Back to Peter. Find the bigrams in the text. "Peter travel," "travel from," "from Tuscon," "Tuscon to," "to Vegas." Now we have the A and B of the trip. Peter goes from Tuscon to Vegas.

N-grams are similar to bag-of-words because they can also be converted into vectors. Here's the vector for the text about Peter:

![Chapter%20Summary%20Text%20Vectorization%20c02ed14b7fa44f07a874ef72a6f4997e/fedor.jpg](Chapter%20Summary%20Text%20Vectorization%20c02ed14b7fa44f07a874ef72a6f4997e/fedor.jpg)

## Creating a bag-of-words

We're going to learn how to create a bag-of-words and find **stop words**.

To convert a text corpus into a bag-of-words, use the **`CountVectorizer()`** class from the **sklearn.feature_extraction.text module.**

Import the class:

```python
from sklearn.feature_extraction.text import CountVectorizer

```

Create a counter:

```python
count_vect = CountVectorizer()

```

Pass the text corpus to the counter. Call the `fit_transform()` function. The counter extracts unique words from the corpus and counts how many times they appear in each text of the corpus. The counter doesn't count separate letters.

```python
# bow = bag of words
bow = count_vect.fit_transform(corpus)

```

This method returns a matrix where rows represent texts and the columns display unique words from the corpus. The numbers at their intersections represent how many times a given word appears in the text.

Let's use the corpus (already lemmatized) from the previous lesson:

```python
corpus = [
    'for want of a nail the shoe be lose',
    'for want of a shoe the horse be lose',
    'for want of a horse the rider be lose',
    'for want of a rider the message be lose',
    'for want of a message the battle be lose',
    'for want of a battle the kingdom be lose',
    'and all for the want of a horseshoe nail'
]
```

Let's create a bag-of-words for the matrix. Use the `shape` attribute to find out the size of the matrix:

```python
bow.shape

```

```python
(7, 16)

```

The result is 7 texts and 16 unique words.

Here's our bag-of-words as an array:

```python
print(bow.toarray())

```

```python
[[0 0 0 1 0 0 0 1 0 1 1 0 1 1 1 1]
 [0 0 0 1 1 0 0 1 0 0 1 0 1 1 1 1]
 [0 0 0 1 1 0 0 1 0 0 1 1 0 1 1 1]
 [0 0 0 1 0 0 0 1 1 0 1 1 0 1 1 1]
 [0 0 1 1 0 0 0 1 1 0 1 0 0 1 1 1]
 [0 0 1 1 0 0 1 1 0 0 1 0 0 1 1 1]
 [1 1 0 1 0 1 0 0 0 1 1 0 0 1 1 0]]

```

The list of unique words in the bag is called a vocabulary. It's stored in the counter and can be accessed by calling the **`get_feature_names()`** method:

```python
count_vect.get_feature_names()
```

Here's the vocabulary for our example:

```python
['all',
 'and',
 'battle',
 'for',
 'horse',
 'horseshoe',
 'kingdom',
 'lost',
 'message',
 'nail',
 'of',
 'rider',
 'shoe',
 'the',
 'want',
 'was']

```

`CountVectorizer()` **is also used for n-gram calculations. Specify the n-gram size with the **`ngram_range`** argument to make it count the phrases. For example, if we need to find two-word phrases, we should specify the range this way:

```python
count_vect = CountVectorizer(ngram_range=(2, 2))
```

The counter works with phrases, just like it does with words.

Since a large corpus means a larger bag-of-words, some of the words may get jumbled up and end up causing more confusion than clarity. To help out with this, usually you can drop conjunctions and prepositions without losing the meaning of the sentence. If you have a smaller and cleaner bag-of-words, it'll be easier to find the words most important for text classification.

To make sure you get a cleaner bag-of-words, find the **stop words** (words that don't mean anything by themselves). There are many of them, and they're different for each language. Let's take a look at the `stopwords` package from the `nltk.corpus` module:

```python
from nltk.corpus import stopwords
```

You'll need to download the package once to make it work:

```python
import nltk
nltk.download('stopwords')
```

Call the `stopwords.words()` function and use ****`'english'` ****as an argument to get a set of stop words for English:

```python
stop_words = set(stopwords.words('russian'))
```

Pass the stop word list to the `CountVectorizer()` when you create the counter:

```python
count_vect = CountVectorizer(stop_words=stop_words)
```

Now the counter knows which words should be excluded from the bag-of-words.

## TF-IDF

The importance of a given word is determined by the **TF-IDF** value (**Term Frequency — Inverse Document Frequency**). TF is the number of occurrences of a word in a text, and IDF measures how frequently it appears in the corpus.

Here's the formula for TF-IDF:

![Chapter%20Summary%20Text%20Vectorization%20c02ed14b7fa44f07a874ef72a6f4997e/tfidf.jpg](Chapter%20Summary%20Text%20Vectorization%20c02ed14b7fa44f07a874ef72a6f4997e/tfidf.jpg)

This is how you calculate TF:

![Chapter%20Summary%20Text%20Vectorization%20c02ed14b7fa44f07a874ef72a6f4997e/tf.jpg](Chapter%20Summary%20Text%20Vectorization%20c02ed14b7fa44f07a874ef72a6f4997e/tf.jpg)

In the formula, *t* (term) is the number of word occurrences and *n* is the total number of words in the text.

IDF's role in the formula is to reduce the weight of the most frequently used words in any other text in the given corpus. IDF depends on the total number of texts in a corpus (*D*) and the number of texts where the word occurs (*d*).

![Chapter%20Summary%20Text%20Vectorization%20c02ed14b7fa44f07a874ef72a6f4997e/idf.jpg](Chapter%20Summary%20Text%20Vectorization%20c02ed14b7fa44f07a874ef72a6f4997e/idf.jpg)

IDF's role in the formula is to reduce the weight of the most frequently used words in any other text in the given corpus. IDF depends on the total number of texts in a corpus (*D*) and the number of texts where the word occurs (*d*).

## TF-IDF in sklearn

You can calculate the TF-IDF by using the sklearn library. The **`TfidfVectorizer()`** class can be found in the `sklearn.feature_extraction.text` module. Import it this way:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
```

Create a counter and define stop words, just like we did with `CountVectorizer()`:

```python
stop_words = set(stopwords.words('english'))
count_tf_idf = TfidfVectorizer(stop_words=stop_words)

```

Call the `fit_transform()` **function to calculate the TF-IDF for the text corpus:

```python
tf_idf = count_tf_idf.fit_transform(corpus)
```

We can calculate n-grams by passing the `ngram_range` **argument **to **`TfidfVectorizer()`*.*

If the data is split into train and test sets, call the `fit()` function only for the training set. Otherwise, the testing will be biased, because the model will take into account the frequencies of the words from the test set.

## Sentiment analysis

In order to determine the tonality of the text, we can use TF-IDF values as features.

Sentiment analysis identifies emotionally-charged texts. This tool can be extremely useful in business when evaluating consumer reactions to a new product. A human would need several hours to analyze thousands of reviews. A computer will do the same in a couple of minutes.

Sentiment analysis works by labeling text as positive or negative. Positive text is given a "1," and negative text is assigned a "0."