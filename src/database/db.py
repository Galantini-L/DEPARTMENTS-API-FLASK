from decouple import config
from mysql.connector import connect, Error

def get_connection():
    try:
        connection = connect(
            user=config('MYSQL_USERNAME'),
            password=config('MYSQL_PASSWORD'),
            host=config('MYSQL_HOST'),
            database=config('MYSQL_DATABASE')
        )
        print('successfully database conection')
        return connection

    except Error as er:
        raise er
