# Takeaway Sheet: Model Quality

[praktikum_data_scientist_takeaways_ML_theme3.pdf](Takeaway%20Sheet%20Model%20Quality%205755ce5ea3894118b1548ef857aa6dbc/praktikum_data_scientist_takeaways_ML_theme3.pdf)

# Practice

```python
# Specifying model parameters to reproduce successful experiment
# random_state - random number

model = DecisionTreeClassifier(random_state=54321)
```

```python
# Accuracy calculation

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(target, predictions)
```

```python
# Specifying decision tree parameter to control max depth of the tree 
model = DecisionTreeClassifier(random_state=54321, max_depth=3)

model.fit(features, target)
```

```python
# Save model 
# first argument is model 
# second argument is path to file 

import joblib

joblib.dump(model, 'model.joblib')
```

```python
# Upload the trained model 

import joblib

model = joblib.load('model.joblib')
```

# Theory

**Test set** is a set used to test the quality of a trained model. 

**Evaluation metrics** are the ways to measure the quality of a machine learning model. 

**Accuracy** is the ratio of the number of correct answers to the size of the test set. 

**Precision** is a evaluation metric that shows the ratio of the number of actual observations with answer "1" to the number of observations marked as "1" by the model.

**Recall** is an evaluation metric that shows what portion of actual "1" observations was marked as "1" by the model.

A **sanity check** is the process of comparing our model with a random one to assess whether the model makes sense.

**Overfitting** is the problem when the model's evaluation metric shows good results for the training set and poor results for the test set.

**Underfitting** is the problem when the model's evaluation metric shows poor results for both the training set and the test set.