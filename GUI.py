import tkinter as tk
from tkinter import filedialog, messagebox, IntVar, ttk
from tkmacosx import Button # Only for macOS users
import cv2


# Importing the 
from database import Database


# Fonts
TITLE_FONT = ("Impact", 140, "bold")
TITLE_FONT_2 = ("Fixedsys", 80, "bold")
SUBTITLE_FONT = ("Fixedsys", 24, "bold")
SUBTITLE_FONT_2 = ("Fixedsys", 40, "bold")
BODY_FONT = ("Verdana", 14)
BODY_FONT2 = ("Verdana", 20)


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
        for i in (Login, Registration, MainMenu, Visualize, Quiz, Assignments, Leaderboard, Help):
            frame = i(screen, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Login)


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
        self.title = tk.Label(self, text="MatrixMate", fg="#ffaa00", font=TITLE_FONT)
        self.title.place(anchor="center", relx=0.5, rely=0.11)
        # label explaining the app
        app_info = tk.Label(self, text="An app to test your linear algebra knowledge with questions,\n"
                                          "class leaderboard and also matrix visualisation.",
                               fg="#ffaa00", font=BODY_FONT2)
        app_info.place(anchor="center", relx=0.5, rely=0.25)
        # login screen label
        self.logintitle = tk.Label(self, text="Login to save your scores", fg="#ffaa00", font=SUBTITLE_FONT_2)
        self.logintitle.place(anchor="center", relx=0.5, rely=0.35)
        # Username label
        self.usernamelabel = tk.Label(self, text="Username:", fg="#ffaa00", font=SUBTITLE_FONT)
        self.usernamelabel.place(anchor="center", relx=0.35, rely=0.45)
        # Password label
        self.passwordlabel = tk.Label(self, text="Password:", fg="#ffaa00", font=SUBTITLE_FONT)
        self.passwordlabel.place(anchor="center", relx=0.35, rely=0.55)
        # Entry square to type in username
        self.usernameentry = tk.Entry(self, font=SUBTITLE_FONT, justify="center", textvariable=self.username)
        self.usernameentry.place(anchor="center", relx=0.54, rely=0.45, relwidth=0.29, relheight=0.07)
        # Entry square to type in password
        passwordentry = tk.Entry(self, font=SUBTITLE_FONT, justify="center", show="*", textvariable=self.password)
        passwordentry.place(anchor="center", relx=0.54, rely=0.55, relwidth=0.29, relheight=0.07)
        # Button for user to register if they dont have an account
        registerbutton = Button(self, text="Register", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                   command=lambda: controller.show_frame(Registration))
        registerbutton.place(anchor="center", relx=0.4, rely=0.65, relwidth=0.19, relheight=0.1)
        # Button to login after credentials are inputted
        loginbutton = Button(self, text="Login", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: [DB.find_user(self.username.get(), self.password.get(), 'user'),
                                                 controller.show_frame(MainMenu)
                                                 if DB.success_check()
                                                 else controller.show_frame(Login)])
        loginbutton.place(anchor="center", relx=0.6, rely=0.65, relwidth=0.19, relheight=0.1)
        # text explaining when to login and when to continue as guest
        explanation = tk.Label(self, text="register to create an account allowing you to compete on the leaderboards\n"
                                          "press below to continue as a guest, your scores will not be saved.",
                               fg="#ffaa00", font=BODY_FONT)
        explanation.place(anchor="center", relx=0.5, rely=0.75)
        # Button to coninue as a guest
        guestbutton = Button(self, text="Continue as a Guest", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
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
        self.title = tk.Label(self, text="MatrixMate", fg="#ffaa00", font=TITLE_FONT)
        self.title.place(anchor="center", relx=0.5, rely=0.11)
        # registration screen title
        self.registertitle = tk.Label(self, text="Account Registration Form", fg="#ffaa00", font=SUBTITLE_FONT_2)
        self.registertitle.place(anchor="center", relx=0.5, rely=0.25)
        # Username label text
        self.usernamelabel = tk.Label(self, text="Username:", fg="#ffaa00", font=SUBTITLE_FONT)
        self.usernamelabel.place(anchor="center", relx=0.35, rely=0.45)
        # password label text
        self.passwordlabel = tk.Label(self, text="Password:", fg="#ffaa00", font=SUBTITLE_FONT)
        self.passwordlabel.place(anchor="center", relx=0.35, rely=0.55)
        # re-enter password level text
        self.password2label = tk.Label(self, text="re-enter\nPassword:", fg="#ffaa00", font=SUBTITLE_FONT)
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
        self.backbutton = Button(self, text="Back", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                    command=lambda: controller.show_frame(Login))
        self.backbutton.place(anchor="center", relx=0.4, rely=0.75, relwidth=0.19, relheight=0.1)
        # Label for the role selection
        role_label = tk.Label(self, text="I am a:", fg="#ffaa00", font=SUBTITLE_FONT)
        role_label.place(anchor="center", relx=0.365, rely=0.35)

        self.user_type = ""

        # create the buttons
        self.student_button = Button(self, text='Student', font=SUBTITLE_FONT, bg='#1f1f1f', fg='#ffaa00', activebackground='#1f1f1f', command=self.on_student_button_clicked)
        self.student_button.place(relx=0.467, rely=0.35, anchor='center', relheight=0.07, relwidth=0.14)
        self.teacher_button = Button(self, text='Teacher', font=SUBTITLE_FONT, bg='#1f1f1f', fg='#ffaa00', activebackground='#1f1f1f', command=self.on_teacher_button_clicked)
        self.teacher_button.place(relx=0.613, rely=0.35, anchor='center', relheight=0.07, relwidth=0.14)

        # Button to register after credentials are typed in
        self.registerbutton = Button(self, text="Register", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                        command=lambda: [DB.register_user(self.username.get(), self.password.get(),
                                                                          self.password2.get(), self.user_type),
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
    
    def on_student_button_clicked(self):
        self.student_button.configure(bg='#ffaa00', fg='white')
        self.teacher_button.configure(bg='#1f1f1f', fg='#ffaa00')
        self.user_type = "student"


    def on_teacher_button_clicked(self):
        self.teacher_button.configure(bg='#ffaa00', fg='white')
        self.student_button.configure(bg='#1f1f1f', fg='#ffaa00')
        self.user_type = "teacher"

# class for the main menu page of the UI
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        # inherits from parent class (BlurringTool) to allow for frames to be brought to front of users screen
        tk.Frame.__init__(self, parent)

        self.logout = Button(self, text="Log Out", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                           command=lambda: [DB.logout(), controller.show_frame(Login)])
        self.logout.place(anchor="center", relx=0.91, rely=0.06, relwidth=0.15, relheight=0.08)

        self.help = Button(self, text="Help", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                           command=lambda: [DB.logout(), controller.show_frame(Help)])
        self.help.place(anchor="center", relx=0.75, rely=0.06, relwidth=0.15, relheight=0.08)

        # section to place all Tkinter objects onto the main menu frame
        self.title = tk.Label(self, text="MatrixMate", fg="#ffaa00", font=TITLE_FONT)
        self.title.place(anchor="center", relx=0.5, rely=0.22)

        self.quiz_button = Button(self, text="Quiz Time", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: controller.show_frame(Quiz))

        self.quiz_button.place(anchor="center", relx=0.5, rely=0.42, relwidth=0.25, relheight=0.12)

        self.vis_button = Button(self, text="Visualize Matricies", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: controller.show_frame(Visualize))

        self.vis_button.place(anchor="center", relx=0.5, rely=0.57, relwidth=0.25, relheight=0.12)

        self.asign_button = Button(self, text="Assignments", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: controller.show_frame(Assignments))

        self.asign_button.place(anchor="center", relx=0.5, rely=0.72, relwidth=0.25, relheight=0.12)

        self.lboard_button = Button(self, text="Leaderboard", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: controller.show_frame(Leaderboard))

        self.lboard_button.place(anchor="center", relx=0.5, rely=0.87, relwidth=0.25, relheight=0.12)


class Visualize(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # create 3x3 matrix of input boxes
        self.input_boxes = []
        for i in range(3):
            row = []
            for j in range(3):
                box = tk.Entry(self, width=3)
                box.place(relx=0.35+0.04*i, rely=0.12+0.04*j, anchor="center")
                row.append(box)
            self.input_boxes.append(row)
        

        self.vis_button = Button(self, text="Visualize", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=self.play_video)
        self.vis_button.place(anchor="center", relx=0.5, rely=0.3, relwidth=0.15, relheight=0.07)

        self.back_button = Button(self, text="Back To Menu", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: controller.show_frame(MainMenu))
        self.back_button.place(anchor="center", relx=0.91, rely=0.06, relwidth=0.15, relheight=0.08)



        self.canvas = tk.Canvas(self, width=880, height=495)
        self.canvas.place(anchor="center", relx=0.5, rely=0.67)
        
    def play_video(self):
        # open video file
        cap = cv2.VideoCapture('test_video.mp4')
        
        # read first frame
        ret, frame = cap.read()
        
        # loop through frames and display them in the canvas
        while ret:
            # convert OpenCV BGR format to RGB format for display in Tkinter
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # resize frame to fit canvas
            frame = cv2.resize(frame, (880, 495))
            # convert frame to PhotoImage for display in Tkinter
            img = self.cv2_to_photoimage(frame)
            
            # display frame in canvas
            self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
            self.canvas.update()
            
            # read next frame
            ret, frame = cap.read()


        
        # release video file
        cap.release()
        
    def cv2_to_photoimage(self, cv2_image):
        """Converts an OpenCV image to a Tkinter PhotoImage."""
        return tk.PhotoImage(data=cv2.imencode('.png', cv2_image)[1].tobytes())
    
class Leaderboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.title_label = tk.Label(self, text="Leaderboard", font=TITLE_FONT, fg="#ffaa00")
        self.title_label.place(anchor="center", relx=0.5, rely=0.1)

        self.rank_label = tk.Label(self, text="RANK", font=SUBTITLE_FONT_2, fg="#ffaa00")
        self.rank_label.place(anchor="center", relx=0.3, rely=0.25)
        self.player_label = tk.Label(self, text="PLAYER", font=SUBTITLE_FONT_2, fg="#ffaa00")
        self.player_label.place(anchor="center", relx=0.5, rely=0.25)
        self.score_label = tk.Label(self, text="SCORE", font=SUBTITLE_FONT_2,  fg="#ffaa00")
        self.score_label.place(anchor="center", relx=0.7, rely=0.25)

        self.back_button = Button(self, text="Back To Menu", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: controller.show_frame(MainMenu))
        self.back_button.place(anchor="center", relx=0.91, rely=0.06, relwidth=0.15, relheight=0.08)

        self.update_score_button = Button(self, text="Update Scores", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=self.updateScores)
        self.update_score_button.place(anchor="center", relx=0.91, rely=0.16, relwidth=0.15, relheight=0.08)


        self.updateScores()

    def updateScores(self):
        scores = DB.get_scores()

        # Keep track of the label widgets
        labels_to_remove = []
        
        for child in self.winfo_children():
            if child not in [self.rank_label, self.player_label, self.score_label, self.back_button, self.update_score_button, self.title_label]:
                labels_to_remove.append(child)
        
        for label in labels_to_remove:
            label.destroy()

        for i in range(min(len(scores), 10)):
            username, score = scores[i]
            self.rank = tk.Label(self, text=f"{i+1}", font=SUBTITLE_FONT)
            self.rank.place(anchor="center", relx=0.3, rely=0.32 + 0.07*i)
            self.player = tk.Label(self, text=username, font=SUBTITLE_FONT)
            self.player.place(anchor="center", relx=0.5, rely=0.32 + 0.07*i)
            self.score = tk.Label(self, text=score, font=SUBTITLE_FONT)
            self.score.place(anchor="center", relx=0.7, rely=0.32 + 0.07*i)

class Assignments(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.back_button = Button(self, text="Back To Menu", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: controller.show_frame(MainMenu))
        self.back_button.place(anchor="center", relx=0.91, rely=0.06, relwidth=0.15, relheight=0.08)

class Quiz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.back_button = Button(self, text="Back To Menu", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: controller.show_frame(MainMenu))
        self.back_button.place(anchor="center", relx=0.91, rely=0.06, relwidth=0.15, relheight=0.08)

class Help(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.back_button = Button(self, text="Back To Menu", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: controller.show_frame(MainMenu))
        self.back_button.place(anchor="center", relx=0.91, rely=0.06, relwidth=0.15, relheight=0.08)



# program section to call the master class and start the program setting window size
if __name__ == "__main__":
    app = MatrixMate()
    app.geometry("1440x810")
    app.mainloop()

