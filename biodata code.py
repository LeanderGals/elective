from tkinter import *
import sqlite3
from tkinter import messagebox as mb

root = Tk()
root.title("Biodata")
root.configure(bg="powder blue")
root.state('zoomed')
width = 600
height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
# root.resizable(0, 0)


# Creating Menubar
pdm = Menu(root)

# Adding File Menu and commands
file = Menu(pdm, tearoff=0)

pdm.add_cascade(label='File', menu=file)
file.add_command(label='New File', command=None)
file.add_command(label='Open...', command=None)
file.add_command(label='Save', command=None)
file.add_separator()
file.add_command(label='Exit', command=root.quit)

# Adding Edit Menu and commands
edit = Menu(pdm, tearoff=0)
pdm.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Undo', command=None)
edit.add_command(label='Redo', command=None)
edit.add_separator()
edit.add_command(label='Cut', command=None)
edit.add_command(label='Copy', command=None)
edit.add_command(label='Paste', command=None)
edit.add_command(label='Select All', command=None)
edit.add_separator()
edit.add_command(label='Find...', command=None)
edit.add_command(label='Find again', command=None)

# Adding Format Menu
format_ = Menu(pdm, tearoff=0)
pdm.add_cascade(label='Format', menu=format_)
format_.add_command(label='Format Paragraph', command=None)
format_.add_command(label='Indent Region', command=None)
format_.add_command(label='Dedent Region', command=None)
format_.add_separator()
format_.add_command(label='Toggle Tabs', command=None)

# Adding Run Menu
run = Menu(pdm, tearoff=0)
pdm.add_cascade(label='Run', menu=run)
run.add_command(label='Run Module', command=None)
run.add_command(label='Run...Customized', command=None)
run.add_command(label='Check Module', command=None)
run.add_command(label='Python Shell', command=None)

# Adding Options Menu
options = Menu(pdm, tearoff=0)
pdm.add_cascade(label='Options', menu=options)
options.add_command(label='Configure IDLE', command=None)
options.add_separator()
options.add_command(label='Show Code Context', command=None)
options.add_command(label='Show Line Numbers', command=None)
options.add_command(label='Zoom Height', command=None)

# Adding Help Menu
help_ = Menu(pdm, tearoff=0)
pdm.add_cascade(label='Help', menu=help_)
help_.add_command(label='Tk Help', command=None)
help_.add_command(label='Demo', command=None)
help_.add_separator()
help_.add_command(label='About Tk', command=None)

# display Menu
root.config(menu=pdm)


# ==============================METHODS========================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("Galasanay.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'l123' AND `password` = 'l123'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('l123', 'l123')")
    conn.commit()


def showMsg():
    mb.showinfo('Log In', 'Please complete the required field!')


def error():
    mb.showerror("Error", "You've entered a wrong username or password!")


def callback():
    if mb.askyesno('Verify', 'Really quit?'):
       root.quit()
    else:
        mb.showinfo('No', 'Quit has been cancelled')




def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        showMsg()
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")

        else:
            USERNAME.set("")
            PASSWORD.set("")
            cursor.close()
            conn.close()
            error()



#============================================New Window=================================================================
def HomeWindow():
    global Home, var
    Home = Toplevel()
    Home.title("My Biodata")
    Home.state('zoomed')
    Home.config(bg='powder blue')
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # Creating Radiobutton
    var = IntVar()
    R1 = Radiobutton(Home, text="Personal Information", variable=var, value=1, indicatoron=0, width=20, font=('arial', 15), bd=10, bg='cadet blue', relief=RIDGE,
                     command=show())
    R1.pack(pady=10, anchor=N)
    R2 = Radiobutton(Home, text="Educational Backgorund", variable=var, value=2, indicatoron=0, width=20, font=('arial', 15), bd=10, bg='cadet blue', relief=RIDGE,
                     command=show())
    R2.pack(pady=10, anchor=N)
    R3 = Radiobutton(Home, text="Hobby", variable=var, value=3, indicatoron=0, width=20, font=('arial', 15), bd=10, bg='cadet blue', relief=RIDGE,
                     command=show())
    R3.pack(pady=10, anchor=N)

    # Creating Menubar
    pdm = Menu(Home)

    # Adding File Menu and commands
    file = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='File', menu=file)
    file.add_command(label='New File', command=None)
    file.add_command(label='Open...', command=None)
    file.add_command(label='Save', command=None)
    file.add_separator()
    file.add_command(label='Exit', command=Home.quit)

    # Adding Edit Menu and commands
    edit = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Edit', menu=edit)
    edit.add_command(label='Undo', command=None)
    edit.add_command(label='Redo', command=None)
    edit.add_separator()
    edit.add_command(label='Cut', command=None)
    edit.add_command(label='Copy', command=None)
    edit.add_command(label='Paste', command=None)
    edit.add_command(label='Select All', command=None)
    edit.add_separator()
    edit.add_command(label='Find...', command=None)
    edit.add_command(label='Find again', command=None)

    # Adding Format Menu
    format_ = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Format', menu=format_)
    format_.add_command(label='Format Paragraph', command=None)
    format_.add_command(label='Indent Region', command=None)
    format_.add_command(label='Dedent Region', command=None)
    format_.add_separator()
    format_.add_command(label='Toggle Tabs', command=None)

    # Adding Run Menu
    run = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Run', menu=run)
    run.add_command(label='Run Module', command=None)
    run.add_command(label='Run...Customized', command=None)
    run.add_command(label='Check Module', command=None)
    run.add_command(label='Python Shell', command=None)

    # Adding Options Menu
    options = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Options', menu=options)
    options.add_command(label='Configure IDLE', command=None)
    options.add_separator()
    options.add_command(label='Show Code Context', command=None)
    options.add_command(label='Show Line Numbers', command=None)
    options.add_command(label='Zoom Height', command=None)

    # Adding Help Menu
    help_ = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Help', menu=help_)
    help_.add_command(label='Tk Help', command=None)
    help_.add_command(label='Demo', command=None)
    help_.add_separator()
    help_.add_command(label='About Tk', command=None)

    # display Menu
    Home.config(menu=pdm)

    btn_back = Button(Home, text='Back', font=('arial', 10), bd=10, bg='light blue', relief=RIDGE, command=Back).pack(padx=500, pady=30, fill=X, side=BOTTOM)
    btn_ok = Button(Home, text='Ok', font=('arial', 10), bd=10, bg='light blue', relief=RIDGE, command=show).pack(padx=500, fill=X, side=BOTTOM)

def Back():
    Home.destroy()
    root.deiconify()


def show():
    if (var.get()==1):
        personal_info()
    elif (var.get()==2):
        educ_bg()
    elif (var.get()==3):
        hobby_()


def personal_info():
    personal = Tk()
    personal.title("Personal Information")
    personal.config(bg='powder blue')
    personal.state('zoomed')
    width = 600
    height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    personal.geometry("%dx%d+%d+%d" % (width, height, x, y))

    # Creating Scrollbar
    scroll = Scrollbar(personal)
    scroll.pack(side=RIGHT, fill=Y)


    lbl_p = Label(personal, text="Personal Information", font=('arial', 35), fg="black", bg='powder blue').pack(pady=50, side=TOP)
    lbl_name = Label(personal, text="Name: Leander B. Galasanay", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    lbl_date = Label(personal, text="Date of Birth: August 15, 2001", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    lbl_age = Label(personal, text="Age: 19", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    lbl_place = Label(personal, text="Place of Birth: Amfana, Macanhan, Carmen, Cagayan de Oro City", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    lbl_nationality = Label(personal, text="Nationality: Filipino", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    lbl_sex = Label(personal, text="Sex: Male", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    lbl_email = Label(personal, text="Email: lgalasanay2@gmail.com", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    lbl_number = Label(personal, text="Contact Number: 09262255369", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    lbl_religion = Label(personal, text="Religion: Roman Catholic", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    lbl_mom = Label(personal, text="Mother's Name: Lucrecia B. Galasanay", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    lbl_mom_occ = Label(personal, text="Mother's Occupation: Deceased", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    lbl_father = Label(personal, text="Father's Name: Leo R. Galasanay", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    lbl_father_occ = Label(personal, text="Father's Occupation: Auto Mechanic", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    btn_quit = Button(personal, text='Quit', font=('arial', 10), bd=10, bg='light blue', relief=RIDGE,
                      command=personal.quit).pack(padx=500, pady=30, fill=X, side=BOTTOM)
    btn_back = Button(personal, text='Back', font=('arial', 10), bd=10, bg='light blue', relief=RIDGE, command=personal.destroy).pack(padx=500, fill=X, side=BOTTOM)
    # Creating Menubar
    pdm = Menu(personal)

    # Adding File Menu and commands
    file = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='File', menu=file)
    file.add_command(label='New File', command=None)
    file.add_command(label='Open...', command=None)
    file.add_command(label='Save', command=None)
    file.add_separator()
    file.add_command(label='Exit', command=personal.quit)

    # Adding Edit Menu and commands
    edit = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Edit', menu=edit)
    edit.add_command(label='Undo', command=None)
    edit.add_command(label='Redo', command=None)
    edit.add_separator()
    edit.add_command(label='Cut', command=None)
    edit.add_command(label='Copy', command=None)
    edit.add_command(label='Paste', command=None)
    edit.add_command(label='Select All', command=None)
    edit.add_separator()
    edit.add_command(label='Find...', command=None)
    edit.add_command(label='Find again', command=None)

    # Adding Format Menu
    format_ = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Format', menu=format_)
    format_.add_command(label='Format Paragraph', command=None)
    format_.add_command(label='Indent Region', command=None)
    format_.add_command(label='Dedent Region', command=None)
    format_.add_separator()
    format_.add_command(label='Toggle Tabs', command=None)

    # Adding Run Menu
    run = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Run', menu=run)
    run.add_command(label='Run Module', command=None)
    run.add_command(label='Run...Customized', command=None)
    run.add_command(label='Check Module', command=None)
    run.add_command(label='Python Shell', command=None)

    # Adding Options Menu
    options = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Options', menu=options)
    options.add_command(label='Configure IDLE', command=None)
    options.add_separator()
    options.add_command(label='Show Code Context', command=None)
    options.add_command(label='Show Line Numbers', command=None)
    options.add_command(label='Zoom Height', command=None)

    # Adding Help Menu
    help_ = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Help', menu=help_)
    help_.add_command(label='Tk Help', command=None)
    help_.add_command(label='Demo', command=None)
    help_.add_separator()
    help_.add_command(label='About Tk', command=None)

    # display Menu
    personal.config(menu=pdm)

def educ_bg():
    educ = Tk()
    educ.title("Educational Background")
    educ.config(bg='powder blue')
    educ.state('zoomed')
    width = 600
    height = 900
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    educ.geometry("%dx%d+%d+%d" % (width, height, x, y))

    #Creating Scrollbar
    scroll = Scrollbar(educ)
    scroll.pack(side=RIGHT, fill=Y)

    lbl_education = Label(educ, text="Educational Background", font=('arial', 35), fg="black", bg='powder blue').pack(pady=50, side=TOP)
    lbl_elementary = Label(educ, text="Elementary: Macanhan Elementary School       2008-2014", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    lbl_secondary = Label(educ, text="Secondary: Gusa Regional Science High School-X        2014-2018", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    lbl_senior_high = Label(educ, text="Senior High: Gusa Regional Science High School-X        2018-2020", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    btn_quit = Button(educ, text='Quit', font=('arial', 10), bd=10, bg='light blue', relief=RIDGE, command=educ.quit).pack(padx=500, pady=30, fill=X, side=BOTTOM)
    btn_back = Button(educ, text='Back', font=('arial', 10), bd=10, bg='light blue', relief=RIDGE, command=educ.destroy).pack(padx=500, fill=X, side=BOTTOM)

    # Creating Menubar
    pdm = Menu(educ)

    # Adding File Menu and commands
    file = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='File', menu=file)
    file.add_command(label='New File', command=None)
    file.add_command(label='Open...', command=None)
    file.add_command(label='Save', command=None)
    file.add_separator()
    file.add_command(label='Exit', command=educ.quit)

    # Adding Edit Menu and commands
    edit = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Edit', menu=edit)
    edit.add_command(label='Undo', command=None)
    edit.add_command(label='Redo', command=None)
    edit.add_separator()
    edit.add_command(label='Cut', command=None)
    edit.add_command(label='Copy', command=None)
    edit.add_command(label='Paste', command=None)
    edit.add_command(label='Select All', command=None)
    edit.add_separator()
    edit.add_command(label='Find...', command=None)
    edit.add_command(label='Find again', command=None)

    # Adding Format Menu
    format_ = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Format', menu=format_)
    format_.add_command(label='Format Paragraph', command=None)
    format_.add_command(label='Indent Region', command=None)
    format_.add_command(label='Dedent Region', command=None)
    format_.add_separator()
    format_.add_command(label='Toggle Tabs', command=None)

    # Adding Run Menu
    run = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Run', menu=run)
    run.add_command(label='Run Module', command=None)
    run.add_command(label='Run...Customized', command=None)
    run.add_command(label='Check Module', command=None)
    run.add_command(label='Python Shell', command=None)

    # Adding Options Menu
    options = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Options', menu=options)
    options.add_command(label='Configure IDLE', command=None)
    options.add_separator()
    options.add_command(label='Show Code Context', command=None)
    options.add_command(label='Show Line Numbers', command=None)
    options.add_command(label='Zoom Height', command=None)

    # Adding Help Menu
    help_ = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Help', menu=help_)
    help_.add_command(label='Tk Help', command=None)
    help_.add_command(label='Demo', command=None)
    help_.add_separator()
    help_.add_command(label='About Tk', command=None)

    # display Menu
    educ.config(menu=pdm)
def hobby_():
    hobby = Tk()
    hobby.title("My Hobby")
    hobby.config(bg='powder blue')
    hobby.state('zoomed')
    width = 600
    height = 900
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    hobby.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_hobby = Label(hobby, text="Hobby", font=('arial', 35), fg="black", bg='powder blue').pack(pady=50, side=TOP)
    lbl_guitar = Label(hobby, text="Playing Guitar", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    lbl_cleaning = Label(hobby, text="Cleaning the House", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    lbl_games= Label(hobby, text="Playing Mobile Games", font=('arial', 15), fg="black", bg='powder blue').pack(side=TOP)
    btn_quit = Button(hobby, text='Quit', font=('arial', 10), bd=10, bg='light blue', relief=RIDGE,
                      command=hobby.quit).pack(padx=500, pady=30, fill=X, side=BOTTOM)
    btn_back = Button(hobby, text='Back', font=('arial', 10), bd=10, bg='light blue', relief=RIDGE, command=hobby.destroy).pack(padx=500, fill=X, side=BOTTOM)

    #Creating Scrollbar
    scroll = Scrollbar(hobby)
    scroll.pack(side=RIGHT, fill=Y)

    # Creating Menubar
    pdm = Menu(hobby)

    # Adding File Menu and commands
    file = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='File', menu=file)
    file.add_command(label='New File', command=None)
    file.add_command(label='Open...', command=None)
    file.add_command(label='Save', command=None)
    file.add_separator()
    file.add_command(label='Exit', command=hobby.quit)

    # Adding Edit Menu and commands
    edit = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Edit', menu=edit)
    edit.add_command(label='Undo', command=None)
    edit.add_command(label='Redo', command=None)
    edit.add_separator()
    edit.add_command(label='Cut', command=None)
    edit.add_command(label='Copy', command=None)
    edit.add_command(label='Paste', command=None)
    edit.add_command(label='Select All', command=None)
    edit.add_separator()
    edit.add_command(label='Find...', command=None)
    edit.add_command(label='Find again', command=None)

    # Adding Format Menu
    format_ = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Format', menu=format_)
    format_.add_command(label='Format Paragraph', command=None)
    format_.add_command(label='Indent Region', command=None)
    format_.add_command(label='Dedent Region', command=None)
    format_.add_separator()
    format_.add_command(label='Toggle Tabs', command=None)

    # Adding Run Menu
    run = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Run', menu=run)
    run.add_command(label='Run Module', command=None)
    run.add_command(label='Run...Customized', command=None)
    run.add_command(label='Check Module', command=None)
    run.add_command(label='Python Shell', command=None)

    # Adding Options Menu
    options = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Options', menu=options)
    options.add_command(label='Configure IDLE', command=None)
    options.add_separator()
    options.add_command(label='Show Code Context', command=None)
    options.add_command(label='Show Line Numbers', command=None)
    options.add_command(label='Zoom Height', command=None)

    # Adding Help Menu
    help_ = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='Help', menu=help_)
    help_.add_command(label='Tk Help', command=None)
    help_.add_command(label='Demo', command=None)
    help_.add_separator()
    help_.add_command(label='About Tk', command=None)

    # display Menu
    hobby.config(menu=pdm)

# ==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()
# ==============================FRAMES=========================================
Top = Frame(root, bd=10, relief=RAISED)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=300, bd=15, relief=RIDGE, bg='cadet blue')
Form.pack(side=TOP, pady=10)
f1 = Frame(root, height=100, bd=15, relief=RIDGE, bg='cadet blue')
f1.pack(side=TOP)
# ==============================LABELS=========================================
lbl_title = Label(Top, text="To See My Biodata, Log In First", font=('times new roman bold', 22), bg='powder blue')
lbl_title.pack(fill=X)
lbl_username = Label(Form, text="Username:", font=('arial', 18), fg="white", bg='cadet blue')
lbl_username.grid(row=4, column=6)
lbl_password = Label(Form, text="Password:", font=('arial', 18), fg="white", bg='cadet blue')
lbl_password.grid(row=5, column=6)
# ==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME, bg='cadet blue', font=('arial', 18))
username.grid(row=4, column=7)
password = Entry(Form, textvariable=PASSWORD, bg='cadet blue', show="*", font=('arial', 18))
password.grid(row=5, column=7)
# ==============================BUTTON WIDGETS=================================
btn_login = Button(f1, text="Login", width=15, font=('arial', 10), command=Login)
btn_exit = Button(f1, text="Exit", width=15, font=('arial', 10), command=callback)
btn_login.grid()
btn_exit.grid()
btn_login.bind('<Return>', Login)
root.mainloop()
