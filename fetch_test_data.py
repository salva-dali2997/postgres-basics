import psycopg2
from credentials import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    curs = conn.cursor()
    curs.execute("SELECT * FROM test")
    # fetchmany(<index>) || cur.fetchall()
    return_data = curs.fetchone()
    print(return_data)
    curs.close()
    conn.close()
    print("Database table fetched successfully")
except:
    print("Database table not fetched successfully")