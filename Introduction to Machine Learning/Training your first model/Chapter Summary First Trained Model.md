# Chapter Summary: First Trained Model

# **Training dataset**

Programs and experts are actually trained in a similar manner: they gather and classify knowledge, discover dependencies, and gain experience. Both human and machine learning includes some form of studying material. In the case of machine learning, models learn from training datasets.

In data analysis, rows are called instances, and columns are variables. In machine learning, rows and columns represent **observations** and **features** respectively. The feature that we need to predict is called the **target**. 

# Supervised learning

You have a training dataset and a target feature (property selling price) that you need to predict by using the rest of the features. This is a **supervised learning** task. The "teacher" poses **questions** (features) and gives **answers** (the target). No explanation is given as to how exactly the features lead to the answer; the machine has to figure it out on its own. Supervised learning is suitable for solving many business tasks. 

There are other classes as well:

- **unsupervised learning** — no target
- **semi-supervised learning** — target is known only for a portion of training data
- **Recommendation** — users and items replace features and observations (something that you can recommend like movies or neighborhoods)

Let's look at the types of supervised learning.  

All variables and features are either categorical or numerical, and the target is no exception.

Classification tasks deal with categorical targets (e.g. to determine animal species in a picture). If we only have two categories, for example, whether a client will revisit the site or not, it is a **binary classification**.

If the target is numerical, then it's a **regression task**. The data is used to find relationships between variables and make predictions based on the information, such as weather forecasting or predicting stock market prices for upcoming days.

# Models and algorithms

We assume that some kind of relationship exists between the features and the target. To make predictions, the machine has to understand what this relationship is. But accounting for all possible reasons why the target came out the way it did is not possible. That's why we have to resort to simplifications of this complex relationship – **machine learning models**.

There are many different models that can be used to represent how the features get transformed into the target, each model entailing its own assumptions about how this relationship is structured. A data scientist accepts these assumptions by picking a model, and then uses that model to make predictions. If these predictions match reality, that means the assumptions were sufficiently accurate and the model was picked correctly. This approach is called **modeling**.

One popular model is called a **decision tree**. It can describe the decision-making process in almost any situation. That's how we make a decision tree with yes/no answers and different scenarios.

![Chapter%20Summary%20First%20Trained%20Model%20b86dec2aafc94eed9eb8e0f25c5de916/otpusk.jpg](Chapter%20Summary%20First%20Trained%20Model%20b86dec2aafc94eed9eb8e0f25c5de916/otpusk.jpg)

Each tree comes out differently. We will **train the model** to build the most suitable one. In addition to the dataset, we'll need a **learning algorithm**. The dataset is processed through our learning algorithm, producing a **trained model**.

![Chapter%20Summary%20First%20Trained%20Model%20b86dec2aafc94eed9eb8e0f25c5de916/process.jpg](Chapter%20Summary%20First%20Trained%20Model%20b86dec2aafc94eed9eb8e0f25c5de916/process.jpg)

After training, the model is ready to make **predictions**: to take in new features as input and output answers (the target), without the need for learning algorithms and training datasets.

It's important to remember that the machine learning process has two steps: model training and model application. 

![Chapter%20Summary%20First%20Trained%20Model%20b86dec2aafc94eed9eb8e0f25c5de916/process_1.jpg](Chapter%20Summary%20First%20Trained%20Model%20b86dec2aafc94eed9eb8e0f25c5de916/process_1.jpg)

# Scikit-learn library

Learning algorithms are often more complex than models. So, for now, think of them as **black boxes** and focus on what we should put in and what to do with the output, rather than on what's going on inside.

Python libraries have many algorithms to offer. In this lesson we will work with the popular **scikit-learn** or **sklearn** library (*scientific kit for learning).* S*klearn* is a great source of tools for working with data and models. For convenience, the library is split into modules. Decision trees are stored in the **tree** module.

Every model corresponds to a separate class in *sklearn.* **DecisionTreeClassifier** is a class for ****decision tree classifications, let's import it from the library:

```python
from sklearn.tree import DecisionTreeClassifier
```

Then we create an instance of the class: 

```python
model = DecisionTreeClassifier()
```

The `model` variable now stores our model, and we have to run a learning algorithm to train the model to make predictions.  

To initiate training, call the **fit()** method and pass it our variables as an argument.

```python
model.fit(features, target)
```

Now we have a trained model in the `model` **variable. To predict answers, call the **predict()** method and pass it the table with the features of the new observations.  

```python
answer = model.predict(new_features)
```