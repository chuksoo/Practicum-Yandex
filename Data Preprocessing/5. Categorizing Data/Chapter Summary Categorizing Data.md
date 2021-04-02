# Chapter Summary: Categorizing Data

# Getting to Know Data

Both implicit conversions (from a derived data type to the parent data type: for instance, int to float, or 5 → 5.0) and explicit conversions (the opposite) are important. It’s essential that the data be presented in a convenient and readable format.

One part of this process is naming columns. This is what the `set_axis()` method is for.

# Classifying by Type

Categories in a dataset might be stored as strings of varying lengths.

What are the implications of storing them like this?

- The table isn't easy to process visually.
- File size and data processing time are greater than they need to be.
- To filter data by ticket type, we need to input the entire name (without any typos!).
- Creating new categories and changing old ones can take a lot of time.

To store information about categories in the best way possible, use a dictionary that maps each category name to a number. This number will be used in place of the category name in the table.

# Classifying by Age Group

There is often just one entry with a specific index value. It’s impossible to work with bits of data like this and reach statistical conclusions. This is why this data must be **categorized** — that is, combined into categories.

One way to categorize the data is to filter it by age group. For example: 18 or under, 19-65, and over 65.

Classification rules like these can be conveniently represented in Python as functions that take parameters and return a category value.

The `group` function that we wrote and the `apply()` method can be used to return a column with a group based on a column with a different index.

```
data['column_group'] = data['column'].apply(group)
```

# Single-Row Functions

When the value from a single column is insufficient for categorization, the function can pass the contents of the whole row as a Series. A function that is given a whole row can also return a value from a specific column.

When processing rows instead of single values, the `apply()` method differs in two ways:

1. The `apply()` method is called for the `data` DataFrame, not just for the `['age']` column.
2. By default, pandas passes columns to the `group()` function. To pass rows into the function, we’ll need to use the `apply()` method with the parameter `axis = 1`.