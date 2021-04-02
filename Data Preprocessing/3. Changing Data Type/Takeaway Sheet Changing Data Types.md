# Takeaway Sheet: Changing Data Types

# Practice

## Python

```python
 # processing exceptions
try:
	# code that might have an error
except: 
	# what to do if there is an error
```

## pandas

### Dataset

```python
# Reading an Excel file.
# Two arguments: a string with the file name and sheet_name
# If there is no second argument, the first sheet will be read

df = pd.read_excel('file.xlsx', sheet_name='Лист 1')
df = pd.read_excel('file.xlsx')
```

```python
# Joining two datasets
# Parameters: 
# - dataset we're joining to
# - on - column we're using to join the tables (common to both)
# - how - type of merge:
#     - left - table data must not have missing values, data2 can have NaN
#     - right - table data2 must not have missing values, data can have NaN

data.merge(data2, on='merge_column', how='left')
data.merge(data2, on='merge_column', how='right')
```

```python
# Creating a pivot table.
# Arguments:
# index: the column or columns whose values become the indices in the pivot table
# columns: the column whose values become columns in the pivot table
# values: the values we want to aggregate in the pivot table
# aggfunc: the aggregate function (see below) that we're applying to the values

data_pivot = data.pivot_table(index=['column1', 'column2'], columns='source', 
																		values='column_pivot', aggfunc='function')
```

### Column

```python
# Converting a column with str type to float type
# Parameters: column from a DataFrame, errors - how to handle errors
# errors='raise': default behavior, whereby invalid values generate errors, blocking conversion to numbers
# errors='coerce': incorrect values are replaced with `NaN`
# errors='ignore': incorrect values are simply ignored and left alone

pd.to_numeric(data['column'])
pd.to_numeric(data['column'], errors='raise' )
pd.to_numeric(data['column'], errors='coerce')
pd.to_numeric(data['column'], errors='ignore')

# Creates a new column without replacing the old one

data['column'] = pd.to_numeric(data['column'])
```

```python
# Converts column values to a different type (int for integers, for instance)

data['column'].astype('type')

# Creates a new column without replacing the old one

data['column'] = data['column'].astype('type')
```

```python
# Converting strings to date and time 
# Mandatory second argument - format string chosen from the following:
# %d: day of the month (01 to 31)
# %m: month (01 to 12)
# %Y: four-digit year (2019)
# Z: standard separator for date and time
# %H: hour in 24-hour format
# %I: hour in 12-hour format
# %M: minutes (00 to 59)
# %S: seconds (00 to 59)
# For instance: 20.03.2017 11:00:50 -> '%d.%m.%Y %H:%M:%S'

pd.to_datetime(data['date_time_column'], format='%d.%m.%Y %H:%M:%S') 

# Creates a new column without replacing the old one

data['date_time_column'] = pd.to_datetime(data['date_time_column'], format='%d.%m.%Y %H:%M:%S')
```

```python
# Getting individual elements of date/time

pd.DatetimeIndex(data['time']).year 
pd.DatetimeIndex(data['time']).month
pd.DatetimeIndex(data['time']).day
pd.DatetimeIndex(data['time']).hour
pd.DatetimeIndex(data['time']).minute
pd.DatetimeIndex(data['time']).second
```

# Theory

**Unix time** - time format giving the number of seconds that have passed since 00:00:00 on January 1, 1970

**Pivot table** - a table summarizing the data in a larger table