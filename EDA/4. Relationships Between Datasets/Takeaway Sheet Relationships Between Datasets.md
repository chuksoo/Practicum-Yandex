# Takeaway Sheet: Relationships Between Datasets

## Practice

```python
# Building a scatterplot

data.plot(x='column_x', y='column_y', kind='scatter');

# Building pairwise scatterplots for DataFrame columns

pd.plotting.scatter_matrix(data)

# Building a cell chart
# gridsize - number of cells along the horizontal axis

data.plot(x='column_x', y='column_y', kind='hexbin', gridsize=20, sharex=False);

# Calculating the Pearson correlation coefficient
# Coefficient does not depend on the calculation procedure

print(data['column_1'].corr(data['column_2']))
print(data['column_2'].corr(data['column_1']))

# Pearson correlation coefficient for every pair of columns

data.corr()
```

## Theory

**Scatterplot** — a graph on which each point represents two values (its X and Y values)

**Hexagonal bin plot** — a graph divided into cells; their color indicates the number of points that falling into that cell

**Pearson correlation coefficient** — a number between -1 to 1 showing how much one value changes when another also changes