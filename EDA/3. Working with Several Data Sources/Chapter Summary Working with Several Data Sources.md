# Chapter Summary: Working with Several Data Sources

# 

## Slices of Data from External Dictionaries

When working with slices, you can use external variables not only of numeric or string types. Sometimes we need to create queries using variables that contain more complicated structures than a standalone number or list — for instance, a dictionary, Series object, or DataFrame. You can address them just as you would ordinary external variables. To find out whether the values from a column are in the list, write the query `' in @our_list'`.

```python
our_list = [1, 2, 3]
print(data.query('column in @our_list'))
```

A similar check is performed for dictionaries. We check for the presence of a certain value in the dictionary keys:

```python
our_dict = {0: 10, 1: 11, 2: 12}
print(data.query('column in @our_dict'))
```

If the variable stores a Series object, then the statement  `in @our_series` will check for presence among the *values* of that series, rather than among its *indices*.

```python
our_series = pd.Series([10,11,12])
print(data.query('column in @our_series'))
```

If you need to check whether `a` values are present among the indices in the Series, use the `.index` attribute: `a in @our_series.index`.

```python
our_series = pd.Series([10,11,12])
print(data.query('column in @our_series.index'))
```

When we're working with a DataFrame object, inclusion in its index is checked in the same way. We just add `.index` to the name of the DataFrame:

```python
our_dataframe = pd.DataFrame ({
'column1': [2, 4, 6],
'column2': [3, 2, 2],
'column3': ['A', 'B', 'C'],
})
print(data.query('column in @our_dataframe.index'))
```

To check for presence in a column, pass the column's name:

```python
our_dataframe = pd.DataFrame ({
'column1': [2, 4, 6],
'column2': [3, 2, 2],
'column3': ['A', 'B', 'C'],
})
print(data.query('column in @our_dataframe.column2'))
```

## Adding a Column

Several histograms can be displayed on a single chart. In order to do so, you can use the following construct:

```python
ax = data1.plot(kind='hist', y='column1', histtype='step', range=(0, 500), bins=25,
                              linewidth=5, alpha=0.7, label='raw')
data2.plot(kind='hist', y='column1', histtype='step', range=(0, 500), bins=25, 
                       linewidth=5, alpha=0.7, label='filtered', ax=ax, grid=True, legend=True)
```

Note that we called the `plot()` method instead of `hist()`. It contains the `kind` parameter, with its value set to `kind = 'hist'`. We get the same histogram, just plotted using `plot()` rather than `hist()` with the following parameters:

- `histtype`: this parameter indicates the type of histogram; by default it's a bar chart (filled in). The value `step` only draws a line.
- `linewidth`: line width in pixels.
- `alpha` ("alpha channel"): sets the line fill density. 1 is 100% filled, while 0 is transparent. Lines are partially transparent with the parameter set to 0.7, making intersections easier to spot.
- `label`: line name.
- `ax` (for "axis"): the `plot()` method returns the axes on which the graph was built. In order for both histograms to be located on a single graph, save the axes of the first graph in the `ax` variable and pass it to the `ax` parameter of the second `plot()`. Thus, by saving the axes of one histogram and building a second on the axes of the first, we merge two graphs together.
- `legend`: prints a legend (a list of the elements of a graph). It can be found in the upper right-hand corner of the graph.

**Adding columns to a DataFrame:** to add a column from `data2` to `data1`, create a new column in `data1` and assign it the values of the `data2` column:

```
data1['new'] = df2['column']
```

If the `new` column had already been in `df1`, all of its elements would have been replaced with the new ones.

It seems relatively simple: pandas copies a column from `data2` and puts it in `data1`.

However, if you take a closer look, things aren't so simple. For each row of the first DataFrame, pandas looks for a "mate," a row with the same index in the second DataFrame, and takes a value from that row. In our case, the indices in `data1` and `data2` are the same, so this is a trivial case: all the values get copied in the same order in which they're positioned. If the indices are different, however, we'll get `NaN` values where the indices are absent. 

Note that our DataFrames don't have to have the same numbers of rows. If `data2` doesn't have as many rows as `data1`, then we end up with some `NaN` values. If `data2` has more rows, they simply won't become part of the new DataFrame.

Columns can also exist separately, outside of DataFrames. A single column can be saved in a Series object – an array of values with indices. Since Series have indices, the assignment of a Series to, say, a column of a DataFrame, will work in the same way that we saw earlier – the values will be copied on the basis of matching indices.

## Combining Data from Two Tables

When working on tasks, it’s important to choose the proper averaging method, since that could impact the findings. In some cases, the arithmetic mean describes the data more precisely, while in others it can yield an incorrect result, making it necessary to calculate the median.

Remember that the `pivot_table()` method groups data, while the `aggfunc` argument defines how to process the data in each group. For example, there's:

- `median`
- `count` (number of values)
- `sum`
- `min`
- `max`
- `first` (the first value from the group)
- `last` (the last value from the group)

When calling `pivot_table()`, we can pass the `aggfunc` parameter several functions at once. For example, `aggfunc=['median', 'count']` will calculate both the median and the number of values. They will show up in neighboring columns in the resulting table.

## Renaming Columns

We've dealt with a table with two-level column names. This is a MultiIndex, a kind of hierarchical indexing structure that we see when an index contains a list of values rather than a single value. 

But what if we don't want those complex column names? Then we need to rename our columns using the `columns` **attribute:

```python
df.columns = ['column_name_1', 'column_name_2', 'column_name_3']
```

## Combining Columns Using the merge() and join() Methods

When you have to add several new columns to an existing DataFrame, **joining** or **merging** is more efficient than adding them one by one.

**Inner merging** results in the logical conjunction of both tables (the records that are present in both DataFrames). `inner` is the `merge()` method's default merging method. **Outer merging** (`outer`) gives the logical disjunction of both tables (the records that are present in either of the two DataFrames). The merging mode is set in the `how` parameter.

```python
data1.merge(data2, on='column', how='inner')
```

The combination mode `left` indicates that all the rows from the left DataFrame should always enter the merge result. If there are missing values in the right DataFrame, they will be replaced by `NaN`. You can probably guess that `right` gives you all the matching rows and all other entries from the right DataFrame (the right DataFrame being the one inside parentheses).

In the table we got above using the `merge()` **method, `_x` and `_y` were added to column names. Column name endings are specified in the `suffixes` argument.

If an index column is given a name, the name can also be passed to the `on` parameter. Combining several columns at once is also possible; just pass a list of them to the `on` argument.

The `join()` method is similar to the `merge()` method. Without the `on` parameter, `join()` will automatically seek matches based on the indices in the first and second DataFrames. If a column is passed to the `on` parameter, `join()` finds it in the first DataFrame and begins comparing it to the index of the second DataFrame.  In `join()`, unlike `merge()`*,* the merge type `how=‘left’` is set the default. But the `suffixes` parameter is divided into two independent ones: `lsuffix` ("left suffix") and `rsuffix` ("right suffix"). It's also possible to combine more than two tables using the `join()` method: they're passed as a list instead of the second DataFrame.