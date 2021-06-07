# Chapter Summary: Relationships Between Tables

## Types of Relationships Between Tables

When a column contains the values of the field of another table, it's called a **foreign key**. It's responsible for the relationship between the tables.

There are three types of relationships:

- one-to-one
- one-to-many
- many-to-many

In a **one-to-one** relationship, each row in a table is connected with one and only one row in the other table. It's as if a table has been split in half. This is a rare type of relationship and is predominantly used for security reasons. 

In a **one-to-many** relationship, each row of a table matches multiple rows in another table.

In a **many-to-many** relationship, several rows from one table match several rows from another table. This type of relationship produces an **association table,** which combines the primary keys of both tables. 

## ER Diagrams

The structure of databases can be shown with **ER** (**entity-relationship**) **diagrams**. They show tables and the relationships between them. 

Tables are shown as rectangles (boxes) with two parts. The table name goes in the upper part.

![Chapter%20Summary%20Relationships%20Between%20Tables%20df473363342c4a8d819d8a3de5ff8f8d/Untitled.png](Chapter%20Summary%20Relationships%20Between%20Tables%20df473363342c4a8d819d8a3de5ff8f8d/Untitled.png)

In the lower part we see lists of table fields with an indication of which keys they are related to: primary or foreign. The keys are usually marked **PK** (primary) or **FK** (foreign), but they can be also marked with a key icon, a #, or another symbol.

ER diagrams also show relationships. The end of the line connecting two tables indicates whether one or several values from one table match values from the other. 

Here's a one-to-many relationship:

![Chapter%20Summary%20Relationships%20Between%20Tables%20df473363342c4a8d819d8a3de5ff8f8d/Untitled%201.png](Chapter%20Summary%20Relationships%20Between%20Tables%20df473363342c4a8d819d8a3de5ff8f8d/Untitled%201.png)

And here's a one-to-one relationship: 

![Chapter%20Summary%20Relationships%20Between%20Tables%20df473363342c4a8d819d8a3de5ff8f8d/Untitled%202.png](Chapter%20Summary%20Relationships%20Between%20Tables%20df473363342c4a8d819d8a3de5ff8f8d/Untitled%202.png)

## Database User Types

Many employees use a company's master database simultaneously. Each of them needs only certain data to do their job. Things must therefore be arranged such that users don't interfere in the others' work. Hence the need for **database administrators**. They manage user access, monitor the load on the system, take care of security, and make backups. 

Databases are like living creatures, growing constantly. **Database architects** and **developers** make sure they grow healthily. These specialists' decisions determine the database's structure, integrity, and fullness, as well as its scaling possibilities (adding new tables, relationships, and functions). Architects and developers are responsible for the database's performance.

**Data engineers** are responsible for adding data to the database. They are also called **ETL specialists**, since they extract, transform, and upload data to databases. 

**Analysts**, in this scheme, are typical users. They write queries to databases and retrieve the necessary data, which they then analyze and use to test hypotheses. Analysts work more closely than the others with the data it, and it's he who is the first to encounter missing fields or tables. Make it your habit to immediately communicate such "discoveries" to developers if you want such errors to be solved promptly. 

## Searching for Empty Values

In SQL, empty cells are said to be **NULL**. The **IS NULL** operator searches for them:

```sql
SELECT 
	* 
FROM 
	table_name
WHERE 
	column_name IS NULL;
```

Note that IS matters! The following won't work:

```sql
SELECT
 * 
FROM 
	table_name
WHERE 
	column_name = NULL; -- this code won't comply!
```

To exclude rows with NULL values from the selection, we use the NOT operator:

```sql
SELECT 
	* 
FROM 
	table_name
WHERE 
	column_name IS NOT NULL;
```

The **CASE** construction is used to carry out actions when certain conditions are met. It's much like `if-elif-else` in Python:

```sql
CASE
    WHEN condition_1 THEN result_1
    WHEN condition_2 THEN result_2
    WHEN condition_3 THEN result_3
    ELSE result_4
END;
```

A condition follows the **WHEN** operator. If a table row matches this condition, the code returns the result indicated in **THEN**. Otherwise, the same row is tested with the next condition. If the row fails to match any of the conditions stated in WHEN, the code returns the value indicated after **ELSE**. The CASE construction is then closed with the **END** operator. 

## Searching for Data in a Table

The **LIKE** operator searches a table for values that follow a given pattern. You can search not only for a word, but also for a fragment of it.

Here's the syntax of LIKE statements:

```sql
column_name LIKE 'regular expression'
```

Indicate the necessary column before LIKE and follow it with a regular expression.  

Regular expressions in SQL are a bit different from those in Python. For example, the `_` symbol replaces one substitute value (1 character) in a regular expression. The `%` symbol replaces any amount of characters. A range or sequence of characters which a string must contain are written within square brackets `[]`. If the characters are to be excluded, the `[^]` construction is used. 

Range or sequence of characters

If we need to find a symbol from regular expression as a substring, we use the **ESCAPE** operator. It's passed a symbol such as an exclamation point. In the regular expression, the exclamation point means the symbol following it is not part of the expression, but rather the substring to be searched for. Here's a fragment of code that will find all substrings ending with the `%`  symbol (say, "100%") in a table:

```sql
column_name LIKE '%!%' ESCAPE '!'
--finds all substrings ending with %
```

## JOIN. INNER JOIN.

It's rare for all the data to be stored in one table. Analysts usually need to merge tables; hence the **JOIN** operator. 

There are two ways to join tables: the **INNER** and **OUTER** join**.**  

The INNER join returns only those rows that have matching values from table to table (the tables' intersection). 

![Chapter%20Summary%20Relationships%20Between%20Tables%20df473363342c4a8d819d8a3de5ff8f8d/inner_join.jpg](Chapter%20Summary%20Relationships%20Between%20Tables%20df473363342c4a8d819d8a3de5ff8f8d/inner_join.jpg)

The OUTER join retrieves **all** the data from one table and adds data from the other one when there are matching rows.

![Chapter%20Summary%20Relationships%20Between%20Tables%20df473363342c4a8d819d8a3de5ff8f8d/outer_join.jpg](Chapter%20Summary%20Relationships%20Between%20Tables%20df473363342c4a8d819d8a3de5ff8f8d/outer_join.jpg)

**INNER JOIN** 

INNER JOIN selects only data for which the join conditions are met. The order in which the tables are joined does not affect the final result. 

Here's a sample query with INNER JOIN:

```sql
SELECT --listing only the necessary fields
	TABLE_1.field_1 AS field_1,
	TABLE_1.field_2 AS field_2,
	...
	TABLE_2.field_n AS field_n
FROM
	TABLE_1
INNER JOIN TABLE_2 ON TABLE_2.field_1 = TABLE_1.field_2;
```

Let's take a closer look at the syntax:

- INNER JOIN is the name of the joining method. Then comes the name of the table to be joined to the table the FROM block.
- ON precedes the join condition: `TABLE_2.field_1 = TABLE_1.field_2`. This means that only the table rows that match this condition will be joined. In our case the condition is that `field_1` from the second table matches `field_2` from the first.

Since fields in different tables can have the same names, they are referred to by both table name and field name. First comes the table name, then the field: `TABLE_1.field_1`.

## Outer Join. LEFT JOIN

There are two types of OUTER JOIN:

- **LEFT OUTER JOIN**
- **RIGHT OUTER JOIN**

We'll give these methods short names: **LEFT JOIN** and **RIGHT JOIN**. 

LEFT JOIN will select all the data from the left table together with the rows from the right table that match the join condition. RIGHT JOIN will do the same, but for the right table.

![Chapter%20Summary%20Relationships%20Between%20Tables%20df473363342c4a8d819d8a3de5ff8f8d/left_join.jpg](Chapter%20Summary%20Relationships%20Between%20Tables%20df473363342c4a8d819d8a3de5ff8f8d/left_join.jpg)

Here's the syntax of a statement with LEFT JOIN: 

```sql
SELECT 
	TABLE_1.field_1 AS field_1,
	TABLE_1.field_2 AS field_2,
	...
	TABLE_2.field_n AS field_n
FROM
	TABLE_1
LEFT JOIN TABLE_2 ON TABLE_2.field = TABLE_1.field;
```

As with INNER JOIN queries, the table name is indicated for each field. Note that with OUTER JOIN the order in which tables are listed is significant.

## Outer Join. RIGHT JOIN

RIGHT JOIN is LEFT JOIN's twin. But unlike its sibling, it takes all the data from the right table, and the matching rows from the left table. 

![Chapter%20Summary%20Relationships%20Between%20Tables%20df473363342c4a8d819d8a3de5ff8f8d/right_join.jpg](Chapter%20Summary%20Relationships%20Between%20Tables%20df473363342c4a8d819d8a3de5ff8f8d/right_join.jpg)

Here's what a RIGHT JOIN query looks like: 

```sql
SELECT 
	TABLE_1.field_1 AS field_1,
	TABLE_1.field_2 AS field_2,
	...
	TABLE_2.field_n AS field_n
FROM
	TABLE_1
RIGHT JOIN TABLE_2 ON TABLE_1.field = TABLE_2.field;
```

## Joining Multiple Tables

Here's the syntax of a query that uses INNER JOIN several times:

```sql
SELECT --listing only the necessary fields
	TABLE_1.field_1 AS field_1,
	TABLE_1.field_2 AS field_2,
	...
	TABLE_3.field_n AS field_n
FROM
	TABLE_1
INNER JOIN TABLE_2 ON TABLE_2.field = TABLE_1.field
INNER JOIN TABLE_3 ON TABLE_3.field = TABLE_1.field;
```

We'll join the second table, then the third, to the first.

## Joining Statements

The **UNION** and **UNION ALL** operators bring together data from tables. The syntax is as follows:

```sql
SELECT 
	column_name_1  
FROM 
	table_1
UNION --( or UNION ALL)
SELECT 
	column_name_1  
FROM 
	table_2;
```

Here two SELECT - FROM statements are separated by the UNION command. 

Here are the conditions that must be met for a UNION to work:

- The first and second tables must match with respect to the number of columns selected and their data types
- Fields must be in the same order in the first and second tables.

UNION avoids duplicating rows when it generates a table.

![Chapter%20Summary%20Relationships%20Between%20Tables%20df473363342c4a8d819d8a3de5ff8f8d/a_union_b.jpg](Chapter%20Summary%20Relationships%20Between%20Tables%20df473363342c4a8d819d8a3de5ff8f8d/a_union_b.jpg)