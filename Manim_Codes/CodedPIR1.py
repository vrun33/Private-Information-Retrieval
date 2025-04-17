from manim import *

class CodedPIR1(Scene):
    def construct(self):
        MDSText = Tex(r"The data storage employs a fixed erasure code,"," typically a", r" Maximum Distance Separable (MDS) Code.").scale(0.8)
        MDSText[2].set_color(YELLOW) # Sets color of "Maximum Distance Separable (MDS) Code" to yellow
        MDSText.to_edge(UP).center()
        self.play(Write(MDSText))
        self.play(Indicate(MDSText[2]))
        self.wait(9)
        self.play(FadeOut(MDSText))
        self.wait(1)
        ConsiderText = Tex("Consider a scenario where M=2 messages", r" ($X_1,X_2$), ($Y_1,Y_2$) $\in {F_5}^2$", " are stored using a", r" \textbf{(4, 2)}", "-MDS code.").scale(0.8)
        ConsiderText[3].set_color(ORANGE) # Sets color of "\textbf{(4, 2)}" to orange
        ConsiderText.to_edge(UP).center()
        self.play(Write(ConsiderText))
        self.play(Indicate(ConsiderText[3]))
        self.wait(1)

        self.play(FadeOut(ConsiderText))
        self.wait()

        Table10 = ImageMobject("table-10.png").scale(2.5)
        Table10.to_edge(UP).center()
        self.play(FadeIn(Table10))
        
        SupposeText = Tex("Suppose that the user is interested in the first message, ",r"$X = (X_1,X_2) \in {F_5}^2$",", and that atmost T=2 servers collude").scale(0.8)
        SupposeText.move_to(DOWN*3)
        self.play(Write(SupposeText))
        self.wait(4)

        self.play(FadeOut(Table10),FadeOut(SupposeText))
        self.wait(1)

        Table11 = ImageMobject("table-11.png").scale(2.5)
        Table11.to_edge(UP).center()
        self.play(FadeIn(Table11))
        self.wait(15)
        Table11.generate_target()
        Table11.target.move_to(UP*3)
        Table11.target.scale(0.7)

        #Equations in the center, one below the previous
        Eqn1 = Tex(r"$G_1 = \langle D_1, R\rangle = X_1R_1 + Y_1R_2$ \\ $G_2 = \langle D_2,S\rangle = X_2S_1 + Y_2S_2$ \\ $G_3 = \langle D_3, R+S\rangle = (X_1 + X_2)(R_1 + S_1) + (Y_1 + Y_2)(R_2 + S_2)$ \\ $G_4 = \langle D_4, e_1 + R + 2S\rangle = (X_1 + 2X_2)(1 + R_1 + 2S_1) + (Y_1 + 2Y_2)(R_2 + 2S_2)$").scale(0.7)

        self.play(MoveToTarget(Table11),Write(Eqn1))
        self.wait(4)

        Eqn2 = Tex(r"$0 = \langle D_1, R \rangle + 3 \langle D_2, S \rangle + 3 \langle D_3, R + S \rangle + \langle D_4, R + 2S \rangle$", color = ORANGE).scale(0.8)
        self.play(ReplacementTransform(Eqn1, Eqn2))
        self.wait(0.5)
        self.play(Wiggle(Eqn2))
        self.wait(1)

        Eqn3 = Tex(r"$X_1 + 2X_2 = \langle D_1, R \rangle + 3 \langle D_2, S \rangle + 3 \langle D_3, R + S \rangle + \langle D_4, e_1, R + 2S \rangle$", color = ORANGE).scale(0.8)
        # Below Eqn2 
        Eqn3.next_to(Eqn2, DOWN)
        self.play(Write(Eqn3))
        self.wait(5)    
        # Move the table11 and eqn3 to top left corner
        Table11.generate_target()
        Table11.target.move_to(LEFT*4 + UP*3.2)
        Table11.target.scale(0.5)
        EqnGroup = VGroup(Eqn2, Eqn3)
        EqnGroup.generate_target()
        EqnGroup.target.scale(0.5)
        EqnGroup.target.move_to(LEFT*4 + UP * 2.5)

        Table12 = ImageMobject("table-12.png").scale(0.7)
        Table12.move_to(RIGHT*4 + UP*3.2)
        self.play(FadeIn(Table12))

        self.play(MoveToTarget(EqnGroup), MoveToTarget(Table11), FadeIn(Table12))        
        self.wait(4)

        Eqn4 = Tex(r"$X_1 + X_2 = \langle D_1, R \rangle + 3 \langle D_2, S \rangle + 3 \langle D_3, e_1 + R + S \rangle + \langle D_4, R + 2S \rangle$", color = ORANGE).scale(0.7)
        Eqn4.to_edge(UP).center()
        self.play(Write(Eqn4))
        self.wait(1)
        self.play(FadeOut(Table11), FadeOut(Table12), FadeOut(Eqn2))

        Table102 = ImageMobject("table-10.png").scale(2.2)
        Table102.move_to(LEFT*3.7 + UP*2.8)

        Eqn3.generate_target()
        Eqn3.target.move_to(RIGHT* 3.7 + UP * 3.0)
        Eqn3.target.scale(1.1)

        Eqn4.generate_target()
        Eqn4.target.move_to(RIGHT*3.4 + UP*2.6)
        Eqn4.target.scale(0.7)
        self.play(FadeIn(Table102), MoveToTarget(Eqn3), MoveToTarget(Eqn4))
        self.wait(3)

        self.play(Wiggle(Eqn4), Wiggle(Eqn3))

        FinalText = Tex("The Download Rate for this example is", r" $\frac{1}{4}$").scale(0.8)
        FinalText.to_edge(DOWN)
        self.play(Write(FinalText))
        self.wait(7)
        self.play(FadeOut(FinalText), FadeOut(Eqn3), FadeOut(Eqn4), FadeOut(Table102))
        self.wait(1)















        


