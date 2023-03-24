
import numpy as np
import random


rounding = 1

class Question:
    def __init__(self,difficulty,type):
        self.QuestionDifficulty = difficulty       
        self.type = type                                
        self.points = 0                                            #this is what kind of question this is (e.g. inverse matrix)
        self.Question = None
        self.MatrixQuestion = [[]]                  #will store the matrices (numpy  2D arrays) in a normal array
        self.SmallHint = None
        self.BigHint  = None
        self.Answer  = []      
                             #will store the answers
        self.generate_question()
        if self.QuestionDifficulty == 'm':
            self.points = self.points *1.5
        elif self.QuestionDifficulty == 'h':
            self.points = self.points * 2
        #leave easy as * 1 multiplier


    def generateBigDifficultMatrix(self):                        #generates a difficult 3x3 matrix, values 0-30 

        #generates a the 3x3 matrix with all random values
        matrix = np.array([[random.randint(0,30),random.randint(0,30),random.randint(0,30)],[random.randint(0,30),random.randint(0,30),random.randint(0,30)],[random.randint(0,30),random.randint(0,30),random.randint(0,30)]])
        determ = np.linalg.det(matrix)  #calculate the determinant and redo if determinant is 0 (as matrix not invertable)
        if determ == 0:
            return self.generateBigDifficultMatrix()
        
        
        return matrix
        
    def generateBigMatrix(self):                        #generates a 3x3 matrix, values 0-10, and a rational inverse 

        #generates a the 3x3 matrix with all random values
        matrix = np.array([[random.randint(0,10),random.randint(0,10),random.randint(0,10)],[random.randint(0,10),random.randint(0,10),random.randint(0,10)],[random.randint(0,10),random.randint(0,10),random.randint(0,10)]])
        determ = np.linalg.det(matrix)  #calculate the determinant and redo if determinant is 0 (as matrix not invertable)
        if determ == 0:
            return self.generateBigMatrix()
       
                
        return matrix
        
        
    def generateEasyMatrix(self):           #2x2 matrix, values 0-10, rational inverse
        matrix = np.array([[random.randint(0,10),random.randint(0,10)],[random.randint(0,10),random.randint(0,10)]])
        
        determ = np.linalg.det(matrix)  #calculate the determinant and redo if determinant is 0 (as matrix not invertable)
        if determ == 0:
            return self.generateEasyMatrix()
                 
                
        return matrix

    def generateVector(self,n):           #generates a 1x3 vector
        range = 10
        if self.QuestionDifficulty == 'h':
            range = 30
        if n == 3:
            vector = np.array([[random.randint(0,range)],[random.randint(0,range)],[random.randint(0,range)]])
        elif n == 2:
            vector = np.array([random.randint(0,range),random.randint(0,range)])
        else:
            return None
        return vector




    def generate_question(self):                    #just calls the appropritate question builder based on question type
        if self.type == 0:
            self.inverseMatrix()               
            self.points = 40

        elif self.type == 1:
            self.matrixMultiplication()
            self.points = 30
         
        elif self.type == 2:
            self.systemOfLinearEquations()
            self.points = 40
        
        elif self.type == 3:
            self.eigenValues()
            self.points = 30
            
        elif self.type == 4:
            self.matrixAddition()
            self.points = 10
        
        elif self.type == 5:
            self.dotProduct()
            self.points = 20

        elif self.type == 6:
            self.crossProduct()
            self.points = 20
        
        return



    def inverseMatrix(self):
        if self.QuestionDifficulty == 'h':
            self.MatrixQuestion = self.generateBigDifficultMatrix() 
        elif self.QuestionDifficulty == 'm':
            self.MatrixQuestion = self.generateBigMatrix()
        elif self.QuestionDifficulty == 'e':
            self.MatrixQuestion = self.generateEasyMatrix()


        self.Answer = np.round(np.linalg.inv(self.MatrixQuestion),rounding)
        determ = np.linalg.det(self.MatrixQuestion)
        self.Question = "Find the inverse of the following matrix"
        self.SmallHint = "First you need to find the determinant of the original matrix."
        self.BigHint = "The determinant of the original matrix is:" + str(round(determ,rounding + 3)) + " .Now you should find the matrix of minors. Then the matrix of cofactors of that and then times it by 1/determinant."

    def matrixMultiplication(self):

        if self.QuestionDifficulty == 'h':
            self.MatrixQuestion = [self.generateBigDifficultMatrix(),self.generateBigDifficultMatrix()]
        elif self.QuestionDifficulty == 'm':
            self.MatrixQuestion = [self.generateBigMatrix(),self.generateBigMatrix()]
        elif self.QuestionDifficulty == 'e':
            self.MatrixQuestion = [self.generateEasyMatrix(),self.generateEasyMatrix()]

        self.Answer = np.round(np.matmul((self.MatrixQuestion[0]),(self.MatrixQuestion[1])),rounding)
        self.Question = "Find the product of these two matrices"
        self.SmallHint = "The element in the result matrix is equal to the dot product of that element's row in the first matrix and the element's column in the second matrix."
        self.BigHint = "To get you started the top left element is: " + str(self.MatrixQuestion[0][0]) + "which is the dot product of the first row in the first matrix, and the first column in the second matrix."
    

    def systemOfLinearEquations(self):
        #To solve this one, store the linear equations as a 3x3 and a 1x3 matrix, where the equations are in the form ax + by + cz = d
        if self.QuestionDifficulty == 'e':
            self.MatrixQuestion = [self.generateEasyMatrix(),self.generateVector(2)]
        elif self.QuestionDifficulty == 'm':
            self.MatrixQuestion = [self.generateBigMatrix(),self.generateVector(3)]
        elif self.QuestionDifficulty == 'h':
            self.MatrixQuestion = [self.generateBigDifficultMatrix(),self.generateVector(3)]
        #the answer will be the vector x the inverse of the matrix
        self.Answer = np.round(np.matmul(np.linalg.inv(self.MatrixQuestion[0]),self.MatrixQuestion[1]),rounding)
        
        self.Question = "Solve for the variables in the following system of system of linear equations"
        self.SmallHint = "Try convert the expressions into a 3x3 matrix and find the inverse."
        self.BigHint  = "Turn the constants on the right into a 3x1 matrix, and multiply that by the inverse matrix from small hint."



    def eigenValues(self):       
        if self.QuestionDifficulty == 'h':
            self.MatrixQuestion = self.generateBigDifficultMatrix() 
        elif self.QuestionDifficulty == 'm':
            self.MatrixQuestion = self.generateBigMatrix()
        elif self.QuestionDifficulty == 'e':
            self.MatrixQuestion = self.generateEasyMatrix()

        determ = np.linalg.det(self.MatrixQuestion)
        self.Answer = np.round(np.linalg.eigvals(self.MatrixQuestion),rounding) 
        self.Question = "Find the eigen values of the following matrix"
        self.SmallHint = "Remember that: Av = λv. (where λ is what we are solving for and A is our matrix). Note λ is a scalar quantity with multiple solutions."
        self.BigHint = "Assuming v is non-zero we get: | A - λI | = 0, where I is the identity matrix of the same dimensions as A. "

    
    def dotProduct(self):
        if self.QuestionDifficulty == 'e':
            self.MatrixQuestion = [self.generateVector(2),self.generateVector(2)]
        else:
            self.MatrixQuestion = [self.generateVector(3),self.generateVector(3)]

        self.Answer = np.round(np.dot(self.MatrixQuestion[0].transpose(),self.MatrixQuestion[1]),rounding)
        self.Question = "Find the dot product of the following two vecotrs"
        self.SmallHint = "Your answer should be a scalar quantity (not a vector)."
        self.BigHint = "Multiply each element with the corresponding one in the other matrix and sum the products."

            
    def crossProduct(self):
        if self.QuestionDifficulty == 'e':
            self.MatrixQuestion = [self.generateVector(2),self.generateVector(2)]
        else:
            self.MatrixQuestion = [self.generateVector(3),self.generateVector(3)]
                
        self.Answer = np.cross(self.MatrixQuestion[0].transpose(),self.MatrixQuestion[1].transpose())
        self.Question = "find the cross product of the following two vectors. Leave your answer in vector form"
        self.SmallHint = "The cross product of two parallel vectors is 0."
        self.BigHint = "Your answer should be the vector perpendicular to the two question vectors"
        

    def matrixAddition(self):
        if self.QuestionDifficulty == 'h':
            self.MatrixQuestion = [self.generateBigDifficultMatrix(),self.generateBigDifficultMatrix()]
        elif self.QuestionDifficulty == 'm':
            self.MatrixQuestion = [self.generateBigMatrix(),self.generateBigMatrix()]
        elif self.QuestionDifficulty == 'e':
            self.MatrixQuestion = [self.generateEasyMatrix(),self.generateEasyMatrix()]

        self.Answer = np.add(self.MatrixQuestion[0],self.MatrixQuestion[1])
        self.Question = "Add the following to matrices"
        self.SmallHint = "Add each element in the same poistion to get the new value in that position."
        self.BigHint = "The first row of the answer is:" + str(self.Answer[0])
