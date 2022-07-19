from pyhive import hive
import datetime

"""
This solution is more robust as it can be executed remotely, although it
requires some dependencies
"""
conn = hive.Connection(host="<cluster_hostname_or_ip>", port=<cluster_port>,
                      username="<hive_username>")
cursor = conn.cursor()

date_list = (datetime.datetime(2021, 9, 1) + datetime.timedelta(days=x)
             for x in range(30))

with open(f'hive_query_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log', 'w') as f:
    for date in date_list:
        # I assume the date format is %Y-%m-%d
        cursor.execute(f'hive -e "select utc_date, sum(1) as num_rows from my_table where \
            utc_date = {datetime.datetime.strftime(date,"%Y-%m-%d")} group by utc_date;"')

        result = cursor.fetchall()

        try:
            f.write(f"{result}\n")
        except Exception as e:
            f.write(f'ERROR: Query failed for day {datetime.datetime.strftime(date,"%Y-%m-%d")} with error: {e}\n')