# CSV to Sqlite3 conversion
# Brygg Ullmer, Clemson University, 2021-09-14
# https://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python
# https://datatofish.com/pandas-dataframe-to-sql/

import sys

try:    csvFn, sqlFn = sys.argv[1], sys.argv[2]
except: print("Expecting two arguments: CSV filename and SQLite filename"); sys.exit(-1)

df = pandas.read_csv(csvfile) # https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
df.to_sql(table_name, conn, if_exists='append', index=False)

### end ###

