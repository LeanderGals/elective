from tkinter import *
import sqlite3
from tkinter import messagebox as mb
from PIL import ImageTk, Image


root = Tk()
root.title("Activity 8")
root.configure(bg="powder blue")
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
    cursor.execute("SELECT * FROM `member` WHERE `username` = '123' AND `password` = '123'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('123', '123')")
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

def Back():
    Home.destroy()
    root.deiconify()

#============================================New Window=================================================================
def HomeWindow():
    global Home
    Home = Toplevel()
    Home.title("Hospital IoT")
    Home.config(bg='powder blue')
    Home.state('zoomed')
    width = 400
    height = 300
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    

    # Creating Menubar
    pdm = Menu(Home)

    # Adding File Menu and commands
    file = Menu(pdm, tearoff=0)
    pdm.add_cascade(label='File', menu=file)
    file.add_command(label='New File', command=None)
    file.add_command(label='Open...', command=None)
    file.add_command(label='Save', command=None)
    file.add_separator()
    file.add_command(label='Exit', command=Home.destroy)

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

    
    lbltext = Label(Home, text='Typical Architecture in Healthcare Application Using MWSN and IoT', bg = 'powder blue', font=('arial', 18)).pack(pady = 10)
    btn_exit= Button(Home, text='Exit', font=('arial', 10), bd=10, bg='light blue', relief=RIDGE, command=callback).pack(padx=500, pady=20, fill=X, side=BOTTOM)
    btn_back = Button(Home, text='Back', font=('arial', 10), bd=10, bg='light blue', relief=RIDGE, command=Back).pack(padx=500, fill=X, side=BOTTOM)
    
    img11 = Image.open("img1.png")
    resized = img11.resize((900,500))
    new_pic = ImageTk.PhotoImage (resized)

    lbl11 = Label(Home, image = new_pic)
    lbl11.pack(pady = 10)
    Home.mainloop()
    

# ==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()
# ==============================FRAMES=========================================
Top = Frame(root, bd=5, relief=RAISED)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=300, bd=5, relief=RIDGE, bg='cadet blue')
Form.pack(side=TOP, pady=10)
f1 = Frame(root, height=100, bd=5, relief=RIDGE, bg='cadet blue')
f1.pack(pady = 20, side=TOP)
# ==============================LABELS=========================================
lbl_title = Label(Top, text="Welcome", font=('times new roman bold', 22), bg='powder blue')
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
btn_login = Button(f1, text="Login", width=15, background="green", font=('arial', 10), command=Login)
btn_exit = Button(f1, text="Exit", width=15, background="red", font=('arial', 10), command=callback)
btn_login.grid()
btn_exit.grid()
#btn_login.bind('<Return>', Login)
root.mainloop()
