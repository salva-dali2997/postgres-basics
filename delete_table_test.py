import psycopg2
from credentials import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    conn.execute("DELETE TABLE test;")
    print("Database table deleted succussfully")
except:
    print("Database table no deleted succussfully")