import subprocess
import datetime

# I propose this as a quick solution when the python script is being executed
# where Hive is installed

# I create a list that hold datetime objects for all the days in September 2021
# We use a generator comprehension so we don't store the whole array in memory
# and generate dates as required
date_list = (datetime.datetime(2021, 9, 1) + datetime.timedelta(days=x)
             for x in range(30))

with open(f'hive_query_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log', 'w') as f:
    for date in date_list:
        # I assume the date format is %Y-%m-%d
        cmd = f'hive -e "select utc_date, sum(1) as num_rows from my_table where \
            utc_date = {datetime.datetime.strftime(date,"%Y-%m-%d")} group by utc_date;"'

        status, output = subprocess.getstatusoutput(cmd)

        if status == 0:
            f.write(f"{output}\n")
        else:
            f.write(f'ERROR: Query failed for day {datetime.datetime.strftime(date,"%Y-%m-%d")} with error: {output}\n')
