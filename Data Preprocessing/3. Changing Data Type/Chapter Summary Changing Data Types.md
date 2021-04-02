# Chapter Summary: Changing Data Types

# How to Read Excel Files

We have a special method called `read_excel()` for reading Excel files. It’s similar to `read_csv()`, the difference being that `read_excel()` needs two arguments: the string with the name of the file or the file path, and the `sheet_name`. If there’s no `sheet_name` argument, the method reads the first sheet by default.

```python
import pandas as pd
df = pd.read_excel('file.xlsx', sheet_name='List1')
```

# Turning String Values into Numbers

We use a standard pandas method to convert string values into numbers: `to_numeric()`. It turns column values into **float64** (floating point number) or **int64** (integer) type, depending on the input value.

The `to_numeric()` method has an `errors` parameter. The errors values determine what `to_numeric` will do when it encounters an invalid value:

- `errors='raise'`: Default behavior. An exception is raised when an incorrect value is encountered, halting the conversion to numbers.
- `errors='coerce'`: Incorrect values are replaced with NaN.
- `errors='ignore'`: Incorrect values are left unchanged.

In order to convert data to the type we’re looking for, we use the `astype()` method. A string with the name of the type is passed as the argument.

# Working with Date and Time using pandas

Python has a special data type we use to work with dates and times: **datetime**.

In order to convert strings into dates and times, we use the **to_datetime()** method. The method’s parameters are the column containing strings and the date format in a string.

We set the date format using a special designation system:

- %d: day of the month (01 to 31)
- %m: month (01 to 12)
- %Y: four-digit year (for example, 2019)
- %H: hour in 24-hour format
- %I: hour in 12-hour format
- %M: minutes (00 to 59)
- %S: seconds (00 to 59).

```python
date['column']= pd.to_datetime(date['column'], format='%d.%m.%YZ%H:%M:%S')
```

There are various ways to represent dates and times, but the **unix time** format deserves special attention. This format gives us the number of seconds that have passed since 00:00:00 on January 1, 1970. Unix time corresponds to Coordinated Universal Time, or UTC.

The `to_datetime()` method works with the unix time format, as well. The first argument is the column with unix times. The second argument is `unit`; it has the `'s'` value and communicates that the time needs to be converted to the usual format with precision to the second.

We often have to study statistics by month, day, or year. To do so, we place the time in the DatetimeIndex class and apply the month*,* day*,* or year attribute to it:

```python
date['column'] = pd.DatetimeIndex(date['column']).month
```

# Processing Errors with try-except

When you’re uploading data from multiple systems, be prepared for surprises:

- Incorrectly formatted data can cause issues when the code runs: a **crash**. You already have some experience with this. If the numbers in the dataset are strings for whatever reason, you'll need to use the `to_numeric()` method.
- Errors can occur toward the end of a file, with code not executing for rows with incorrect values. That means we lose our calculations for the previous, error-free rows.
- Data sometimes changes. For example, a company might start working with a new partner that sends faulty data for accounting, causing the code to crash.

Unfortunately, it’s impossible to predict all the problems that may occur. However, there’s a function called **try-except** that we use when we’re working with unpredictable data. You stick the source code in the **try** block, and if there’s a problem with it, the code in the **except** block is executed instead.

```python
try:
    # code that might have an error in it
except: 
    # what happens when the aforementioned error is discovered
```

# The merge() Method

Data is stored across multiple sheets in Excel tables. Before you can use all the data, you have to join the tables together.

We can combine multiple tables by using the `merge()` method.

Arguments:

- `right`: the name of the DataFrame or Series we’re joining with the source table.
- `on`: a field present in both tables that’s used to combine them.
- `how`: which key values will be used in the resulting table. It can have the value `left`, where the key values from the left table are included in the result, or `right`, where the key values from the right table are included in the result.

```python
data.merge(data2, on='merge_column', how='left')
data.merge(data2, on='merge_column', how='right')
```

# Pivot Tables

Pivot tables are your best friends when it comes to processing rearranged or concentrated data derived from huge tables, focused on particulr aspects.

In order to prepare pivot tables in pandas, we use the `pivot_table()` method.

Method arguments:

- `index`: the column or columns data is grouped by
- `columns`: the column with the values used to group the data
- `values`: the values we want to see in the pivot table
- `aggfunc`: the function applied to those values

```python
data_pivot = data.pivot_table(index=['column1', 'column2'], columns='source', 
															alues='column_pivot', aggfunc='function')
```