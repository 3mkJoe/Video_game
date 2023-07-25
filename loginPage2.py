import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import user as fileUser
import connect

root = tk.Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

user = fileUser.user(connect.DB_URl)

img = PhotoImage(
    file="D:\\ahmad\\Programming\\GKC\\DataBase\\FinalProject\\step4\\step4\\FinalCode\\login.png"
)
Label(root, image=img, bg="white").place(x=50, y=50)


def showHide():
    password = logPassBox.get()
    if checkBoxInt.get() == 1:
        logPassBox.config(show="")
    elif checkBoxInt.get() != 1:
        if password.lower() != "password" and password.lower() != "invalid password":
            logPassBox.config(show="*")


def signInDefault():
    logNameBox.delete(0, "end")
    logPassBox.delete(0, "end")
    logPassBox.config(show="")
    logNameBox.insert(0, "Username")
    logPassBox.insert(0, "Password")


# sign in function
def signIn():
    username = logNameBox.get()
    password = logPassBox.get()
    user = fileUser.user(connect.DB_URl)

    if user.login(username, password):
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")
        ttk.Label(
            screen,
            text=f"Welcome {username}",
            background="white",
            foreground="#57a1f8",
            font=("Calibri(Body)", 25),
        ).place(x=330, y=30)
        global userBtn
        global scoreBtn
        global gameBtn
        userBtn = Button(
            screen,
            text="User Page",
            width=39,
            pady=7,
            bg="#57a1f8",
            fg="white",
            border=0,
            command=lambda: userPage(screen),
        ).place(x=330, y=100)
        userBtn = Button(
            screen,
            text="All users",
            width=39,
            pady=7,
            bg="#57a1f8",
            fg="white",
            border=0,
            command=lambda: allUsers(screen),
        ).place(x=330, y=150)
        scoreBtn = Button(
            screen,
            text="Score Page",
            width=39,
            pady=7,
            bg="#57a1f8",
            fg="white",
            border=0,
            command=lambda: scorePage(screen),
        ).place(x=330, y=200)
        gameBtn = Button(
            screen,
            text="Game Page",
            width=39,
            pady=7,
            bg="#57a1f8",
            fg="white",
            border=0,
            command=lambda: gamePage(screen),
        ).place(x=330, y=250)
        screen.mainloop()

    elif not user.login(username, password):
        signInDefault()
        logNameBox.delete(0, "end")
        logNameBox.insert(0, "Invalid username")
        logNameBox.config(fg="red")
        logPassBox.config(show="")
        logPassBox.delete(0, "end")
        logPassBox.insert(0, "Invalid password")
        logPassBox.config(fg="red")


# login page frame
frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)


# sign in heading
heading = Label(
    frame,
    text="Sign in",
    fg="#57a1f8",
    bg="white",
    font=("Microsoft YaHei UI Light", 23, "bold"),
)
heading.place(x=100, y=5)


# username hide when entry is selected
def onEnterLogName(e):
    name = logNameBox.get()
    if name.lower() == "username" or name.lower() == "invalid username":
        logNameBox.delete(0, "end")
        logNameBox.config(fg="black")


# username show if the entry is empty
def onLeaveLogName(e):
    name = logNameBox.get()
    if name == "":
        logNameBox.insert(0, "Username")


logNameBox = Entry(
    frame,
    width=25,
    fg="black",
    border=0,
    bg="white",
    font=("Microsoft YaHei UI Light", 11),
)
logNameBox.place(x=30, y=80)
logNameBox.insert(0, "Username")
logNameBox.bind("<FocusIn>", onEnterLogName)
logNameBox.bind("<FocusOut>", onLeaveLogName)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)


# password hide when entry is selected
def onEnterLogPass(e):
    name = logPassBox.get()
    if name == "Password" or name.lower() == "invalid password":
        logPassBox.delete(0, "end")
        logPassBox.config(fg="black")
        logPassBox.config(show="*")


# password show if the entry is empty
def onLeaveLogPass(e):
    name = logPassBox.get()
    if name == "":
        logPassBox.config(show="")
        logPassBox.insert(0, "Password")


logPassBox = Entry(
    frame,
    width=25,
    fg="black",
    border=0,
    bg="white",
    font=("Microsoft YaHei UI Light", 11),
)
logPassBox.place(x=30, y=150)
logPassBox.insert(0, "Password")
logPassBox.bind("<FocusIn>", onEnterLogPass)
logPassBox.bind("<FocusOut>", onLeaveLogPass)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

checkBoxInt = IntVar(value=0)

loginCheckBox = ttk.Checkbutton(
    frame,
    variable=checkBoxInt,
    onvalue=1,
    offvalue=0,
    command=showHide,
).place(x=300, y=150)

# sign in button
Button(
    frame,
    width=41,
    pady=7,
    text="Sign in",
    bg="#57a1f8",
    fg="white",
    border=0,
    command=signIn,
).place(x=27, y=204)

label = Label(
    frame,
    text="Don't have an acount",
    fg="black",
    bg="white",
    font=("Microsoft YaHei UI Light", 9),
)
label.place(x=75, y=270)


# sign up function


def signup():
    # register Screen
    regScreen = Toplevel(root)
    regScreen.title("Register")
    regScreen.geometry("925x500+300+200")
    regScreen.config(bg="white")
    regScreen.resizable(False, False)

    def destroy():
        regScreen.destroy()

    def signUpDefault():
        regNameBox.delete(0, "end")
        regFullNameBox.delete(0, "end")
        regPassBox.delete(0, "end")
        regConfirm.delete(0, "end")
        checkBoxInt.get() == 0
        regPassBox.config(show="")
        regConfirm.config(show="")
        regNameBox.insert(0, "Username")
        regFullNameBox.insert(0, "Fullname")
        regPassBox.insert(0, "Password")
        regNameBox.config(fg="black")
        regFullNameBox.config(fg="black")
        regPassBox.config(fg="black")
        regConfirm.config(fg="black")
        regConfirm.insert(0, "Confirm Password")

    def register():
        username = regNameBox.get()
        fullname = regFullNameBox.get()
        password = regPassBox.get()
        confirmPassword = regConfirm.get()
        if password == confirmPassword:
            if (
                username.lower() != "username"
                and username.lower() != "inavlid username"
                and username.lower() != ""
            ):
                if (
                    fullname.lower() != "fullname"
                    and fullname.lower() != "invalid fullname"
                    and fullname.lower() != ""
                ):
                    if (
                        password.lower() != "password"
                        and password.lower() != "invalid password"
                        and password.lower() != ""
                    ):
                        if (
                            confirmPassword.lower() != " confirm password"
                            and confirmPassword.lower() != " invalid password"
                            and confirmPassword.lower() != ""
                            and confirmPassword.lower() != "password"
                        ):
                            if user.register(username, fullname, password):
                                messagebox.showinfo("Signup", "Sucessfully sign up")
                                regScreen.destroy()
                            else:
                                signUpDefault()
                                signUpHeading.config(text="User already exists")
                                signUpHeading.config(foreground="red")
                                signUpHeading.place(x=50, y=80)

                        else:
                            regConfirm.config(show="")
                            regConfirm.delete(0, "end")
                            regConfirm.insert(0, "Invalid password")
                            regConfirm.config(fg="red")
                            regPassBox.config(show="")
                            regPassBox.delete(0, "end")
                            regPassBox.insert(0, "Invalid password")
                            regPassBox.config(fg="red")
                    else:
                        regPassBox.config(show="")
                        regPassBox.delete(0, "end")
                        regPassBox.insert(0, "Invalid password")
                        regPassBox.config(fg="red")
                        regConfirm.config(show="")
                        regConfirm.delete(0, "end")
                        regConfirm.insert(0, "Invalid password")
                        regConfirm.config(fg="red")
                else:
                    regFullNameBox.delete(0, "end")
                    regFullNameBox.insert(0, "Invalid fullname")
                    regFullNameBox.config(fg="red")
            else:
                # messagebox.showerror("Invalid", "")
                regNameBox.delete(0, "end")
                regNameBox.insert(0, "Invalid username")
                regNameBox.config(fg="red")

        else:
            # messagebox.showerror("Invalid", "Both Password must match")
            regPassBox.config(show="")
            regPassBox.delete(0, "end")
            regPassBox.insert(0, "Invalid password")
            regPassBox.config(fg="red")
            regConfirm.config(show="")
            regConfirm.delete(0, "end")
            regConfirm.insert(0, "Invalid password")
            regConfirm.config(fg="red")

    # show and hide password
    def showHideReg():
        password = regPassBox.get()
        confirmPassword = regConfirm.get()
        if checkBoxInt.get() == 1:
            regConfirm.config(show="")
            regPassBox.config(show="")
        elif checkBoxInt.get() != 1:
            if (
                password.lower() != "password"
                and password.lower() != "invalid password"
            ):
                regPassBox.config(show="*")
                if (
                    confirmPassword.lower() != "confirm password"
                    and confirmPassword.lower() != "invalid password"
                ):
                    regConfirm.config(show="*")

    def onEnterRegNameBox(e):
        name = regNameBox.get()
        if name.lower() == "username" or name.lower() == "invalid username":
            regNameBox.delete(0, "end")
            regNameBox.config(fg="black")
            signUpHeading.config(text="Sign up")
            signUpHeading.config(foreground="#57a1f8")
            signUpHeading.place(x=140, y=80)

    def onLeaveRegNameBox(e):
        name = regNameBox.get()
        if name == "":
            regNameBox.insert(0, "Username")

    def onEnterRegFullNameBox(e):
        name = regFullNameBox.get()
        if name.lower() == "fullname" or name.lower() == "invalid fullname":
            regFullNameBox.delete(0, "end")
            regFullNameBox.config(fg="black")
            signUpHeading.config(text="Sign up")
            signUpHeading.config(foreground="#57a1f8")
            signUpHeading.place(x=140, y=80)

    def onLeaveRegFullNameBox(e):
        name = regFullNameBox.get()
        if name == "":
            regFullNameBox.insert(0, "Fullname")

    def onEnterRegPassBox(e):
        name = regPassBox.get()
        if name == "Password" or name.lower() == "invalid password":
            regPassBox.delete(0, "end")
            regPassBox.config(fg="black")
            regPassBox.config(show="*")
            signUpHeading.config(text="Sign up")
            signUpHeading.config(foreground="#57a1f8")
            signUpHeading.place(x=140, y=80)

    def onLeaveRegPassBox(e):
        name = regPassBox.get()
        if name == "":
            regPassBox.config(show="")
            regPassBox.insert(0, "Password")

    def onEnterRegConfPassBox(e):
        # regConfirm.delete(0, "end")
        name = regConfirm.get()
        if name == "Confirm Password" or name.lower() == "invalid password":
            regConfirm.delete(0, "end")
            regConfirm.config(fg="black")
            regConfirm.config(show="*")
            signUpHeading.config(text="Sign up")
            signUpHeading.config(foreground="#57a1f8")
            signUpHeading.place(x=140, y=80)

    def onLeaveRegConfPassBox(e):
        name = regConfirm.get()
        if name == "":
            regConfirm.config(show="")
            regConfirm.insert(0, "Confirm Password")

    # heading (sign up)
    signUpHeading = ttk.Label(
        regScreen,
        text="Sign up",
        background="white",
        foreground="#57a1f8",
        font=("Microsoft YaHei UI Light", 23, "bold"),
    )
    signUpHeading.place(x=140, y=80)

    # username box
    regNameBox = Entry(
        regScreen,
        width=25,
        fg="black",
        border=0,
        bg="white",
        font=("Microsoft YaHei UI Light", 11),
    )
    regNameBox.place(x=50, y=155)
    regNameBox.insert(0, "Username")
    regNameBox.bind("<FocusIn>", onEnterRegNameBox)
    regNameBox.bind("<FocusOut>", onLeaveRegNameBox)
    Frame(regScreen, width=295, height=2, bg="black").place(x=50, y=182)

    # fullname box
    regFullNameBox = Entry(
        regScreen,
        width=25,
        fg="black",
        border=0,
        bg="white",
        font=("Microsoft YaHei UI Light", 11),
    )
    regFullNameBox.place(x=50, y=225)
    regFullNameBox.insert(0, "Fullname")
    regFullNameBox.bind("<FocusIn>", onEnterRegFullNameBox)
    regFullNameBox.bind("<FocusOut>", onLeaveRegFullNameBox)
    Frame(regScreen, width=295, height=2, bg="black").place(x=50, y=252)

    # password box
    regPassBox = Entry(
        regScreen,
        width=25,
        fg="black",
        border=0,
        bg="white",
        font=("Microsoft YaHei UI Light", 11),
    )
    regPassBox.place(x=50, y=295)
    regPassBox.insert(0, "Password")
    regPassBox.bind("<FocusIn>", onEnterRegPassBox)
    regPassBox.bind("<FocusOut>", onLeaveRegPassBox)
    Frame(regScreen, width=295, height=2, bg="black").place(x=50, y=322)

    # confirm password box
    regConfirm = Entry(
        regScreen,
        width=25,
        foreground="black",
        border=0,
        background="white",
        font=("Microsoft YaHei UI Light", 11),
    )
    regConfirm.place(x=50, y=365)
    regConfirm.insert(0, "Confirm Password")
    regConfirm.bind("<FocusIn>", onEnterRegConfPassBox)
    regConfirm.bind("<FocusOut>", onLeaveRegConfPassBox)
    Frame(regScreen, width=295, height=2, bg="black").place(x=50, y=392)

    # sign up button
    Button(
        regScreen,
        width=41,
        pady=7,
        text="Sign up",
        bg="#57a1f8",
        fg="white",
        border=0,
        command=register,
    ).place(x=51, y=420)

    # back button
    backBtn = Button(
        regScreen,
        width=6,
        text="⬅",
        font=50,
        border=0,
        bg="white",
        cursor="hand2",
        fg="#57a1f8",
        command=destroy,
    )
    backBtn.place(x=-10, y=0)

    registerCheckBox = ttk.Checkbutton(
        regScreen,
        variable=checkBoxInt,
        onvalue=1,
        offvalue=0,
        command=showHideReg,
    ).place(x=320, y=295)
    ttk.Label(regScreen, image=img, background="white").place(x=450, y=50)

    regScreen.mainloop()


# sign up button
signUp = Button(
    frame,
    width=6,
    text="Sign up",
    border=0,
    bg="white",
    cursor="hand2",
    fg="#57a1f8",
    command=signup,
)
signUp.place(x=215, y=270)


# function to show, edit and delete user data
def userPage(screen):
    user = fileUser.user(connect.DB_URl)

    def userDelete():
        user = fileUser.user(connect.DB_URl)
        user.deleteUser(int(userPage.focus()))
        screen.destroy()

    def destroy():
        # findUser.destroy()
        # findBtn.destroy()
        # frameSearch.destroy()
        userPage.destroy()
        backBtn.destroy()
        deleteBtn.destroy()
        editBtn.destroy()
        # newData.destroy()
        # frame1.destroy()
        # frame2.destroy()
        # dataType.destroy()
        # searchBtn.destroy()

    def editUser():
        user = fileUser.user(connect.DB_URl)

        def onEnter(e):
            name = newData.get()
            if name == "Column value":
                newData.delete(0, "end")

        def onLeave(e):
            name = newData.get()
            if name == "":
                newData.insert(0, "Column value")

        global newData
        newData = Entry(
            screen,
            width=25,
            fg="black",
            border=0,
            bg="white",
            font=("Microsoft YaHei UI Light", 11),
        )
        newData.place(x=30, y=100)
        newData.insert(0, "Column value")
        newData.bind("<FocusIn>", onEnter)
        newData.bind("<FocusOut>", onLeave)

        # line
        global frame1
        frame1 = Frame(screen, width=200, height=2, background="black")
        frame1.place(x=25, y=130)

        def onEnterDataType(e):
            name = dataType.get()
            if name == "Column":
                dataType.delete(0, "end")

        def onLeaveDataType(e):
            name = dataType.get()
            if name == "":
                dataType.insert(0, "Column")

        global dataType
        dataType = Entry(
            screen,
            width=25,
            fg="black",
            border=0,
            bg="white",
            font=("Microsoft YaHei UI Light", 11),
        )
        dataType.place(x=30, y=150)
        dataType.insert(0, "Column")
        dataType.bind("<FocusIn>", onEnterDataType)
        dataType.bind("<FocusOut>", onLeaveDataType)
        global frame2
        frame2 = Frame(screen, width=200, height=2, background="black")
        frame2.place(x=25, y=180)

        def updateUser():
            user = fileUser.user(connect.DB_URl)
            newDataSelect = newData.get()
            dataTypeSelect = dataType.get()
            user.updateUserTableElement(
                int(userPage.focus()), newDataSelect, dataTypeSelect
            )
            if dataType.get() == "password":
                logPassBox.delete(0, "end")
                logPassBox.insert(0, newData.get())
                allUsers = user.getUser(logNameBox.get(), logPassBox.get())
                for user in allUsers:
                    userPage.insert(parent="", index="end", values=list(user))
            elif dataType.get() == "username":
                logNameBox.delete(0, "end")
                logNameBox.insert(0, newData.get())
                allUsers = user.getUser(logNameBox.get(), logPassBox.get())
                for user in allUsers:
                    userPage.insert(parent="", index="end", values=list(user))
            else:
                allUsers = user.getUser(logNameBox.get(), logPassBox.get())
                for user in allUsers:
                    userPage.insert(parent="", index="end", values=list(user))

        global searchBtn
        searchBtn = Button(
            screen,
            width=7,
            pady=0.5,
            text="Confirm",
            bg="#57a1f8",
            fg="white",
            border=0,
            command=updateUser,
        )
        searchBtn.place(x=168, y=100)

    # user
    screen.title("User page")
    screen.geometry("925x500+300+200")

    userPage = ttk.Treeview(screen)
    userPage.place(x=300, y=100)
    userdata = user.meta.tables["user"].c.keys()
    userPage["columns"] = userdata
    userPage.column("#0", width=0, stretch=tk.NO)
    userPage.heading("#0", text="")

    for col in userdata:
        userPage.column(col, width=80, stretch=tk.NO)
        userPage.heading(col, text=col)

    allUsers = user.getUser(logNameBox.get(), logPassBox.get())

    for user in allUsers:
        userPage.insert(parent="", index="end", iid=user[0], values=list(user))

    deleteBtn = tk.Button(
        screen,
        text="Delete",
        width=20,
        pady=7,
        bg="#57a1f8",
        fg="white",
        border=0,
        command=userDelete,
    )
    deleteBtn.place(x=315, y=340)

    editBtn = tk.Button(
        screen,
        text="Edit",
        width=20,
        pady=7,
        bg="#57a1f8",
        fg="white",
        border=0,
        command=editUser,
    )
    editBtn.place(x=465, y=340)

    backBtn = tk.Button(
        screen,
        text="Back",
        width=41,
        pady=7,
        bg="#57a1f8",
        fg="white",
        border=0,
        command=destroy,
    )
    backBtn.place(x=318, y=380)


# function to show, edit, delete and find users
def allUsers(screen):
    user = fileUser.user(connect.DB_URl)
    userPageAllPage = tk.ttk.Treeview(screen)
    userPageAllPage.place(x=300, y=100)
    userdata = user.meta.tables["user"].c.keys()
    userPageAllPage["columns"] = userdata

    userPageAllPage.column("#0", width=0, stretch=tk.NO)
    userPageAllPage.heading("#0", text="")

    def userDelete():
        user = fileUser.user(connect.DB_URl)
        user.deleteUser(int(userPageAllPage.focus()))

    def destroy():
        findUserAllPage.destroy()
        findBtnAllPage.destroy()
        frameSearchAllPage.destroy()
        userPageAllPage.destroy()
        backBtn.destroy()
        deleteBtn.destroy()
        editBtn.destroy()
        # newDataAllPage.destroy()
        # frame1AllPage.destroy()
        # frame2AllPage.destroy()
        # dataTypeAllPage.destroy()
        # searchBtnAllPage.destroy()

    def editUser():
        user = fileUser.user(connect.DB_URl)

        def onEnter(e):
            name = newDataAllPage.get()
            if name == "Column value":
                newDataAllPage.delete(0, "end")

        def onLeave(e):
            name = newDataAllPage.get()
            if name == "":
                newDataAllPage.insert(0, "Column value")

        global newDataAllPage
        newDataAllPage = Entry(
            screen,
            width=25,
            fg="black",
            border=0,
            bg="white",
            font=("Microsoft YaHei UI Light", 11),
        )
        newDataAllPage.place(x=30, y=100)
        newDataAllPage.insert(0, "Column value")
        newDataAllPage.bind("<FocusIn>", onEnter)
        newDataAllPage.bind("<FocusOut>", onLeave)
        global frame1AllPage
        frame1AllPage = Frame(screen, width=200, height=2, background="black")
        frame1AllPage.place(x=25, y=130)

        def onEnterDataType(e):
            name = dataTypeAllPage.get()
            if name == "Column":
                dataTypeAllPage.delete(0, "end")

        def onLeaveDataType(e):
            name = dataTypeAllPage.get()
            if name == "":
                dataTypeAllPage.insert(0, "Column")

        global dataTypeAllPage
        dataTypeAllPage = Entry(
            screen,
            width=25,
            fg="black",
            border=0,
            bg="white",
            font=("Microsoft YaHei UI Light", 11),
        )
        dataTypeAllPage.place(x=30, y=150)
        dataTypeAllPage.insert(0, "Column")
        dataTypeAllPage.bind("<FocusIn>", onEnterDataType)
        dataTypeAllPage.bind("<FocusOut>", onLeaveDataType)
        global frame2AllPage
        frame2AllPage = Frame(screen, width=200, height=2, background="black")
        frame2AllPage.place(x=25, y=180)

        def updateUser():
            user = fileUser.user(connect.DB_URl)
            allUsers = user.getAllUsers()
            newDataAllPageSelect = newDataAllPage.get()
            dataTypeSelect = dataTypeAllPage.get()

            user.updateUserTableElement(
                int(userPageAllPage.focus()), newDataAllPageSelect, dataTypeSelect
            )

        global searchBtnAllPage
        searchBtnAllPage = Button(
            screen,
            width=7,
            pady=0.5,
            text="Confirm",
            bg="#57a1f8",
            fg="white",
            border=0,
            command=updateUser,
        )
        searchBtnAllPage.place(x=168, y=100)

    screen.title("User page")
    screen.geometry("925x500+300+200")

    for col in userdata:
        userPageAllPage.column(col, width=80, stretch=tk.NO)
        userPageAllPage.heading(col, text=col)

    allUsers = user.getAllUsers()

    for user in allUsers:
        userPageAllPage.insert(parent="", index="end", iid=user[0], values=list(user))

    deleteBtn = tk.Button(
        screen,
        text="Delete",
        width=20,
        pady=7,
        bg="#57a1f8",
        fg="white",
        border=0,
        command=userDelete,
    )
    deleteBtn.place(x=315, y=340)

    editBtn = tk.Button(
        screen,
        text="Edit",
        width=20,
        pady=7,
        bg="#57a1f8",
        fg="white",
        border=0,
        command=editUser,
    )
    editBtn.place(x=465, y=340)

    backBtn = tk.Button(
        screen,
        text="Back",
        width=41,
        pady=7,
        bg="#57a1f8",
        fg="white",
        border=0,
        command=destroy,
    )
    backBtn.place(x=318, y=380)

    def find():
        user = fileUser.user(connect.DB_URl)
        for item in userPageAllPage.get_children():
            userPageAllPage.delete(item)
        for user in user.findUser(findUserAllPage.get()):
            userPageAllPage.insert(parent="", index="end", values=list(user))

    def onEnterFind(e):
        name = findUserAllPage.get()
        if name == "Username":
            findUserAllPage.delete(0, "end")

    def onLeaveFind(e):
        name = findUserAllPage.get()
        if name == "":
            findUserAllPage.insert(0, "Usename")

    findUserAllPage = Entry(
        screen,
        width=25,
        fg="black",
        border=0,
        bg="white",
        font=("Microsoft YaHei UI Light", 11),
    )
    findUserAllPage.place(x=30, y=100)
    findUserAllPage.insert(0, "Username")
    findUserAllPage.bind("<FocusIn>", onEnterFind)
    findUserAllPage.bind("<FocusOut>", onLeaveFind)

    findBtnAllPage = Button(
        screen,
        width=7,
        pady=0.5,
        text="Search",
        bg="#57a1f8",
        fg="white",
        border=0,
        command=find,
    )
    findBtnAllPage.place(x=168, y=100)
    frameSearchAllPage = Frame(screen, width=200, height=2, background="black")
    frameSearchAllPage.place(x=25, y=130)


# score page links the users with there scores
def scorePage(screen):
    def onEnter(e):
        name = userIDBox.get()
        if name == "userID":
            userIDBox.delete(0, "end")

    def onLeave(e):
        name = userIDBox.get()
        if name == "":
            userIDBox.insert(0, "userID")

    userIDBox = Entry(
        screen,
        width=25,
        fg="black",
        border=0,
        bg="white",
        font=("Microsoft YaHei UI Light", 11),
    )
    userIDBox.place(x=30, y=100)
    userIDBox.insert(0, "userID")
    userIDBox.bind("<FocusIn>", onEnter)
    userIDBox.bind("<FocusOut>", onLeave)
    frame = Frame(screen, width=200, height=2, background="black")
    frame.place(x=25, y=130)

    def scoreTable():
        user = fileUser.user(connect.DB_URl)
        name = int(userIDBox.get())

        allUsers = user.userScoreData(name)

        def destroy():
            scorePage.destroy()
            backBtn.destroy()
            searchBtn.destroy()
            userIDBox.destroy()
            frame.destroy()

        screen.title("User page")
        screen.geometry("925x500+300+200")

        scorePage = ttk.Treeview(screen)
        scorePage.place(x=300, y=100)

        userdata = ["Username", "Score number"]
        scorePage["columns"] = userdata

        scorePage.column("#0", width=0, stretch=tk.NO)
        scorePage.heading("#0", text="")

        for col in userdata:
            scorePage.column(col, width=160, stretch=tk.NO)
            scorePage.heading(col, text=col)

        for user in allUsers:
            scorePage.insert(parent="", index="end", values=list(user))

        backBtn = tk.Button(
            screen,
            text="Back",
            width=39,
            pady=7,
            bg="#57a1f8",
            fg="white",
            border=0,
            command=destroy,
        )
        backBtn.place(x=320, y=340)

    searchBtn = Button(
        screen,
        width=7,
        pady=0.5,
        text="Search",
        bg="#57a1f8",
        fg="white",
        border=0,
        command=scoreTable,
    )
    searchBtn.place(x=168, y=100)


# game page links the game with the users
def gamePage(screen):
    def onEnter(e):
        name = userIDBox.get()
        if name == "userID":
            userIDBox.delete(0, "end")

    def onLeave(e):
        name = userIDBox.get()
        if name == "":
            userIDBox.insert(0, "userID")

    userIDBox = Entry(
        screen,
        width=25,
        fg="black",
        border=0,
        bg="white",
        font=("Microsoft YaHei UI Light", 11),
    )
    userIDBox.place(x=30, y=100)
    userIDBox.insert(0, "userID")
    userIDBox.bind("<FocusIn>", onEnter)
    userIDBox.bind("<FocusOut>", onLeave)
    frame = Frame(screen, width=200, height=2, background="black")
    frame.place(x=25, y=130)

    def gameTable():
        user = fileUser.user(connect.DB_URl)
        name = int(userIDBox.get())

        allUsers = user.userGameData(name)

        def destroy():
            gamePage.destroy()
            backBtn.destroy()
            searchBtn.destroy()
            userIDBox.destroy()
            frame.destroy()

        screen.title("User page")
        screen.geometry("925x500+300+200")

        gamePage = ttk.Treeview(screen)
        gamePage.place(x=300, y=100)

        userdata = ["Username", "Game name"]
        gamePage["columns"] = userdata

        gamePage.column("#0", width=0, stretch=tk.NO)
        gamePage.heading("#0", text="")

        for col in userdata:
            gamePage.column(col, width=160, stretch=tk.NO)
            gamePage.heading(col, text=col)

        for user in allUsers:
            gamePage.insert(parent="", index="end", values=list(user))

        backBtn = tk.Button(
            screen,
            text="Back",
            width=39,
            pady=7,
            bg="#57a1f8",
            fg="white",
            border=0,
            command=destroy,
        )
        backBtn.place(x=320, y=340)

    searchBtn = Button(
        screen,
        width=7,
        pady=0.5,
        text="Search",
        bg="#57a1f8",
        fg="white",
        border=0,
        command=gameTable,
    )
    searchBtn.place(x=168, y=100)


root.mainloop()
