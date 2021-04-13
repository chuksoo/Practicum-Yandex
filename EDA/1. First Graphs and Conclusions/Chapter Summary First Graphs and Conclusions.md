# Chapter Summary: First Graphs and Conclusions

## The Task at Hand

Data in CSV files might be separated by commas, semicolons, tab characters, or other symbols. Also watch out for decimals written using commas.

The parameters of the `read_csv()` function indicate which symbol we use to separate decimals and columns. We use the `sep` parameter to indicate which symbol marks the end of one column and the beginning of the next. The decimal parameter indicates the symbol used for decimals.

```python
file = pd.read_csv('file.csv',  sep=';' , decimal=',')
```

## Calculating the Mean with Pivot Tables

 In Data Preprocessing, you used `pivot_table()`, a method for building pivot tables. You set the value of `aggfunc` to `sum`, totaling all the elements in the column. If you don't enter an `aggfunc` parameter, the `pivot_table()` **method will by default calculate the arithmetic mean of the values listed in the `values` parameter.

## Basic Data Verification

Keep in mind that all kinds of problems can pop up when you're working with data:

- Incomplete or inaccurate data
- Mistakes in the recording of time values
- Seconds getting mixed up with minutes
- Important facts being overlooked.

As an analyst, you're directly responsible for the quality of data and the conclusions you draw. When you get new data, you need to get a sense of how reliable it is. In this case, you can explore some basic questions. Then you and your coworkers can see whether the results are reasonable.

A basic check like this might uncover a problem in the data. Of course, it might also tell you that everything's okay, at least for now.

## Bar Charts

We sometimes use bar charts to plot quantitative data. Each bar on such a plot corresponds to a value: the higher the value, the higher the bar. Differences between values are clearly visible. 

In pandas, charts are plotted with the `plot()` method. Various graph types are passed in the `kind` parameter. To plot a bar chart, indicate `'bar'`. 

## Histograms

A histogram is a graph that shows how frequently different values appear in a dataset. It groups numeric values by ranges; that is, it finds the frequency with which values within each interval occur. Histograms are somewhat similar to bar charts, but for the former, the grouping is made for defined ranges of values. You can modify the interval width to change the appearance of your histogram.
In pandas, histograms are plotted with the `hist()` method. It can be applied to a list or a column from a DataFrame, in which case the column is passed as an argument. The `hist()` method finds the highest and lowest values in a set and breaks the resulting range into 10 equally spaced intervals, or **bins**. Then the method finds the number of values inside each bin and renders it on the graph. 

Another way to plot a histogram is to call the `plot()` method with the `kind='hist'` parameter. This allows you to include more parameters. The `bins` parameter determines how many sections a range of data will be divided into, with the default being `bins=10`. You can also manually set the scale using the `range` ****parameter**:** `range=(min_value, max_value)`.

```python
import pandas as pd
import matplotlib.pyplot as plt # importing the library using the standard name plt

pd.Series(...).hist(bins=n_bins, range=(min_value, max_value) 

plt.show() # giving the command to display the histogram
```

## Boxplots

When describing a distribution, analysts calculate the mean or median. You learned about the `mean()` and `median()` methods in the course on Data Preprocessing. Besides the mean and median, it's also important to know the **dispersion**: which values and how many of them are far from the average.

The easiest way to get a sense of the dispersion is to look at the minimum and maximum values, but if there are outliers, this won't tell you much. It's much better to look at the **interquartile range.**

**Quartiles** (from the Latin *quartus*, or quarter) break up ordered sets of data into four parts. The first quartile, or Q1, marks the value greater than 25% of the dataset's elements and less than 75%. The median is Q2; here the elements are split in two. Q3 is greater than 75% of the elements and less than 25%*.* The interquartile range is everything that falls between Q1 and Q3.

We can find the median and quartiles in Python using a special graph called a **boxplot**, or box-and-whisker plot.

The box stretches from the first to the third quartile, and the median is drawn inside of it.

The whiskers extend a maximum of 1.5 interquartile ranges (IQR) to the left and right of the box. (Each whisker goes to the largest value that falls within this range.) Typical values fall within the whiskers, while outliers are displayed as points outside of them.

![Chapter%20Summary%20First%20Graphs%20and%20Conclusions%20fca77daf78264004bfc6067c4cf9f8d4/___2_7_11_copy.jpg](Chapter%20Summary%20First%20Graphs%20and%20Conclusions%20fca77daf78264004bfc6067c4cf9f8d4/___2_7_11_copy.jpg)

Python has a `boxplot()` ****method for creating these plots:

```python
import matplotlib.pyplot as plt
data.boxplot()
plt.show()
```

We can import the **Matplotlib** library and its pyplot module in order to do more advanced work with histograms and graphs in general. For instance, we can adjust the axes names by specifying the range of the X and Y axes. To do so, we need to use Matplotlib methods: `ylim(y_min, y_max)` for the vertical axis, `xlim(x_min, x_max)` for the horizontal axis.

```
import matplotlib.pyplot as plt 
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
```

## Describing Data

Histograms and box plots allow us to describe data sets visually. In addition to the `quantile()` method, `describe()` can be used to get quartile and median values. It's convenient in that it gives **numerical descriptions of data**. A numerical description is more than simply an accessory to graphs; it can stand on its own as an initial tool for analysis. It tells you about all of a table's columns at one go. 

The **standard deviation** describes the way values are dispersed, letting us know how far they tend to be from the mean. The standard deviation often helps us understand distributions and figure out how uniform datasets are. 

```
data['column'].describe()
```