from manim import *

class Refining(Scene):
    def construct(self):
        RefiningText = Tex(r"REFINING", color = BLUE).scale(1.3)
        RefiningText.to_edge(UP).center()
        self.play(Write(RefiningText))
        self.wait(2)

#         Next Frame →
# “Consider the One time pad Secret Sharing method discussed earlier. We achieved a download rate of ½.

        NextFrameText = Tex(r"Consider the One-Time Pad"," Secret Sharing",r" method discussed earlier. We achieved a download rate of ",r"$\frac{1}{2}$", color = WHITE).scale(0.7)
        NextFrameText[1].set_color(ORANGE)
        NextFrameText[3].set_color(YELLOW)
        self.play(ReplacementTransform(RefiningText, NextFrameText))
        self.wait(5)

        NextFrame2 = Tex(r"Consider the PIR setting with ", "N=2",r" where a user wants to download a single file privately ," "out of a total of ", r"M=2 files.", color = WHITE).scale(0.7)
        NextFrame2[1].set_color(ORANGE) #Sets color of N=2 to orange
        NextFrame2[3].set_color(YELLOW) # Sets color of M=2 to yellow
        self.play(ReplacementTransform(NextFrameText, NextFrame2))
        self.wait(0.8)
        self.play(FocusOn(NextFrame2[1]))
        self.wait(1)
        self.play(FadeOut(NextFrame2))
        self.wait(1)

        # Let us now define the files as W^1 , W^2, belongs to F^2_q=. Thus the data base is
        # D = (W^1, W^2) belongs to F^4_q 

        Text1 = Tex(r"Let us denote the files as, ", color = BLUE).scale(0.7)
        Text1.to_edge(UP).center()
        self.play(Write(Text1))
        self.wait(1)
        Text1.generate_target()
        Text1.target.move_to(LEFT*3 + UP*1)
        Text2 = Tex(r" $W^1, W^2$ ","$\in$ ", " ${{F_q}^2}$.",color = WHITE).scale(0.7)
        Text2[0].set_color(ORANGE)
        Text2[2].set_color(YELLOW)
        self.play(MoveToTarget(Text1))
        Text2.next_to(Text1, RIGHT, buff = 0.1)
        self.play(Write(Text2))
        self.wait(1)

        Text3 = Tex(r"Thus the database is, ", r" $D = (W^1, W^2)$", r" $\in$ ", r"${{F_q}^4}$", color = WHITE).scale(0.7)
        Text3[1].set_color(ORANGE)
        Text3[3].set_color(YELLOW)
        Text3.next_to(Text1, DOWN, buff = 0.1)
        self.play(Write(Text3))
        self.wait(1)

        NextText = Tex(r"So let's just assume without loss of generality, that the user is interested in ","$W^1$").scale(0.7)
        NextText.move_to(DOWN*3)
        self.play(Write(NextText))
        self.wait(1)

        #Fade Out everything
        self.play(FadeOut(Text1), FadeOut(Text2), FadeOut(Text3), FadeOut(NextText))
        self.wait(1)

        Chart = ImageMobject("Chart.png").scale(1.2)
        #Take it to top left
        Chart.move_to(UP*2.67 + LEFT*4.5)
        self.play(FadeIn(Chart))
        self.wait(1)

        #Create a bulleted list with the entries as follows:
        #Bullet 1: Queries a_1, a_2 $\in$ span(e_1, e_2) $\subseteq$ F^4_q are chosen unifrormly at random, subject to being linearly independent.
        #Bullet 2: The query b_1 $\in$ span(e_3,e_4) $\subseteq$ F^4_q is chosen uniformly at random subject to being linearly independent, i.e. such that b_1 $\neq$ 0 in this case.
        # These bullets in top right
        blistText = Tex("The Queries are chosen as follows:").scale(0.5)
        blistText.move_to(UP*3.5 + RIGHT*2.5)
        self.play(Write(blistText))

        Blist1 = r"Queries $a_1, a_2$ $\in$ span($e_1, e_2$) $\subseteq$ $F_q^4$ are chosen uniformly at random, subject to being linearly independent."
        Blist2 = r"The query $b_1$ $\in$ span($e_3, e_4$) $\subseteq$ $F_q^4$ is chosen uniformly at random subject to being linearly independent, i.e. such that $b_1 \neq 0$ in this case."

        blist = BulletedList(Blist1, Blist2).scale(0.5)
        blist.next_to(blistText, DOWN, buff = 0.1)
        self.play(blistText.animate.shift(LEFT*2.5))
        self.play(Write(blist))
        self.wait(1)

        # Now write the inner product of D and a_1 using \langle D, a_1 \rangle, 
        # Similarly \langel D, a_2+ b_1 \rangel - \langel D, b_1\rangel = \langel D, a_2 \rangel

        # Write the first and second inner products on left bottom side of the screen, and then on the bottom right, the corresponding texts
        # A linear combination L_1 of the first two entries 
        # A linear combination L_2 of the first two entries    
        # draw a straight arrow from the inner product to the corresponding text 

        # Write the first inner product
        InnerProduct1 = Tex(r"$\langle D, a_1 \rangle$", color = BLUE).scale(0.6)
        InnerProduct1.move_to(DOWN*2.5 + LEFT*3.7)

        # Arrow 1
        Text4 = Tex(r"A linear combination $L_1$ of the first two entries", r" \\ ${W_1}^1$ and ${W_2}^1$ in $W^1$", color = BLUE).scale(0.6)
        Text4.move_to(DOWN*2.5 + RIGHT*3)

        # Write the second inner product
        InnerProduct2 = Tex(r"$\langle D, a_2 + b_1 \rangle - \langle D, b_1 \rangle = \langle D, a_2 \rangle$", color = RED).scale(0.6)
        InnerProduct2.move_to(DOWN*3.5 + LEFT*3.7)

        # Write the corresponding texts
        Text5 = Tex(r"A linear combination $L_2$ of the first two entries",  r" \\ ${W_1}^1$ and ${W_2}^1$ in $W^1$", color = RED).scale(0.6)
        Text5.move_to(DOWN*3.5 + RIGHT*3)
        self.play(Write(InnerProduct1), Write(InnerProduct2), Write(Text4), Write(Text5))
        self.wait(3)

        TextGroup1 = VGroup(InnerProduct1, InnerProduct2)
        TextGroup2 = VGroup(Text4, Text5)
        TextGroup1.generate_target()
        TextGroup1.target.move_to(UP*0.5 + LEFT*3)
        TextGroup2.generate_target()
        TextGroup2.target.move_to(UP*0.5 + RIGHT*3)

        self.play(MoveToTarget(TextGroup1), MoveToTarget(TextGroup2))

        DR = Tex(r"Download Rate for this scheme is ", r"$\frac{2}{3}$").scale(0.7)
        DR.move_to(DOWN*3)
        self.play(Write(DR))
        self.play(Indicate(DR[1]))

        self.play(FadeOut(Chart), FadeOut(blistText), FadeOut(blist), FadeOut(TextGroup1), FadeOut(TextGroup2), FadeOut(DR))
        self.wait(1)  

        NewText1 = Tex(r"This simple technique can be extended when the size of the files are"," greater than 2").scale(0.7)
        NewText1.move_to(UP*3)
        self.play(Write(NewText1))
        self.wait(1)

        #Consider the PIR setting with N = 3 servers where a user wants to download a single file privately out of a total of M = 2 files
        NewText2 = Tex(r"Consider the PIR setting with"," N=3 servers", r" where a user wants to download a single file", " privately", r" out of a total of ", "M=2 files.", color = WHITE).scale(0.7)
        NewText2[1].set_color(BLUE_C) # Sets color of N=3 to orange
        NewText2[3].set_color(YELLOW_C) # Sets color of M=2 to yellow
        self.play(Write(NewText2))
        self.wait(1)
        # Keep it below NewText1
        NewText2.generate_target()
        NewText2.target.next_to(NewText1, DOWN, buff = 0.1)
        self.play(MoveToTarget(NewText2))
        self.wait(1)

        NewText3 = Tex(r"Let us denote the files by $W^1, W^2 \in {F_q}^3$.").scale(0.7)
        NewText3.move_to(LEFT * 3.7 + UP * 0.8)
        self.play(Write(NewText3))
        
        NewText4 = Tex(r"Thus the database is $D = (W^1, W^2) \in {F_q}^6$.").scale(0.7)
        NewText4.next_to(NewText3, DOWN, buff = 0.1)
        self.play(Write(NewText4))
        self.wait(1)

        NewText5 = Tex(r"Also, assume that", " atmost T=2 servers collude.",r" Let the user want to retrieve $W^1$").scale(0.7)
        NewText5.move_to(DOWN*3)
        NewText5[1].set_color(YELLOW_C)
        self.play(Write(NewText5))
        self.wait(1)

        self.play(FadeOut(NewText1), FadeOut(NewText2), FadeOut(NewText3), FadeOut(NewText4), FadeOut(NewText5))
        self.wait(1)

        NewNewText1 = Tex(r"We can directly use the", " secret sharing ", r"scheme to obtain the data about $W^1$").scale(0.7)
        NewNewText1.move_to(UP*3)
        self.play(Write(NewNewText1))
        # circumscrbie the secret sharing
        self.play(Circumscribe(NewNewText1[1]))
        self.wait(1)

        Chart2 = ImageMobject("Chart2.png").scale(1.4)
        Chart3 = ImageMobject("Chart3.png").scale(1.4)

        #Fade In Chart2 on center of screen
        self.play(FadeIn(Chart2))
        self.wait(1)
        Chart2.generate_target()
        Chart2.target.move_to(LEFT*2.67)
        self.play(MoveToTarget(Chart2))

        Chart3.move_to(RIGHT*2.67)
        #CReate Dotted arrow pointing from Chart2 to Chart3
        arrow = Arrow(Chart2.get_center(), Chart3.get_center(), stroke_width = 1.2)
        self.play(GrowArrow(arrow), FadeIn(Chart3))
        self.wait(1)
        Chart3.generate_target()
        Chart3.target.move_to(UP*2.67 + LEFT * 3.67)
        Chart3.target.scale(0.8)
        self.play(FadeOut(Chart2), FadeOut(NewNewText1), FadeOut(arrow), MoveToTarget(Chart3))

        blistText2 = Tex("The Queries are chosen as follows:").scale(0.5)
        blistText2.move_to(UP*3.5 + RIGHT*2.5)
        self.play(Write(blistText2))

        Blist11 = r"Queries $a_1, a_2, a_3 \in$ span($e_1, e_2, e_3$) $\subseteq$ $F_q^6$ are chosen uniformly at random, subject to being linearly independent."
        Blist22 = r"The query $b_1, b_2$ $\in$ span($e_4, e_5, e_6$) $\subseteq$ $F_q^6$ are chosen uniformly at random subject to being linearly independent."

        blist = BulletedList(Blist11, Blist22).scale(0.5)

        blist.next_to(blistText2, DOWN, buff = 0.1)
        self.play(blistText2.animate.shift(LEFT*2.5))
        self.play(Write(blist))
        self.wait(1)

        Uhh = Tex(r"The Download Rate here is ", r"$\frac{3}{5}$", r"!! This is better than,"," the rate obtained in the secret sharing which was",r" $\frac{1}{2}$" ).scale(0.7)
        Uhh.move_to(DOWN*3)
        Uhh[1].set_color(ORANGE) #Sets color of 3/5 to orange
        Uhh[4].set_color(ORANGE) #Sets color of 1/2 to orange
        self.play(Write(Uhh))
        self.play(Indicate(Uhh[1]))

        self.wait(2)
        #Fade Out everything
        self.play(FadeOut(Chart3), FadeOut(blistText2), FadeOut(blist), FadeOut(Uhh))
        self.wait(1)

        FinalText = Tex(r"In general", ", we can refine an $(N, N-T, T)$-ramp secret sharing scheme \\ with download rate,",r"  $1 - \frac{T}{N}$  ", r"to obtain a refined PIR scheme with \\ optimal download rate of", r"  $\frac{(N-T)\cdot N}{N^2 - T^2}$  ").scale(0.7)
    
        FinalText[2].set_color(ORANGE) #Sets color of 1 - T/N to orange
        FinalText[4].set_color(PURE_RED) #Sets color of (N-T)N/N^2 - T^2 to yellow
        self.play(Write(FinalText))
        self.play(Wiggle(FinalText[2]), Wiggle(FinalText[4]))
        self.wait(1)

        self.play(FadeOut(FinalText))
        self.wait(1)
























