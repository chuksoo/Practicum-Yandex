# Takeaway Sheet: Looking for Duplicate Values

# Practice

## Python

```python
# Making a string lowercase

string.lower()
```

```python
# Counting up values in a list
# Counter creates a dictionary containing values and their counts

from collections import Counter
Counter(lst)
```

## pandas

```python
# Making the values in a column lowercase

data['column'].str.lower()
```

## NLTK

```python
# Getting a stemmer for English

english_stemmer = SnowballStemmer('english')
```

```python
# Getting a stem from a word

english_stemmer.stem(word)
```

# Theory

**Stemming** - finding the base, or stem, of a word

**Lemmatization** - finding the dictionary form, or lemma, of a word