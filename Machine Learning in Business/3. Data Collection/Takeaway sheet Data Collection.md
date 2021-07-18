# Takeaway sheet: Data Collection

## Practice

```python
# Cross-validation
# model — untrained model for cross-validation;
# cv — number of blocks for cross-validation (by default, it's 3).

from sklearn.model_selection import cross_val_score
cross_val_score(model, features, target, cv=3)
```

## Theory

**A crawler** or **scraper** is a software that is used to extract data from  websites.

**Unlabeled data** is data that lacks the target value.

**Data labeling** or **data annotation** is the process of determining the target values.

**Labeled data** is data with known target value.  

**Target Leakage** is a situation when ****information about the target accidentally leaks into the features.

**Cross-validation** is a method of model training and testing when the training set is split into K equal blocks. At each of the K stages, the  block *i* index is used for validation, and the rest for training.