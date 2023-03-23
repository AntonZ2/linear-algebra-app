import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkmacosx import Button # Only for macOS users
import cv2

from visualisation import MatrixCalculation, LinearEquation, LinearTransformation, LinearTransformation3D
#                         #add mult           #systems         # 2d annn
# for add and mult second parameter = addition or "multiplication", third is 2 or 3
from database import Database


# Fonts
TITLE_FONT = ("Impact", 140, "bold")
TITLE_FONT_2 = ("Fixedsys", 80, "bold")
SUBTITLE_FONT = ("Fixedsys", 24, "bold")
SUBTITLE_FONT_2 = ("Fixedsys", 40, "bold")
BODY_FONT = ("Verdana", 14)
BODY_FONT2 = ("Verdana", 20)


DB = Database()

DB.upload_question("e", 0)

class MatrixMate(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "MatrixMate")
        screen = tk.Frame(self)
        screen.pack(side="top", fill="both", expand=True)
        screen.grid_rowconfigure(0, weight=1)
        screen.grid_columnconfigure(0, weight=1)

        self.frames = {}
        

        for i in (Login, Registration, MainMenu, Visualize, Quiz, Leaderboard, Help, Questions, Finish):
            frame = i(screen, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Login)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.event_generate("<<ShowFrame>>")
        frame.tkraise()


class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.title = tk.Label(self, text="MatrixMate", fg="#ffaa00", font=TITLE_FONT)
        self.title.place(anchor="center", relx=0.5, rely=0.11)
        app_info = tk.Label(self, text="An app to test your linear algebra knowledge with questions,\n"
                                          "class leaderboard and also matrix visualisation.",
                               fg="#ffaa00", font=BODY_FONT2)
        app_info.place(anchor="center", relx=0.5, rely=0.25)
        self.logintitle = tk.Label(self, text="Login to save your scores", fg="#ffaa00", font=SUBTITLE_FONT_2)
        self.logintitle.place(anchor="center", relx=0.5, rely=0.35)
        self.usernamelabel = tk.Label(self, text="Username:", fg="#ffaa00", font=SUBTITLE_FONT)
        self.usernamelabel.place(anchor="center", relx=0.35, rely=0.45)
        self.passwordlabel = tk.Label(self, text="Password:", fg="#ffaa00", font=SUBTITLE_FONT)
        self.passwordlabel.place(anchor="center", relx=0.35, rely=0.55)
        self.usernameentry = tk.Entry(self, font=SUBTITLE_FONT, justify="center", textvariable=self.username)
        self.usernameentry.place(anchor="center", relx=0.54, rely=0.45, relwidth=0.29, relheight=0.07)
        passwordentry = tk.Entry(self, font=SUBTITLE_FONT, justify="center", show="*", textvariable=self.password)
        passwordentry.place(anchor="center", relx=0.54, rely=0.55, relwidth=0.29, relheight=0.07)
        registerbutton = Button(self, text="Register", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                   command=lambda: controller.show_frame(Registration))
        registerbutton.place(anchor="center", relx=0.4, rely=0.65, relwidth=0.19, relheight=0.1)
        loginbutton = Button(self, text="Login", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: [DB.find_user(self.username.get(), self.password.get(), 'user'),
                                                 controller.show_frame(MainMenu)
                                                 if DB.success_check()
                                                 else controller.show_frame(Login)])
        loginbutton.place(anchor="center", relx=0.6, rely=0.65, relwidth=0.19, relheight=0.1)
        explanation = tk.Label(self, text="register to create an account allowing you to compete on the leaderboards\n"
                                          "press below to continue as a guest, your scores will not be saved.",
                               fg="#ffaa00", font=BODY_FONT)
        explanation.place(anchor="center", relx=0.5, rely=0.75)
        guestbutton = Button(self, text="Continue as a Guest", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: [DB.find_user('', '', 'guest'), controller.show_frame(MainMenu)])
        guestbutton.place(anchor="center", relx=0.5, rely=0.85, relwidth=0.4, relheight=0.1)

class Registration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.password2 = tk.StringVar()
        self.title = tk.Label(self, text="MatrixMate", fg="#ffaa00", font=TITLE_FONT)
        self.title.place(anchor="center", relx=0.5, rely=0.11)
        self.registertitle = tk.Label(self, text="Account Registration Form", fg="#ffaa00", font=SUBTITLE_FONT_2)
        self.registertitle.place(anchor="center", relx=0.5, rely=0.25)
        self.usernamelabel = tk.Label(self, text="Username:", fg="#ffaa00", font=SUBTITLE_FONT)
        self.usernamelabel.place(anchor="center", relx=0.35, rely=0.35)
        self.passwordlabel = tk.Label(self, text="Password:", fg="#ffaa00", font=SUBTITLE_FONT)
        self.passwordlabel.place(anchor="center", relx=0.35, rely=0.45)
        self.password2label = tk.Label(self, text="re-enter\nPassword:", fg="#ffaa00", font=SUBTITLE_FONT)
        self.password2label.place(anchor="center", relx=0.35, rely=0.55)
        self.usernameentry = tk.Entry(self, font=SUBTITLE_FONT, justify="center", textvariable=self.username)
        self.usernameentry.place(anchor="center", relx=0.54, rely=0.35, relwidth=0.29, relheight=0.07)
        self.passwordentry = tk.Entry(self, font=SUBTITLE_FONT, justify="center", show="*", textvariable=self.password)
        self.passwordentry.place(anchor="center", relx=0.54, rely=0.45, relwidth=0.29, relheight=0.07)
        self.password2entry = tk.Entry(self, font=SUBTITLE_FONT, justify="center", show="*",
                                       textvariable=self.password2)
        self.password2entry.place(anchor="center", relx=0.54, rely=0.55, relwidth=0.29, relheight=0.07)
        self.backbutton = Button(self, text="Back", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                    command=lambda: controller.show_frame(Login))
        self.backbutton.place(anchor="center", relx=0.4, rely=0.75, relwidth=0.19, relheight=0.1)


        self.registerbutton = Button(self, text="Register", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                        command=lambda: [DB.register_user(self.username.get(), self.password.get(),
                                                                          self.password2.get()),
                                                         self.clear_details(), controller.show_frame(Login)
                                                         if DB.success_check()
                                                         else (controller.show_frame(Registration))])
        self.registerbutton.place(anchor="center", relx=0.6, rely=0.75, relwidth=0.19, relheight=0.1)
        self.password_explained = tk.Label(self, text="Password must be at least 8 characters "
                                                      "long and should contain at least\n"
                                                      "one number, one uppercase character "
                                                      "and one lowercase character.",
                                           fg="#FF0000", font=BODY_FONT)
        self.password_explained.place(anchor="center", relx=0.5, rely=0.65)

    def clear_details(self):
        self.passwordentry.delete(0, 'end')
        self.password2entry.delete(0, 'end')
    


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.logout = Button(self, text="Log Out", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                           command=lambda: [DB.logout(), controller.show_frame(Login)])
        self.logout.place(anchor="center", relx=0.91, rely=0.06, relwidth=0.15, relheight=0.08)

        self.help = Button(self, text="Help", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                           command=lambda: [DB.logout(), controller.show_frame(Help)])
        self.help.place(anchor="center", relx=0.75, rely=0.06, relwidth=0.15, relheight=0.08)

        self.title = tk.Label(self, text="MatrixMate", fg="#ffaa00", font=TITLE_FONT)
        self.title.place(anchor="center", relx=0.5, rely=0.22)

        self.quiz_button = Button(self, text="Take a Quiz", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: controller.show_frame(Quiz))

        self.quiz_button.place(anchor="center", relx=0.5, rely=0.42, relwidth=0.25, relheight=0.12)

        self.vis_button = Button(self, text="Visualize Matricies", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: controller.show_frame(Visualize))

        self.vis_button.place(anchor="center", relx=0.5, rely=0.62, relwidth=0.25, relheight=0.12)

        self.lboard_button = Button(self, text="Leaderboard", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: controller.show_frame(Leaderboard))

        self.lboard_button.place(anchor="center", relx=0.5, rely=0.82, relwidth=0.25, relheight=0.12)


class Visualize(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #self.config(bg="Black")

        # create dropdown menu
        '''self.menu_var = tk.StringVar(value="")
        self.menu = ttk.Combobox(self, values=["Matrix Addition", "Matrix Multiplication", "Vector/Matrix transformation", "System of Linear Equations", "3D Matrix Visualisation"], 
                                 textvariable=self.menu_var, state="readonly", background="#1f1f1f", foreground="#ffaa00")
        self.menu.place(relx=0.5, rely=0.05, anchor="center", relwidth=0.15, relheight=0.05, bordermode="outside")'''
        self.type=""
        self.temp_widgets = []
        self.entries = []
        self.entries2 = []
        self.vector = []
        self.prev_pressed = None
        self.add_button = Button(self, text="Matrix Addition", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=BODY_FONT,
                                command=lambda: [self.press_button(self.add_button), self.addition()])
        self.add_button.place(anchor="center", relx=0.1, rely=0.045, relwidth=0.16, relheight=0.05)

        self.trans_button = Button(self, text="Vector/Matrix Transformation", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", 
                                 font=BODY_FONT, command=lambda: [self.press_button(self.trans_button), self.transform()])
        self.trans_button.place(anchor="center", relx=0.263, rely=0.045, relwidth=0.16, relheight=0.05)

        self.mult_button = Button(self, text="Matrix Multiplication", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", 
                                font=BODY_FONT, command=lambda: [self.press_button(self.mult_button), self.multiply()])
        self.mult_button.place(anchor="center", relx=0.426, rely=0.045, relwidth=0.16, relheight=0.05)

        self.eq_button = Button(self, text="System of Linear Equations", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", 
                                font=BODY_FONT, command=lambda: [self.press_button(self.eq_button), self.linear_eq()])
        self.eq_button.place(anchor="center", relx=0.589, rely=0.045, relwidth=0.16, relheight=0.05)

        self.threeD_button = Button(self, text="3D Matrix Visualisation", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", 
                                font=BODY_FONT, command=lambda: [self.press_button(self.threeD_button), self.graph_visual()])
        self.threeD_button.place(anchor="center", relx=0.752, rely=0.045, relwidth=0.16, relheight=0.05)




        self.vis_button = Button(self, text="Visualize", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=self.generate_video)
        self.vis_button.place(anchor="center", relx=0.5, rely=0.3, relwidth=0.15, relheight=0.07)

        self.back_button = Button(self, text="Back To Menu", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: controller.show_frame(MainMenu))
        self.back_button.place(anchor="center", relx=0.91, rely=0.06, relwidth=0.15, relheight=0.08)



        self.canvas = tk.Canvas(self, width=910, height=520, highlightthickness=0)
        self.canvas.place(anchor="center", relx=0.5, rely=0.67)

        rect = self.round_rectangle(5, 5, 905, 515, radius=25, fill="#000000")
        self.canvas.tag_lower(rect)

    def generate_video(self):
        arr = []
        arr2 = []
        if self.type == "add" or self.type == "mult":
            if self.type == "add":
                par = "addition"
            else:
                par = "multiplication"
            size = len(self.entries)
            for row in range(size):
                temp = []
                temp2 = []
                for entry in range(size):
                    temp.append(int(self.entries[entry][row].get()))
                    temp2.append(int(self.entries2[entry][row].get()))
                arr.append(temp)
                arr2.append(temp2)
            video = MatrixCalculation(np.array(arr), np.array(arr2), par, len(arr))
            video.render()
            file_name = "./media/videos/500p60/MatrixCalculation.mp4"
        
        elif self.type == "trans":
            arr = []
            vec = []
            for row in range(2):
                temp = []
                for entry in range(2):
                    temp.append(int(self.entries[entry][row].get()))
                arr.append(temp)
            for v in self.vector:
                vec.append(int(v.get()))
            video = LinearTransformation(np.array(arr), np.array(vec))
            video.render()
            file_name = "./media/videos/500p60/LinearTransformation.mp4"

        elif self.type == "lin":
            arr = []
            vec = []
            for row in range(3):
                temp = []
                for entry in range(3):
                    temp.append(int(self.entries[entry][row].get()))
                arr.append(temp)
            for v in self.vector:
                vec.append(int(v.get()))
            video = LinearEquation(np.array(arr), np.array(vec))
            video.render()
            file_name = "./media/videos/500p60/LinearEquation.mp4"
        else:
            arr = []
            for row in range(3):
                temp = []
                for entry in range(3):
                    temp.append(int(self.entries[entry][row].get()))
                arr.append(temp)
            video = LinearTransformation3D(np.array(arr))
            video.render()
            file_name = "./media/videos/500p60/LinearTransformation3D.mp4"

        self.play_video(file_name)



    def press_button(self, button):
        button.configure(bg='#ffaa00', fg='white')
        if self.prev_pressed != None and self.prev_pressed != button:
            self.prev_pressed.configure(bg='#1f1f1f', fg='#ffaa00')
        self.prev_pressed = button

    def mat_size_but(self, button):
        button.configure(bg='#ffaa00', fg='white')
        if button == self.two_button:
            self.three_button.configure(bg='#1f1f1f', fg='#ffaa00')
            self.display_matrix(2)
        else:
            self.two_button.configure(bg='#1f1f1f', fg='#ffaa00')
            self.display_matrix(3)
    
    def display_matrix(self, size):
        self.clear_matrix()
        if size == 2:
            constx = 0.435
            consty = 0.15
            constx2 = 0.535
            consty2 = 0.15
        else:
            if self.type == 'vis':
                constx = 0.47
                consty = 0.13
            else:
                constx = 0.41
                consty = 0.13
                constx2 = 0.53
                consty2 = 0.13
        for i in range(size):
            row = []
            row2 = []
            for j in range(size):
                box = tk.Entry(self, width=2)
                box.place(relx=constx+0.03*i, rely=consty+0.04*j, anchor="center")
                row.append(box)
                if self.type != 'vis':
                    box2 = tk.Entry(self, width=2)
                    box2.place(relx=constx2+0.03*i, rely=consty2+0.04*j, anchor="center")
                    row2.append(box2)
            self.entries.append(row)
            if self.type != 'vis':
                self.entries2.append(row2)

    def clear_matrix(self):
        for i in range(len(self.entries)):
            for j in range(len(self.entries[i])):
                self.entries[i][j].destroy()
                if self.entries2 != []:
                    self.entries2[i][j].destroy()
        for i in self.vector:
            i.destroy()
        self.vector = []
        self.entries = []
        self.entries2 = []

    def create_mat_buttons(self):
        self.two_button = Button(self, text="2 X 2", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", 
                                font=BODY_FONT, command=lambda: self.mat_size_but(self.two_button))
        self.three_button = Button(self, text="3 X 3", bg='#ffaa00', fg='white', activebackground="#212121", 
                                font=BODY_FONT, command=lambda: self.mat_size_but(self.three_button))
        self.two_button.place(anchor="center", relx=0.39, rely=0.28, relwidth=0.05, relheight=0.03)
        self.three_button.place(anchor="center", relx=0.39, rely=0.32, relwidth=0.05, relheight=0.03)
        self.temp_widgets.append(self.two_button)
        self.temp_widgets.append(self.three_button)

    def clear_screen(self):
        self.clear_matrix()
        for widget in self.temp_widgets:
            widget.destroy()
        self.temp_widgets = []
        
    def addition(self):
        self.type = "add"
        self.clear_screen()
        self.display_matrix(3)
        self.create_mat_buttons()
        self.plus_sign = tk.Label(self, text="+", font=SUBTITLE_FONT_2)
        self.plus_sign.place(anchor="center", relx=0.5, rely=0.165)
        self.temp_widgets.append(self.plus_sign)

    
    def multiply(self):
        self.type = "mult"
        self.clear_screen()
        self.display_matrix(3)
        self.create_mat_buttons()
        self.mult_sign = tk.Label(self, text="×", font=SUBTITLE_FONT_2)
        self.mult_sign.place(anchor="center", relx=0.5, rely=0.165)
        self.temp_widgets.append(self.mult_sign)

    def transform(self):
        self.type = "trans"
        self.clear_screen()
        for i in range(2):
            row = []
            for j in range(2):
                box = tk.Entry(self, width=2)
                box.place(relx=0.445+0.03*i, rely=0.15+0.04*j, anchor="center")
                row.append(box)
            self.entries.append(row)
            box2 = tk.Entry(self, width=2)
            box2.place(relx=0.545, rely=0.15+0.04*i, anchor="center")
            self.vector.append(box2)
        self.trans_sign = tk.Label(self, text="by", font=SUBTITLE_FONT)
        self.trans_sign.place(anchor="center", relx=0.51, rely=0.165)
        self.temp_widgets.append(self.trans_sign)

    def linear_eq(self):
        self.type = "lin"
        self.clear_screen()
        letters = ['x', 'y', 'z']
        for i in range(3):
            row = []
            for j in range(3):
                box = tk.Entry(self, width=2)
                box.place(relx=0.405+0.06*i, rely=0.15+0.04*j, anchor="center")
                letter = tk.Label(self, text=letters[i], font=SUBTITLE_FONT)
                letter.place(anchor="center", relx=0.425+0.06*i, rely=0.15+0.04*j)
                self.temp_widgets.append(letter)
                if i != 2:
                    plus = tk.Label(self, text="+", font=SUBTITLE_FONT)
                    plus.place(anchor="center", relx=0.445+0.06*i, rely=0.15+0.04*j)
                    self.temp_widgets.append(plus)
                row.append(box)
            self.entries.append(row)

        for y in range(3):
            equal = tk.Label(self, text="=", font=SUBTITLE_FONT)
            equal.place(anchor="center", relx=0.57, rely=0.15+0.04*y)
            self.temp_widgets.append(equal)
            box = tk.Entry(self, width=2)
            box.place(relx=0.6, rely=0.15+0.04*y, anchor="center")
            self.vector.append(box)

    def graph_visual(self):
        self.type = "vis"
        self.clear_screen()
        self.display_matrix(3)

    def round_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]
        
        return self.canvas.create_polygon(points, **kwargs, smooth=True)
        
    def play_video(self, vid_name):
        cap = cv2.VideoCapture(vid_name) 
        ret, frame = cap.read()
        
        # loop through frames and display them in the canvas
        while ret:
            img = tk.PhotoImage(data=cv2.imencode('.png', frame)[1].tobytes())
            self.canvas.create_image(10, 10, anchor=tk.NW, image=img)
            self.canvas.update()
            for i in range(2):
                ret, frame = cap.read()

        img = tk.PhotoImage(data=cv2.imencode('.png', frame)[1].tobytes())
        self.canvas.create_image(15, 15, anchor=tk.NW, image=img)
        self.canvas.update()


        cap.release()

    
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


class Quiz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.prev_pressed = None

        self.difficulty = "m"


        upload = tk.Label(self, text="Upload Questions", font=SUBTITLE_FONT_2, fg="#ffaa00")
        upload.place(anchor="center", relx=0.25, rely=0.2)
        
        generate = tk.Label(self, text="Generate Questions", font=SUBTITLE_FONT_2, fg="#ffaa00")
        generate.place(anchor="center", relx=0.75, rely=0.2)

        self.back_button = Button(self, text="Back To Menu", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: controller.show_frame(MainMenu))
        self.back_button.place(anchor="center", relx=0.91, rely=0.06, relwidth=0.15, relheight=0.08)

        self.upload = Button(self, text="Select text file", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: [self.select_text_file(), controller.show_frame(Questions)])
        self.upload.place(anchor="center", relx=0.25, rely=0.5, relwidth=0.25, relheight=0.1)


        self.options = [
            "Inverse Matrix",
            "Matrix Multiplication",
            "System of Linear Equations",
            "Eigen Values",
            "Matrix Addition",
            "Dot Product",
            "Cross Product",
        ]

        self.option_var = tk.StringVar()
        self.option_var.set("Choose an operation")

        option_label = tk.Label(self, text="Question Type", font=SUBTITLE_FONT, fg="#ffaa00")
        option_label.place(anchor="center", relx=0.75, rely=0.3)

        option_menu = tk.OptionMenu(self, self.option_var, *self.options)
        option_menu.place(anchor="center", relx=0.75, rely=0.37, relwidth=0.15, relheight=0.05)

        self.diff = tk.Label(self, text="Difficulty", font=SUBTITLE_FONT, fg="#ffaa00")
        self.diff.place(anchor="center", relx=0.75, rely=0.45)

        self.easy_button = Button(self, text="E", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", 
                                font=BODY_FONT, command=lambda: [self.press_button(self.easy_button), self.set_difficulty("e")])
        self.easy_button.place(anchor="center", relx=0.7, rely=0.54, relwidth=0.05, relheight=0.05)

        self.med_button = Button(self, text="M", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", 
                                font=BODY_FONT, command=lambda: [self.press_button(self.med_button), self.set_difficulty("m")])
        self.med_button.place(anchor="center", relx=0.75, rely=0.54, relwidth=0.05, relheight=0.05)

        self.hard_button = Button(self, text="H", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", 
                                font=BODY_FONT, command=lambda: [self.press_button(self.hard_button), self.set_difficulty("h")])
        self.hard_button.place(anchor="center", relx=0.8, rely=0.54, relwidth=0.05, relheight=0.05)

        # Add a label on top of the slider
        self.questions_label = tk.Label(self, text="Number of questions", font=SUBTITLE_FONT, fg="#ffaa00")
        self.questions_label.place(anchor="center", relx=0.75, rely=0.65)

        self.slider_value = tk.IntVar()
        self.slider_value.set(5)

        # Add a slider (drag bar)
        self.slider = ttk.Scale(self, from_=1, to=10, orient=tk.HORIZONTAL, length=200,
                               variable=self.slider_value, command=self.update_label)
        self.slider.place(anchor="center", relx=0.75, rely=0.72)

        # Add labels for the left and right sides
        left_label = tk.Label(self, text="1")
        left_label.place(anchor="center", relx=0.67, rely=0.72)
        right_label = tk.Label(self, text="10")
        right_label.place(anchor="center", relx=0.83, rely=0.72)

        self.current_value_label = tk.Label(self, textvariable=self.slider_value)
        self.current_value_label.place(anchor="center", relx=0.75, rely=0.75)

        self.gen = Button(self, text="Generate", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: [self.get_questions(), self.send_questions(self.option_var.get()), controller.show_frame(Questions)])
        self.gen.place(anchor="center", relx=0.75, rely=0.82, relwidth=0.15, relheight=0.05)

    def update_label(self, value):
        int_value = round(float(value))
        self.slider_value.set(int_value)

    def press_button(self, button):
        button.configure(bg='#ffaa00', fg='white')
        if self.prev_pressed != None and self.prev_pressed != button:
            self.prev_pressed.configure(bg='#1f1f1f', fg='#ffaa00')
        self.prev_pressed = button

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def select_text_file(self):
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select question file",filetypes = (("text files","*.txt"),))
        self.questions = []
        for qType, question, bigHint, smallHint, matrix1, matrix2, answer in self.read_lines(filename):
            self.questions.append((question, bigHint, smallHint, 10, matrix1, matrix2, answer))
        self.send_questions(qType)
        
    
    def read_lines(self, filename):
        with open(filename, 'r') as file:
            lines = []
            while True:
                for _ in range(7):
                    line = file.readline().rstrip()
                    if not line:
                        break
                    lines.append(line)
                if len(lines) == 7:
                    yield tuple(lines)
                    lines.clear()
                else:
                    break

    def get_questions(self):
        self.questions = DB.get_question(self.difficulty, self.options.index(self.option_var.get()), self.slider_value.get())

    def send_questions(self, Qtype):
        questions_frame = self.controller.frames[Questions]
        questions_frame.recieve_info(self.questions, Qtype)


class Help(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.back_button = Button(self, text="Back To Menu", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                command=lambda: controller.show_frame(MainMenu))
        self.back_button.place(anchor="center", relx=0.91, rely=0.06, relwidth=0.15, relheight=0.08)





class Questions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.controller = controller
        self.current_question = 0
        self.questions = []
        self.q_texts = []
        self.q_small_hints = []
        self.q_big_hints = []
        self.q_points = []
        self.q_matrix1s = []
        self.q_matrix2s = []
        self.q_answers = []

        self.user_answers = []

        self.temp = []

        self.entries = []

        self.question_number_label = tk.Label(self, font=SUBTITLE_FONT)
        self.question_number_label.place(anchor="center", relx=0.5, rely=0.1)

        self.question_label = tk.Label(self, font=SUBTITLE_FONT, fg="#ffaa00")
        self.question_label.place(anchor="center", relx=0.5, rely=0.2)


        self.previous_button = Button(self, text="Previous Question", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=BODY_FONT,
                                  command=self.previous_question)
        self.previous_button.place(anchor="center", relx=0.425, rely=0.9, relwidth=0.15, relheight=0.08)

        self.next_button = Button(self, text="Next Question", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=BODY_FONT,
                                  command=self.next_question)
        self.next_button.place(anchor="center", relx=0.575, rely=0.9, relwidth=0.15, relheight=0.08)

        self.small_hint_button = Button(self, text="Small Hint", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=BODY_FONT,
                                        command=self.show_small_hint)
        self.small_hint_button.place(anchor="center", relx=0.75, rely=0.9, relwidth=0.15, relheight=0.08)

        self.big_hint_button = Button(self, text="Big Hint", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=BODY_FONT,
                                      command=self.show_big_hint)
        self.big_hint_button.place(anchor="center", relx=0.9, rely=0.9, relwidth=0.15, relheight=0.08)

        self.menu_button = Button(self, text="Back To Menu", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                  command=lambda: [controller.show_frame(MainMenu), self.clear_screen(), self.reset_q()])
        self.menu_button.place(anchor="center", relx=0.91, rely=0.06, relwidth=0.15, relheight=0.08)

        self.finish_button = Button(self, text="Finish Quiz", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=BODY_FONT,
                                    command=self.finish_quiz)
        self.finish_button.place(anchor="center", relx=0.575, rely=0.9, relwidth=0.15, relheight=0.08)
        self.finish_button.lower()


    def next_question(self):
        self.store_inputs()
        if self.current_question < len(self.q_texts) - 1:
            self.current_question += 1
            self.update_question()
            if self.current_question == len(self.q_texts) - 1:  
                self.next_button.lower()  
                self.finish_button.lift()  

    def previous_question(self):
        self.store_inputs()
        if self.current_question > 0:
            self.current_question -= 1
            self.update_question()
            if self.current_question < len(self.q_texts) - 1:
                self.finish_button.lower()  
                self.next_button.lift()  


    def clear_screen(self):
        for i in self.temp:
            i.destroy()
        if self.type in ["Matrix Multiplication", "Matrix Addition", "Inverse Matrix"]:
            for row in self.entries:
                for entry in row:
                    entry.destroy()
        else:
            for entry in self.entries:
                entry.destroy()
        self.temp = []
        self.entries = []

    def reset_q(self):
        self.current_question = 0


    def update_question(self):
        self.clear_screen()
        self.question_number_label.config(text=f"Question {self.current_question + 1}")
        self.question_label.config(text=self.q_texts[self.current_question])
        self.display_matrices_and_vectors()
        

    def store_inputs(self):
        if self.type in ["Matrix Multiplication", "Matrix Addition", "Inverse Matrix"]:
            for i in range(len(self.entries)):
                for j in range(len(self.entries[i])):
                    self.user_answers[self.current_question][i][j] = self.entries[j][i].get()
        elif self.type == "Dot Product":
                self.user_answers[self.current_question] = self.entries[0].get()
        else:
            for i in range(len(self.entries)):
                self.user_answers[self.current_question][i] = self.entries[i].get()
        print(self.user_answers)

    

    def display_matrices_and_vectors(self):
        # Display matrix1 and matrix2 or vectors depending on the question type
        if self.type in ["Matrix Multiplication", "Matrix Addition", "System of Linear Equations"]:
            matrix1_str = self.q_matrix1s[self.current_question]
            matrix2_str = self.q_matrix2s[self.current_question]
            if self.type == "Matrix Multiplication":
                symbol = tk.Label(self, text="×", font=SUBTITLE_FONT_2, fg="#ffaa00")
                symbol.place(anchor="center", relx=0.445, rely=0.5)
                self.temp.append(symbol)
                self.display_double_matrix(matrix1_str, matrix2_str)
            elif self.type == "Matrix Addition":
                symbol = tk.Label(self, text="+", font=SUBTITLE_FONT_2, fg="#ffaa00")
                symbol.place(anchor="center", relx=0.445, rely=0.5)
                self.temp.append(symbol)
                self.display_double_matrix(matrix1_str, matrix2_str)
            else:
                self.systems_of_lin(matrix1_str, matrix2_str)
        elif self.type in ["Dot Product", "Cross Product"]:
            vector1_str = self.q_matrix1s[self.current_question]
            vector2_str = self.q_matrix2s[self.current_question]
            self.display_double_vector(vector1_str, vector2_str)
            if self.type == "Dot Product":
                symbol = tk.Label(self, text="•", font=SUBTITLE_FONT_2, fg="#ffaa00")
                symbol.place(anchor="center", relx=0.5, rely=0.5)
                self.temp.append(symbol)
            else:
                symbol = tk.Label(self, text="×", font=SUBTITLE_FONT_2, fg="#ffaa00")
                symbol.place(anchor="center", relx=0.5, rely=0.5)
                self.temp.append(symbol)

        else: 
            matrix_str = self.q_matrix1s[self.current_question]
            self.display_single_matrix(matrix_str)
    
    def systems_of_lin(self, matrix1, matrix2):
        size = len(matrix1)
        if size == 2:
            constx = 0.445
            constx2 = 0.465
            constxplus = 0.485
            consty = 0.4
            consteq = 0.55
            constxans = 0.58
        else:
            constx = 0.405
            consty = 0.3
            constx2 = 0.425
            constxplus = 0.445
            consteq = 0.57
            constxans = 0.6
        letters = ['x', 'y', 'z']
        for i in range(size):
            for j in range(size):
                num = tk.Label(self, text=str(matrix1[j][i]), font=SUBTITLE_FONT)
                num.place(relx=constx+0.06*i, rely=consty+0.08*j, anchor="center")
                letter = tk.Label(self, text=letters[i], font=SUBTITLE_FONT)
                letter.place(anchor="center", relx=constx2+0.06*i, rely=consty+0.08*j)
                self.temp.append(letter)
                self.temp.append(num)
                if i != (size-1):
                    plus = tk.Label(self, text="+", font=SUBTITLE_FONT, fg="#ffaa00")
                    plus.place(anchor="center", relx=constxplus+0.06*i, rely=consty+0.08*j)
                    self.temp.append(plus)

        for y in range(size):
            equal = tk.Label(self, text="=", font=SUBTITLE_FONT, fg="#ffaa00")
            equal.place(anchor="center", relx=consteq, rely=consty+0.08*y)
            self.temp.append(equal)
            if size == 3:
                num = tk.Label(self, text=str(matrix2[y][0]), font=SUBTITLE_FONT)
            else:
                num = tk.Label(self, text=str(matrix2[y]), font=SUBTITLE_FONT)
            num.place(relx=constxans, rely=consty+0.08*y, anchor="center")
            self.temp.append(num)

            equalAns = tk.Label(self, text="=", font=SUBTITLE_FONT, fg="#ffaa00")
            equalAns.place(anchor="center", relx=0.5, rely=0.6+0.08*y)
            letter2 = tk.Label(self, text=letters[y], font=SUBTITLE_FONT)
            letter2.place(anchor="center", relx=0.47, rely=0.6+0.08*y)
            self.temp.append(letter2)
            self.temp.append(equalAns)
            box = tk.Entry(self, width=2)
            box.insert(0, self.user_answers[self.current_question][y])                
            box.place(anchor="center", relx=0.53, rely=0.6+0.08*y)
            self.entries.append(box)


            

    def display_double_matrix(self, matrix1, matrix2):
        equals = tk.Label(self, text="=", font=SUBTITLE_FONT_2, fg="#ffaa00")
        size = len(matrix1)
        if size == 2:
            constx = 0.38
            consty = 0.485
            constx2 = 0.48
            constx3 = 0.58
            equals.place(anchor="center", relx=0.545, rely=0.5)
        else:
            constx = 0.355
            consty = 0.46
            constx2 = 0.475
            constx3 = 0.595
            equals.place(anchor="center", relx=0.565, rely=0.5)
        self.temp.append(equals)
        
        for i in range(size):
            row = []
            for j in range(size):
                letter = tk.Label(self, text=str(matrix1[j][i]), font=SUBTITLE_FONT)
                letter.place(relx=constx+0.03*i, rely=consty+0.04*j, anchor="center")
                self.temp.append(letter)
                letter2 = tk.Label(self, text=str(matrix2[j][i]), font=SUBTITLE_FONT)
                letter2.place(relx=constx2+0.03*i, rely=consty+0.04*j, anchor="center")
                self.temp.append(letter2)
                box = tk.Entry(self, width=2)
                box.insert(0, self.user_answers[self.current_question][j][i])                
                box.place(relx=constx3+0.03*i, rely=consty+0.04*j, anchor="center")
                row.append(box)
            self.entries.append(row)
            
    def display_double_vector(self, vector1, vector2):
        equals = tk.Label(self, text="=", font=SUBTITLE_FONT_2, fg="#ffaa00")
        size = len(vector1)
        constx = 0.47
        constx2 = 0.53
        constx3 = 0.595
        equals.place(anchor="center", relx=0.565, rely=0.5)
        if size == 2:
            consty = 0.485
        else:
            consty = 0.46
        self.temp.append(equals)
        
        for i in range(size):
            letter = tk.Label(self, text=str(vector1[i]) if size == 2 else str(vector1[i][0]), font=SUBTITLE_FONT)
            letter.place(relx=constx, rely=consty+0.04*i, anchor="center")
            self.temp.append(letter)
            letter2 = tk.Label(self, text=str(vector2[i]) if size == 2 else str(vector2[i][0]), font=SUBTITLE_FONT)
            letter2.place(relx=constx2, rely=consty+0.04*i, anchor="center")
            self.temp.append(letter2)
            if self.type == "Cross Product":
                box = tk.Entry(self, width=2)
                box.insert(0, self.user_answers[self.current_question][i])                
                box.place(relx=constx3, rely=consty+0.04*i, anchor="center")
                self.entries.append(box)
        if self.type == "Dot Product":
            box = tk.Entry(self, width=2)
            box.insert(0, self.user_answers[self.current_question])                
            box.place(relx=constx3, rely=0.5, anchor="center")
            self.entries.append(box)

    def display_single_matrix(self, matrix):
        size = len(matrix)
        equals = tk.Label(self, text="=", font=SUBTITLE_FONT, fg="#ffaa00")
        vals = tk.Label(self, text="Eigen Values", font=SUBTITLE_FONT, fg="#ffaa00")
        if size == 2:
            constx2 = 0.535
            if self.type == "Inverse Matrix":
                equals.place(anchor="center", relx=0.5, rely=0.5)
                symbol = tk.Label(self, text="-1", font=BODY_FONT2, fg="#ffaa00")
                symbol.place(anchor="center", relx=0.485, rely=0.45)
                self.temp.append(symbol)
                constx = 0.44
                consty = 0.485            
            else:
                constx = 0.48
                consty = 0.48
                consty2 = 0.7
                equals.place(anchor="center", relx=0.5, rely=consty2)
                vals.place(anchor="center", relx=0.425, rely=consty2)
                self.temp.append(vals)
        else:
            constx2 = 0.53
            if self.type == "Inverse Matrix":
                equals.place(anchor="center", relx=0.5, rely=0.5)
                symbol = tk.Label(self, text="-1", font=BODY_FONT2, fg="#ffaa00")
                symbol.place(anchor="center", relx=0.49, rely=0.435)
                self.temp.append(symbol)
                constx = 0.41
                consty = 0.46
                equals.place(anchor="center", relx=0.5, rely=0.5)
            else:
                constx = 0.47
                consty = 0.47
                consty2 = 0.7
                vals.place(anchor="center", relx=0.425, rely=consty2)
                equals.place(anchor="center", relx=0.5, rely=consty2)
                self.temp.append(vals)
        self.temp.append(equals)


        for i in range(size):
            row = []
            for j in range(size):
                letter2 = tk.Label(self, text=str(matrix[j][i]), font=SUBTITLE_FONT)
                letter2.place(relx=constx+0.03*i, rely=consty+0.04*j, anchor="center")
                self.temp.append(letter2)
                if self.type == "Inverse Matrix":
                    box = tk.Entry(self, width=2)
                    box.insert(0, self.user_answers[self.current_question][j][i])                
                    box.place(relx=constx2+0.03*i, rely=consty+0.04*j, anchor="center")
                    row.append(box)
            if self.type == "Inverse Matrix":
                self.entries.append(row)
            else:
                box = tk.Entry(self, width=2)
                box.insert(0, self.user_answers[self.current_question][i])                
                box.place(relx=constx2+0.03*i, rely=consty2+0.005, anchor="center")
                self.entries.append(box)

    def show_small_hint(self):
        messagebox.showinfo("Small Hint", self.q_small_hints[self.current_question])
        self.q_points[self.current_question] /= 1.5

    def show_big_hint(self):
        messagebox.showinfo("Big Hint", self.q_big_hints[self.current_question])
        self.q_points[self.current_question] /= 2

    def recieve_info(self, questions, type):
        self.type = type
        self.questions.clear()
        self.q_texts.clear()
        self.q_small_hints.clear()
        self.q_big_hints.clear()
        self.q_points.clear()
        self.q_matrix1s.clear()
        self.q_matrix2s.clear()
        self.q_answers.clear()
        self.user_answers.clear()

        self.questions = questions
        print(self.questions)
        for i in self.questions:
            self.q_texts.append(i[0])
            self.q_big_hints.append(i[1])
            self.q_small_hints.append(i[2])
            self.q_points.append(i[3])
            self.q_matrix1s.append(i[4])
            self.q_matrix2s.append(i[5])
            self.q_answers.append(i[6])
        self.q_matrix1s = [eval(i) for i in self.q_matrix1s]
        if self.type not in ["Inverse Matrix", "Eigen Values"]:
            self.q_matrix2s = [eval(j) for j in self.q_matrix2s]
        size = len(self.q_matrix1s[0])
        if self.type in ["Matrix Multiplication", "Matrix Addition", "Inverse Matrix"]:
            for i in range(len(self.q_texts)):
                self.user_answers.append([[""] * size for _ in range(size)])
        elif self.type == "Dot Product":
            for i in range(len(self.q_texts)):
                self.user_answers.append("")
        else:
            for i in range(len(self.q_texts)):
                self.user_answers.append([""] * size)
        self.update_question()
        self.format_answers(size)

    def format_answers(self, size):
        self.formatted_answers = []
        for ans in self.q_answers:
            if self.type in ["System of Linear Equations", "Cross Product"] and size == 2:
                self.formatted_answers.append(list(map(float, ans.strip('[]').split(','))))
            elif self.type == "Cross Product" and size == 3:
                self.formatted_answers.extend(list(map(float, item.split(','))) for item in ans.strip('[]').split('], ['))
            elif self.type == "System of Linear Equations" and size == 3:
                self.formatted_answers.append(list(map(float, ans.strip('[]').replace('[','').replace(']','').split(','))))
            elif self.type in ["Matrix Multiplication", "Matrix Addition", "Inverse Matrix"]:
                self.formatted_answers.append([list(map(float, item.split(','))) for item in ans.strip('[]').split('], [')])
            elif self.type in ["Dot Product"] and size == 2:
                self.formatted_answers.append(float(ans))
            elif self.type in ["Dot Product"] and size == 3:
                self.formatted_answers.extend(float(item) for item in ans.strip('[').strip(']').split(','))

    
    def calculate_score(self):
        total_points = 0
        if self.type in ["System of Linear Equations", "Cross Product", "Dot Product", "Eigen Values"]:
            self.formatted_user_ans = [[float(num) if num != '' else -1000 for num in sublist] for sublist in self.user_answers]
        else:
            self.formatted_user_ans = [[[float(num) if num != '' else -1000 for num in sublist2] for sublist2 in sublist]for sublist in self.user_answers]

        for i in range(len(self.formatted_answers)):
            if self.formatted_answers[i] == self.formatted_user_ans[i]:
                total_points += self.q_points[i]
        print(self.formatted_user_ans)
        print(self.formatted_answers)
        return total_points

    
    def finish_quiz(self):
        self.store_inputs()
        total_points = self.calculate_score()
        finish_frame = self.controller.frames[Finish]
        finish_frame.display_results(self.formatted_answers, self.formatted_user_ans, total_points)
        self.controller.show_frame(Finish)
        DB.add_score(total_points) 

    def send_questions(self, Qtype):
        questions_frame = self.controller.frames[Questions]
        questions_frame.recieve_info(self.questions, Qtype)


class Finish(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.menu_button = Button(self, text="Back To Menu", bg="#1f1f1f", fg="#ffaa00", activebackground="#212121", font=SUBTITLE_FONT,
                                  command=lambda: [controller.show_frame(MainMenu)])
        self.menu_button.place(anchor="center", relx=0.91, rely=0.06, relwidth=0.15, relheight=0.08)

    def display_results(self, answers, user_answers, points):
        for widget in self.winfo_children():
            widget.destroy()

        title = tk.Label(self, text="Quiz Complete", font=TITLE_FONT, fg="#ffaa00")
        title.place(anchor="center", relx=0.5, rely=0.1)

        points_label = tk.Label(self, text=f"Total Points: {points}", font=SUBTITLE_FONT_2 , fg="#ffaa00")
        points_label.place(anchor="center", relx=0.5, rely=0.3)

        for i in range(len(answers)):
            q_number = f"Question {i + 1}:"
            is_correct = answers[i] == user_answers[i]
            result = "Correct" if is_correct else f"Wrong (Correct Answer: {answers[i]})"
            result_color = "green" if is_correct else "red"
            result_label = tk.Label(self, text=f"{q_number} {result}", font=SUBTITLE_FONT, foreground=result_color)
            result_label.place(anchor="w", relx=0.2, rely=0.4 + i * 0.05)






# program section to call the master class and start the program setting window size
if __name__ == "__main__":
    app = MatrixMate()
    app.geometry("1440x810")
    app.mainloop()

