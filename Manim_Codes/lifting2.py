# Put the title “Symbolic Matrix \n” in the centre in orange. in manim

from manim import *

class Lifting2(Scene):
    def construct(self):
        title = Tex("Symbolic Matrix").scale(2)
        title.color = ORANGE
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        text1 = Tex("We never query the same $a_{i}$ $b_{i}$ to the same server").scale(1)
        text2 = Tex("but we can do so for different servers.").scale(1)
        text3 = Tex("For example sending $b_{1}$ to both Server $1$").scale(1)
        text4 = Tex("and $2$ But this holds as long as the servers").scale(1)
        text5 = Tex("themselves are not colluding among each other.").scale(1)
        # the text 
        # text.scale(0.7)
        # the text is not coming in the center of the screen
        # text.move_to(ORIGIN)
        text1.shift(UP*1.5)
        text2.next_to(text1,DOWN);
        text3.next_to(text2,DOWN);
        text4.next_to(text3,DOWN);
        text5.next_to(text4,DOWN);

        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Write(text4))
        self.play(Write(text5))
        self.wait(12)

        # fade out all the above text, and insert the table-2.png image
      
        table = ImageMobject("table-2.png").scale(2.5)
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3), FadeOut(text4), FadeOut(text5))
        self.play(FadeIn(table))
        self.wait(15)

        #create a 1x2 matrix
        matrix = Matrix([["1","2"]])  
        #i want my table to get transformed into matrix
        self.play(FadeOut(table), Create(matrix))
        self.wait(1)

        table6 = ImageMobject("table_6.png").scale(2.5)
        self.play(FadeIn(table6),FadeOut(matrix))
        self.wait(2)

        matrix2 = Matrix([["1","2"],["3"]]).scale(1.5)
        self.play(FadeOut(table6), Create(matrix2))
        self.wait(6)
        self.play(FadeOut(matrix2))

        some = Tex("M $=$ 4").scale(0.8)
        some.color = ORANGE

        write = Tex("Thus applying the same logic for").scale(0.8)
        someshit = Tex("files we have the following symbolic matrix").scale(0.8)
        some.next_to(write,RIGHT)
        someshit.next_to(write,DOWN)
       # write.shift(UP*2)
        self.play(Write(write))
        self.play(Wiggle(some))
        self.play(Write(someshit))
        
        matrix3 = Matrix([["1","2"],["3","4"]]).scale(0.75)
        matrix3.move_to(DOWN*2)
        self.play(Create(matrix3))

        table8 = ImageMobject("table-8.png").scale(1.5)
        self.play(FadeOut(matrix3), FadeOut(write), FadeOut(some), FadeOut(someshit),FadeIn(table8))

        self.wait(2)

        table8.move_to(ORIGIN)

        something = Tex("$\\frac{8}{15}$").scale(0.8)
        something.color = ORANGE

        texting = Tex("The download rate for this scheme is").scale(0.8)
        texting.move_to(DOWN*3)
        something.next_to(texting,RIGHT)
        self.play(Write(texting))
        self.play(Wiggle(something))

        self.play(FadeOut(table8), FadeOut(texting), FadeOut(something))

        text6 = Tex("Now consider the case of collusion.").scale(1)
        text7 = Tex("Let a scheme with N $=$ 3, T $=$ 2 and M $=$ 2").scale(1)
        text7.next_to(text6,DOWN)
        self.play(Write(text6))
        self.play(Write(text7))
        text6.move_to(UP*3)
        text7.move_to(UP*2)

        table4 = ImageMobject("table-4.png").scale(1.5)
        table4.move_to(RIGHT*2)

        matrix4 = Matrix([["1","1","2"]]).scale(1.25)
        matrix4.move_to(LEFT*2.5)

        self.play(FadeIn(table4),Create(matrix4))

        self.wait(4)

        table9 = ImageMobject("table-9.png").scale(1.25)
        matrix5 = Matrix([["1","1","1"],["1","2","1"],["3"]]).scale(1)

        table9.move_to(RIGHT*2.5)
        matrix5.move_to(LEFT*2.5)

        self.play(FadeOut(table4),FadeOut(matrix4),FadeIn(table9),Create(matrix5))
        
        rate = Tex("$\\frac{9}{19}$").scale(0.9)
        rate.color = ORANGE
        texte = Tex("The download rate for this scheme is").scale(0.9)
        texte.move_to(DOWN*2.5)
        rate.next_to(texte,RIGHT)
        self.play(Write(texte))
        self.play(Wiggle(rate))

        self.play(FadeOut(table9),FadeOut(matrix5),FadeOut(texte),FadeOut(rate),FadeOut(text6),FadeOut(text7))
        

        last_thing = Tex("Finally, We obtain the optimal Download rate $-$").scale(1)
        last_thing.color = BLUE
        last_thing.move_to(UP*1)
        formula = Tex("$\\frac{(N - T) \\cdot N^{M - 1}}{N^{M} - T^{M}}.$")
        formula.color = ORANGE
        formula.scale(1.5)
        formula.move_to(DOWN*1)
        self.play(Write(last_thing))
        self.play(Wiggle(formula))





        


