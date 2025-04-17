from manim import *

class BasicTextualScene(Scene):
    def construct(self):
        Text1 = Tex(r"In 1948, ", "Shannon", r" published a seminal paper in which he introduced the concept of ",  
                    "perfect security for encryption schemes", color=WHITE).scale(0.8)
        Text1[1].set_color(ORANGE)  # Color "Shannon"
  # Underline the desired phrase
        Text1.to_edge(UP).center() 

        self.play(Write(Text1))
        self.wait(1)
        self.play(Circumscribe(Text1[3]))
        self.wait(2)

        Text2 = Tex(r"A ","cryptographic scheme",r" is said to be", " perfectly secure", r" if the mutual information between the message M, and the received signal X is ","zero.", color=WHITE).scale(0.8)
        Text2[1].set_color(YELLOW)  # Color "cryptographic scheme"
        self.play(ReplacementTransform(Text1, Text2))
        self.wait(1)
        self.play(Indicate(Text2[3]), Circumscribe(Text2[5]), run_time=2)
        self.wait(1)

        Text2.generate_target()
        Text2.target.to_edge(UP)
        Text2.target.scale(0.6)
        self.play(MoveToTarget(Text2))
        self.wait(1)

        circle1 = Circle(radius=1.5, color=BLUE)
        circle2 = Circle(radius=1.5, color=YELLOW)
        circle1.shift(LEFT*2)
        circle2.shift(RIGHT*2)
        #Draw circle2 in reverse direction
        circle2.reverse_direction()
        self.play(Create(circle1), Create(circle2))
        M = Tex("M", color=BLUE).scale(0.8)
        M.move_to(circle1.get_center())
        X = Tex("X", color=YELLOW).scale(0.8)
        X.move_to(circle2.get_center())
        self.play(Write(M), Write(X))

        MCircle = VGroup(circle1, M)
        XCircle = VGroup(circle2, X)
        NoInt = Tex("No Intersection!", color = RED).scale(0.8)
        NoInt.move_to(DOWN*2)
        self.play(Create(NoInt))
        self.wait(1)
        MCircle.generate_target()
        MCircle.target.shift(UP*3 + LEFT * 4)
        MCircle.target.scale(0.5)
        XCircle.generate_target()
        XCircle.target.shift(UP*3 + RIGHT * 4)
        XCircle.target.scale(0.5)

        self.play(FadeOut(NoInt), MoveToTarget(MCircle), MoveToTarget(XCircle))
        # Now animate the equations in order as below:
        # The mutual Information between M and X I(M;X), then Fade out the sentence before, and shift I(M;X) to the left
        I = MathTex("I(M;X)", color = RED).scale(0.7)
        MutuMX = Tex("Consider the mutual information between M and X", color = WHITE).scale(0.7)
        MutuMX.to_edge(UP).center()
        I.next_to(MutuMX, DOWN)
        self.play(Write(MutuMX), Write(I))
        self.wait(1)
        self.play(FadeOut(MutuMX))
        I.generate_target()
        I.target.shift(UP*2+ LEFT * 3.5)
        I.target.scale(1.3)
        self.play(MoveToTarget(I))
        Equals = MathTex("=", color = RED).scale(0.7)
        Form1 = MathTex(r"H(X)", color = RED).scale(0.9)
        Minus = MathTex("-", color = RED).scale(1.0)
        Form2 = MathTex(r"H(X|M)", color = RED).scale(0.9)
        Equals.next_to(I, RIGHT)
        Form1.next_to(I, RIGHT*2.2)
        Minus.next_to(Form1, RIGHT)
        Form2.next_to(Minus, RIGHT)
        self.play(Write(Equals), Write(Form1), Write(Minus), Write(Form2))

        Group1 = VGroup(Equals, Form1, Minus, Form2)
        Group1copy = Group1.copy()
        # Copy Group1copy below Group1
        Group1copy.generate_target()
        Group1copy.target.shift(DOWN*1)
        self.wait(0.7)
        self.play(MoveToTarget(Group1copy))

        Exp3 = MathTex(r"H(M + R|M)", color = RED).scale(0.9)
        Exp4 = MathTex(r"H(R)", color = RED).scale(0.9)
        # use script F inside the log
        Exp5 = MathTex(r"\log(|\mathbb{F_{q}}|)", color=RED).scale(0.9)
        Exp6 = MathTex(r"\log(|\mathbb{F_{q}}|)", color=RED).scale(0.9)
        Exp7 = MathTex("0", color = RED).scale(0.9)
        
        # Replace Form 2 with Exp3 in the lower equation
        
        # Then shift this newer equation down again and replace Exp3 with Exp4 
        #Now shift this equation again, and replace both Exp4 and Form1 with Exp5
        # Finally, shift this equation down and replace the entire equation with 0 (Exp6)

        # ... Replace Form 2 with Exp3 in the lower equation ...
        Exp3.next_to(Group1copy.submobjects[2], RIGHT)
        self.play(ReplacementTransform(Group1copy.submobjects[3], Exp3))  # Replace Form2

        # ... Then shift this newer equation down again and replace Exp3 with Exp4 ...
        new_group_target = Group1copy.copy()
        new_group_target.generate_target()
        new_group_target.target.shift(DOWN)
        self.play(MoveToTarget(new_group_target))  # Shift down
        self.wait(0.5)
        Exp4.next_to(new_group_target.submobjects[2], RIGHT)
        self.play(ReplacementTransform(new_group_target.submobjects[3], Exp4))  # Replace Exp3

        new2_group_target = new_group_target.copy()
        new2_group_target.generate_target()
        new2_group_target.target.shift(DOWN)
        self.play(MoveToTarget(new2_group_target))  # Shift down
        self.wait(0.5)
        Exp5.next_to(new2_group_target.submobjects[0], RIGHT)
        new2_group_target.submobjects[2].next_to(Exp5, RIGHT)
        Exp6.next_to(new2_group_target.submobjects[2], RIGHT)
        self.play(ReplacementTransform(new2_group_target.submobjects[1], Exp5), ReplacementTransform(new2_group_target.submobjects[3], Exp6))  # Replace Exp3

        new3_group_target = new2_group_target.copy()
        new3_group_target.generate_target()
        new3_group_target.target.shift(DOWN)
        self.play(MoveToTarget(new3_group_target))
        self.wait(0.5)
        
        Exp7.next_to(new3_group_target.submobjects[0], RIGHT)
        TempGroup = VGroup(new3_group_target.submobjects[1], new3_group_target.submobjects[2], new3_group_target.submobjects[3])
        self.play(ReplacementTransform(TempGroup, Exp7))
        self.wait(0.5)
        self.play(Indicate(Exp7))
        self.wait(0.5)

        #Fade Out everything on the screen and write the final statement as below:
        # To construct asymptotically optimal PIR schemes for any number of servers N, with up to T collisions, we explore a generalisation of the one-time pad called secret sharing
        # Secret Sharing Being in orange

        self.play(*[FadeOut(mob) for mob in self.mobjects])  

# Write the final statement
        final_statement = Tex(
            r"To construct asymptotically optimal PIR schemes for any number of servers N, ",
            r"with up to T collisions, we explore a generalisation of the one-time pad called ",
            r"secret sharing", 
            color=WHITE
        ).scale(0.7)

        secret_sharing_text = final_statement[2].set_color(ORANGE)
        final_statement.to_edge(UP).center() 

        self.play(Write(final_statement))
        self.wait(1)
        self.play(Wiggle(secret_sharing_text))
        self.play(*[FadeOut(mob) for mob in self.mobjects])  
        self.wait(2) 



        

