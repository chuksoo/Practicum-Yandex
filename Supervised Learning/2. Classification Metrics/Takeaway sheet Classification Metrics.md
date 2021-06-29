# Takeaway sheet: Classification Metrics

# Practice

```python
# Calculating the confusion matrix 

from sklearn.metrics import confusion_matrix

print(confusion_matrix(target, predictions))
```

```python
# Calculating the recall value 

from sklearn.metrics import recall_score

print(recall_score(target, predictions))
```

```python
# Calculating the precision value

from sklearn.metrics import precision_score

print(precision_score(target, predictions))
```

```python
# Calculating F1 score value 

from sklearn.metrics import f1_score

print(f1_score(target, predictions))
```

# Theory

**True Positive answers (TP)**: the model labeled an observation as "1", and its real value is also "1";

**True Negative answers (TN):** the model labeled an observation as "0", and its real values is also "0"; 

**False Positive answers (FP):** the model labeled an observation as "1", but its actual value is "0";

**False Negative answers (FN)**: the model labeled an observation as "0", but its actual value is "1".

**Recall** is an evaluation metric that measures the share of TP answers among all answers that actually have label "1". To calculate it, use this formula:

$$Recall = \frac{TP}{TP+FN}$$

**Precision** is an evaluation metric that measures the share of observations that were labeled as positive class and were actually from the positive class. To calculate it, use this formula: 

$$Precision = \frac{TP}{TP + FP}$$

**F1 score** is an evaluation metric that is the harmonic mean of recall and precision metrics. To calculate it, use this formula:

$$F1 =\frac{2 \cdot Precision \cdot Recall}{Precision + Recall}$$