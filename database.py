import sqlite3
import hashlib
from tkinter import messagebox


import sqlite3

class Database:
    def __init__(self):
        
        self.conn = sqlite3.connect('matrix.db')
        self.cursor = self.conn.cursor()

        # Create the Users table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Users
                    (userID INTEGER PRIMARY KEY NOT NULL,
                    Username VARCHAR NOT NULL,
                    Password VARCHAR NOT NULL,
                    Score INTEGER NOT NULL,
                    UserType CHAR(7) NOT NULL);''')


        # Create the Questions table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Questions
                    (questionID INTEGER PRIMARY KEY NOT NULL,
                    UserID INTEGER,
                    QuestionType INTEGER NOT NULL,
                    QuestionDiff TEXT NOT NULL CHECK(QuestionDiff IN ('easy', 'medium', 'hard')),
                    Question TEXT,
                    SmallHint TEXT NOT NULL,
                    BigHint TEXT NOT NULL,
                    FOREIGN KEY (UserID) REFERENCES Users(userID));''')

        # Create the Answers table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Answers
                    (AnswerID INTEGER PRIMARY KEY NOT NULL,
                    QuestionID INTEGER NOT NULL,
                    Answer TEXT,
                    FOREIGN KEY (QuestionID) REFERENCES Questions(questionID));''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Matrices
                            (MatrixID INTEGER PRIMARY KEY NOT NULL,
                            QuestionID INTEGER,
                            AnswerID INTEGER,
                            Matrix TEXT NOT NULL,
                            FOREIGN KEY (QuestionID) REFERENCES Questions(QuestionID),
                            FOREIGN KEY (AnswerID) REFERENCES Answers(AnswerID));''')


        self.conn.commit()

        self.UserID = 0

        self.success = False
    
    def get_scores(self):
        self.cursor.execute("SELECT username, score FROM users ORDER BY score DESC LIMIT 10")
        results = self.cursor.fetchall()
        return results
    
    def hash_string(self,text):
        text_as_bytes = text.encode()
        hash_object = hashlib.sha256(text_as_bytes)
        hexadecimal_rep = hash_object.hexdigest()
        return hexadecimal_rep

    # Method to ensure user disconnects from database when logged out
    def logout(self):
        self.UserID = 0

    # Method to login and search for user in database
    def find_user(self, username, password, usertype):
        # hashes inputted password
        password = self.hash_string(password)
        if usertype == 'guest':
            self.UserID = 'guest'
        else:
            statement = "SELECT * FROM Users WHERE Username=? AND Password=?;"
            values = (username, password)
            self.cursor.execute(statement, values)
            result = self.cursor.fetchone()
            # user was not found in the database or incorrect login data entered
            if not result:
                messagebox.showinfo("User Not Found", "User Not Found\n\n"
                                                      "Please make sure correct username and\n"
                                                      "password were entered and try again")
            else:
                self.UserID = result[0]
                self.success = True

    # Method to register a new user
    def register_user(self, username, password, password2, usertype):
        # password strength parameters checked
        weaknesses = 3
        if any('a' <= character <= 'z' for character in password):
            weaknesses -= 1
        if any('A' <= character <= 'Z' for character in password):
            weaknesses -= 1
        if any(character.isdigit() for character in password):
            weaknesses -= 1
        # check if username already exists in database
        username_statement = "SELECT * FROM Users WHERE Username=?;"
        value = (username,)
        self.cursor.execute(username_statement, value)
        if self.cursor.fetchone():
            # error message that username already in use
            messagebox.showinfo("Username already exists", "Username already exists\n\n"
                                                           "Please enter a new Username and retype passwords\n"
                                                           "and try again by pressing Register")
        # error message in username too long
        #elif len(username) > 15:
        #    messagebox.showinfo("Username is too long", "Username is too long\n\n"
        #                                                "Username should not exceed 15 characters in length")
        # error message if username too short
        elif len(username) < 3:
            messagebox.showinfo("Username is too short", "Username is too short\n\n"
                                                         "Username should not be less than 3 characters in length")
        # error message if password and retyped password do not match
        elif password != password2:
            messagebox.showinfo("Passwords do not match", "Passwords do not match\n\n"
                                                          "Please enter passwords again and press Register")
        # error message if password too short
        elif len(password) < 8:
            messagebox.showinfo("Password is too short", "Password is too short\n\n"
                                                         "Please ensure password is at least 8 characters long")
        # error message if password doesn't meet all strength requirements
        elif weaknesses != 0:
            messagebox.showinfo("Password does not meet all strength requirement",
                                "Password does not meet all strength requirement\n\n"
                                "Please ensure password contains\n"
                                "at least one lowercase character, "
                                "one uppercase character and"
                                "one numerical digit.")
        elif usertype == '':
            messagebox.showinfo("User Type not selected", "User Type not selected\n\n"
                                                          "Please select a user type and try again")
        else:
            # If there are no errors new user is added to tblUsers in the database
            password = self.hash_string(password)
            register_statement = "INSERT INTO Users(?, ?, ?, ?);" 
            values =  (username,password,0,usertype)
            self.cursor.execute(register_statement, values)
            self.conn.commit()
            # registered successfully message shown and user is sent back to login screen
            messagebox.showinfo("Registered Successfully", "Registered Successfully\n\n "
                                                           "Login with your new account")
            self.success = True

    def success_check(self):
        x = self.success
        self.success = False
        return x

