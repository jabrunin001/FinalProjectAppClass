import pandas as pd
import psycopg2

# Parameters for Redshift connection
host = 'default-namespace.547743c6-146c-4fb5-9733-b7efa63486f6.us-east-2.redshift.amazonaws.com'
port = '5439' # Default Redshift port
user = 'jabrunin'
password = 'test-password'
dbname = 'traffic'

# Connect to Redshift
conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)
cur = conn.cursor()

# Load data from CSV
data_path = 'TrafficDataSample.csv'
df = pd.read_csv(data_path)

# Assuming df columns match the Redshift table's columns one-to-one
for index, row in df.iterrows():
    cur.execute(
        "INSERT INTO traffic_accidents VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        row
    )

conn.commit()
cur.close()
conn.close()
