# Chapter Summary: Looking for Duplicate Values

## Looking for Duplicates by Hand

You'll come across duplicate entries often when you’re analyzing data. If you don’t identify them in time, you might end up with flawed conclusions.

There are two ways to look for duplicate data.

**Method 1.** We can use the `duplicated()` method together with `sum()` to get the number of duplicates. Remember that if you call `duplicated()` without calculating the total, every row will get displayed on the screen, and you'll see the value `True` where there’s a duplicate and `False` where there isn’t.

**Method 2.** Call the `value_counts()` method. This method analyzes a column, selects all the unique values, and then calculates how often they appear. We can apply this method to Series objects to get lists of value-frequency pairs in descending order. The entries duplicated most frequently can be found at the top of the list.

# Looking for Duplicates by Hand with Case Sensitivity

Duplicates in string data demand special attention. From Python’s point of view, a capital `'A'` and a lowercase `'a'` are different symbols.

To catch duplicate entries like those, we can change all the characters in the string to lowercase by calling the `lower()` method**.**

Over in pandas, we change characters to **lowercase** with a method that follows a similar syntax: `str.lower()`.

# Stemming

When you’re categorizing strings, checking they contain particular substrings doesn’t always give you a correct result. One way to handle that is through stemming.

**Stemming** is the process of finding the **stem** of a given word.

The Python library NLTK contains stemmers, or objects with rules for identifying stems. The `stem()` method is used to find the stem of each word in a string.

```python
from nltk.stem import SnowballStemmer 
english_stemmer = SnowballStemmer('english')
english_stemmer.stem(text)
```

# Lemmatization

### Theory

Stemming isn’t the only process used to find words written in different forms. **Lemmatization** is a more advanced process that returns words to their dictionary forms (**lemmas**).

Here’s how lemmas are formed in English:

- For nouns, it’s the singular form.
- For adjectives, it’s the positive form (e.g. *funny*, not *funnier*).
- For verbs, it’s the infinitive.

### Practice

In NLTK, you can use WordNet Lemmatizer. It will look up a word's lemma in the WordNet database.

```python
# WordNet Lemmatizer is imported as follows:
import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemma = WordNetLemmatizer()
word_lemma = wordnet_lemma.lemmatize(word, pos = 'n')

# pos = 'n' - process only nouns
# pos = 'v' - process only verbs
# pos = 'a' - process only adjectives
# pos = 'r' - process only adverbs
```

Let's call the `word_tokenize()` method to split a sentence by words:

```python
words = nltk.word_tokenize(text)
```

Getting lemmas of the words in the list:

```python
lemmas = [wordnet_lemma.lemmatize(w, pos = 'n') for w in words]
```

Then we use Counter from the collections module to count the frequency of values in a list.

```python
from collections import Counter
print(Counter(list))
```