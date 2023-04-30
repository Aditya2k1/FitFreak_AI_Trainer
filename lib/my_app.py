from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

root = Tk()
root.title('Fitness AI Trainer')
root.geometry('925x500+300+200')
root.configure(bg='#e03481')
root.iconbitmap('icon_f.ico')
root.resizable(False, False)


# 2.0executes after "next" button is pressed
# 2.0stores the name and date and opens the second window
def next_but():
    name = user_entry.get()
    tdate = date_entry.get()
    screen = Toplevel(root)
    # destroys existing window
    root.destroy()
    screen = Tk()
    screen.title('Fitness AI Trainer')
    screen.geometry('925x500+300+200')
    screen.config(bg='#e03481')
    screen.iconbitmap('icon_f.ico')
    screen.resizable(False, False)

    # 2.0Executes after "submit" button is pressed
    def submit_but():
        exercise = var.get()
        goal = goal_entry.get()
        screen.destroy()

    # 2.0Logo on top
    img = PhotoImage(file='FITNESS.png')
    Label(screen, image=img, bg='#e03481').place(x=46, y=20)
    # 2.0frame for exercise,goal
    frame = Frame(screen, width=715, height=350, bg='#e03481')
    frame.place(x=100, y=110)
    # 2.0Please Choose Exercise
    ex_choice = Label(frame,
                      text='What Would You Like To Do?',
                      fg='#FF9E5E', bg='#e03481',
                      font=('Digital-7 Mono', 32, 'bold'))
    ex_choice.place(x=74, y=5)

    var = StringVar()
    exer = ttk.Combobox(screen,
                        width=15, background='red',
                        font=("Courier", 16),
                        values=["Bicep Curls", "Squats", "View History"],
                        textvariable=var)
    exer.place(x=333, y=190)

    # 2.0Border under Choice field
    Frame(frame, width=525, height=2, bg='black').place(x=85, y=114)

    # 2.0Please Enter Goal
    goal_label = Label(frame,
                       text='Please Enter Your Goal For Today',
                       fg='#FF9E5E', bg='#e03481',
                       font=('Digital-7 Mono', 32, 'bold'))
    goal_label.place(x=16, y=130)

    # 2.0Border under Goal field
    Frame(frame, width=525, height=2, bg='black').place(x=85, y=235)

    # Goal
    def on_enter(e):
        goal_entry.delete(0, 'end')

    def on_leave(e):
        nm = goal_entry.get()
        if nm == '':
            goal_entry.insert(0, 'Goal')

    goal_entry = Entry(frame, width=28, fg='black',
                       justify=CENTER, border=0, bg='#e03481',
                       disabledbackground="#e03481", state='disabled',
                       font=('Courier', 22))
    goal_entry.place(x=105, y=200)

    def toggle_entry(*args):
        if var.get() in ("Bicep Curls", "Squats"):
            goal_entry.config(state='normal')
            goal_entry.insert(0, 'Goal')
        else:
            goal_entry.config(state='disabled')

    goal_entry.bind('<FocusIn>', on_enter)
    goal_entry.bind('<FocusOut>', on_leave)
    var.trace("w", toggle_entry)
    # 2.0Submit Button
    Button(frame, width=39, pady=7,
           text='Submit', bg='#57a1f8',
           fg='white', border=0,
           command=submit_but).place(x=205, y=304)

    screen.mainloop()

    # root.destroy()


# 2.0Logo on top
img = PhotoImage(file='FITNESS.png')
Label(root, image=img, bg='#e03481').place(x=46, y=20)

# 2.0frame for name,date
frame = Frame(root, width=715, height=350, bg='#e03481')
frame.place(x=100, y=110)

# 2.0Please Enter Your Name
heading = Label(frame,
                text='Please Enter Your Name',
                fg='#FF9E5E',
                bg='#e03481',
                font=('Digital-7 Mono', 32, 'bold'))
heading.place(x=135, y=5)


# 2.0Entry for Name
def on_enter(e):
    user_entry.delete(0, 'end')


def on_leave(e):
    nm = user_entry.get()
    if nm == '':
        user_entry.insert(0, 'Name')


user_entry = Entry(frame, width=28, fg='black',
                   justify=CENTER, border=0,
                   bg='#e03481', font=('Courier', 22))
user_entry.place(x=130, y=80)
user_entry.insert(0, 'Name')
user_entry.bind('<FocusIn>', on_enter)
user_entry.bind('<FocusOut>', on_leave)

# 2.0Border under Name field
Frame(frame, width=478, height=2, bg='black').place(x=130, y=114)

# 2.0Please Enter Date
heading2 = Label(frame,
                 text="Please Enter Today's Date",
                 fg='#FF9E5E', bg='#e03481',
                 font=('Digital-7 Mono', 32, 'bold'))
heading2.place(x=105, y=135)

# 2.0Date Entry
date_entry = DateEntry(root,
                       width=12, cursor='ibeam',
                       foreground='black', background='#FF9E5E',
                       borderwidth=2, font=("Courier", 16))
date_entry.place(x=390, y=315)

# 2.0Border under Date field
Frame(frame, width=478, height=2, bg='black').place(x=130, y=240)

# 2.0Next Button
Button(frame, width=39, pady=7, text='Next', bg='#57a1f8',
       fg='white', border=0, command=next_but).place(x=235, y=304)

root.mainloop()

################################################################
# The values are stored in the variables as given below:
# name --> Stores the user's name
# tdate --> Date entered by the user
# exercise --> Stores user's choice, i.e Bicep Curls/Squats/History
# goal --> Stores the user entered goal for the day

# All values in string
