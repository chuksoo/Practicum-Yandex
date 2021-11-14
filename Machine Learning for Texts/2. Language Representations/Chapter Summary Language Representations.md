# Chapter Summary: Language Representations

## Word embeddings

Machines cannot work directly with words, images, and audio because they are designed to work with numbers. Language models transform text into vectors and use a set of techniques which are collectively called **word embeddings**. That is, a word is embedded into a vector space that represents a language model. Different areas in that vector space have different meanings from the language perspective.

A vector made from a word using word embedding will carry some contextual information about the word and its semantic properties. This way, the conventional definition of a word and its meaning in context isn't lost.

Semantic properties are the components of a word that contribute to its meaning. The word "seaman" has the following semantic properties: "male," "occupation," "person," "naval." These properties distinguish the word "seaman" from other words. But words don't usually stand on their own and are surrounded by other words in a sentence. Compare "The cat tangled up all the threads," and "I bumped my thread several times." The word "thread" has different meanings based on the context.

This concept allows for working with words in their vectorized form while still keeping the context in mind. This means that words with similar contexts will have similar vectors. The distance (cosine, euclidean, etc.) between the vectors is a common measure of their similarity.

## Word2vec

So how does word2vec work? You'll remember that in the past lesson, the words "finch" and "puffin" were considered similar because they can both be used in context with red beaks, and the words "anteater" and "sloth" can be used in sentences about Peru. That is to say, the meaning of the words depends on context.

Another thing word2vec can do is train a model to distinguish pairs of true neighbors from random ones. This task is like a binary classification task, where features are words and the target is the answer to the question of whether or not the words are true neighbors.

## Embeddings for classification

Now we're going to figure out how vector representation can help solve classification and regression tasks. Let's say there is a text corpus that needs to be classified. In that case, our model will consist of two blocks:

1. Models for converting words into vectors: words are converted into numerical vectors.
2. Classification models: vectors are used as features.

![Chapter%20Summary%20Language%20Representations%20940f60ea802f42d98784dc90300a6b65/12n.jpg](Chapter%20Summary%20Language%20Representations%20940f60ea802f42d98784dc90300a6b65/12n.jpg)

Let's walk through the details:

1. Before moving on to the vectorization of words, we need to perform the preprocessing:
- Each text is tokenized (broken down into words);
- Then the words are lemmatized (reduced to their root form). However, more complex models, such as BERT, don't require this step because they understand word forms;
- The text is cleaned of any stop words or unnecessary characters;
- For some algorithms (e.g. BERT), special tokens are added to mark the beginning and end of sentences.

2. Each text acquires its own list of tokens after preprocessing. 

3. Then tokens are passed to the model, and the model vectorizes them by using a pre-compiled token vocabulary. At the output, we get vectors of predetermined length formed for each text.

4. The final step is to pass the features (vectors) to the model. The model then predicts the tonality of the text: "0" — negative, or "1" — positive.

## BERT

**BERT** (Bidirectional Encoder Representations from Transformers) is a neural network model created for language representation. It was made by Google to enhance the relevance of search results and was published in 2018 (the original article can be found at: [https://arxiv.org/abs/1810.04805](https://arxiv.org/abs/1810.04805)). This algorithm is capable of "understanding" the context of a whole text, not just short phrases. BERT is frequently used in machine learning to convert texts into vectors. Specialists usually use existing BERT models that are pre-trained (by Google or, possibly, other contributors) on large text corpora. The pre-trained BERT models work for many languages. (104, to be exact.) You can train your own language representation model, but it will require a lot of computational resources.

BERT is an evolutionary step when compared to word2vec. BERT quickly became the popular choice for coders and has inspired researchers to create other language representation models: FastText, GloVe (Global Vectors for Word Representation), ELMO (Embeddings from Language Models), GPT (Generative Pre-Training Transformer). The most accurate models today are BERT and GPT-3 (though GPT-3 isn't available to the public at the moment).

![Chapter%20Summary%20Language%20Representations%20940f60ea802f42d98784dc90300a6b65/___2.jpg](Chapter%20Summary%20Language%20Representations%20940f60ea802f42d98784dc90300a6b65/___2.jpg)

When processing words, BERT takes into account both immediate neighbors and more distant words. This allows BERT to produce accurate vectors with respect to the natural meaning of words.

This is how it works:

- Here's an example of an input for the model: "The red beak of the puffin [MASK] in the blue [MASK]" where **MASK** represents unknown or masked words. The model has to guess what these masked words are.
- The model learns to figure out whether the words in the sentence are related. We had the words "flashed" and "sky" masked. The model has to comprehend that one word follows the other. So, if we hid the word "crawled" instead of "flashed", the model wouldn't find a connection.

## BERT and preprocessing

We are going to solve a classification task for movie reviews by using BERT language representation, i.e. by using BERT to create vectors for words. We're going to take a pre-trained model called bert-base-uncased (trained on lowercased English texts).

We are going to solve a classification task for movie reviews by using BERT language representation, i.e. by using BERT to create vectors for words. We're going to take a pre-trained model called bert-base-uncased (trained on lowercased English texts).

```python
import torch
import transformers
```

Before converting texts into vectors, we need to preprocess the text. BERT has its own **tokenizer** based on the corpus it was trained on. Other tokenizers won't work with BERT, and lemmatization is not required.

Preprocessing steps for the text:

1. Initialize the tokenizer as an instance of `BertTokenizer()` with the name of the pre-trained model.

```python
tokenizer = transformers.BertTokenizer.from_pretrained('bert-base-uncased')

```

2. Convert the text into IDs of tokens, and the BERT tokenizer will return IDs of tokens rather than tokens:

```python
example = 'It is very handy to use transformers'
ids = tokenizer.encode(example, add_special_tokens=True)
print(ids)
```

We get:

```python
[101, 2009, 2003, 2200, 18801, 2000, 2224, 19081, 102]

```

To operate the model correctly, we set the `add_special_tokens` argument to `True`. It means that we added the beginning token (101) and the end token (102) to any text that's being transformed. 

3. BERT accepts vectors of a fixed length, e.g. of 512 tokens. If there are not enough words in an input string to fill in the whole vector with tokens (or, rather, their identifiers), the end of the vector is padded with zeros. If there are too many words and the vector length exceeds 510 (remember, two positions are reserved for the beginning and end tokens), the input string is either limited to the size of 510 or some identifiers returned from `tokenizer.encode()` are usually skipped, e.g. all identifiers after the position 512 in the list:

```python
n = 512

padded = np.array(ids[:n] + [0]*(n - len(ids)))

print(padded)

```

We get:

```python
[101 2009 2003 2200 18801 2000 2224 19081 102 0 0 0 0 ... 0 ]
```

Now we have to tell the model why zeros don't carry significant information. This is necessary for the component of the model that is called **attention**. Let's discard these tokens and create a mask for the important tokens, indicating zero and non-zero values:

```python
attention_mask = np.where(padded != 0, 1, 0)
print(attention_mask.shape)

```

We get:

```python
(512, )

```

## BERT embeddings

Initialize the `**BertConfig**` configuration. Pass it a JSON file with the model settings description. **JSON** (JavaScript Object Notation) is a keyed stream of numbers, letters, colons, and braces that returns a server when called.

Initialize the model of **`BertModel`** class. Pass the file with the pre-trained model and configuration:

```python
config = BertConfig.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

```

Let's start by converting texts into embeddings. It may take several minutes, so engage the **tqdm** (Arabic: taqadum, تقدّم, “progress”) library. It displays the progress of the operation. In Jupyter, use the `notebook()` function from this library:

```python
from tqdm.auto import tqdm

```

The BERT model creates embeddings in batches. Make the batch size small so that the RAM won't be overwhelmed:

```python
batch_size = 100
```

Make a loop for the batches. The `notebook()` function will indicate the progress:

```python
# creating an empty list of review embeddings 
embeddings = []

for i in tqdm(range(len(ids_list) // batch_size)):
    ...

```

Transform the data into a **tensor** format. Tensor is a multidimensional vector in the torch library. `LongTensor` data type stores numbers in the "long format," that is, it allocates 64 bits for each number.

```python
# putting together vectors of ids (of tokens) to a tensor
ids_batch = torch.LongTensor(ids_list[batch_size*i:batch_size*(i+1)])
# putting together vectors of attention masks to a tensor
attention_mask_batch = torch.LongTensor(attention_mask_list[batch_size*i:batch_size*(i+1)])

```

Pass the data and the mask to the model to obtain embeddings for the batch:

```python
batch_embeddings = model(ids_batch, attention_mask=attention_mask_batch)

```

Use the **`no_grad()`** (no gradient) function to indicate that we don't need gradients in the torch library (gradients are required for the training mode when creating your own BERT model). It will make calculations faster:

```python
with torch.no_grad():
    batch_embeddings = model(ids_batch, attention_mask=attention_mask_batch)

```

Extract the required elements from the tensor and add the list of all the embeddings:

```python
# converting elements of tensor to numpy.array with the numpy() function
embeddings.append(batch_embeddings[0][:,0,:].numpy())

```

Putting all the above together, we get this loop:

```python
batch_size = 100

embeddings = []

for i in tqdm(range(len(ids_list) // batch_size)):
    
    ids_batch = torch.LongTensor(ids_list[batch_size*i:batch_size*(i+1)])
    attention_mask_batch = torch.LongTensor(attention_mask_list[batch_size*i:batch_size*(i+1)])

    with torch.no_grad():
        batch_embeddings = model(ids_batch, attention_mask=attention_mask_batch)

    embeddings.append(batch_embeddings[0][:,0,:].numpy())

```

Call the `concatenate()` function to concatenate all the embeddings in a matrix of features:

```python
features = np.concatenate(embeddings)

```