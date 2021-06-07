# Takeaway Sheet: Relationships Between Tables

## Practice

```sql
-- Selecting table rows with empty values

SELECT 
	* 
FROM 
	table_name
WHERE 
	column_name IS NULL;
```

```sql
-- Excluding rows with empty values from the selection

SELECT 
	* 
FROM 
	table_name
WHERE 
	column_name IS NOT NULL;
```

```sql
-- Actions determined by conditions

CASE
    WHEN condition_1 THEN result_1
    WHEN condition_2 THEN result_2
    WHEN condition_3 THEN result_3
    ELSE result_4
END;
```

```sql
-- A search condition with a regular expression

column_name LIKE 'regular expression'
```

```sql
-- Inner join

SELECT --listing only the necessary fields
	TABLE_1.field_1 AS field_1,
	TABLE_1.field_2 AS field_2,
	...
	TABLE_2.field_n AS field_n
FROM
	TABLE_1
INNER JOIN TABLE_2 ON TABLE_2.field_1 = TABLE_1.field_2;
```

```sql
-- Left outer join

SELECT 
  TABLE_1.field_1 AS field_1,
	TABLE_1.field_2 AS field_2,
	...
	TABLE_2.field_n AS field_n
FROM
	TABLE_1
LEFT JOIN TABLE_2 ON TABLE_2.field = TABLE_1.field;
```

```sql
-- Right outer join

SELECT 
	TABLE_1.field_1 AS field_1,
	TABLE_1.field_2 AS field_2,
	...
	TABLE_2.field_n AS field_n
FROM
	TABLE_1
RIGHT JOIN TABLE_2 ON TABLE_1.field = TABLE_2.field;
```

```sql
-- Joining several tables

SELECT --list only necessary fields
	TABLE_1.field_1 AS field_1,
	TABLE_1.field_2 AS field_2,
	...
	TABLE_3.field_n AS field_n
FROM
	TABLE_1
INNER JOIN TABLE_2 ON TABLE_2.field = TABLE_1.field
INNER JOIN TABLE_3 ON TABLE_3.field = TABLE_1.field
```

```sql
-- Joining queries

SELECT 
	column_name_1  
FROM 
	table_1
UNION --( or UNION ALL)
SELECT 
	column_name_1  
FROM 
	table_2
```

## Theory

A **foreign key** is a table column that contains field values from another table.

In a **one-to-one** relationship, a row in one table is connected with one and only one row in another table. 

In a **one-to-many** relationship, each of the rows in one table matches several (or many) rows in another table. ****

In a **many-to-many** relationship, several rows from one table match several rows in another table. 

**ER diagrams** are special diagrams that illustrate the structure of a database, including tables and the relationships between them.