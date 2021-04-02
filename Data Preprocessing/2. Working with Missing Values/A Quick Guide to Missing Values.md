# A Quick Guide to Missing Values

### When to fill missing values... and when not to

Sometimes you'll see hard rules, like "If more than 20% of a variable is missing, delete the variable entirely." But we hesitate to give any hard rules because so much depends on the context of the problem. As a data analyst, part of your job is to take nuances into account when making decisions. With that said, here are some guidelines: 

1. **Never fill the main variable of interest, and never use the main variable of interest to fill missing values.** Often your final goal is to understand the relationships between a main variable and other variables. This is the objective, not a data preprocessing step.  
2. **Always keep track of (document) when, where, why, and how missing values were filled.** Always have a justifiable reason for any filling you do. If asked why, you must have an answer. 
3. **Filled values should not have a significant impact on your analysis.** If in doubt, run your analysis twice, once with the filled values and once with missing values removed. If the results are significantly different, the filled values are driving the change. You do not want this. This is an example of sensitivity analysis. 

Before we talk about how to replace missing categorical values, get into a power pose and repeat after me: "I will not allow filled values to drastically change the results of my analysis."

### Dealing with missing values

So, you've determined that a dataset has missing values. What do you do?

1. Report the issue and find out if there's a way to get the full data. If there isn't, proceed to step 2.

2. Determine how many missing values there are — call the `value_counts()` method and `print()` .

```jsx
print(file_name['column_name'].value_counts())
```

3. Determine how significant their absence is for the dataset. What proportion of the data do they represent? In most cases, if it's not much (say, 5-10%, depending on the situation), you can delete them.

4. Check how significant their absence is for their category or column — call the `isnull()` and `count()` methods and print.

```jsx
print(file_name[file_name['row_name'].isnull()].count())
```

5. Determine whether the missing values belong to categorical or quantitative variables.

6. If **categorical**:

- Determine whether or not the missing values exhibit a pattern — whether their appearance in the dataset is random or not. If you can't detect a correlation with other values in the rows where they appear (say, for respondents under 21, a question about alcohol is unanswered), then they're probably random. There are three types of missing values:
    - Missing completely at random (MCAR)
    - Missing at random (MAR)
    - Missing not at random (MNAR)

- Depending on the pattern, decide how to handle them:
    - If the values are MCAR or MAR, there's no pattern, so you can replace them with default values — an empty string, a particular word. Use the `loc[]` method and boolean indexing. The `fillna()` method may also work, but not in every case.
    - With MNAR values, there's a pattern. This is the most complex case, and we won't dive into its intricacies in this chapter.

7. If **quantitative:**

- Determine whether your data has significant outliers.
- If there aren't any significant outliers, сalculate the mean of your data —  apply the `mean()` method to the column or the entire dataset.
- If your data has significant outliers, calculate the median of your data — apply the `median()` method to the column or the entire dataset.
- Replace missing values with the mean or median using the `fillna()` method.