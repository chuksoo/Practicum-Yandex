# Takeaway Sheet: Working with Several Data Sources

```python
# data is a DataFrame

our_list = [1, 2, 3, 4]
data.query('column in @our_list') # Checks if values from the column are in the list

our_dict = {0: 1, 4: 82, 71: 1414}
data.query('column in @our_dict') # Checks if values from the column 
																	 # are among the dict keys

our_series = pd.Series([81, 12, 64])
data.query('column in @our_series') # Checks if values from the column
                                    # are among the Series values

our_series = pd.Series([81, 12, 64])
data.query('column in @our_series.index') # Checks if values from the column
                                          # are among the Series indices

our_dataframe = pd.DataFrame({
'column1': [0, 1, 10, 11, 12],
'column2': [5, 4, 3, 2, 1],
})
data.query('column in @our_dataframe.index') # Checks if values from the column
                                             # are among the DataFrame indices

our_dataframe = pd.DataFrame({
'column1': [0, 1, 10, 11, 12],
'column2': [5, 4, 3, 2, 1],
})
data.query('column in @our_dataframe.column2') # Checks if values from the column
                                               # are among the column2 values

# Building histograms with additional parameters
# histtype - type of diagram
# linewidth - graph line width in pixels
# alpha - density of fill, from 0 to 1 (for adjusting transparency)
# label - line name
# ax - axes
# legend - whether to display a legend on a graph

data.plot(kind='hist', y='column', histtype='step', range=(y_min, y_max), bins=n_bins, 
          linewidth=our_linewidth, alpha=our_alpha, label='label', ax=our_ax, 
                    grid=True, legend=True)

# Returning the first and last values from a group

df.pivot_table(index='index_column', values='values_column', aggfunc='first')
df.pivot_table(index='index_column', values='values_column', aggfunc='last')
```

##