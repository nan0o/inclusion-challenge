# Questions

## Database Design

1 - What are the advantages and disadvantages of creating and using normalized tables?

There are lots, in fact there are books that cover this topic entirely. The main ones are:

- Advantages:
  - Data integrity and consistency, it is non-redundant
  - Tables are more performant against Updates and Inserts (Write operations)
  - Compaction of tables, which means less space is required since we are removing data redundancy
  - Granularity in which tables need to be joined
- Disadvantages:
  - Since data is not duplicated, it is common to join two or several tables.
  - Read times are slower

2 - What are the advantaged and disadvantages of creating and using non-normalized tables?

- Advantages:
  - Minimizing needs for joins, it's better for analytics
  - Reducing number of tables (less chances for multiple-table joins)
  - Improving Read speeds, retrieval of data is faster
- Disadvantages:
  - Slow down updates and writes
  - Be inconsistent
  - More storage is required since there's redundancy

Basically I would choose between normalization or no depending if my application
is heavily dependent on analytics (reads) or transactions (updates, inserts, deletes)

## Hive

1 - Given a table in Hive, how de we identify where the data is stored?

`DESCRIBE FORMATTED my_table;`

2 - How can we see what partitions the table may have?

`$hive -e 'show partitions table;' > partitions` (This way we save the output to a file so
it doesn't get limited by the CLI output)

3 - How can we see if the table is missing any partitions?

`SHOW PARTITIONS table_name;`
If the goal is to fill up partitions from existing HDFS files that are not updating 
in Hive Metastore we should run `MSCK REPAIR TABLE table_name`.

## Hive Queries

1 - Provide an HQL query to provide a distribution of the number of auctions and line items, 
grouped by the number of segments within each auction record.
```
SELECT auctionid, line, size(arysegments) FROM auctions
GROUP BY size(arysegments)
```

2 - Provide an HQL query to provide the distinct count of auctions and line items, 
associated to each segment within arysegments. 
```
SELECT count(distinct auctionid), count(distinct idlineitem), segment FROM auctions
LATERAL VIEW explode(arysegments) segments AS segment
```