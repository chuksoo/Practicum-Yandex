# Takeaway sheet: Imbalanced Classification

## Practice

```python
# model training with class weight adjustment
model = LogisticRegression(class_weight='balanced', random_state=12345)
```

```python
# concatenation of tables 

pd.concat([table1, table2])
```

```python
# shuffling observations

features, target = shuffle(features, target, random_state=12345)
```

```python
# Removing random observations from the table
# frac is a fraction of observations from the initial table that the method will return

features_sample = features_train.sample(frac=0.1, random_state=12345)
```

```python
# Calculate probabilities of classes

probabilities = model.predict_proba(features)
```

```python
# loop over elements of the range
# first, last, step can be fractional numbers

for value in np.arange(first, last, step):
```

```python
# plotting the ROC curve
# Returns FPR, TPR and thresholds

from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(target, probabilities)
```

```python
# calculating AUC-ROC
# takes the true values of observation classes and the predicted probability of the class

from sklearn.metrics import roc_auc_score
auc_roc = roc_auc_score(target_valid, probabilities_one_valid)
```

## Theory

**Upsampling** is a class balancing technique that increases the number of observations by duplicating the rarer class observations several times. 

**Downsampling** is a class balancing technique that decreases the number of observations by randomly dropping the majority class observations. 

**A threshold** is the probability boundary that separates the positive and negative classes.

**PR curve** is a plot that shows precision against recall.

**True Positive Rate, or TPR** is the result of the *TP* answers divided by all positive answers: 

![https://pictures.s3.yandex.net/resources/tpr-73506a98-737c-4dfe-b0eb-492c6a4045aa_1573943196.jpg](https://pictures.s3.yandex.net/resources/tpr-73506a98-737c-4dfe-b0eb-492c6a4045aa_1573943196.jpg)

**False Positive Rate, or FPR** is the result of the *FP* answers divided by all negative answers:

![https://pictures.s3.yandex.net/resources/fpr-3f76bd61-54ea-418e-8078-deb9d21735c2_1573943193.jpg](https://pictures.s3.yandex.net/resources/fpr-3f76bd61-54ea-418e-8078-deb9d21735c2_1573943193.jpg)

**ROC curve** is a plot that shows the true positive rate against the false positive rate.

**AUC-ROC** is an evaluation metric for classification tasks that equals the area under the ROC curve. The metric's values are in the range from 0 to 1. The *AUC-ROC* value for a random model is 0.5.