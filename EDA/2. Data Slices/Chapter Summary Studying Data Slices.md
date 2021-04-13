# Chapter Summary: Studying Data Slices

# 

## Data Slices and Looking for Plane Tickets

When you're working on a task, you often need to use a carefully selected portion of data, or **data slice.**

One way to get a slice is to apply a filter. An option for that filter is a **Boolean array** with true/false values. `True` will mark the lines we want to include in our data slice (lines with a certain value, for instance), while `False` will indicate values that we don't want to include. The problem is that manually marking lines takes time. Fortunately, pandas has automatic filters. Here's an example:

```python
data['column'] == 'value'
```

That filter will serve as a DataFrame index:

```python
data[data['column'] == 'value']
```

In addition to the equals sign, the condition for creating a Boolean array can also use comparison symbols such as `!=`, `>`, `>=`, `<`, and `<=`. We can compare the values in the columns to each other, not just to numbers:

```python
data['column1'] > data['column2']
```

We can also use arithmetic operations in the condition:

```python
data['column1'] / 2 > data['column2'] + 0.5
```

To see whether there are particular values in the column, we can call the `isin()` method:

```python
data['column'].isin(('value1', 'value2', 'value3'))
```

Sometimes you need a selection that meets multiple conditions simultaneously; in those cases, logical operations come in handy. The conditions are placed in parentheses, while the operators themselves are symbols:

[Untitled](https://www.notion.so/e6a0aa02e6d24264b6b88d409f208c7c)

## Creating Data Slices with the query() Method

A simpler way to get slices is the `query()` method. We put the condition for the slice in the string given as an argument for the `query()` method, then applying it to the DataFrame. That gets us the slice we're looking for.

```python
data.query('column == value')
```

Conditions set with the `query()` parameter:

- Support various comparison operators, such as `!=`, `>`, `>=`, `<`, and `<=`
- Can check whether specific values are in the list using constructs like `Date_To in ("07.07.19", "09.07.2019")` or whether values are NOT in the list using constructs like `Date_To not in ("07.07.19", "09.07.2019")`
- Work with the logical operators AND, OR, and NOT the way we're used to, with no need to enclose the conditions in parentheses, since operations are always executed in the order of *not*, *and*, *or* when there are no parentheses.

We can pull values from external variables in the `query()` method as well:

```python
variable = 2
data.query('column > @variable')
```

## Working with Times and Dates

Remember the `to_datetime()` method from the course on preprocessing, which we used to turn strings into dates? The method's `format` argument follows the exact order we have in the `date_time` string:

- `%d`: day of the month (01 to 31)
- `%m`: month (01 to 12)
- `%Y`: four-digit year (for example, 1994)
- `%y`: two-digit year (for example, 94)
- `Z` or `T`: standard separator for date and time
- `%H`: hour in a 24-hour format
- `%I`: hour in a 12-hour format
- `%M`: for minutes (00 to 59)
- `%S`: for seconds (00 to 59)

Data experts typically use the **dt** (date-time) attribute to notify pandas explicitly that the operation will have to do with dates. `dt` indicates that the data type we’re going to be applying the methods to is datetime, so that pandas won't treat it as a string or number.

To round times, use the `dt.round()` method*.* It gets passed strings that indicate whether rounding should be to the day, hour, minute, or second:

- `D`: day
- `H`: hour
- `min` or `T`: minute
- `S`: second

```python
data['datetime_round'] = df['datetime'].dt.round('3H')
```

If you want to round up, use the `dt.ceil()` (ceiling) ****method***.*** To round down, use `dt.floor()`.

We can find the day of the week with the `dt.weekday()` ****method. 

## Graphs

`plot()` builds graphs using the values in the DataFrame columns. The indices are on the X axis, and the column values are on the Y axis.

```python
data.plot()
```

The `plot()` method also has `style` parameter that is responsible for how points look:

- `'o'`: instead of an unbroken line, each value will be marked as a point
- `'x'`: instead of an unbroken line, each point will be marked as an x
- `'o-'`: will show both lines and points

You can change the axes indices, assigning the values from the column we need to the corresponding axis.

```python
data.plot(x='column_x', y='column_y')
```

We can fix the borders using the parameters `xlim` **and **`ylim`*,* which you learned about when studying boxplots:

```python
data.plot(xlim=(x_min, x_max), ylim=(y_min, y_max))
```

To display gridlines, set the `grid` parameter to `True`:

```python
data.plot(grid=True)
```

We can manage the size of the graph with the `figsize` patareter. The width and height in inches are passed in parentheses:

```python
data.plot(figsize = (x_size, y_size))
```

## Grouping with pivot_table()

When there's a lot of data, points merge together, making it hard to draw conclusions. You can improve the visualization by grouping the data. The example below uses grouping to make the graph much more informative.

```python
(data
     .query('column_id == "value"')
     .pivot_table(index='column1', values='column2')
     .plot(grid=True, figsize=(12, 5))
)
```

Graphs featuring grouping help you find outliers that weren't previously visible. And sometimes these outliers seriously skew the mean. How do you ensure anomalies don’t drive up the mean? There are two potential solutions:

- Getting rid of the outliers
- Using the median instead of the mean. The median is resistant to outliers, if still imperfect — there might still be peaks.

## Saving the Results

As you're going about your work, you might find errors in the data. In that case, you need to formulate the problem in a way that allows you to simplify your search for potential issues in the algorithm for exporting data. To let people know about errors, you need to send a **bug report** making clear what the error was and explaining how to replicate it.