# Chapter Summary: Advanced SQL Features for Analysts

## Grouping Data

When data is to be divided into groups by field values, the **GROUP BY** command is used:

```sql
 SELECT 
	field_1, 
	field_2, 
	..., 
	field_n, 
	AGGREGATE_FUNCTION(field) AS here_you_are
FROM
	table_name
WHERE -- if needed
	condition 
GROUP BY 
	field_1, 
	field_2, 
	..., 
	field_n
```

Once you know which fields you'll be grouping by, make sure all those fields are listed in both the SELECT block and the GROUP BY block. The aggregate function itself shouldn't be included in the GROUP BY block; otherwise, the query won't comply. SQL's GROUP BY operates much like the `groupby()` method in pandas. 

GROUP BY can be used with any aggregate function: COUNT, AVG, SUM, MAX, MIN. You can call several functions at a time.

## Sorting Data

Analysis results are usually presented in a certain order. To sort data by a field, you use the **ORDER BY** command. 

```sql
SELECT 
	field_1, 
	field_2,
	..., 
	field_n, 
	AGGREGATE_FUNCTION(field) AS here_you_are
FROM
	table_name
WHERE -- if needed
	condition
GROUP BY  
	field_1, 
	field_2, 
	..., 
	field_n,
ORDER BY -- if needed. List only those fields
--by which the table data is to sorted
	field_1, 
	field_2, 
	..., 
	field_n, 
	here_you_are;
```

Unlike GROUP BY, with ORDER BY, only those fields by which we want to sort the data should be listed in the the command block. 

Two modifiers can be used with the ORDER BY command to sort the data in columns:

- **ASC** (the default) sorts data in ascending order.
- **DESC** sorts data in descending order.

The ORDER BY modifiers are placed right after the field by which the data is sorted:

```sql
ORDER BY 
	field_name DESC
-- sorting data in descending order 

ORDER BY 
	field_name ASC; 
-- sorting data in ascending order
```

The **LIMIT** command sets a limit to the number of rows in the result. It always comes at the end of a statement, followed by the number of rows at which the limit is to be set (*n*):

```sql
SELECT 
	field_1, 
	field_2, 
	..., 
	field_n, 
	AGGREGATE_FUNCTION(field) AS here_you_are
FROM
	table_name
WHERE -- if needed
	condition
GROUP BY  
	field_1, 
	field_2, 
	..., 
	field_n,
ORDER BY -- if needed. List only those fields
--by which the table data is to sorted
	field_1, 
	field_2, 
	..., 
	field_n, 
	here_you_are
LIMIT -- if needed
	n;
-- n: the maximum number of rows to be returned
```

## Processing Data within a Grouping

The **WHERE** construction is used to sort data by rows. Its parameters are, in fact, table rows. When we need to sort data by aggregate function results, we use the **HAVING** construction, which has a lot in common with **WHERE**:

```sql
 SELECT 
	field_1, 
	field_2, 
	..., 
	field_n, 
	AGGREGATE_FUNCTION(field) AS here_you_are
FROM
	TABLE
WHERE -- if needed
	condition
GROUP BY 
	field_1, 
	field_2, 
	..., 
	field_n
HAVING
	AGGREGATE_FUNCTION(field_for_grouping) > n
ORDER BY -- if needed. List only those fields
--by which the data is to be sorted
	field_1, 
	field_2, 
	..., 
	field_n,
	here_you_are
LIMIT -- if needed
	n;
	
```

The resulting selection will include only those rows for which the aggregate function produces results that meet the condition indicated in the HAVING and WHERE blocks. 

HAVING and WHERE have a lot in common. So why can't we pass all of our conditions to one of them? The thing is that the WHERE command is compiled before grouping and arithmetic operations are carried out. That's why it's impossible to set sorting parameters for the results of an aggregate function with WHERE. Hence the need for HAVING. 

Pay special attention to the order in which the commands are introduced:

1) GROUP BY

2) HAVING

3) ORDER BY

This order is **mandatory**. Otherwise, the code won't work.

## Operators and Functions for Working with Dates

We have two major functions for working with date and time values: **EXTRACT** and **DATE_TRUNC***.* Both functions are called in the SELECT block. 

Here's what the EXTRACT function looks like: 

```sql
SELECT
  EXTRACT(date_fragment FROM column_name) AS new_column_with_date 
FROM 
	Table_with_all_dates;
```

EXTRACT, unsurprisingly, extracts the information you need from the timestamp. You can retrieve:

- `century`
- `day`
- `doy` — day of the year, from 1 to 365/366
- `isodow` (day of the week under ISO 8601, the international date and time format); Monday is 1, Sunday is 7
- `hour`
- `milliseconds`
- `minute`
- `second`
- `month`
- `quarter`
- `week` — week of the year
- `year`

**DATE_TRUNC** truncates **the date when you only need a certain level of precision. (For example, if you need to know what day an order was placed but the hour doesn't matter, you can use DATE_TRUNC with the argument "day.") Unlike with EXTRACT, the resulting truncated date is given as a string. The column from which the full date is to be taken comes after a comma:

```sql
SELECT
  DATE_TRUNC('date_fragment_to_be_truncated_to', column_name) AS new_column_with_date 
FROM 
	Table_with_all_dates;
```

You can use the following arguments with the DATE_TRUNC function:

`'microseconds'`
`'milliseconds'`
`'second'`
`'minute'`
`'hour'`
`'day'`
`'week'`
`'month'`
`'quarter'`
`'year'`
`'decade'`
`'century'`

## Subqueries

**A subquery,** or **inner query,** is a query inside a query. It retrieves information that will later be used in the **outer query**.  

Subqueries can be used at various locations within a query. If a subquery is inside the FROM block, SELECT will select data from the table that gets generated by the subquery. The name of the table is indicated within the inner query, and the outer query refers to the table's columns. Subqueries are always put in parentheses:

```sql
SELECT 
SUBQUERY_1.column_name, 
SUBQUERY_1.column_name_2
FROM -- to make the code readable, put subqueries in new lines
	-- indent subqueries
	(SELECT 
		column_name,
		column_name_2
  FROM 
		table_name
  WHERE 
		column_name = value) AS SUBQUERY_1; 
-- remember to name your subquery in FROM block
```

You may need subqueries at various places within your query. Let's put one in the WHERE block. The main query will compare the results of the subquery with values from the table in the outer FROM block. When there's a match, the data will be selected:

```sql
SELECT 
	column_name, 
	column_name_1
FROM 
	table_name
WHERE 
	column_name = 
		(SELECT 
			column_1
		FROM 
			table_name_2 
		WHERE
			column_1  = value);
```

Now let's add the IN construction to our sample and collect data from several columns:

```sql
SELECT 
	column_name, 
	column_name_1
FROM 
	table_name
WHERE 
	column_name IN  
			(SELECT 
				column_1
			FROM 
				table_name_2  
			WHERE 
				column_1 = value_1 OR column_1 = value_2);
```

## Window Functions

In SQL, a window is a sequence of rows on which the calculations are made. It can be either the entire table or, for instance, the six rows above the current one. Working with such windows is different from working with regular requests. 

```sql
SELECT
	author_id,
	name,
	price/SUM(price) AS ratio OVER ()
FROM 
	books_price;
```

The function preceding the OVER keyword will be executed on the data inside the window. If we don't indicate any parameters (as here), the entire result of the query will be used. 

If we want to group the data, we use PARTITION BY:

```sql
SELECT
	author_id,
	name,
	price/SUM(price) AS ratio OVER (PARTITION BY 
																		author_id)
FROM 
	books_price;
```

## A Closer Look at Window Functions

More important keywords when using window functions:

ORDER BY — lets us define the sorting order of the rows through which the window will run

ROWS — where we indicate the window frames above which an aggregate function is to be calculated

```sql
SELECT
	author_id,
	name,
	SUM(price) OVER (ORDER BY 
											author_id 
									ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
FROM 
	books_price;
```

Indicating frames:

- UNBOUNDED PRECEDING — all rows that are above the current one
- N PRECEDING — the *n* rows above the current one
- CURRENT ROW — the current row
- N FOLLOWING —  the *n* rows below the current one
- UNBOUNDED FOLLOWING — all rows below the current one