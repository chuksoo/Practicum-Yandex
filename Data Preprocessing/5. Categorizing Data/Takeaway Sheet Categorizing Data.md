# Takeaway Sheet: Categorizing Data

```python
# Using apply() for the values in a column
# To apply the method to rows, use the parameter axis=1

data['column'].apply(method)
data['column'].apply(method, axis=1)
```

```python
# function for a row

def function(row):
		info1 = row['column1']
		info2 = row['column2']

		# Then the values are processed
```

## Ways to tidy up data

- **Creating a dictionary for categories.** In the dictionary, every category name is matched with a number, which is then used in the main dataset.
- **Categorization**. Data is joined into categories. Categorization can be carried out using data from:
    - One column. In this case, the categorization method takes only one value (the value of the relevant column).
    - Several columns. In this case, the method takes an entire row from the DataFrame.