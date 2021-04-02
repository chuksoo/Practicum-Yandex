# Chapter Summary: Working with Missing Values

# Metrics for Evaluating Traffic Sources

### Theory

There are many kinds of **traffic sources**:

- Search results (organic traffic)
- Contextual ads
- Email newsletters
- Social media
- Click-throughs from other websites

Performance metrics help us evaluate and compare traffic sources to figure out which of them is best. Knowing how traffic sources perform helps you adjust your marketing strategy as you go.

There are two methods for calculating **website conversion**: calculating the **percentage of visitors** who perform **target actions** on a website and calculating the **percentage of target actions** among total actions.

A **visit** is the sequence of actions a user performs starting when they get to a website and ending when they’ve been inactive for 30 minutes.

Another important metric for evaluating a traffic source is the **repeat purchase rate**: the ratio of users who make at least two purchases to the number of users who make at least one purchase.

### Practice

In pandas, you can perform **arithmetic operations** on columns: addition, subtraction, multiplication, and division. For example:

```
data['column1'] = data['column12'] + data['column3']
```

# User IDs and Cookies

### Theory

A **counter** collects data about user behavior on webpages and sends it to a **web analytics system**, such as Google Analytics. The information includes things like which traffic source users come from, which pages they view, and which purchases they make. Counters assign a **unique number** to each user that differentiates them from other users. This is called a **user ID**.

Data from these counters is called **raw data**. Web analytics systems convert raw data into reports on audience, traffic, and sources. **Reports** allow you to combine different metrics and visualize results.

**Cookies** are used to identify a user who returns to a website. Cookies are text files left in your device’s memory after your first visit to a website and sent to the server when you visit again.

But if a user visits a website from different browsers, the same user is assigned different user IDs, because each browser has its own cookies. That’s why analysts collect additional information, like email addresses. The user ID and email address are encrypted to protect personal data.

Text files that contain information about website visits are called **logs**.

When new information is added to data that has already been collected, this is called **data enrichment**. A dataset, however, may contain missing information*.* Sometimes these missing values can be ignored, but at other times they need to be processed and filled in before analysis can take place.

### Practice

The `unique()`method is used to search for unique values in a column: `data['column'].unique()`.

To delete rows with missing values, call the `dropna()` method. To renumber, call the `reset_index()` method with the argument `drop=True`.

# NaN and None

### Theory

`NaN` and `None` indicate that there is no value in a cell. `NaN` means "not a number" and is float type, so you can perform mathematical operations on it. `None` is NoneType, meaning you can’t perform mathematical operations with it. `NaN` values can lead to incorrect results when grouping data. Don’t just delete rows with these values: missing values can often be restored.

### Practice

In pandas, the `value_counts()` method returns unique values and their counts.

The `isnull()` method returns a Boolean list, in which "true" means that a value is missing in the column.

To substitute a value for a missing one, use the `fillna()` method with the `value` argument.

# Categorical and Quantitative Variables

There are two types of variables: **categorical** and **quantitative**. Categorical variables take their values from a limited set, while quantitative variables take numeric values from within a limited range.

Variables can also be **logical (Boolean)**, meaning they indicate whether a statement is true or false. If a statement is true, the variable takes the value 1. If a statement is false, it is 0.

# Working with Missing Values: Categorical Variables. Dictionaries

### Theory

Before processing missing values, you need to determine whether there is a pattern; that is, whether their appearance in the dataset is random.

There are three types of missing values:

- **Missing completely at random (MCAR)** — the likelihood that a value is missing doesn’t depend on other values.
- **Missing at random (MAR)** — the likelihood that a value is missing can explained with reference to other values in the data.
- **Missing not at random (MNAR)** — neither MCAR nor MAR. The value is missing for a reason, though the reason might not be obvious.

### Practice

There are several ways to replace missing categorical values. For example, you can replace them with default values. This option works well for filling in randomly missing values. That’s what the pandas method `fillna()` is for.

That doesn't always work all empty values, though; for example, it can’t be used for missing `None` values. `fillna()` only recognizes `NaN` values in a table. To replace `None` values, call the `loc` method. Boolean indexing allows you to select all rows containing `None` in the desired column and replace them with a new value.

The `agg()` method is used to apply functions to particular columns. The column name and the functions themselves are recorded in a data structure called a **dictionary**. Dictionaries are comprised of **keys** and **values**. The key is the name of the column the functions must be used on, while the value is the list of function names.

```
{'column':['function1','function2']}
```

When you use the `agg()` method, column names become binary. To refer to the result of using `['function1']` on `['column']`, simply write them one after the other:

```
data['column']['function1']
```

# Working with Missing Values: Quantitative Variables

### Theory

Missing values in quantitative variables are filled in with **representative values**: values that characterize the ****dataset being analyzed. The **mean** or the **median** can be taken as the characteristic value for a dataset.

The **mean** is the sum of all values divided by the number of values.

The **median** is the midpoint in a dataset, meaning exactly half the elements fall above it and the other half fall below it. When there is an even number of values, the median is calculated by finding the average of the two middlemost values.

### Practice

To get the mean, use the `mean()` method. It can be applied to an entire table, a column, or grouped data.

The `median()` method can be applied to a table, a column, or grouped data.