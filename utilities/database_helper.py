import mysql.connector as sql


def sql_connector(host, database, user, password):
    """
      This functions helps to make connection with the sql server
      :param host: host name for the sql server
      :param database: database name for the sql server
      :param user: username for the sql server
      :param password: password for the sql server
      :return: connection to sql server
      """
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
    """
    This function helps to execute the query
    :param connection: established connection
    :param query: query to execute
    :return: executed query
    """
    mycursor = connection.cursor()
    mycursor.execute(query)
    connection.commit()
    mycursor.close()
    return mycursor
