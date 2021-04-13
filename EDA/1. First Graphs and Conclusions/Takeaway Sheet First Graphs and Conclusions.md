# Takeaway Sheet: First Graphs and Conclusions

# 

## Practice

```python
# Reading data from a file using sep and decimal separators

data = read_csv('file.csv',  sep=';' , decimal=',')

# Displaying a histogram with an n_bins (number of bins) and minimum and maximum values (min_value and max_value) 

import matplotlib.pyplot as plt

data['column'].hist(bins=n_bins, range=(min_value, max_value))

plt.show()

# Displaying a boxplot

import matplotlib.pyplot as plt

data.boxplot('column')

plt.show()

# Changing axes' scales: x_min and x_max for the X axis, y_min and y_max for the Y axis

import matplotlib.pyplot as plt 
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

# Numerical description of a column in data

data['column'].describe()
```

## Theory

**Histograms** — graphs that show how often values occur in a particular dataset

**Distribution** — all the possible values of a variable, as well as their frequency

**Normal distribution —** a symmetrical bell-shaped curve with average and near-average values occurring frequently and those farther out being less common

**Quartile** — ****divide datasets into two separate parts: a group less than the quartile and a group greater than it (it can be greater than 25%, 50%, or 75% of the data)

**First quartile (Q1)** — 25% of the elements are less, while 75% are greater

**Median (Q2)** — half the elements are less

**Third quartile** (Q3) — 75% of the elements are less

**Interquartile range —** Q3 minus Q1

**Standard deviation —** a measure of dispersion telling you by how much values in a dataset differ from the mean; represented by sigma (σ)

**Numerical description of data** — ****the mean, median, standard deviation, number of observations in the dataset, as well as their distribution