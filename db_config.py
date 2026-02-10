import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="pbas",
        user="postgres",          # change if needed
        password="1423", # change this
        host="localhost",
        port="5432"
    )
    return conn
