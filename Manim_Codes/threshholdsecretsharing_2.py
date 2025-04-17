from manim import *

class ThresholdSecretSharing_2(Scene):
    def construct(self):
        rate = Tex("$q = 7$").scale(0.8)
        rate.color = ORANGE
        text = Tex("Consider a $(5,3)$ Secret Sharing Scheme with").scale(0.8)
        text.shift(UP*3)
        rate.next_to(text,RIGHT)
        self.play(Write(text))
        self.play(Wiggle(rate))

        text2 = MathTex(
            r"F\text{or some randomly generated vectors  } R_{1} \text{ and } R_{2} \in F_{q}  \text{and a secret message } S \in F_{q}"
        ).scale(0.7)
        text2.next_to(text, DOWN)
        self.play(Write(text2))

        text3 = Tex("Let $R_{1}$ = 1101010101, $R_{2}$ = 1101010101, S = 1101010101").scale(0.8)
        text3.next_to(text2, DOWN)
        self.play(Write(text3))

        text5 = Tex(
            "$f(x) = S + R_{1}t + R_{2}t^{2}$"
        ).scale(0.8)
        text5.set_color(ORANGE)
        
        text4 = Tex("We have the polynomial", color=WHITE).scale(0.8)

        text4.next_to(text3, DOWN)
        text4.shift(LEFT*3)
        text5.next_to(text4,RIGHT)
        # text4.add(text5)
        self.play(Write(text4))
        self.play(Write(text5))

        text6 = Tex("Here each participant receives the share f(i)").scale(0.8)
        text6.next_to(VGroup(text4,text5), DOWN)
        self.play(Write(text6))

        self.wait(2)
      
        text8 = Tex("$I(S;f(i_{1}),f(i_{2})) = 0$", color=ORANGE)
        text7 = Tex("Thus, for any two evaluations i1 and i2, the mutual information ", color=WHITE).scale(0.65)
        text7.next_to(text6, DOWN)
        text8.next_to(text7,DOWN)
        text8.shift(RIGHT*1)
        # text7.add(text8)
        self.play(Write(text7),Write(text8))

        self.wait(2)
        
        #i want to clear the screen and show the next part
        self.play(FadeOut(text), FadeOut(text2), FadeOut(text3), FadeOut(text4), FadeOut(text5), FadeOut(text6), FadeOut(text7), FadeOut(text8),FadeOut(rate),run_time=1)

        matrix = Matrix([["f(1)"], ["f(2)"], ["f(3)"], ["f(4)"], ["f(5)"]], left_bracket="(", right_bracket=")")
        matrix.scale(0.8)
        matrix.shift(LEFT*2)
        self.play(Create(matrix))
        #i want a equal to sign to appear next to the matrix
        equal = Tex("=").scale(0.8)
        equal.next_to(matrix, RIGHT)
        self.play(Create(equal))

        #now i want to create a 5x3 matrix
        matrix2 = Matrix([["1", "1", "1"], ["1", "2", "4"], ["1", "3", "2"], ["1", "4", "2"], ["1", "5", "4"]], left_bracket="(", right_bracket=")")
        matrix2.scale(0.8)
        matrix2.next_to(equal,RIGHT)
        self.play(Create(matrix2))

        #now i want a 3x1 matrix to appear next to the 5x3 matrix as multiplication of two matrices
        multiplication = Tex("x").scale(0.8)
        multiplication.next_to(matrix2, RIGHT)
        self.play(Create(multiplication))

        #now i want to create a 3x1 matrix
        matrix3 = Matrix([["S"], ["R1"], ["R2"]], left_bracket="(", right_bracket=")")
        matrix3.scale(0.8)
        matrix3.next_to(multiplication, RIGHT*2)
        self.play(Create(matrix3))

        self.wait(2)

        self.play(FadeOut(matrix),FadeOut(equal),FadeOut(matrix2),FadeOut(multiplication),FadeOut(matrix3),run_time = 1)

        text = Tex("In general, we have a $(N,T+1)$ Threshold Secret Sharing Scheme").scale(0.8)
        text.shift(UP*3)

        #now i want to add bullet points one by one to the screen
        bullet1 = Tex("The Secret is an element S in $F_{q}$").scale(0.8)
        bullet1.next_to(text, DOWN)
        bullet1.shift(RIGHT*1)
        #self.play(Write(text))
        #self.play(Write(bullet1))

        bullet2 = Tex("The number of shareholders is N $(N < q)$").scale(0.8)
        bullet2.next_to(bullet1, DOWN)
        #bullet2.shift(RIGHT*1)
        #self.play(Write(bullet2))

        bullet3 = Tex("The minimum number of shareholders required to decode the secret is $T+1$").scale(0.7)
        bullet3.next_to(bullet2, DOWN)
       # bullet3.shift(RIGHT*1)
        #self.play(Write(bullet3))

        bullet4 = Tex("Step 1 : Choose T random keys $R_{1},R_{2}.....R_{T}$ $\\in$ $F_{q}$ uniformly at random").scale(0.7)
        bullet4.move_to(LEFT*0.2)
        bullet4.next_to(bullet3, DOWN)
       # bullet4.shift(RIGHT*1)
        #self.play(Write(bullet4))

        bullet5 = Tex("Step 2 : Define a polynomial $f(t) = S + R_{1} \\cdot t + .... + R_{T} \\cdot t^{T}$").scale(0.8)
        bullet5.next_to(bullet4, DOWN)
       # bullet5.shift(RIGHT*1)
        #self.play(Write(bullet5))

        bullet6 = Tex("Step 3 : Each shareholder i receives the share f(i)").scale(0.8)
        bullet6.next_to(bullet5, DOWN)
       # bullet6.shift(RIGHT*1)
        #self.play(Write(bullet6))

        #i want all the bullet points to appear together without any delay

        self.play(Write(text), Write(bullet1), Write(bullet2), Write(bullet3), Write(bullet4), Write(bullet5), Write(bullet6))   

        self.wait(8)


        


