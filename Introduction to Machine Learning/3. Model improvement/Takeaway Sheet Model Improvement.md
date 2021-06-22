# Takeaway Sheet: Model Improvement

# Practice

```python
# Splitting data into training and validation sets 
# test_size - the fraction of total number of objects that has to be split as the validation set (a number from 0 to 1)
from sklearn.model_selection import train_test_split

df_train, df_valid = train_test_split(df, test_size=0.25, random_state=54321)
```

```python
# Initializing the decision tree model 
# n_estimators - a number of trees
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=54321, n_estimators=3)
```

```python
# Initializing the logistic regression model
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(random_state=54321)
```

# Theory

A **validation set** is a set of data that is a part of a source dataset. It's used to check an algorithm‘s quality during a model's training.  

**Parameters** are model's settings obtained from training data that determine the model's work. 

**Hyperparameters** are settings for learning algorithms.