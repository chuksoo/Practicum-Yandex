# Takeaway Sheet: Working with Missing Values

# Practice

```python
# Unique column values and counts
data['column'].value_counts()
```

```python
# Arithmetic operations with columns
# NB!: columns must have numeric values
data['column1'] = data['column2'] + data['column3']
data['column1'] = data['column2'] - data['column3']
data['column1'] = data['column2'] * data['column3']
data['column1'] = data['column2'] / data['column3']
```

```python
# Important operations for columns with numeric values
data['column'].sum()
data['column'].min()
data['column'].max()
data['column'].mean()
data['column'].median()

# Number of values in a column
data['column'].count()
```

```python
# Performing several operations on a column while grouping
data.groupby('column1').agg({'column2': ['count', 'sum'], 'column3': ['min', 'max']})
```

# Theory

**Traffic sources** - channels through which visitors come to websites

**Conversion rate** - a metric measuring the effectiveness of a traffic source (either the percentage of visitors who perform target actions or the percentage of target actions compared with total actions)

**Repeat customer rate** - the ratio of customers who complete more than one purchase to total customers

**Web analytics system** - a system that automatically gathers data from counters on site to track user behavior

**User ID** - a number assigned to a visitor to distinguish them from others

**Cookies** - special text files that remain in a device's memory after the user's first visit and are sent to the server on repeat visits

**Logs** - text files with data on site visits

**NaN** ("not a number") - a special float value used when a computation cannot be carried out (e.g. 0/0) or displayed

**None** - a special NoneType value used when a value is missing

**Categorical variable** - a variable that takes its values from a limited set

**Quantitative variable** - a variable that takes numeric values from within a range

**Logical (Boolean) variable** - a variable that takes the values True or False

**Dictionary** - a data structure that contains **key-value** pairs