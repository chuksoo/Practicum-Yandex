# Takeaway Sheet: Data Slices

# 

## Practice

```python
# Checking for the presence of an element in a column

data['column'].isin('element')
```

```python
# Quick data slicing

data.query('column != "value"')
data.query('column < column.mean()')

variable = 2
data.query('column > @variable')
```

```python
# yearfirst=True indicates that the date in the string starts with the year
data['datetime'] = pd.to_datetime(df['datetime'], yearfirst=True)
```

```python
# Working with dates and times

data['datetime'].dt.date # Retrieve date
data['datetime'].dt.year # Retrieve year
data['datetime'].dt.weekday # Retrieve day of the week
```

```python
# Shift date and time
data['shifted_dt'] = data['datetime'] + pd.Timedelta(hours=10) # Add 10 hours
```

```python
# Rounding time

data['datetime'] = data['datetime'].dt.round('1H') # round to hour
data['datetime'] = data['datetime'].dt.round('1D') # round to day
data['datetime'] = data['datetime'].dt.round('5T') # round to 5 minutes
data['datetime'] = data['datetime'].dt.round('10S') # round to 10 seconds
data['datetime'] = data['datetime'].dt.floor('1H') # always round down
data['datetime'] = data['datetime'].dt.ceil('1H') # always round up
```

```python
# Plotting graphs based on a DataFrame
# X parameter: which column will be used for the horizontal axis
# Y parameter: which column will be used for the vertical axis
# style: plot style; 'o': scatter plot; 'o-': connected scatterplot
# xlim: boundaries for X axis
# ylim: boundaries for Y axis
# grid: display or hide the grid
# figsize: image size, (x_size, y_size)

data.plot(x='column1', y='column2', style='o-', xlim=(0, 30), figsize = (4, 5), grid=True)

```

## Theory

**Data slice** — part of a dataset selected according to specific conditions

**Bug report** — a message with detailed information on an error: a description of the error, as well as where, when, and how it was encountered