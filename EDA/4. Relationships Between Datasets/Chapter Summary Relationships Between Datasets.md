# Chapter Summary: Relationships Between Datasets

## Scatterplots

Plotting discrete data points can help us identify relationships between pieces of data. When we're looking for a relationship between two parameters, we can use a **scatterplot**. We call the `plot()` function and specify `kind='scatter`'.

```python
data.plot(x='column_x', y='column_y', kind='scatter')
```

Such a graph makes it possible to see the relationship between the two values and understand which data points are typical and which are abnormal.

## Correlation

An obvious shortcoming of scatterplots is that there can be so many points clustered together that they're indistinguishable. There are two ways to make a graph clearer:

- making the points semitransparent by modifying the **alpha** parameter
- plotting a hexagonal binning plot

The graph is divided into cells, and the points in each cell are calculated. The cells are then colored: the more points there are, the denser the color.

To plot such a graph, pass `hexbin` (hexagonal binning plot) to the `kind` parameter.

The number of cells along the horizontal axis is set with the `gridsize` parameter, which is similar to `bins` for `hist()`. 

```python
data.plot(x='column_x', y='column_y', kind='hexbin', gridsize=our_gridsize, sharex=False, grid=True)
```

Like a histogram, this graph illustrates frequency. However, a histogram shows only one value, while here we have two. The high frequency of certain combinations indicates that there are clear tendencies. 

Often, the goal of data analysis is to show the relationship between two values. The interdependence of two values is known as **correlation**. Height and weight are **positively correlated**, because an increase in one generally means an increase in the other. An example of **negative correlation** would be height and voice pitch; generally (again, not always), the taller you are, the lower the frequency of your voice.

It's one thing to look at a graph, but we'll also need a numerical way to describe correlation. For this we have the **Pearson correlation coefficient**, which tells us how much one value changes when the other changes. It takes values from -1 to 1.

- If one values increases together with the other, the Pearson correlation coefficient is positive.
- If one remains the same when the other changes, the coefficient is 0.
- If one decreases when the other increases, the coefficient is negative.

The closer the coefficient is to -1 or 1, the stronger the dependency. A value close to 0 means that there's a weak connection, while a value of 0 can mean either that there's none or that there's a complex, non-linear connection that the coefficient can't reflect.

In pandas, the Pearson correlation coefficient is calculated with the **corr()** method. It is applied to the column containing the first value, and the column with the second is passed as a parameter. It doesn't matter which is which.

```python
print(data['column_1'].corr(data['column_2']))
print(data['column_2'].corr(data['column_1']))
```

## Joint Distributions for Multiple Values

Unfortunately, it's impossible to plot a coherent graph for multiple parameters right away. However, we can build scatterplots for every possible pair of parameters. In pandas, we do so not with `df.plot()`, but with a different method: `pd.plotting.scatter_matrix(df)`.

```python
pd.plotting.scatter_matrix(data)
```

Moreover, we can find the correlation coefficients for all the pairs of parameters. We can simply call the `corr()` method without any parameters. This kind of table is called a **correlation matrix:**

```python
data.corr()
```