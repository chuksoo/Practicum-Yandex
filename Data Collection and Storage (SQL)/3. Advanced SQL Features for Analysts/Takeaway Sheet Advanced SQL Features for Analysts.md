# Takeaway Sheet: Advanced SQL Features for Analysts

```sql
-- Dividing data into groups according to field values

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

```sql
-- Sorting data

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
ORDER BY -- when necessary, list only those fields
--by which the data in the table is to be sorted
	field_1 DESC, -- sorting data in descending order  
	field_2 ASC, -- sorting data in ascending order
	..., 
	field_n, -- sorting data in ascending order
	here_you_are
LIMIT -- if needed
	n -- n: the maximum number of rows to be returned
```

```sql
-- Selection by condition with aggregate functions
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
ORDER BY -- when necessary, list only those fields
--by which the data in the table is to be sorted
	field_1, 
	field_2, 
	..., 
	field_n,
	here_you_are
LIMIT -- if needed
	n

```

```sql
-- Retrieving date fragments

SELECT
  EXTRACT(date_fragment FROM column) AS new_column_with_date 
FROM 
	Table_with_all_dates
```

```sql
-- Truncating date to a fragment

SELECT
  DATE_TRUNC('date_fragment_to_be_truncated_to', column) AS new_column_with_date
FROM 
	Table_with_all_dates
```

```sql
-- Subqueries in FROM block

SELECT 
SUBQUERY_1.column_name, 
SUBQUERY_1.column_name_2
FROM -- to make the code readable, start subqueries in new lines
	-- indent subqueries 
	(SELECT 
		column_name,
		column_name_2 
  FROM 
		table_name
  WHERE 
		column_name = value) AS SUBQUERY_1; 
-- remember to name your subquery in the FROM block
```

```sql
-- Subqueries in the WHERE block

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
			column_1  = value)

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
				column_1 = value_1 OR column_1 = value_2)
```