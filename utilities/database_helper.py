import mysql.connector as sql


def sql_connector(host, database, user, password):
    try:
        conn = sql.connect(host=host,
                           database=database,
                           user=user,
                           password=password)

        if conn.is_connected():
            print(f'Connected to MySQL database {database}')
            return conn

    except Exception as ex:
        print(f'Error connecting to MySQL database: {ex}')


def execute_query(connection, query: str):
    mycursor = connection.cursor()
    mycursor.execute(query)
    return mycursor
