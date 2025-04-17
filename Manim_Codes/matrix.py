from manim import *

class matrix(Scene):
    def construct(self):
        matrix = Matrix([["f(1)"], ["f(2)"], ["f(3)"], ["f(4)"], ["f(5)"]], left_bracket="(", right_bracket=")")
        matrix.scale(0.8)
        matrix.shift(LEFT*2)
        self.play(Create(matrix))
        #i want a equal to sign to appear next to the matrix
        equal = Text("=").scale(0.8)
        equal.next_to(matrix, RIGHT)
        self.play(Create(equal))

        #now i want to create a 5x3 matrix
        matrix2 = Matrix([["1", "1", "1"], ["1", "2", "4"], ["1", "3", "9"], ["1", "4", "5"], ["1", "5", "3"]], left_bracket="(", right_bracket=")")
        matrix2.scale(0.8)
        matrix2.next_to(equal,RIGHT)
        self.play(Create(matrix2))

        #now i want a 3x1 matrix to appear next to the 5x3 matrix as multiplication of two matrices
        multiplication = Text("x").scale(0.8)
        multiplication.next_to(matrix2, RIGHT)
        self.play(Create(multiplication))

        #now i want to create a 3x1 matrix
        matrix3 = Matrix([["S"], ["R1"], ["R2"]], left_bracket="(", right_bracket=")")
        matrix3.scale(0.8)
        matrix3.next_to(multiplication, RIGHT*2)
        self.play(Create(matrix3))

        self.wait(2)
