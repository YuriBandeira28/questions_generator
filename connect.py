import psycopg as pg
import config

def connect():
    try:
        conn = pg.connect('host={0} user={1} dbname={2} password={3}'
                                      .format(config.host, config.user, 
                                              config.database, config.pasword))

        return conn
    except Exception as e:
        raise ConnectionError(e)
