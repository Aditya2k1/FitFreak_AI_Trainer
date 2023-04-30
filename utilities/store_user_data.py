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
    connection = sql_connector(db_host, db_name, db_user, db_password)

    try:
        create_query = f"""CREATE TABLE {db_table}
                        (id int primary key auto_increment,
                        name varchar(50),
                        goal int,
                        date varchar(30), 
                        exercise varchar(50))"""
        execute_query(connection, create_query)

        query = f"""INSERT INTO {db_table}(name,goal,date,exercise) values(('{name}'), ('{goal}'),
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
        query = f"""INSERT INTO {db_table}(name,goal,date,exercise) values(('{name}'), ('{goal}'),
                ('{date}'), ('{exercise}'))"""
        print('---Data Inserted---')
        try:
            execute_query(connection, query)
        except Exception as ex:
            print(f'Unable to run query: {ex}')
        connection.close()
