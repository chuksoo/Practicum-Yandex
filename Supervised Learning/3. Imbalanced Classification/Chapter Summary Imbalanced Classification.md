# Chapter Summary: Imbalanced Classification

## Class weight adjustment

Machine learning algorithms consider all observations in the training set to be equally weighted by default. If we need to indicate that some observations are more important, we assign a **weight** to the respective class.

 Logistic regression, decision tree, and random forrest in the *sklearn* library have *class_weight* argument. By default, it is `None` — i.e., classes are equivalent:

`class "0" weight = 1.0`

`class "1" weight = 1.0`

If we specify `class_weight='balanced'`, the algorithm will calculate how many times class "0" occurs more often than class "1". We’ll denote this number as N (an unknown number of times). The new class weights look like this:

`class "0" weight = 1.0`

`class "1" weight = N`

The rare class will have a higher weight.

## Upsampling

When we train models, the classes can be balanced by increasing the sample size. The technique is called **upsampling**.

Upsampling is performed in several steps:

- Split the training sample by class.
- Determine the class with fewer observations. Call it the rare class.
- Duplicate the rarer class observations several times.
- Create a new training sample based on the data obtained.
- Shuffle the data.

Copying observations several times can be done using Python's list multiplication syntax. To repeat the list elements, the list is multiplied by a number (the required number of repetitions):

```python
answers = [0, 1, 0]
print(answers)
answers_x3 = answers * 3
print(answers_x3)
```

```
[0, 1, 0]
[0, 1, 0, 0, 1, 0, 0, 1, 0]
```

Use the **pd.concat()** function to concatenate the tables. It takes a list of tables as input. The source data can be obtained as follows:

```python
pd.concat([table1, table2])
```

To shuffle observations randomly, use the *shuffle* method from the *sklearn.utils* library:

```python
features, target = shuffle(features, target, random_state=54321)
```

The *upsample()* function:

```python
def upsample(features, target, repeat):
    features_zeros = features[target == 0]
    features_ones = features[target == 1]
    target_zeros = target[target == 0]
    target_ones = target[target == 1]

    features_upsampled = pd.concat([features_zeros] + [features_ones] * repeat)
    target_upsampled = pd.concat([target_zeros] + [target_ones] * repeat)
    
    features_upsampled, target_upsampled = shuffle(
        features_upsampled, target_upsampled, random_state=54321)
    
    return features_upsampled, target_upsampled
```

## Downsampling

Instead of repeating the important questions, we can also remove a part of the unimportant ones. For this, we can use the **downsampling** technique.

Downsampling is performed in several steps:

- Split the training sample by class;
- Determine the class with more observations. Let's call it the majority class;
- Randomly drop a portion of majority class observations;
- Create a new training sample based on the data obtained;
- Shuffle the data.

To randomly discard some of the table elements use the *sample()* function. It takes *frac* (from *fraction*) and returns random elements in such amounts that their fraction in the initial table equals *frac.*

```python
features_sample = features_train.sample(frac=0.1, random_state=54321)
```

The *downsample()* function:

```python
def downsample(features, target, fraction):
    features_zeros = features[target == 0]
    features_ones = features[target == 1]
    target_zeros = target[target == 0]
    target_ones = target[target == 1]

    features_downsampled = pd.concat(
        [features_zeros.sample(frac=fraction, random_state=54321)] + [features_ones])
    target_downsampled = pd.concat(
        [target_zeros.sample(frac=fraction, random_state=54321)] + [target_ones])
    
    features_downsampled, target_downsampled = shuffle(
        features_downsampled, target_downsampled, random_state=54321)
    
    return features_downsampled, target_downsampled
```

## Classification Threshold

To determine the answer, logistic regression computes the **probability of classes**. We have only two classes (zero and one). The probability of class "1" will be enough for us. The value is in the range from zero to one: if it is greater than 0.5, the observation is positive; otherwise, it's negative.

The line where the negative class ends and the positive class begins is called the threshold. By default, it is 0.5, but we can change it.

## Threshold Adjustment

In *sklearn,* the class probability can be calculated with the **predict_proba()** function. It takes features of the observations and returns the probabilities:

```python
probabilities = model.predict_proba(features)
```

Strings correspond to observations. The first column indicates the negative class probability, and the second indicates the positive class probability (the two probabilities sum to unity). 

To create a loop with the desired range, we use the *arange()* function from the *numpy* library. Just like the *range()* function, it iterates over the specified elements of the range, but it's different in that it works with fractional numbers in addition to integers:

```python
for value in np.arange(first, last, step):
```

## PR curve

Let's plot the values of the metrics and see how the curve responds to the threshold changing.  

On the graph, the precision value is plotted vertically, and recall — horizontally. A curve plotted from **P**recision and **R**ecall values is called a **PR curve**. The higher the curve, the better the model.

![Chapter%20Summary%20Imbalanced%20Classification%206832e0925bf14f0ebcded9072fb6c20a/Recall.jpg](Chapter%20Summary%20Imbalanced%20Classification%206832e0925bf14f0ebcded9072fb6c20a/Recall.jpg)

## TPR & FPR

You can't calculate the precision when there are no positive observations. Let's consider the metrics that don't imply division by zero.

Before moving on to the new curve, let's define a few important terms.

*True Positive Rate*, **or *TPR*, **is the result of the *TP* answers divided by all positive answers. Here's the formula, where *P* is all positive answers:

$$TPR = \frac{TP}{P}$$

The *False Positive Rate*, or *FPR*, is the result of the *FP* answers divided by all negative answers. It is calculated using a similar formula, where *N* is all negative answers:

$$FPR = \frac{FP}{N}$$

There will be no division by zero: the denominators are constant values that don't depend on changes in the model.

## ROC curve

We have witnessed a new confrontation: *TPR* vs *FPR*. Let's plot the curve.

We put the *false positive rate* values (*FPR) along the horizontal axis*, and *true positive rate* values (*TPR*) along the vertical axis. Then we iterate over the logistic regression threshold values and plot a curve. It is called the **ROC curve** (***R**eceiver **O**perating **C**haracteristic —*  a term from signal processing theory*)*.

For a model that always answers randomly, the *ROC* curve is a diagonal line going from the lower left to the upper right. The higher the curve, the greater the *TPR* value and the better the model's quality.

![Chapter%20Summary%20Imbalanced%20Classification%206832e0925bf14f0ebcded9072fb6c20a/roc-krivaya.jpg](Chapter%20Summary%20Imbalanced%20Classification%206832e0925bf14f0ebcded9072fb6c20a/roc-krivaya.jpg)

To find how much our model differs from the random model, let's calculate the **AUC-ROC** value (**A**rea **U**nder **C**urve **ROC**) This is a new evaluation metric with values in the range from 0 to 1. The *AUC-ROC* value for a random model is 0.5.

We can plot a *ROC* curve with the *roc_curve()* variable from the *sklearn.metrics* module*:*

```python
from sklearn.metrics import roc_curve
```

It takes the target values and the positive class probabilities, goes over different thresholds, and returns three lists: *FPR* values, *TPR* values, and the thresholds it went over.

```python
 fpr, tpr, thresholds = roc_curve(target, probabilities)
```

To calculate *AUC-ROC,* use the *roc_auc_score()* function from the *sklearn* library*:*

```python
from sklearn.metrics import roc_auc_score
```

Unlike other metrics, it takes class "1" probabilities instead of predictions:

```python
auc_roc = roc_auc_score(target_valid, probabilities_one_valid)
```