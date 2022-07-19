#!/bin/bash

result="hive_query_$(date +%Y-%m-%d).log"

DATE="2021-09-01"

for i in {0..29}
do
    NEXT_DATE=$(date +%Y-%m-%d -d "$DATE + $i day")
    HQL_QUERY='hive -e "select utc_date, sum(1) as num_rows from my_table where utc_date = '${NEXT_DATE}' group by utc_date"'
    $HQL_QUERY 2>&1 |& tee -a  ${result}
done
