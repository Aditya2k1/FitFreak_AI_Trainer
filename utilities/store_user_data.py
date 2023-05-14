from FitFreak_AI_Trainer.utilities.file_constants import db_host, db_name, db_user, db_password, db_table
from FitFreak_AI_Trainer.utilities.database_helper import sql_connector, execute_query
#from FitFreak_AI_Trainer.src.user_interface import display_data

#these r the new stuff that has been imported
from tkinter import *
from tkinter import ttk
from FitFreak_AI_Trainer.utilities.file_constants import title_name, title_geometry, title_width, title_height, \
    title_bg_color, title_fg_color, button_bg
#and thats all that has been imported

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


        #changes made from here
        #for the display window
        win = Tk()
        win.title(title_name)
        win.geometry(title_geometry)
        win.configure(bg=title_bg_color)
        win.iconbitmap('icon_f.ico')
        win.resizable(title_width, title_height)
        # Logo on top
        logo_top = PhotoImage(file='FITNESS.png')
        Label(win, image=logo_top, bg=title_bg_color).place(x=46, y=20)
        style=ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="#e03481",
                        foreground="black",
                        bordercolor="#e03481",
                        rowheight=25,
                        fieldbackground="#e03481"
                        )

        tree = ttk.Treeview(win)
        tree.place(x=60,y=120)
        tree["columns"] = ("name", "goal","date","exercise")
        tree["show"]='headings'
        tree.heading("name", text="Name")
        tree.heading("goal", text="Goal")
        tree.heading("date", text="Date")
        tree.heading("exercise", text="Exercise")
        index = 0
        for tuple_item in cursor:
            tree.insert("", END, values=tuple_item, iid=index)
            index += 1
        win.mainloop()
        #changes made till here


        #for data in cursor:
         #   print(data)
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
