# Takeaway sheet: Language Representations

Practice

```python
# classification by using embeddings
# df - dataset
# model - classification model

import math
import numpy as np
import pandas as pd

import torch
import transformers

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

from tqdm.auto import tqdm

# check for other models at https://huggingface.co/transformers/pretrained_models.html
tokenizer = transformers.BertTokenizer.from_pretrained('bert-base-uncased')
model = transformers.BertModel.from_pretrained('bert-base-uncased')

def BERT_text_to_embeddings(texts, max_length=512, batch_size=100, force_device=None, disable_progress_bar=False):
    
    ids_list = []
    attention_mask_list = []

    # text to padded IDs of tokens along with their attention masks
    
    for input_text in tqdm(texts, disable=disable_progress_bar):
        ids = tokenizer.encode(input_text.lower(), add_special_tokens=True, truncation=True, max_length=max_length)
        padded = np.array(ids + [0]*(max_length - len(ids)))
        attention_mask = np.where(padded != 0, 1, 0)
        ids_list.append(padded)
        attention_mask_list.append(attention_mask)
    
    if force_device is not None:
        device = torch.device(force_device)
    else:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
    model.to(device)
    if not disable_progress_bar:
        print(f'Using the {device} device.')
    
    # gettings embeddings in batches

    embeddings = []

    for i in tqdm(range(math.ceil(len(ids_list)/batch_size)), disable=disable_progress_bar):
            
        ids_batch = torch.LongTensor(ids_list[batch_size*i:batch_size*(i+1)]).to(device)
        attention_mask_batch = torch.LongTensor(attention_mask_list[batch_size*i:batch_size*(i+1)]).to(device)
            
        with torch.no_grad():            
            model.eval()
            batch_embeddings = model(input_ids=ids_batch, attention_mask=attention_mask_batch)   
        embeddings.append(batch_embeddings[0][:,0,:].detach().cpu().numpy())
        
    return np.concatenate(embeddings)

# Attention! 
# Running BERT for thousands of texts may take long run on the CPU, several hours
# Try to find a machine with GPU, it will run BERT in several minutes instead of hours
features = BERT_text_to_embeddings(df['text'])
target = df['target']

train_features, test_features, train_target, test_target = train_test_split(
    features, target, train_size=.8)

model.fit(train_features, train_target)

print(model.score(test_features, test_target))
```

Theory

**Word embeddings** is a method of representing text with vectors with respect to a language model obtained from a large corpus of texts.