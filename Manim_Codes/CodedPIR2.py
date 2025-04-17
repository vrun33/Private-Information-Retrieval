from manim import *

class CodedPIR2(Scene):
    def construct(self):
        Text1 = Tex(r"Now, $X_1, X_2, Y_1,Y_2 \in {F_5}^2.$ \\Thus, the first message is now $(X_1,X_2) \in {F_5}^4$.").scale(0.8)
        Text1.to_edge(UP).center()
        self.play(Write(Text1))
        self.wait(1)
        self.play(FadeOut(Text1))
        Table13 = ImageMobject("table-13.png").scale(1.7)
        Table13.move_to(LEFT*3 + UP*2.8)
        self.play(FadeIn(Table13))
        self.wait(1)
        # self.play(FadeOut(Table13))

        blistText2 = Tex("The Queries are chosen as follows:").scale(0.6)
        blistText2.move_to(DOWN*1.5 + RIGHT*2.3)
        self.play(Write(blistText2))

        Blist11 = r"The queries $a_1, a_2 \in$ span($e_1, e_2$) $\subseteq$ ${\mathbb{F}_5}^2$ are chosen uniformly at random,\\ subject to being linearly independent."
        Blist22 = r"The queries $b_1, b_2$ $\in$ span($e_4, e_5$) $\subseteq$ ${\mathbb{F}_5}^2$ are chosen uniformly at random \\ subject to being linearly independent."

        blist = BulletedList(Blist11, Blist22).scale(0.6)

        blist.next_to(blistText2, DOWN, buff = 0.1)
        self.play(blistText2.animate.shift(LEFT*2.6))
        self.play(Write(blist))
        self.wait(18)

        group1 = VGroup(blist, blistText2)
        # self.play(FadeOut(blist), FadeOut(blistText2))
        Eqn1 = Tex(r"$0 = \langle D_1,b_1 \rangle + 3 \langle D_2, b_2 \rangle + 3 \langle D_3, b_1 + b_2 \rangle + \langle D_4, b_1 + 2b_2 \rangle$", color = ORANGE).scale(0.7)
        self.play(ReplacementTransform(group1,Eqn1))
        self.play(Circumscribe(Eqn1))
        self.wait(1)

        Text2 = Tex(r"Thus the Download Rate of this PIR scheme is $\frac{4}{7}$").scale(0.8)
        Text2.to_edge(DOWN)
        self.play(Write(Text2))
        self.wait(1.5)
        self.play(FadeOut(Text2), FadeOut(Table13), FadeOut(Eqn1))
        self.wait()

        Table10 = ImageMobject("table-10.png").scale(2.2)
        Table10.move_to(RIGHT*3 + UP*1.5)

        m2 = Matrix([[1, 1, 1, 2]],
            element_alignment_corner=UL,
            left_bracket="(",
            right_bracket=")").scale(0.8)
        
        label = Tex(r"${\mathcal{S}}_2 = $").scale(0.8)
        label.next_to(m2, LEFT)
        equation = VGroup(label, m2)
        equation.arrange(RIGHT)
        equation.move_to(LEFT * 3 + UP *1.5)
        self.play(Write(equation), FadeIn(Table10))
        self.wait(10)

        Text3 = Tex(r"In general, we need 'M' number of k queries \\ to obtain one (k+1) query, where \\ M is the number of messages.", color = BLUE).scale(0.65)
        #Write under the matrix
        Text3.next_to(equation, DOWN*0.9)
        self.play(Write(Text3))
        self.wait(2)

        self.play(FadeOut(equation), FadeOut(Text3), FadeOut(Table10))
        self.wait(0.5)

        Table14 = ImageMobject("table-14.png").scale(1.1)
        Table14.move_to(RIGHT*3.5 + UP*1.5)

        m3 = Matrix([[1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [3 ]],
            element_alignment_corner=UL,
            left_bracket="(",
            right_bracket=")").scale(0.8)
        label2 = Tex(r"${\mathcal{S}}_3 = $").scale(0.8)
        label2.next_to(m3, LEFT)
        equation2 = VGroup(label, m3)
        equation2.arrange(RIGHT)
        equation2.move_to(LEFT * 3.7 + UP *1.5)
        self.play(FadeIn(Table14), Write(equation2))
        self.wait(1)

        Text4 = Tex(r"Thus, we have a download rate of $\frac{16}{37}$", color = BLUE).scale(0.75)
        #Write under the matrix
        Text4.next_to(equation2, DOWN*0.9)
        self.play(Write(Text4))
        self.wait(14)
        self.play(FadeOut(equation2), FadeOut(Text4), FadeOut(Table14))
        self.wait(0.7)
        Text5 = Tex(r"Thus the communication rate is given by, \\", r"$$\boxed{ \frac{(N-r)(N^{M -1})}{N^{M} - r^M} } $$", color = ORANGE).scale(0.7)
        Text5.move_to(UP*1.8)
        self.play(Write(Text5))
        self.play(Wiggle(Text5[1]))
        self.wait(0.7)

        FinalText = Tex(r"The best rate is obtained for",r" $r = K + T -1$").scale(0.7)
        FinalText.move_to(DOWN*1.8)
        FinalText[1].set_color(BLUE)
        self.play(Write(FinalText))
        self.play(Wiggle(FinalText[1]))
        self.wait(0.9)

        ## ENDING ##
        self.play(FadeOut(Text5), FadeOut(FinalText))
        self.wait(1)




