import numpy as np
from manim import *


config.pixel_width = 890
config.pixel_height = 500
# config.background_color = GREY


# Equation visuals
class MatrixCalculation(Scene):
    # def __init__(self, renderer=None, camera_class=..., always_update_mobjects=False, random_seed=None, skip_animations=False, matrix1=None, matrix2=None):
    #     super().__init__(renderer, camera_class, always_update_mobjects, random_seed, skip_animations)
    #     self.matrix1 = matrix1
    #     self.matrix2 = matrix2
        
    def __init__(self, matrix1, matrix2, type, dimension):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.type = type
        self.dimension = dimension
        Scene.__init__(self)
    
    
    def addition2D(self):
        
        # get matrix
        matrix1 = self.matrix1
        matrix2 = self.matrix2
        rMatrix = np.add(matrix1,matrix2)
        
        
        # text on top
        t1 = MathTex("This", "is", "the", "first","matrix")
        t2 = MathTex("This", "is", "the", "second","matrix")
        t3 = MathTex("This", "is", "the", "result","matrix")
        
        # matrices
        mat = MathTex(r"\begin{bmatrix} "+str(matrix1[0][0])+" & \quad "+str(matrix1[0][1])+" \\\\ "+str(matrix1[1][0])+" & \quad "+str(matrix1[0][1])+" \end{bmatrix}")
        mat2 = MathTex(r"+\begin{bmatrix} "+str(matrix2[0][0])+" & \quad "+str(matrix2[0][1])+" \\\\ "+str(matrix2[1][0])+" & \quad "+str(matrix2[0][1])+" \end{bmatrix}")
        mat3 = MathTex(r"=\begin{bmatrix} "+str(rMatrix[0][0])+" & \quad "+str(rMatrix[0][1])+" \\\\ "+str(rMatrix[1][0])+" & \quad "+str(rMatrix[1][1])+" \end{bmatrix}")
        
        # mat3 = MathTex(r"=\quad 1\begin{bmatrix} -1 \\ 1 \end{bmatrix}\quad +\quad 2\begin{bmatrix} \quad 1 \\ -1 \end{bmatrix}")
        
        # color correction
        t1[3].set_color(RED)
        t2[3].set_color(YELLOW)
        t3[3].set_color(BLUE)
        mat.set_color(RED)
        mat2.set_color(YELLOW)
        mat3.set_color(BLUE)
        
        # spacing
        t1.arrange(RIGHT, buff=0.2)
        t2.arrange(RIGHT, buff=0.2)
        t3.arrange(RIGHT, buff=0.2)
        
        # positioning
        t1.move_to(3*UP)
        t2.move_to(3*UP)
        t3.move_to(3*UP)
        
        ''' addition '''
        mat.move_to(3.5*LEFT)
        mat2.move_to(1*LEFT)
        mat3.move_to(2*RIGHT)
        
        
        # animations
        self.play(Write(t1))
        self.play(Transform(t1,mat))
        self.wait()
        self.play(Write(t2))
        self.play(Transform(t2,mat2))
        self.wait()
        self.play(Write(t3))
        self.play(Transform(t3,mat3))
        self.wait()
        
        
    def addition3D(self):
        
        # get matrix
        matrix1 = self.matrix1
        matrix2 = self.matrix2
        rMatrix = np.add(matrix1,matrix2)
        
        # text on top
        t1 = MathTex("This", "is", "the", "first","matrix")
        t2 = MathTex("This", "is", "the", "second","matrix")
        t3 = MathTex("This", "is", "the", "result","matrix")
        
        # matrices
        mat = MathTex(r"\begin{bmatrix} "+str(matrix1[0][0])+" & \quad "+str(matrix1[0][1])+" & \quad "+str(matrix1[0][2])+" \\\\ "+str(matrix1[1][0])+" & \quad "+str(matrix1[1][1])+" & \quad "+str(matrix1[1][2])+" \\\\ "+str(matrix1[2][0])+" & \quad "+str(matrix1[2][1])+" & \quad "+str(matrix1[2][2])+" \end{bmatrix}")
        mat2 = MathTex(r"+\begin{bmatrix} "+str(matrix2[0][0])+" & \quad "+str(matrix2[0][1])+" & \quad "+str(matrix2[0][2])+" \\\\ "+str(matrix2[1][0])+" & \quad "+str(matrix2[1][1])+" & \quad "+str(matrix2[1][2])+" \\\\ "+str(matrix2[2][0])+" & \quad "+str(matrix2[2][1])+" & \quad "+str(matrix2[2][2])+" \end{bmatrix}")
        mat3 = MathTex(r"=\begin{bmatrix} "+str(rMatrix[0][0])+" & \quad "+str(rMatrix[0][1])+" & \quad "+str(rMatrix[0][2])+" \\\\ "+str(rMatrix[1][0])+" & \quad "+str(rMatrix[1][1])+" & \quad "+str(rMatrix[1][2])+" \\\\ "+str(rMatrix[2][0])+" & \quad "+str(rMatrix[2][1])+" & \quad "+str(rMatrix[2][2])+" \end{bmatrix}")
        
        # mat3 = MathTex(r"=\quad 1\begin{bmatrix} -1 \\ 1 \end{bmatrix}\quad +\quad 2\begin{bmatrix} \quad 1 \\ -1 \end{bmatrix}")
        
        # color correction
        t1[3].set_color(RED)
        t2[3].set_color(YELLOW)
        t3[3].set_color(BLUE)
        mat.set_color(RED)
        mat2.set_color(YELLOW)
        mat3.set_color(BLUE)
        
        # spacing
        t1.arrange(RIGHT, buff=0.2)
        t2.arrange(RIGHT, buff=0.2)
        t3.arrange(RIGHT, buff=0.2)
        
        # positioning
        t1.move_to(3*UP)
        t2.move_to(3*UP)
        t3.move_to(3*UP)
        
        ''' addition '''
        mat.move_to(4*LEFT)
        mat2.move_to(0.5*LEFT)
        mat3.move_to(3.5*RIGHT)
        
        
        # animations
        self.play(Write(t1))
        self.play(Transform(t1,mat))
        self.wait()
        self.play(Write(t2))
        self.play(Transform(t2,mat2))
        self.wait()
        self.play(Write(t3))
        self.play(Transform(t3,mat3))
        self.wait()
        
        
    def multiplication2D(self):
        
        # get matrix
        matrix1 = self.matrix1
        matrix2 = self.matrix2
        rMatrix = np.matmul(matrix1,matrix2)
        
        
        # text on top
        t1 = MathTex("This", "is", "the", "first","matrix")
        t2 = MathTex("This", "is", "the", "second","matrix")
        t3 = MathTex("This", "is", "the", "result","matrix")
        
        # matrices
        mat = MathTex(r"\begin{bmatrix} "+str(matrix1[0][0])+" & \quad "+str(matrix1[0][1])+" \\\\ "+str(matrix1[1][0])+" & \quad "+str(matrix1[1][1])+" \end{bmatrix}")
        mat2 = MathTex(r"\begin{bmatrix} "+str(matrix2[0][0])+" & \quad "+str(matrix2[0][1])+" \\\\ "+str(matrix2[1][0])+" & \quad "+str(matrix2[1][1])+" \end{bmatrix}")
        mat3 = MathTex(r"=\begin{bmatrix} "+str(rMatrix[0][0])+" & \quad "+str(rMatrix[0][1])+" \\\\ "+str(rMatrix[1][0])+" & \quad "+str(rMatrix[1][1])+" \end{bmatrix}")
        
        # mat3 = MathTex(r"=\quad 1\begin{bmatrix} -1 \\ 1 \end{bmatrix}\quad +\quad 2\begin{bmatrix} \quad 1 \\ -1 \end{bmatrix}")
        
        # color correction
        t1[3].set_color(RED)
        t2[3].set_color(YELLOW)
        t3[3].set_color(BLUE)
        mat.set_color(RED)
        mat2.set_color(YELLOW)
        mat3.set_color(BLUE)
        
        # spacing
        t1.arrange(RIGHT, buff=0.2)
        t2.arrange(RIGHT, buff=0.2)
        t3.arrange(RIGHT, buff=0.2)
        
        # positioning
        t1.move_to(3*UP)
        t2.move_to(3*UP)
        t3.move_to(3*UP)
        
        ''' addition '''
        mat.move_to(3*LEFT)
        mat2.move_to(1*LEFT)
        mat3.move_to(1.75*RIGHT)
        
        
        # animations
        self.play(Write(t1))
        self.play(Transform(t1,mat))
        self.wait()
        self.play(Write(t2))
        self.play(Transform(t2,mat2))
        self.wait()
        self.play(Write(t3))
        self.play(Transform(t3,mat3))
        self.wait()
        
    def multiplication3D(self):
        # get matrix
        matrix1 = self.matrix1
        matrix2 = self.matrix2
        rMatrix = np.matmul(matrix1,matrix2)
        
        # text on top
        t1 = MathTex("This", "is", "the", "first","matrix")
        t2 = MathTex("This", "is", "the", "second","matrix")
        t3 = MathTex("This", "is", "the", "result","matrix")
        
        # matrices
        mat = MathTex(r"\begin{bmatrix} "+str(matrix1[0][0])+" & \quad "+str(matrix1[0][1])+" & \quad "+str(matrix1[0][2])+" \\\\ "+str(matrix1[1][0])+" & \quad "+str(matrix1[1][1])+" & \quad "+str(matrix1[1][2])+" \\\\ "+str(matrix1[2][0])+" & \quad "+str(matrix1[2][1])+" & \quad "+str(matrix1[2][2])+" \end{bmatrix}")
        mat2 = MathTex(r"\begin{bmatrix} "+str(matrix2[0][0])+" & \quad "+str(matrix2[0][1])+" & \quad "+str(matrix2[0][2])+" \\\\ "+str(matrix2[1][0])+" & \quad "+str(matrix2[1][1])+" & \quad "+str(matrix2[1][2])+" \\\\ "+str(matrix2[2][0])+" & \quad "+str(matrix2[2][1])+" & \quad "+str(matrix2[2][2])+" \end{bmatrix}")
        mat3 = MathTex(r"=\begin{bmatrix} "+str(rMatrix[0][0])+" & \quad "+str(rMatrix[0][1])+" & \quad "+str(rMatrix[0][2])+" \\\\ "+str(rMatrix[1][0])+" & \quad "+str(rMatrix[1][1])+" & \quad "+str(rMatrix[1][2])+" \\\\ "+str(rMatrix[2][0])+" & \quad "+str(rMatrix[2][1])+" & \quad "+str(rMatrix[2][2])+" \end{bmatrix}")
        
        # mat3 = MathTex(r"=\quad 1\begin{bmatrix} -1 \\ 1 \end{bmatrix}\quad +\quad 2\begin{bmatrix} \quad 1 \\ -1 \end{bmatrix}")
        
        # color correction
        t1[3].set_color(RED)
        t2[3].set_color(YELLOW)
        t3[3].set_color(BLUE)
        mat.set_color(RED)
        mat2.set_color(YELLOW)
        mat3.set_color(BLUE)
        
        # spacing
        t1.arrange(RIGHT, buff=0.2)
        t2.arrange(RIGHT, buff=0.2)
        t3.arrange(RIGHT, buff=0.2)
        
        # positioning
        t1.move_to(3*UP)
        t2.move_to(3*UP)
        t3.move_to(3*UP)
        
        ''' addition '''
        mat.move_to(4*LEFT)
        mat2.move_to(0.5*LEFT)
        mat3.move_to(3.5*RIGHT)
        
        
        # animations
        self.play(Write(t1))
        self.play(Transform(t1,mat))
        self.wait()
        self.play(Write(t2))
        self.play(Transform(t2,mat2))
        self.wait()
        self.play(Write(t3))
        self.play(Transform(t3,mat3))
        self.wait()
    
    def construct(self):
        if self.dimension == 2:
            if self.type == "addition":
                self.addition2D()
            elif self.type == "multiplication":
                self.multiplication2D()
                
        elif self.dimension == 3:
            if self.type == "addition":
                self.addition3D()
            elif self.type == "multiplication":
                self.multiplication3D()
                
                
class LinearEquation(Scene):
    
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.vector = vector
        Scene.__init__(self)
    
    
    def construct(self):
        
        matrix1 = self.matrix
        vector2 = self.vector
        inverseC = np.linalg.inv(matrix1)
        inverse = np.linalg.inv(matrix1).round(1)
        try:
            finalVec = np.round(np.matmul(inverseC,vector2), 1)
        except:
            print("Error: Matrix cannot be inverted")
        
        # text
        t1 = MathTex("This", "is", "the", "system", "of", "linear", "equations")
        t2 = MathTex(r"\begin{cases} "+str(matrix1[0][0])+"x + "+str(matrix1[0][1])+"y + "+str(matrix1[0][2])+"z = "+str(vector2[0])+" \\\\ "+str(matrix1[1][0])+"x + "+str(matrix1[1][1])+"y + "+str(matrix1[1][2])+"z = "+str(vector2[1])+" \\\\ "+str(matrix1[2][0])+"x + "+str(matrix1[2][1])+"y + "+str(matrix1[2][2])+"z = "+str(vector2[2])+" \end{cases}")
        # t2ul = MathTex(r"\begin{cases} 2x + 3y + 4z = 5 \\ 3x + 4y + z = 6 \\ x + 4y + 3z = 5 \end{cases}")
        t3 = MathTex("Turn", "into", "matrix", "form")
        t4 = MathTex("Inverse", "the", "matrix", "and", "multiply", "both", "sides", "by", "the", "it")
        t5 = MathTex("This", "is", "the", "result")
        
        
        # matrix and vector
        mat1 = MathTex(r"\begin{bmatrix} "+str(matrix1[0][0])+" & \quad "+str(matrix1[0][1])+" & \quad "+str(matrix1[0][2])+" \\\\ "+str(matrix1[1][0])+" & \quad "+str(matrix1[1][1])+" & \quad "+str(matrix1[1][2])+" \\\\ "+str(matrix1[2][0])+" & \quad "+str(matrix1[2][1])+" & \quad "+str(matrix1[2][2])+" \end{bmatrix}")
        invMat = MathTex(r"=\begin{bmatrix} "+str(inverse[0][0])+" & \quad "+str(inverse[0][1])+" & \quad "+str(inverse[0][2])+" \\\\ "+str(inverse[1][0])+" & \quad "+str(inverse[1][1])+" & \quad "+str(inverse[1][2])+" \\\\ "+str(inverse[2][0])+" & \quad "+str(inverse[2][1])+" & \quad "+str(inverse[2][2])+" \end{bmatrix}")
        vec1 = MathTex(r"\begin{bmatrix} x \\ y \\ z \end{bmatrix}")
        vec1L = MathTex(r"\begin{bmatrix} x \\ y \\ z \end{bmatrix}")
        finalVec1 = MathTex(r"\begin{bmatrix} x \\ y \\ z \end{bmatrix}")
        vec2 = MathTex(r"=\begin{bmatrix} "+str(vector2[0])+" \\\\ "+str(vector2[1])+" \\\\ "+str(vector2[2])+" \end{bmatrix}")
        vec2R = MathTex(r"\begin{bmatrix} "+str(vector2[0])+" \\\\ "+str(vector2[1])+" \\\\ "+str(vector2[2])+" \end{bmatrix}")
        rVec = MathTex(r"=\begin{bmatrix} "+str(finalVec[0])+" \\\\ "+str(finalVec[1])+" \\\\ "+str(finalVec[2])+" \end{bmatrix}")
        
        
        # spacing
        t1.arrange(RIGHT, buff=0.2)
        t3.arrange(RIGHT, buff=0.2)
        t4.arrange(RIGHT, buff=0.2)
        t5.arrange(RIGHT, buff=0.2)
        
        
        # sizing
        # t2ul.scale(0.5)
        
        # positioning
        # t2ul.move_to(3*UP + 5*LEFT)
        t1.move_to(3*UP)
        t3.move_to(3*UP)
        t4.move_to(3*UP)
        t5.move_to(3*UP)
        mat1.move_to(2.5*LEFT)
        # vec1.move_to(0.5*LEFT)
        vec2.move_to(1*RIGHT)
        vec2R.move_to(4*RIGHT)
        # invMat.move_to(RIGHT)
        vec1L.move_to(4*LEFT)
        finalVec1.move_to(1.5*LEFT)
        
        # animations
        self.play(Write(t1))
        self.wait()
        self.play(Transform(t1,t2))
        self.play(Write(t3))
        self.wait()
        self.play(Transform(t1,mat1),
                  Write(vec1), 
                  Write(vec2)
        )

        self.play(Transform(t3,t4))
        self.wait()
        self.play(
            Transform(vec2,vec2R),
            Transform(t1,invMat),
            Transform(vec1,vec1L)
        )
        self.play(Transform(t3,t5))
        self.wait()
        self.play(
            Transform(vec1,finalVec1),
            Transform(vec2,rVec),
            Transform(t1,rVec)
        )
        
        
        
        
        self.wait(2)

# Graphical visuals
class LinearTransformation(LinearTransformationScene):
    def __init__(self, matrix, vector=None):
        self.matrix = matrix
        self.vector = vector
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors=True
        )
        
    def construct(self):
        
        matrix = self.matrix
        vector = self.vector
        
        matrixText = MathTex("\\begin{bmatrix} "+str(matrix[0][0])+" & \quad "+str(matrix[0][1])+" \\\\ "+str(matrix[1][0])+" & \quad "+str(matrix[1][1])+" \\end{bmatrix}").to_edge(UL).add_background_rectangle()
        
        vect = self.get_vector(vector, color=RED)
        
        rect = Rectangle(height=2, width=2, color=BLUE, fill_opacity=0.5)
        
        
        
        
        self.add_transformable_mobject(vect, rect)
        self.add_background_mobject(matrixText)
        self.apply_matrix(matrix)
        
        self.wait(3)        
         
        
        
        

class LinearTransformation3D(ThreeDScene):
    
    def __init__(self, matrix):
        self.matrix = matrix
        ThreeDScene.__init__(self)

    CONFIG = {
        "x_axis_label": "x",
        "y_axis_label": "y",
    }

    def create_matrix(self, np_matrix):

        m = Matrix(np_matrix)

        m.scale(0.5)
        m.set_column_colors(GREEN, RED, GOLD)

        m.to_corner(UP + LEFT)

        return m

    def construct(self):

        M = self.matrix

        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = MathTex("i", ",", "j", ",", "k")
        basis_vector_helper[0].set_color(GREEN)
        basis_vector_helper[2].set_color(RED)
        basis_vector_helper[4].set_color(GOLD)

        basis_vector_helper.to_corner(UP + RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE_E)

        i_vec = Vector(np.array([1, 0, 0]), color=GREEN)
        j_vec = Vector(np.array([0, 1, 0]), color=RED)
        k_vec = Vector(np.array([0, 0, 1]), color=GOLD)

        i_vec_new = Vector(M @ np.array([1, 0, 0]), color=GREEN)
        j_vec_new = Vector(M @ np.array([0, 1, 0]), color=RED)
        k_vec_new = Vector(M @ np.array([0, 0, 1]), color=GOLD)

        self.play(
            Create(cube),
            GrowArrow(i_vec),
            GrowArrow(j_vec),
            GrowArrow(k_vec),
            Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)

            
        
mat1 = np.array([[1,0],[1,1]])
mat2 = np.array([[2,0],[0,2]])
mat3 = np.array([[2,3,4],[3,4,1],[1,4,3]])
mat4 = np.array([[1,0,0],[0,1,0],[0,0,1]])
vec1 = np.array([1,1])
# t = (mat3,mat4,"multiplication",3)
t = LinearTransformation3D(mat3)
t.render()