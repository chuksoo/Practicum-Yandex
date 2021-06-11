# Takeaway Sheet: First Trained Model

# Practice

```python
# Obtaining class for decision tree classification

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
```

```python
# Model training 

model.fit(features, target)
```

```python
# Making predictions for new data 

answer = model.predict(new_features)
```

# Theory

The **Training dataset** is a dataset that we use to train our machine learning algorithm.

**Observations** are instances (rows) in a dataset. 

**Features** are variables (columns) in a dataset. 

The **target** is the feature we want to predict. 

**Supervised learning** is a task where you need to train a model using a training dataset (with a known target value) to predict the target for unknown data. 

**Classification** is a type of supervised learning with a categorical target. 

**Binary (or binomial) classification** is a classification with a target that can fall into one of two classes. 

**Regression** is a type of supervised learning with a numerical target.