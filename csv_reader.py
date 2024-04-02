import csv
import psycopg2
from credentials import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

data_to_insert = []
with open('data.csv', newline='') as csvfile:
    data_reader = csv.reader(csvfile, delimiter=',')
    for row in data_reader:
        data_to_insert.append(row)
print(data_to_insert)

try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    curs = conn.cursor()
    for data in data_to_insert:
        curs.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (data[0], data[1]))
    conn.commit()
    curs.close()
    conn.close()
    print("Database table updated successfully")
except:
    print("Database table not created successfully")