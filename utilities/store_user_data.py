from FitFreak_AI_Trainer.utilities.config import db_host, db_name, db_user, db_password, db_table
from FitFreak_AI_Trainer.utilities.database_helper import sql_connector, execute_query


def user_database(name, date, exercise, goal):
    """
    This function helps to insert the user value into database
    :param name: Name of the user
    :param date: Exercise date
    :param exercise: Exercise perform by the user
    :param goal: User goal
    :return: None
    """
    try:
        create_database()
        print(f'Database: {db_name} is created')
    except:
        print(f'Found database: {db_name}')

    connection = sql_connector(db_host, db_name, db_user, db_password)
    print(f'Connected to MySQL database: {db_name}')
    try:
        create_query = f"""CREATE TABLE {db_table}
                        (id int primary key auto_increment,
                        Name varchar(50),
                        Goal int,
                        Date varchar(30), 
                        Exercise varchar(50))"""
        execute_query(connection, create_query)

        query = f"""INSERT INTO {db_table}(Name,Goal,Date,Exercise) values(('{name}'), ('{goal}'),
                ('{date}'),('{exercise}'))"""
        print('---Table created successfully---')
        print('---Data Inserted---')
        try:
            execute_query(connection, query)
        except Exception as ex:
            print(f'Unable to run query: {ex}')
        connection.close()
    except:
        print(f'==== Found table: {db_table} ====')
        query = f"""INSERT INTO {db_table}(Name,Goal,Date,Exercise) values(('{name}'), ('{goal}'),
                ('{date}'), ('{exercise}'))"""
        print('---Data Inserted---')
        try:
            execute_query(connection, query)
        except Exception as ex:
            print(f'Unable to run query: {ex}')
        connection.close()


def show_data(name):
    """
    This function enables to show data for the returned user's name
    'data' variable type: tuple
    :param name: name of the user to see data
    :return: None
    """
    connection = sql_connector(db_host, db_name, db_user, db_password)
    try:
        query = f""" SELECT Name, Goal, Date, Exercise FROM {db_table} WHERE Name = '{name}' """
        cursor = execute_query(connection, query)
        for data in cursor:
            print(data)
    except Exception as ex:
        print(f'Unable to execute query: {ex}')


def create_database():
    """
    This function creates a new database in sql
    :return: None
    """
    query = f"""CREATE DATABASE {db_name}"""
    connection = sql_connector(db_host, '', db_user, db_password)
    execute_query(connection, query)
