import psycopg
import config

def connect():
    try:
        conn = psycopg.Connection()
        
        return conn
    except Exception as e:
        raise ConnectionError(e)
    
connect()