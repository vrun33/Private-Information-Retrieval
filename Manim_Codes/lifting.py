from manim import *

class lifting(Scene):
    def construct(self):

        text = Tex("LIFTING").scale(2)
        text.set_color(ORANGE)
        self.play(Wiggle(text))
        self.play(FadeOut(text),run_time = 1)
        
        someText = Tex("M $=$ 3").scale(0.8)
        someText.color = ORANGE
        text1 = Tex("Now let us lift the refined scheme from the previous section to").scale(0.8)
        text1.shift(UP*3)
        someText.next_to(text1,RIGHT)
        self.play(Write(text1))
        self.play(Wiggle(someText))
        text2 = Tex("Consider the PIR setting with N $=$ 2 servers where a user wants to download").scale(0.8)
        text2.next_to(text1,DOWN)
        some = Tex("M $=$ 3 files").scale(0.8)
        some.color = ORANGE
        text3 = Tex("a single file privately out of a total of").scale(0.8)
        text3.next_to(text2,DOWN)
        text3.shift(LEFT*1.5)
        some.next_to(text3,RIGHT)
        textOk = Tex("$W^{1},W^{2},W^{3} \\in {F_q}^4 $.").scale(0.8)
        textOk.set_color(ORANGE)
        textOk.shift(LEFT*3)
        text4 = Tex("Denote the files by").scale(0.8)
        text4.next_to(text3,DOWN)
        text4.shift(LEFT*1.5)
        textOk.next_to(text4,RIGHT)
        texthmm = Tex("$D =(W^{1},W^{2},W^{3}) \\in {F_q}^{12} $").scale(0.8)
        texthmm.set_color(ORANGE)
       
        text5 = Tex("Thus the database").scale(0.8)
        text5.shift(LEFT*1)
        texthmm.next_to(text5,RIGHT)

        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Write(some))
        self.play(Write(text4))
        self.play(Write(textOk))
        self.play(Write(text5))
        self.play(Write(texthmm))
        self.wait(1)

        text6 = Tex("Without loss of generality ,suppose that the user is intrested in the first file $W^{1}$").scale(0.8)
        text6.shift(DOWN*1.5)
        self.play(Write(text6))

        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3),FadeOut(text4),FadeOut(text5),FadeOut(textOk),FadeOut(texthmm),FadeOut(text6),FadeOut(someText),FadeOut(some),run_time = 1)



        table1 = ImageMobject("tablee1.png").scale(2.5)
        table1.shift(ORIGIN)
        self.play(FadeIn(table1))
        

        table2 = ImageMobject("table_6.png").scale(1.5)

        #now i want to trasnform table1 to table 2
        self.play(FadeOut(table1),FadeIn(table2))
        table2.scale(1)
        table2.shift(UP*2.5+LEFT*4)

        #i want all the below quriers to be on the right side of the screen without overlapping with the table and going out of tghe screen
        

        text7 = Tex("The Queries are choosen as follows $:-$").scale(0.8)
        text7.shift(RIGHT*2+UP*3)
        self.play(Write(text7))
        #now i want to write bullet points
        Bullet1 = Tex("1.Queries $a_{1},..,a_{4} \\in span(e_{1},..,e_{4}) \\subseteq {F_q}^{12} $").scale(0.8)
        Bullet1.next_to(text7,DOWN)
        self.play(Write(Bullet1))
        random = Tex("are choosen uniformly at random,").scale(0.8)
        random.next_to(Bullet1,DOWN)
        random.shift(LEFT*0.5)
        self.play(Write(random))
        sdf = Tex("subject to being linearly independent").scale(0.7)
        sdf.next_to(random,DOWN)
        sdf.shift(LEFT*0.1)
        self.play(Write(sdf))

        Bullet2 = Tex("2.Queries $b_{1},b_{2} \\in span(e_{5},..,e_{8}) \\subseteq {F_q}^{12} $").scale(0.8)
        Bullet2.next_to(sdf,DOWN)
        self.play(Write(Bullet2))
        random2 = Tex("are choosen uniformly at random,").scale(0.8)
        random2.next_to(Bullet2,DOWN)
        random2.shift(LEFT*0.1)
        self.play(Write(random2))
        sdf2 = Tex("subject to being linearly independent").scale(0.8)
        sdf2.next_to(random2,DOWN)
        sdf2.shift(LEFT*0.01)
        self.play(Write(sdf2))


        Bullet3 = Tex("3.Queries $c_{1},c_{2} \\in span(e_{9},..,e_{12}) \\subseteq {F_q}^{12} $").scale(0.8)
        Bullet3.next_to(sdf2,DOWN)
        self.play(Write(Bullet3))

        random3 = Tex("are choosen uniformly at random,").scale(0.8)
        random3.next_to(Bullet3,DOWN)
        random3.shift(LEFT*0.1)
        self.play(Write(random3))
        sdf3 = Tex("subject to being linearly independent").scale(0.8)
        sdf3.next_to(random3,DOWN)
        sdf3.shift(LEFT*0.1)
        self.play(Write(sdf3))

        

        # self.play(Write(Bullet1))
        # self.play(Write(random))
        # self.play(Write(Bullet2))
        # self.play(Write(random2))
        # self.play(Write(Bullet3))
        # self.play(Write(random3))
        self.wait(4)

        self.play(FadeOut(text7),FadeOut(Bullet1),FadeOut(Bullet2),FadeOut(Bullet3),FadeOut(random),FadeOut(random2),FadeOut(random3),FadeOut(table2),FadeOut(sdf),FadeOut(sdf2),FadeOut(sdf3),run_time = 1)


        okay = Tex("$\\frac{4}{7} !!$.").scale(0.8)
        okay.set_color(ORANGE)  
        text = Tex("The download rate for this scheme is ").scale(0.8)
        text.shift(ORIGIN)
        okay.next_to(text,RIGHT)
        self.play(Write(text))
        self.play(Wiggle(okay))
        text.shift(UP*3)
        okay.shift(UP*3)

        text13 = Tex("As we increase the number of files,the optimal scheme will perform worse").scale(0.8)
        text11 = Tex(",quickly approaching the rate of the secret sharing scheme.").scale(0.8)
        text13.next_to(text,DOWN)
        text11.next_to(text13,DOWN)
        self.play(Write(text13))
        self.play(Write(text11))

        #now i want to fadein table 6 to the right side of the screen without overlapping with the text
        table6 = ImageMobject("table_6.png").scale(1.5)
        table6.shift(RIGHT*4+DOWN*2)
        table2 = ImageMobject("table-2.png").scale(1.5)
        table2.shift(LEFT*4+DOWN*2)
        self.play(FadeIn(table6),FadeIn(table2))
        self.wait(2)

        self.play(FadeOut(text),FadeOut(text11),FadeOut(text13),FadeOut(table6),FadeOut(table2),run_time = 1)

        #done with lifting 1 ---------------------------------------------------------------------------





        
        