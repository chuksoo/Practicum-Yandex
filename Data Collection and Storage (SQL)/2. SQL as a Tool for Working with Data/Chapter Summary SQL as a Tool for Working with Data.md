# Chapter Summary: SQL as a Tool for Working with Data

## Databases and Tables

A **database** is a place where structured data is stored. **Entities** are groups of objects that share common characteristics. **Objects** are individual instances of entities. 

We are going to study relational databases, where *entities* are tables and table *rows* are their *objects*. 

To work with databases you need a **DBMS**, or database management system. This is a set of programs that allows you to create a database, fill it with new tables, and edit and display the contents of existing tables. In our course we will use **PostgreSQL,** one of the most popular DBMS. 

## Tables

A **table** is a set of rows and columns. Columns are called **fields**. They contain the object's features.  Each field has a unique name and a specific data type. Table rows are called **tuples** or **records**. Each row contains information about one particular object. A **cell** is a unit where a row and column intersect.

**Primary keys** are used to give each row a **unique** identifier. Some tables use several fields at once as their primary keys; in such cases, they're called **composite primary keys**.

## Your First SQL Statement

**SQL** is a computer language designed for managing data in relational databases. SQL syntax is different from Python's. Here are its basic characteristics: 

1) The beginning of a single-line comment is marked with two hyphens: `--`

```sql
-- a single-line comment in SQL 
```

2) A multi-line comment is put between `/*` and `*/`: 

```sql
/* a multi-line comment
has
several 
lines */
```

3) Commands are written in capital letters: 

```sql
SELECT, WHERE, FROM 
```

4) Every statement (or query) ends with a semicolon  `;` : 

```sql
SELECT 
	* 
FROM 
	table_name;
-- A statement that requests all the data from the table ends with ";"
SELECT 
	* 
FROM
	table_name
WHERE 
	column_name IN (1,7,9);
-- A statement that selects data by condition also ends with ";"
```

5) Line breaks after each keyword: 

```sql
SELECT
	column_1,
	column_2, 
	column_3, 
	column_4
FROM 
	table_name
WHERE 
	column_1 = value_1 AND
	column_2 = value_2 AND
	column_4 = value_3;
```

To select data from tables, you need to write a **statement**, or **query**. A **statement** is a request written according to SQL syntax. Your statement should specify what data to select and how to process it.

The **SELECT** operator takes the selection you need. SELECT statements look like this:

```sql
SELECT 
	column_1,
	column_2, 
	column_3 ...  
FROM 
	table_name;
--Select columns from the table
```

We have two keywords in our statement: **SELECT** and **FROM**. SELECT specifies the necessary columns from the database table. To select all columns from the table, add  `*` symbol to the `SELECT` operator. FROM specifies the table from which the data should be taken.

## Data Slices in SQL

The beginning of the condition used to select data is marked with the **WHERE** command. The condition is evaluated in each row of the table. In conditions, comparison operators are used:

```sql
SELECT 
	column_1, 
	column_2 --selecting column names
FROM 
	table_name --specifying the table
WHERE 
	condition; --defining the condition of row selection
```

The order of operators is strictly defined:

1)`SELECT` 

2)`FROM`

3)`WHERE`

Like Python, SQL uses the logical operators `AND`, `OR`, `NOT`. They let you make a selection with several conditions:

```sql
SELECT 
	* 
FROM 
	table_name
WHERE 
	condition_1 AND condition_2;
--Select rows where both conditions are true 
SELECT 
	* 
FROM 
	table_name
WHERE 
	condition_1 OR condition_2;
--Select rows where either or both conditions are true
SELECT 
	* 
FROM 
	table_name
WHERE 
	condition_1 AND NOT condition_2;
--Select rows where condition_1 is true and condition_2 is false
```

If you need to make a selection of rows for which a field's values fall within a certain range, use the **BETWEEN** statement. `BETWEEN` includes the start and end boundaries in the resulting selection:

```sql
SELECT 
	* 
FROM 
	table_name
WHERE 
	field_1 BETWEEN value_1 AND value_2;
-- Selecting rows where field_1 value is between value_1 and value_2 (inclusive)
```

If you need to make a selection of rows for which a field's values match those in a list, use the **IN** operator. Indicate the list of values after `IN`:

```sql
SELECT 
	* 
FROM 
	table_name
WHERE 
	column_name IN ('value_1','value_2','value_3');
```

If the values are numbers, they are separated from each other by commas: `IN (3,7,9)`. If they're strings, they're put in single quotes and, again, separated by commas: `IN ('value_1','value_2','value_3')`. Date and time are indicated as follows: `IN ('yyyy-mm-dd','yyyy-mm-dd')`

## Aggregate Functions

Like Python, SQL has specific functions for calculating the total number of rows, sums, averages, and minimum and maximum values. These are referred to as **aggregate functions**. They collect, or *aggregate*, all the objects within a group to calculate a single summary value.

Here's the syntax of a statement with an aggregate function:

```sql
SELECT 
	**AGGREGATE_FUNCTION**(field) AS here_you_are
--here_you_are - name of the column where the function's output will be stored
FROM
	table;
```

When you call an aggregate function, it gives the column an unwieldy name. To avoid this, use the **AS** command and type a new, simpler one. 

The **COUNT** function returns the number of rows in a table:

```sql
SELECT 
	COUNT(*) AS cnt
FROM
	table
```

The number of rows can be calculated in various ways depending on the task:

- **COUNT(*)** returns the total number of table rows
- **COUNT(column) ****returns the number of rows in a `column`
- **COUNT(DISTINCT column)** returns the number of *unique* rows in a `column`

The **SUM(column)** function returns the sum of the values in a `column`. It ignores missing values.

The **AVG (column)** returns the average value of ****`column` values*.*

The smallest and largest values can be found using the **MIN** and **MAX** functions.

## Converting Data Types

Some aggregate functions can only be used with number values. 

The data in a field might look like numbers but actually be stored as strings in the database. This happens often, most commonly because of mistakes in designing databases. 

We can use a **CAST** statement to convert the data type of values in a column:

```sql
CAST (*column_name* **AS** *data_type*)
```

`column_name` is the field whose data type is to be converted. `data_type` is the desired type. We can also write this:

```sql
*column_name* **::** *data_type*
```

### Numeric data types

**integer**: an integer type similar to *int* in Python. In PostgreSQL integers range from -2147483648 to 2147483647.

**real**: a floating point number, like *float* in Python. Number precision for the *real* type is up to 6 decimal points.

### String data types

**'Practicum'**: this is an example of a string-type value. In SQL statements, it goes in single quotes.

**varchar(n)**: a varying-length character string, where **n** is the maximum number of characters.

**text**: a string of any length. This type is just like Python's string type.

### Date and time

Dates and times go in single quotes.

**timestamp**: a date and time. Analogous to `datetime` **in **pandas*.* This format is most often used to store events that occur several times a day, such as website user logs.

**date**: a date

### Logical

**boolean** — a logical data type. It can have three values in PostgreSQL: **TRUE**, **FALSE**, and **NULL** (unknown).