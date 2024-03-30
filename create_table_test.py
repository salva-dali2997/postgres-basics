import psycopg2
from credentials import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
print(DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER)
try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    curs = conn.cursor()
    curs.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    print("Database table created successfully")
    conn.commit()
    curs.close()
    conn.close()
    
except:
    print("Database table not created successfully")