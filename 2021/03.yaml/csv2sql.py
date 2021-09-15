# CSV to Sqlite3 conversion
# Brygg Ullmer, Clemson University, 2021-09-14
# https://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python
# https://datatofish.com/pandas-dataframe-to-sql/

import sys, pandas, sqlite3

try:    csvFn, sqlFn, tableName = sys.argv[1:3]
except: print("Expecting three arguments: CSV filename, SQLite filename, tablename"); sys.exit(-1)

conn = sqlite3.connect(sqlFn)

df = pandas.read_csv(csvfile) # https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
df.to_sql(tableName, conn, if_exists='append', index=False)

### end ###

