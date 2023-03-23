import sqlite3
import hashlib
from tkinter import messagebox
from QuestionGenerator import Question
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
                    Score INTEGER NOT NULL);''')


        # Create the Questions table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Questions
                    (questionID INTEGER PRIMARY KEY NOT NULL,
                    UserID INTEGER,
                    QuestionType INTEGER NOT NULL,
                    QuestionDiff TEXT NOT NULL CHECK(QuestionDiff IN ('e', 'm', 'h')),
                    Points INTEGER NOT NULL,
                    Question TEXT,
                    SmallHint TEXT,
                    BigHint TEXT,
                    FOREIGN KEY (UserID) REFERENCES Users(userID));''')

        # Create the Answers table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Answers
                    (AnswerID INTEGER PRIMARY KEY NOT NULL,
                    QuestionID INTEGER NOT NULL,
                    Answer TEXT,
                    FOREIGN KEY (QuestionID) REFERENCES Questions(questionID));''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS MatricesVectors
                            (MatrixID INTEGER PRIMARY KEY NOT NULL,
                            QuestionID INTEGER,
                            Matrix TEXT NOT NULL,
                            MatrixOrder INTEGER NOT NULL,
                            FOREIGN KEY (QuestionID) REFERENCES Questions(QuestionID));''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS UserQuestions (
                            UserQuestionID INTEGER PRIMARY KEY NOT NULL,
                            UserID INTEGER,
                            QuestionID INTEGER,
                            DateAnswered DATETIME NOT NULL,
                            FOREIGN KEY (UserID) REFERENCES Users(UserID),
                            FOREIGN KEY (QuestionID) REFERENCES Questions(QuestionID));''')

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
    def register_user(self, username, password, password2):
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
        elif len(username) > 15:
            messagebox.showinfo("Username is too long", "Username is too long\n\n"
                                                        "Username should not exceed 15 characters in length")
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
        else:
            # If there are no errors new user is added to tblUsers in the database
            password = self.hash_string(password)
            register_statement = "INSERT INTO Users(Username, Password, Score) VALUES (?, ?, ?);" 
            values =  (username,password,0)
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
    
    def upload_question(self, diff, type):
        q = Question(diff, type)
        answer = str(q.Answer.tolist())
        print(answer)
        question = q.Question
        small_hint = q.SmallHint
        big_hint = q.BigHint
        points = q.points

        statement = "INSERT INTO Questions(UserID, QuestionType, QuestionDiff, Points, Question, SmallHint, BigHint) VALUES(?, ?, ?, ?, ?, ?, ?);"
        values = (self.UserID, type, diff, points, question, small_hint, big_hint)
        self.cursor.execute(statement, values)

        questionID = self.cursor.lastrowid

        matrix2 = None
        if type == 0: # Inverse matrix
            matrix = str(q.MatrixQuestion.tolist())
        if type == 1: # Matrix multiply
            matrix = str(q.MatrixQuestion[0].tolist())
            matrix2 = str(q.MatrixQuestion[1].tolist())
        if type == 2: # System of linear
            matrix = str(q.MatrixQuestion[0].tolist())
            matrix2 = str(q.MatrixQuestion[1].tolist()) #Vector
        if type == 3: # eigenvalues
            matrix = str(q.MatrixQuestion.tolist())
        if type == 4: # Matrix addition
            matrix = str(q.MatrixQuestion[0].tolist())
            matrix2 = str(q.MatrixQuestion[1].tolist())
        if type == 5: # dot product
            matrix = str(q.MatrixQuestion[0].tolist()) #Vector
            matrix2 = str(q.MatrixQuestion[1].tolist()) #Vector
        if type == 6: # cross product
            matrix = str(q.MatrixQuestion[0].tolist()) #Vector
            matrix2 = str(q.MatrixQuestion[1].tolist()) #Vector
        
        if matrix2 is None:
            statement = "INSERT INTO MatricesVectors(QuestionID, Matrix, MatrixOrder) VALUES(?, ?, ?);"
            values = (questionID, matrix, 1)
            self.cursor.execute(statement, values)
        else:
            statement = "INSERT INTO MatricesVectors(QuestionID, Matrix, MatrixOrder) VALUES(?, ?, ?);"
            values = (questionID, matrix, 1)
            self.cursor.execute(statement, values)
            statement = "INSERT INTO MatricesVectors(QuestionID, Matrix, MatrixOrder) VALUES(?, ?, ?);"
            values = (questionID, matrix2, 2)
            self.cursor.execute(statement, values)

        statement = "INSERT INTO Answers(QuestionID, Answer) VALUES(?, ?);"
        values = (questionID, answer)
        self.cursor.execute(statement, values)

        self.conn.commit()

    def get_question(self, diff, type, num):
        statement = """
        SELECT Questions.Question, Questions.BigHint, Questions.SmallHint, Questions.Points,
            mv1.Matrix AS Matrix1, mv2.Matrix AS Matrix2, Answers.Answer
        FROM Questions
        LEFT JOIN UserQuestions ON Questions.QuestionID = UserQuestions.QuestionID AND UserQuestions.UserID = ?
        LEFT JOIN Answers ON Questions.QuestionID = Answers.QuestionID
        LEFT JOIN (SELECT * FROM MatricesVectors) AS mv1 ON Questions.QuestionID = mv1.QuestionID AND mv1.MatrixOrder = 1
        LEFT JOIN (SELECT * FROM MatricesVectors) AS mv2 ON Questions.QuestionID = mv2.QuestionID AND mv2.MatrixOrder = 2
        WHERE Questions.QuestionDiff=? AND Questions.QuestionType=? AND UserQuestions.UserID IS NULL
        LIMIT ?;
        """


        values = (self.UserID, diff, type, num)
        self.cursor.execute(statement, values)
        questions = self.cursor.fetchall()
        print(questions)

        if len(questions) < num:
            for i in range(num - len(questions)):
                self.upload_question(diff, type)
            return self.get_question(diff, type, num)
        else:
            return questions
        
    def add_score(self, score):
        if self.UserID is not 'guest':
            statement = "UPDATE Users SET Score = Score + ? WHERE UserID = ?;"
            values = (score, self.UserID)
            self.cursor.execute(statement, values)
            self.conn.commit()




