# Chapter Summary: Data Collection

## Data Sources

There are many data sources that you can use to train models.

One of the sources is the company's data warehouse. All we need to do is to extract that history and prepare for analysis.  But that's a rather optimistic scenario.

Most often, the company cannot provide the data. If the task is common, datasets can be found in open sources:

- [Kaggle Data Science competition platform;](https://www.kaggle.com/)
- [UC Irvine Machine Learning Repository;](http://mlr.cs.umass.edu/ml/)
- [U.S. Government’s open database](https://www.data.gov/about);
- [FiveThirtyEight: Open data on opinion poll analysis, politics, economics, and more.](https://data.fivethirtyeight.com/)

For some tasks, data can be collected on the Internet. Download all the pages of the required portal and use **crawler** or **scraper** software to extract the data.

## Data Labeling

Perhaps the company has the data, but it lacks the target values. Such data is **unlabeled**, but you can still use it. To get a training set, we need to conduct **data labeling** or **data annotation**. That is, set the correct answer for each photo (a person or something else). This will effectively **label** the data. Sometimes labeling can be performed without special knowledge (as is the case with profile photos), but when the data relates to the health and well-being of people, you may need a professional consultation.

There are dedicated online services for labeling. Unlabeled data is uploaded to the resource and the price for labeling per observation is specified. Anyone can go to the service, label the data, and get paid for it.

Here are some popular services:

- [Amazon Mechanical Turk](https://www.mturk.com/)
- [Yandex.Toloka](https://toloka.yandex.com/)

## Labeling Quality Control

The data's quality after labeling can be improved by using the methods for **labeling quality control**. How do they work? All the observations or a part thereof are labeled several times, and then the final answer is formed.

Let's look at one such method, the **majority vote**. Who is "voting" and how? For example, each observation is labeled by three assessors. The final answer is the one chosen by the majority.

## Target Leakage

So you have collected the data. Now we can check it for **target leakage**. It occurs when information about the target accidentally leaks into the features.

## Cross-Validation

You already know how to form training, test, and validation samples and that representativeness is achieved through random sampling. But how can we ensure that the distribution is correct on a large dataset? Take several random samples!

**Cross-validation** will help to train and test the model using several randomly formed samples.

How does it work? We split all the data into training set and test set. We hold out the test set until the final evaluation, and randomly split the training set into *K* equal blocks. The split method itself is called *K-Fold*, where *K* is the number of blocks or folds (hence the name).

Suppose at the first stage of the procedure, "Block 1" is validation set, and the rest of the blocks are for training. At the second stage, "Block 2" is used for validation, and the rest of the blocks are used for training. Moving forward in this way, each block gets to be the validation set. So the process is repeated *K* times. 

![Chapter%20Summary%20Data%20Collection%20111965356ee74f2ea6ffa04646e878f3/viborka.jpg](Chapter%20Summary%20Data%20Collection%20111965356ee74f2ea6ffa04646e878f3/viborka.jpg)

We are "crossing" the data, each time taking a new block for validation. And the mean of all scores obtained through cross-validation is our model's evaluation score.

The cross-validation method resembles a bootstrap in that several samples are formed, but the difference is that cross-validation uses blocks with fixed content that doesn't change at each stage of training and validation. Each observation passes through both the training set and validation set. 

Cross-validation is useful when we need to compare models, select hyperparameters, or evaluate the usefulness of features. It minimizes the randomness of data splitting and gives a more accurate result. The only drawback of cross-validation is the computing time, especially with many observations or a large *K* value. A lot of time.

## Cross-Validation in Sklearn

Cross-validation can take less time if we use the *sklearn* tools. To evaluate the model by cross-validation we will use the **cross_val_score** function from the *sklearn.model_selection* module.

Here's how the function is called:

```python
from sklearn.model_selection import cross_val_score
cross_val_score(model, features, target, cv=3)
```

The function takes several arguments, such as:

- *model* — model for cross-validation. It is trained in the process of cross-validation, so we have to pass it untrained. Suppose we need this model for a decision tree:

```python
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
```

- *features*
- *target*
- *cv* — number of blocks for cross-validation (by default, it's 3)

The function does not require splitting data into blocks or samples for validation and training. All these steps are performed automatically. The function returns a list of model evaluation scores from each validation. Each score is equal to *model.score()* for the validation sample. For example, for a classification task, this is *accuracy*.