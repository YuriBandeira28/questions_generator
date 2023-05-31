import psycopg
import config

def connect():
    try:
        conn = psycopg.
        
        return conn
    except Exception as e:
        raise ConnectionError(e)
    
connect()