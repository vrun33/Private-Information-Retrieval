from manim import *

class BitPermutation(Scene):
    def construct(self):
        # Generate random bits
        bits = [0, 1, 0, 1, 1, 0, 1, 0]
        bits2 = [1,1, 1, 0, 0, 0, 1, 1]
        bits3 = [1, 0, 1, 0, 1, 0, 1, 0]
        bits4 = [1, 0, 1, 1, 1, 0, 1, 1]
        bits5 = [0, 0, 1, 0, 0, 0, 1, 0]
        bits6 = [0, 1, 0, 1, 1, 0, 1, 0]

        #now i want these 6 bits to be at the random locations in the screen
        bits.move_to(UP*2)
        bits2.move_to(UP*1+RIGHT*2)
        bits3.move_to(UP*1+LEFT*2)
        bits4.move_to(DOWN*3+RIGHT*2)
        bits5.move_to(DOWN*2.5+LEFT*2)
        bits6.move_to(DOWN*2.5)