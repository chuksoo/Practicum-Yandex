# Chapter Summary: Classification Metrics

## Balance and Imbalance of the Classes

There is a strong **class imbalance** in some problems, which negatively affects how the model is trained. Classes are unbalanced when their ratio is far from 1:1. **Class balance** is observed if their number is approximately equal.

*Accuracy* doesn't get rid of this class imbalance. We need a new metric!

You already know that a class labeled "1" is called **positive**, and a class labeled "0" is called **negative**.

If we combine these responses with predictions, we will get the following division:

**True Positive answers (TP)**: the model labeled an object as "1", and its real value is also "1";

**True Negative answers (TN):** the model labeled an object as "0", and its real values is also "0"; 

**False Positive answers (FP):** the model labeled an object as "1", but its actual value is "0";

**False Negative answers (FN)**: the model labeled an object as "0", but its actual value is "1".

## Confusion Matrix

When *TP, FP, TN, FN* are collected into a table, it is called a **confusion matrix**. The matrix is formed as follows:

- The algorithm‘s labels (0 and 1) are placed on the horizontal axis ("Predictions").
- True labels of the class (0 and 1) are placed on the vertical axis ("Answers").

What we get:

1. The correct predictions are on the main diagonal (from the upper-left corner):
    - *TN* in the upper-left corner
    - *TP* in the lower right corner
2. Incorrect predictions are outside of the main diagonal:
    - *FP* in the upper right corner
    - *FN* in the lower left corner

    ![Chapter%20Summary%20Classification%20Metrics%20848637e95c52465280cfc9f342274070/False.jpg](Chapter%20Summary%20Classification%20Metrics%20848637e95c52465280cfc9f342274070/False.jpg)

The confusion matrix is located in the *sklearn.metrics* module, which is already familiar to you*.* The *confusion_matrix()* function takes correct answers and predictions and returns a confusion matrix.

```python
from sklearn.metrics import confusion_matrix

print(confusion_matrix(target, predictions))
```

## Recall

The confusion matrix will help you to build new metrics. Let's start with **recall**.

*Recall* reveals what portion of positive answers the model has identified among all answers. *Recall* is calculated using this formula:

$$Recall = \frac{TP}{TP+FN}$$

**Recall** is an evaluation metric that measures the share of TP answers among all answers that actually have a label 1. We want the recall value to be close to 1. This would mean that the model is good at identifying true positives. If it is closer to zero, the model needs to be checked and fixed.

The *recall_score()* function is located in the *sklearn.metrics* module*.* The function takes correct answers and predictions and returns the recall value. 

```python
from sklearn.metrics import recall_score

print(recall_score(target, predictions))
```

## Precision

Another metric for evaluating the quality of a target class prediction is **precision**.

Precision measures how many negative answers the model found while searching for positive ones. The more negative answers found, the lower the *precision*.

*Precision* is calculated using this formula:

$$Precision = \frac{TP}{TP + FP}$$

We want the precision value to be close to 1. The *precision_score()* function is located in the *sklearn.metrics* module*.* The function takes correct answers and predictions and returns the precision value. 

```python
from sklearn.metrics import precision_score

print(precision_score(target, predictions))
```

## F1 score

Separately, recall and precision are not very informative. You need to simultaneously increase the values for both metrics... Or we can turn to a new metric that will combine them!

*Recall* and *precision* evaluate the quality of predictions of the positive class from different angles. *Recall* describes how well the model understood the properties of this class and how well it recognized the class. *Precision* detects whether the model is overdoing it by assigning too many positive labels.

Both metrics are important. Aggregating metrics — one of which is the **F1 score** — ****help to control them simultaneously. This is the harmonic mean of *recall* and *precision*. In *F1,* 1 means that the ratio of *recall* to *precision* is 1:1.

$$F1 =\frac{2 \cdot Precision \cdot Recall}{Precision + Recall}$$

It's important to understand that when *recall* or *precision* is close to zero, the harmonic mean itself approaches 0.

The graph shows the values of *F1* score with different values of *recall* and *precision*. The blue color corresponds to zero, and the yellow color corresponds to one.

![Chapter%20Summary%20Classification%20Metrics%20848637e95c52465280cfc9f342274070/Untitled.png](Chapter%20Summary%20Classification%20Metrics%20848637e95c52465280cfc9f342274070/Untitled.png)

If a positive class is poorly predicted on one of the scales (*Recall* or *Precision*), then an F1 score close to zero will show that the prediction of class 1 has failed.

The *f1_score()* function is located in the *sklearn.metrics* module*.* The function takes correct answers and predictions and returns the harmonic mean of *recall* and *precision.*

```python
from sklearn.metrics import f1_score

print(f1_score(target, predictions))
```