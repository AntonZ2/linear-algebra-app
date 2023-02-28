import tkinter as tk
from tkinter import filedialog, messagebox, IntVar, ttk

# Importing the 
from database import Database


# Fonts
TITLE_FONT = ("Fixedsys", 100, "bold")
TITLE_FONT_2 = ("Fixedsys", 80, "bold")
SUBTITLE_FONT = ("Fixedsys", 24, "bold")
SUBTITLE_FONT_2 = ("Fixedsys", 40, "bold")
BODY_FONT = ("Verdana", 14)

# Object initialization
DB = Database()

# master class to control which screen GUI shows and file handling
class MatrixMate(tk.Tk):
    def __init__(self, *args, **kwargs):

        # calls the Tk library to use OOP for frames in GUI
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "MatrixMate")
        screen = tk.Frame(self)
        screen.pack(side="top", fill="both", expand=True)
        screen.grid_rowconfigure(0, weight=1)
        screen.grid_columnconfigure(0, weight=1)

        # dict stores the frames of the GUI
        self.frames = {}

        # loop to flip through every frame in TkInter, each child object represents a frame and every function within it
        for i in (Login, Registration, MainMenu):
            frame = i(screen, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Login)
        self.resizable(False, False)

    # function to bring selected frame to top
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.event_generate("<<ShowFrame>>")
        frame.tkraise()


# class for the login and registration page of the UI
class Login(tk.Frame):
    def __init__(self, parent, controller):
        # inherits tk.Frame characteristics to allow for frames to be brought to front of users screen
        tk.Frame.__init__(self, parent)
        # variables storing the username and password that user inputs
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # title of the program on the login screen
        self.title = tk.Label(self, text="MatrixMate", fg="#584689", font=TITLE_FONT)
        self.title.place(anchor="center", relx=0.5, rely=0.2)
        # login screen label
        self.logintitle = tk.Label(self, text="Login to save your scores", fg="#584689", font=SUBTITLE_FONT_2)
        self.logintitle.place(anchor="center", relx=0.5, rely=0.35)
        # Username label
        self.usernamelabel = tk.Label(self, text="Username:", fg="#584689", font=SUBTITLE_FONT)
        self.usernamelabel.place(anchor="center", relx=0.35, rely=0.45)
        # Password label
        self.passwordlabel = tk.Label(self, text="Password:", fg="#584689", font=SUBTITLE_FONT)
        self.passwordlabel.place(anchor="center", relx=0.35, rely=0.55)
        # Entry square to type in username
        self.usernameentry = tk.Entry(self, font=SUBTITLE_FONT, justify="center", textvariable=self.username)
        self.usernameentry.place(anchor="center", relx=0.54, rely=0.45, relwidth=0.29, relheight=0.07)
        # Entry square to type in password
        passwordentry = tk.Entry(self, font=SUBTITLE_FONT, justify="center", show="*", textvariable=self.password)
        passwordentry.place(anchor="center", relx=0.54, rely=0.55, relwidth=0.29, relheight=0.07)
        # Button for user to register if they dont have an account
        registerbutton = tk.Button(self, text="Register", fg="#584689", font=SUBTITLE_FONT,
                                   command=lambda: controller.show_frame(Registration))
        registerbutton.place(anchor="center", relx=0.4, rely=0.65, relwidth=0.19, relheight=0.1)
        # Button to login after credentials are inputted
        loginbutton = tk.Button(self, text="Login", fg="#584689", font=SUBTITLE_FONT,
                                command=lambda: [DB.find_user(self.username.get(), self.password.get(), 'user'),
                                                 controller.show_frame(MainMenu)
                                                 if DB.success_check()
                                                 else (controller.show_frame(Login))])
        loginbutton.place(anchor="center", relx=0.6, rely=0.65, relwidth=0.19, relheight=0.1)
        # text explaining when to login and when to continue as guest
        explanation = tk.Label(self, text="register to create an account allowing you to compete on the leaderboards\n"
                                          "press below to continue as a guest, your scores will not be saved.",
                               fg="#584689", font=BODY_FONT)
        explanation.place(anchor="center", relx=0.5, rely=0.75)
        # Button to coninue as a guest
        guestbutton = tk.Button(self, text="Continue as a Guest", fg="#584689", font=SUBTITLE_FONT,
                                command=lambda: [DB.find_user('', '', 'guest'), controller.show_frame(MainMenu)])
        guestbutton.place(anchor="center", relx=0.5, rely=0.85, relwidth=0.4, relheight=0.1)

# Class frame for registration screen
class Registration(tk.Frame):
    def __init__(self, parent, controller):
        # inherits tk.Frame characteristics to allow for frames to be brought to front of users screen
        tk.Frame.__init__(self, parent)
        # Variables to store username and password entries
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.password2 = tk.StringVar()
        # program title
        self.title = tk.Label(self, text="MatrixMate", fg="#584689", font=TITLE_FONT)
        self.title.place(anchor="center", relx=0.5, rely=0.2)
        # registration screen title
        self.registertitle = tk.Label(self, text="Account Registration Form", fg="#584689", font=SUBTITLE_FONT_2)
        self.registertitle.place(anchor="center", relx=0.5, rely=0.35)
        # Username label text
        self.usernamelabel = tk.Label(self, text="Username:", fg="#584689", font=SUBTITLE_FONT)
        self.usernamelabel.place(anchor="center", relx=0.35, rely=0.45)
        # password label text
        self.passwordlabel = tk.Label(self, text="Password:", fg="#584689", font=SUBTITLE_FONT)
        self.passwordlabel.place(anchor="center", relx=0.35, rely=0.55)
        # re-enter password level text
        self.password2label = tk.Label(self, text="re-enter\nPassword:", fg="#584689", font=SUBTITLE_FONT)
        self.password2label.place(anchor="center", relx=0.35, rely=0.64)
        # Username entry box
        self.usernameentry = tk.Entry(self, font=SUBTITLE_FONT, justify="center", textvariable=self.username)
        self.usernameentry.place(anchor="center", relx=0.54, rely=0.45, relwidth=0.29, relheight=0.07)
        # passwrd entry box
        self.passwordentry = tk.Entry(self, font=SUBTITLE_FONT, justify="center", show="*", textvariable=self.password)
        self.passwordentry.place(anchor="center", relx=0.54, rely=0.55, relwidth=0.29, relheight=0.07)
        # Passowrd re-enter box
        self.password2entry = tk.Entry(self, font=SUBTITLE_FONT, justify="center", show="*",
                                       textvariable=self.password2)
        self.password2entry.place(anchor="center", relx=0.54, rely=0.65, relwidth=0.29, relheight=0.07)
        # Button to go back to login screen
        self.backbutton = tk.Button(self, text="Back", fg="#584689", font=SUBTITLE_FONT,
                                    command=lambda: controller.show_frame(Login))
        self.backbutton.place(anchor="center", relx=0.4, rely=0.75, relwidth=0.19, relheight=0.1)
        # Button to register after credentials are typed in
        self.registerbutton = tk.Button(self, text="Register", fg="#584689", font=SUBTITLE_FONT,
                                        command=lambda: [DB.register_user(self.username.get(), self.password.get(),
                                                                          self.password2.get()),
                                                         self.clear_details(), controller.show_frame(Login)
                                                         if DB.success_check()
                                                         else (controller.show_frame(Registration))])
        self.registerbutton.place(anchor="center", relx=0.6, rely=0.75, relwidth=0.19, relheight=0.1)
        # explanation of all passwor parameters tat have to be met
        self.password_explained = tk.Label(self, text="Password must be at least 8 characters "
                                                      "long and should contain at least\n"
                                                      "one number, one uppercase character "
                                                      "and one lowercase character.",
                                           fg="#FF0000", font=BODY_FONT)
        self.password_explained.place(anchor="center", relx=0.5, rely=0.85)
    # method to clear typed in details if user doesnt meet requirements and has to try again
    def clear_details(self):
        self.passwordentry.delete(0, 'end')
        self.password2entry.delete(0, 'end')


# class for the main menu page of the UI
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        # inherits from parent class (BlurringTool) to allow for frames to be brought to front of users screen
        tk.Frame.__init__(self, parent)

        logout = tk.Button(self, text="Log Out", fg="#584689", font=SUBTITLE_FONT,
                           command=lambda: [DB.logout(), controller.show_frame(Login)])
        logout.place(anchor="center", relx=0.87, rely=0.05, relwidth=0.15, relheight=0.08)

        # section to place all Tkinter objects onto the main menu frame
        title = tk.Label(self, text="MatrixMate", fg="#584689", font=TITLE_FONT)
        title.place(anchor="center", relx=0.5, rely=0.2)






# program section to call the master class and start the program setting window size
if __name__ == "__main__":
    app = MatrixMate()
    app.geometry("1440x810")
    app.mainloop()

