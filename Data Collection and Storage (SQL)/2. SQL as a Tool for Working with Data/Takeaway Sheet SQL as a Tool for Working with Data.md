# Takeaway Sheet: SQL as a Tool for Working with Data

## Practice

```sql
-- a single-line comment in SQL
/* a multi-line
comment 
*/
```

```sql
-- selecting specific table columns
SELECT 
	column_1,
	column_2, 
	column_3 ...  
FROM 
	table_name;

-- selecting all table columns

SELECT 
	* 
FROM 
	table_name;
```

```sql
-- selecting table data with conditions

SELECT 
	column_1, 
	column_2 --selecting column names
FROM 
	table_name --specifying the table
WHERE 
	condition; --defining the condition for selecting rows
```

```sql
/*
Selecting rows 
where the field_1 value
is between value_1 and value_2 (inclusive)
*/

SELECT 
	* 
FROM 
	table_name
WHERE 
	field_1 BETWEEN value_1 AND value_2;

```

```sql
-- Selection of rows based on field values in a list
SELECT 
	* 
FROM 
	table_name
WHERE 
	column_name IN ('value_1','value_2','value_3');
```

```sql
-- Calculating the number of rows in the selection
SELECT 
	COUNT(*) AS cnt,
	COUNT(column) AS cnt_column, -- returns the number of rows in the column
	COUNT(DISTINCT column) AS cnt_distinct_column, 
	/* returns the number of unique values
	in the column */
	SUM(column) AS sum_column, -- sum of column values
	AVG(column) AS sum_column, -- average column value
	MIN(column) AS sum_column, -- minimum column value
	MAX(column) AS sum_column -- maximum column value
FROM
	table;
```

```sql
-- converting the column to another data type

CAST (*column_name* **AS** *data_type*) 
*column_name* **::** *data_type*
```

## Theory

A **database** is a place where structured data is stored.

**Entities** are groups of objects that share common characteristics. 

**Objects** are individual instances of entities. 

**Relational databases** are databases where tables are *entities* and table *rows* are their *objects*. 

A **DBMS** (database management system) is a set of programs that makes it possible to create a database, fill it with new tables, display the contents, and edit existing tables.

A **table** is set of rows and columns. 

A **field** is a table column containing the object's features. It has a unique name and a specific data type. 

A **tuple** or **record** is a table row containing information on one particular object. 

A **cell** is a unit where a row and column intersect.

A **primary key** is a field or a group of fields used to identify a tuple. All primary key values are **unique**. 

**SQL** is a computer language designed for managing data in relational databases. 

A **statement** or **query** is a request written according to SQL syntax. Your statement should specify what data to select and how to process it.