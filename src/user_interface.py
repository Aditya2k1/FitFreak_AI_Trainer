from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

from FitFreak_AI_Trainer.utilities.file_constants import title_name, title_geometry, title_width, title_height, \
    title_bg_color, title_fg_color, button_bg
from FitFreak_AI_Trainer.utilities.store_user_data import user_database, show_data

root = Tk()
root.title(title_name)
root.geometry(title_geometry)
root.configure(bg=title_bg_color)
root.iconbitmap('icon_f.ico')
root.resizable(title_width, title_height)


'''def display_data(my_tuples):
    #for the display window
    win = Tk()
    win.title(title_name)
    win.geometry(title_geometry)
    win.configure(bg=title_bg_color)
    win.iconbitmap('icon_f.ico')
    win.resizable(title_width, title_height)
    tree = ttk.Treeview(win)
    tree.pack()
    tree["columns"] = ("name", "goal","date","exercise")
    tree.heading("name", text="Name")
    tree.heading("goal", text="Goal")
    tree.heading("date", text="Date")
    tree.heading("exercise", text="Exercise")

    for tuple_item in my_tuples:
        tree.insert("", END, values=tuple_item, iid=index)
        index += 1
    win.mainloop()'''

def next_button():
    """
    This function executes after "Next" button is pressed
    Stores the name and date and opens the second window
    :return: None
    """
    name = user_entry.get()
    t_date = date_entry.get()
    screen = Toplevel(root)

    # Destroys an existing window
    root.destroy()
    screen = Tk()
    screen.title(title_name)
    screen.geometry(title_geometry)
    screen.config(bg=title_bg_color)
    screen.iconbitmap('icon_f.ico')
    screen.resizable(title_width, title_height)

    def submit_button():
        """
        This function executes after "submit" button is pressed
        :return: None
        """
        exercise = var.get()
        goal = goal_entry.get()
        screen.destroy()
        if exercise == "View History":
            # shows the user history
            show_data(name)
        else:
            # returns the values to make database entry
            user_database(name, t_date, exercise, goal)


    # Logo on top
    favicon = PhotoImage(file='FITNESS.png')
    Label(screen, image=favicon, bg=title_bg_color).place(x=46, y=20)

    # Frame for exercise,goal
    frame = Frame(screen, width=715, height=350, bg=title_bg_color)
    frame.place(x=100, y=110)

    # Select exercise
    get_choice = Label(frame, text='What Would You Like To Do?', fg=title_fg_color,
                       bg=title_bg_color, font=('Digital-7 Mono', 32, 'bold'))
    get_choice.place(x=74, y=5)
    var = StringVar()
    get_exercise = ttk.Combobox(screen, width=15, background='red',
                                font=("Courier", 16), values=["Bicep Curls", "Squats", "View History"],
                                textvariable=var)
    get_exercise.place(x=333, y=190)
    # Border under Choice field
    Frame(frame, width=525, height=2, bg='black').place(x=85, y=114)

    # Goal Entry
    get_goal = Label(frame, text='Please Enter Your Goal For Today',
                     fg='#FF9E5E', bg='#e03481', font=('Digital-7 Mono', 32, 'bold'))
    get_goal.place(x=16, y=130)
    # Border under Goal field
    Frame(frame, width=525, height=2, bg='black').place(x=85, y=235)

    def on_click_goal(e):
        """
        Event handler: removes text when clicked on goal
        :param e: e
        :return: None 
        """
        goal_entry.delete(0, 'end')

    def on_leave_goal(e):
        """
        Event handler: takes entry of given number of goals
        :param e: e
        :return: None
        """
        nm = goal_entry.get()
        if nm == '':
            goal_entry.insert(0, 'Goal')

    goal_entry = Entry(frame, width=28, fg='black', justify=CENTER, border=0,
                       bg=title_bg_color, disabledbackground=title_bg_color, state='disabled',
                       font=('Courier', 22))
    goal_entry.place(x=105, y=200)

    def toggle_entry(*args):
        """
        :param args: *args
        :return: None
        """
        if var.get() in ("Bicep Curls", "Squats"):
            goal_entry.config(state='normal')
            goal_entry.insert(0, 'Goal')
        else:
            goal_entry.config(state='disabled')

    goal_entry.bind('<FocusIn>', on_click_goal)
    goal_entry.bind('<FocusOut>', on_leave_goal)
    var.trace("w", toggle_entry)
    # Submit Button
    Button(frame, width=39, pady=7, text='Submit',
           bg=button_bg, fg='white', border=0,
           command=submit_button).place(x=205, y=304)

    screen.mainloop()
    # root.destroy()


# Logo on top
title_image = PhotoImage(file='FITNESS.png')
Label(root, image=title_image, bg=title_bg_color).place(x=46, y=20)

# Frame for name,date
frame = Frame(root, width=715, height=350, bg=title_bg_color)
frame.place(x=100, y=110)

# Please Enter Your Name
get_name = Label(frame, text='Please Enter Your Name', fg=title_fg_color,
                 bg='#e03481', font=('Digital-7 Mono', 32, 'bold'))
get_name.place(x=135, y=5)


def on_click_name(e):
    """
    Event handler: removes text when clicked on name
    :param e:
    :return: None
    """
    user_entry.delete(0, 'end')


def on_leave_name(e):
    """
    Event handler: takes entry of users' name
    :param e:
    :return: None
    """
    nm = user_entry.get()
    if nm == '':
        user_entry.insert(0, 'Name')


user_entry = Entry(frame, width=28, fg='black', justify=CENTER,
                   border=0, bg=title_bg_color, font=('Courier', 22))
user_entry.place(x=130, y=80)
user_entry.insert(0, 'Name')
user_entry.bind('<FocusIn>', on_click_name)
user_entry.bind('<FocusOut>', on_leave_name)
# Border under Name field
Frame(frame, width=478, height=2, bg='black').place(x=130, y=114)

# Please Enter Date
get_goal = Label(frame, text="Please Enter Today's Date", fg=title_fg_color,
                 bg=title_bg_color, font=('Digital-7 Mono', 32, 'bold'))
get_goal.place(x=105, y=135)
# Date Entry
date_entry = DateEntry(root, width=12, cursor='ibeam', foreground='black',
                       background=title_fg_color, borderwidth=2, font=("Courier", 16))
date_entry.place(x=390, y=315)
# Border under Date field
Frame(frame, width=478, height=2, bg='black').place(x=130, y=240)

# Next Button
Button(frame, width=39, pady=7, text='Next',
       bg=button_bg, fg='white', border=0,
       command=next_button).place(x=235, y=304)

root.mainloop()

################################################################
# The values are stored in the variables as given below:
# name --> Stores the user's name
# t_date --> Date entered by the user
# exercise --> Stores user's choice, i.e Bicep Curls/Squats/History
# goal --> Stores the user entered goal for the day

# All values in string
