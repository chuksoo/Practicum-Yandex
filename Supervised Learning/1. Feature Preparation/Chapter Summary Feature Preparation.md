# Chapter Summary: Feature Preparation

Let's recap. The *OHE* technique allows us to transform categorical features into numerical features in two steps:

## One-Hot Encoding

There is a special technique for transforming categorical features into numerical features. It is called **One-Hot Encoding (OHE)**.

1. Add a separate column for each feature value.
2. If the category fits the observation, 1 is assigned; otherwise, 0 is assigned.

New features (`Gender_F`, `Gender_M`, `Gender_None`) are called **dummy variables**.

You can get dummy variables for *OHE* using the **get_dummies()** function. It can be found in the pandas library.

```python
pd.get_dummies(df['column'])
```

## Dummy Trap

When data is abundant, we have a chance of falling into the dummy feature trap. We have added three new columns to our table, but their high correlation will confuse our model. To avoid this, we can safely remove any one column, since its values can be easily inferred from the other two columns (it has 1 where the other two columns have zeroes, and it has zeroes everywhere else). This way, we will not fall into the dummy trap.

To remove the column, call the `pd.get_dummies()` function along with the **drop_first** parameter. If you pass `drop_first=True` then the first column is dropped. Otherwise it's `drop_first=False` by default, and no columns are dropped.

```python
pd.get_dummies(df['column'], drop_first=teTrue)
```

## **Ordinal Encoding**

We need a new encoding technique, one that allows encoding textual categories with numbers. We are going to use **Ordinal Encoding**. Here's how it works:

1. It encodes each class with a number.
2. The numbers are put in the columns.

S*klearn* provides a class for such encoding. It is called **OrdinalEncoder**. You can find it in the `sklearn.preprocessing` module.

Import `OrdinalEncoder` from the library:

```python
from sklearn.preprocessing import OrdinalEncoder
```

The transformation is performed in three steps:

1. Create an instance of this class.

```python
encoder = OrdinalEncoder()
```

2. Call the `fit()` method to obtain the list of categorical features — the same process we do when training a model. Pass it the data.

```python
encoder.fit(data)
```

3. Use the `transform()` ****method. The transformed data will be stored in the `data_ordinal` **variable*.*

```python
data_ordinal = encoder.transform(data)
```

Use `DataFrame()` **to add column names*:*

```python
data_ordinal = pd.DataFrame(encoder.transform(data), 
													  columns=data.columns)
```

If we need to transform the data only once, like in our case, you can also call the `fit_transform()` method. It combines `fit()` and `transform()`*.*

```python
data_ordinal = pd.DataFrame(encoder.fit_transform(data), 
													  columns=data.columns)
```

## Feature Scaling

If we have data with numerical features that have different dispersion of values, the algorithm may find the features with higher magnitudes and dispersion to be more important. This issue can be addressed with **feature scaling**.

One of the ways to scale the features is to **standardize the data**.

Suppose that all features are normally distributed, the mean (*M*) and variance (*Var*) are determined from the sample. Feature values are converted by the formula:

![Chapter%20Summary%20Feature%20Preparation%2030957d82a6d14c33a310a448b13ebcd0/A3DA0F9C-0ABF-43D1-AEC6-4EA9B7E952E8.png](Chapter%20Summary%20Feature%20Preparation%2030957d82a6d14c33a310a448b13ebcd0/A3DA0F9C-0ABF-43D1-AEC6-4EA9B7E952E8.png)

For the new feature, the mean becomes 0 and variance equals 1.

There is a dedicated *sklearn* class for data standardizing that is called *StandardScaler*. It's in the *sklearn.preprocessing* module*.*

```python
from sklearn.preprocessing import StandardScaler
```

Create an instance of the class and tune it using the training data. The tuning process involves calculating the mean and variance:

```python
scaler = StandardScaler()
scaler.fit(df)
```

Transform the training set and the validation set using *transform()*. 

```python
df_scaled = scaler.transform(df)
```