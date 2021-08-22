# Chapter Summary: Gradient Boosting

## Ensembles and boosting

An **ensemble** is a set of models for solving the same problem. The strength of ensembles is that the mean error of a group of models is less significant than their individual errors.

You are already familiar with one of the types of ensemble models — the random forest. In a random forest, the results of **base** or **weak** learners (models comprising the ensemble) are averaged. The base classifiers for a random forest are decision trees.

Another approach to ensemble building is **boosting**, where each subsequent model takes into account the errors of the previous one and, in the final prediction, the forecasts of basic learners. Take a look:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/anx.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/anx.jpg)

where *aN(x)* is the ensemble prediction, *N* is the number of base learners, *bk(x)* is the base learner prediction, and γn is the model weight.

For example, we are dealing with a regression task. We have *n* observations with features *x* and correct answers *y*. Our task is to minimize the *MSE* loss function:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/MAE.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/MAE.jpg)

For convenience, equate the model weights to unity:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/yk.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/yk.jpg)

We get:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/anx1.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/anx1.jpg)

Now we create an ensemble of sequential models.

First, build the base learner *b₁* by solving the minimization task:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/b1.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/b1.jpg)

The result is this ensemble:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/a1x.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/a1x.jpg)

Indicate the **residual**. It is the difference between the prediction at the first step and the correct answers:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/a1x%201.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/a1x%201.jpg)

At the second step, we build the model like this:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/b2.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/b2.jpg)

The ensemble will take the following form:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/a2x.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/a2x.jpg)

The ensemble will take the following form:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/e2i.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/e2i.jpg)

At each subsequent step, the algorithm minimizes the ensemble error from the preceding step.

Let's summarize the formulas. At step *N-1*, the residual is calculated as follows:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/en1i.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/en1i.jpg)

The ensemble itself is represented as the sum of predictions of all the base learners combined up to this step:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/anx1%201.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/anx1%201.jpg)

So, at step N, the algorithm will pick the model with the ensemble error at step N-1:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/bnx.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/bnx.jpg)

## Gradient boosting

In boosting, each base learner tries to "push" the predictions of the previous step towards correct answers. That's how the loss function is minimized. Gradient boosting makes the process even more efficient.

As before, our goal is to minimize the loss function, but now the argument along which the descent will be performed is the model's answers! And thus we get **gradient boosting**.

For example, our loss function is *L(y, a),* and it has a derivative. Let’s recall the ensemble formula:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/anx%201.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/anx%201.jpg)

At each step, select the answers that will minimize the function:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/lyax.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/lyax.jpg)

Minimize the function with gradient descent. To do so, at each step, calculate the negative gradient of the loss function for prediction *gN*:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/gnx.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/gnx.jpg)

To push the predictions towards correct answers, the base learner learns to predict *gN*: 

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/bn.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/bn.jpg)

Obtain the weight for *bN* from the minimization task by iterating various numbers:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/yN.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/yN.jpg)

It is the coefficient for the base learner that helps adjust the ensemble to make predictions as accurate as possible.

Gradient boosting is suitable for different loss functions that have derivatives — for example, the mean square in a regression task or logarithmic in a binary classification task.

## Gradient boosting regularization

Regularization can be used to reduce overfitting during gradient boosting. If the weights in a linear regression have been reduced, then the gradient boosting regularization is:

1. step size reduction;
2. adjustment of tree parameters;
3. subsample randomization for base learners *bᵢ.*

Reduce the step size. Revise the formula for calculating predictions at step *N*:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/anx%202.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/anx%202.jpg)

When an algorithm takes steps which are too large, it quickly remembers the training set. This results in overfitting the model.

Introduce the *η* coefficient*.* It controls the **learning rate** and can be used to reduce the step size:

![Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/anxn.jpg](Chapter%20Summary%20Gradient%20Boosting%203f402b10fc3542adb1db838a77a51aff/anxn.jpg)

The value for this coefficient is picked by iterating over different values in the range from 0 to 1. A smaller value means a smaller step towards the negative gradient and a higher accuracy of the ensemble. But if the learning rate is too low, the training process will take too long.

The second way to regularize gradient boosting is to adjust tree parameters. We can limit the tree depth or number of elements in each node, try different values, and see how it affects the result. For example, let's limit the depth for each tree to 2. At each step of the boosting, we won't have to make a complex tree that would adjust to all the residuals and the model won't be too overfitted.

The third method of regularization is working with subsamples. The algorithm works with subsamples instead of the whole set. This algorithm version is similar to SGD and is called **stochastic gradient boosting.**

## Libraries for gradient boosting

1. XGBoost (extreme gradient boosting) is a popular gradient boosting library on Kaggle. Open source. Released in 2014.
2. LightGBM (light gradient boosting machine). Developed by Microsoft. Fast and accurate gradient boosting training. Directly works with categorical features. Released in 2017. Comparison with XGBoost: [https://lightgbm.readthedocs.io/en/latest/Experiments.html](https://lightgbm.readthedocs.io/en/latest/Experiments.html)
3. CatBoost (categorical boosting). Developed by Yandex. Superior to other algorithms in terms of evaluation metrics. Applies various encoding techniques for categorical features (LabelEncoding, One-Hot Encoding). Released in 2017. Comparison with XGBoost and LightGBM: [https://catboost.ai/#benchmark](https://catboost.ai/#benchmark)

Let's have a look at the CatBoost library.

Import `CatBoostClassifier` from the library and create a model. Since we have a classification problem, specify the logistic loss function. Take 10 iterations so that we don't have to wait too long.

```python
from catboost import CatBoostClassifier

model = CatBoostClassifier(loss_function="Logloss", iterations=10)
```

Train the model with the `fit()` method*.* In addition to target and features, pass the categorical features to the model:

```python
# cat_features - categorical features

model.fit(features_train, target_train, cat_features=cat_features)
```

When we have many iterations and don't want to output information for each one, use the **`verbose`** argument:

```python
model = CatBoostClassifier(loss_function="Logloss", iterations=50)
model.fit(features_train, target_train, cat_features=cat_features, verbose=10)
```

Calculate the prediction with `predict()`:

```python
pred_valid = model.predict(features_valid)
```