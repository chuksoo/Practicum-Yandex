# Chapter Summary: Model Quality

# Randomness in learning algorithms

The addition of randomness to the learning algorithms is a great booster for the model's ability to discover relationships in the data. Shuffling introduces randomness to the learning algorithm. A computer can't generate truly random numbers. It uses **Pseudorandom Number Generators** that create sequences that appear random.

Random numbers are not that simple. They are unpredictable. Pseudorandom number generators can be configured so that the results are always the same. All you have to do to add pseudo-randomness when creating a learning algorithm is specify the `random_state` **parameter:

```python
# specify a ramdom state (number)
model = DecisionTreeClassifier(random_state=54321)

# train the model the same way as before
model.fit(features, target)
```

If you set `random_state` to `None` (its default), the pseudorandomness will always be different.

# Test dataset

To test if our model makes accurate predictions even when it faces new data, we are going to use a new dataset. That will be the **test dataset**.

# A**ccuracy**

The ratio of the number of correct answers to the total number of questions (i.e., the test dataset size) is called **accuracy.** 

To calculate *accuracy*, use this formula:

![Chapter%20Summary%20Model%20Quality%20cdcca2361ba347cab718e66bed4d46d5/accuracy.jpg](Chapter%20Summary%20Model%20Quality%20cdcca2361ba347cab718e66bed4d46d5/accuracy.jpg)

# **Evaluation metrics**

**Evaluation metrics** are used to measure the quality of a model and can be expressed numerically. You've already encountered one of these metrics - *accuracy*. There are others, such as:

- ***Precision*** takes all apartments that were deemed expensive by the model (they’re marked as "1") and calculates what fraction of them was actually expensive. The apartments that weren’t recognized by the model are ignored.
- ***Recall*** takes all apartments that are actually expensive and calculates what fraction of them was recognized by the model. Apartments that were recognized by the model by mistake are ignored.

Always make sure that your model performs **better than chance** — that is, do a **sanity check**. 

# Evaluation metrics in Scikit-Learn

The metric functions of the scikit-learn library can be found in the **metrics** module. Use the **accuracy_score()** function to calculate the *accuracy*.

```python
from sklearn.metrics import accuracy_score
```

The function takes two arguments (correct answers and model predictions) and returns the *accuracy* value. 

```python
accuracy = accuracy_score(target, predictions)
```

# Underfitting and overfitting

The model had no problems with the examples from the training set, but struggled when it came to the test set. This is a symptom of **overfitting**. ****The opposite effect is **underfitting**. It occurs when the *accuracy* is low and approximately the same for the training set and the test set. 

It is not always possible to avoid overfitting or underfitting. When you improve on one of these, the risk of the other increases.

Take a look at this example of fine-tuning a training algorithm. How does it affect the balance between overfitting and underfitting? **The depth of the tree** (**height)** is the maximum number of conditions from the "top" of the tree to the final answer based on the number of node-to-node transitions. 

![Chapter%20Summary%20Model%20Quality%20cdcca2361ba347cab718e66bed4d46d5/glubina.jpg](Chapter%20Summary%20Model%20Quality%20cdcca2361ba347cab718e66bed4d46d5/glubina.jpg)

The depth of the tree in *sklearn* can be set by the `max_depth` parameter:

```python
# specify the depth (unlimited by default)
model = DecisionTreeClassifier(random_state=54321, max_depth=3)

model.fit(features, target)
```

# Experiments with decision tree

To save the trained model in the correct format, use the *dump* function of this library. 

```python
# save model 
# first argument is model 
# second argument is path to file 

from joblib import dump

joblib.dump(model, 'model.joblib')
```

You can open and run the model using the *load* function.

```python
import joblib

# an argument is a path to the file 
# a return value is the model 
model = joblib.load('model.joblib')
```

-