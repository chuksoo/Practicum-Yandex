# Chapter Summary: Model Improvement

# Validation datasets

For quality evaluation to be reliable, we need a **validation** data set.

The validation dataset is separated from the source dataset before the model is trained. Otherwise, the model would know all the answers after learning from the training set. Validation shows how the models act in the field and helps to reveal overfitting.

The portion of the data to be assigned to the validation set depends on the number of observations and features, as well as the data variation. Here are the two most common scenarios: 

1) The test set exists (or will exist in the near future), but is unavailable for the time being. The preferable ratio is 3:1. This means 75% for the training set and 25% for the validation set. This scenario will be used on our online training platform.

2) The test set doesn't exist. In that case, the source data has to be split into three parts: training, validation, and test. The sizes of the validation set and the test set are usually equal. This scenario gives us a 3:1:1 ratio (60% for the training set and 20% each for the validation and test sets).

# Splitting data into two sets

Scikit-learn has a special function **train_test_split()** for this purpose. It can split any data set in two, and is named so because it is usually used to split sets into training and test sets. But we are going to use this function to obtain a training set and a validation set.

```python
from sklearn.model_selection import train_test_split
```

Before splitting, we need to set two parameters: 

- **Name of the dataset** that we are going to split.
- **Size of validation set** (`test_size`). The size is expressed as a decimal from 0 to 1 that represents a fraction of the source dataset. In our case, we have `test_size=0.25` because we want to work with 25% of the source set.

The `t*rain_test_split()`* function returns two sets of data: training and validation.

```python
df_train, df_valid = train_test_split(df, test_size=0.25, random_state=54321)
```

Note: we can assign any value to `random_state` except for `None`. 

# Hyperparameters

The model acquires all the parameters from the training set. In addition to regular model parameters, we have **hyperparameters.** These are settings for learning algorithms. You need to specify them before training.

For example, in the decision tree, hyperparameters are:

— **max_depth:** the max depth of the tree.

— **criterion:**  the criterion of splitting.

— **min_samples_split:** this prohibits creating nodes that don't contain enough observations from the training set. 

— **min_samples_leaf:** Leaves are the lowest nodes with the answers that do not split the data any further. This hyperparameter prevents the algorithm from adding leaf nodes that don't have enough observations from the training set.

# New models: random forest

Let's try a new learning algorithm called a random forest. It trains a large quantity of independent trees and makes a decision by voting. A random forest helps to improve results and avoid overfitting.

In the scikit-learn library, you can find the **RandomForestClassifier**, which is a random forest algorithm. Import it from the **ensemble** module:

```python
from sklearn.ensemble import RandomForestClassifier
```

To set the number of trees in the forest, we will use the `n_estimators` *(number of estimators)* hyperparameter. The quality of the end result and the duration of training are directly proportional to the number of trees. 

```python
model = RandomForestClassifier(random_state=54321, n_estimators=3)
```

# Logistic regression

If we increase the value of the `n_estimators` **hyperparameter, the model gets bulky and the training process slows down, which is bad. But if we keep the number of trees low, the results won't improve. So that's also bad. 

Let's try **logistic regression.** Even though the name is suggestive of a regression problem, it is still a classification algorithm.

To predict the class of an apartment, logistic regression does the following: 

- First, it decides which class the observation is closest to.
- Depending on the answer, it chooses the class: if the calculation result is positive, then "1" (high prices); negative — "0" (low prices).

There are only a few parameters in logistic regression. The model will not be able to memorize anything from the features in the formula, so the probability of overfitting is low.

The **LogisticRegression** model is located in *sklearn.linear_model* module of the *sklearn* library. Import it: 

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(random_state=54321)
```