from manim import *

class VennEntropy(Scene):
    def construct(self):
        Hentropy = Tex("H(X)", color = BLUE).scale(0.9)
        HXtext = Text("Consider the entropies of X and Y").scale(0.55)
        Yentropy = Tex("H(Y)", color = YELLOW).scale(0.9)
        HgivenY = MathTex(
            r"H(X|Y)", color = BLUE
        ).scale(0.85)
        YgivenH = MathTex(
            r"H(Y|X)", color = YELLOW
        ).scale(0.85)
        IXY = Tex("I(X;Y)", color = BLACK).scale(1.2)

        # Create the entropy of X
        HXtext.move_to(UP*3+LEFT*1)
        Hentropy.next_to(HXtext, RIGHT)
        Yentropy.next_to(Hentropy, RIGHT)
        self.play(Write(HXtext),run_time=1)
        self.play(Write(Hentropy), Write(Yentropy), run_time=1)
        self.wait(1)
        # Fade out HXtext
        self.play(FadeOut(HXtext))
        #Shift H(X) and H(Y) to the left
        Hentropy.generate_target()
        Yentropy.generate_target()
        Hentropy.animate.shift(LEFT*2)
        Yentropy.animate.shift(LEFT*2)
        self.wait(0.3)
        # Now create a venn diagram with 2 circles intersecting with blue and yellow colors and move target Hentropy and Yentropy to the top left and top right corners
        # Venn diagram with 2 circles
        # Show the intersecting part in orange color
        circle1 = Circle(radius=2.5, color=BLUE)
        circle2 = Circle(radius=2.5, color=YELLOW)
        circle1.shift(LEFT)
        circle2.shift(RIGHT)
        self.play(Create(circle1), Create(circle2))
        Hentropy.generate_target()
        Yentropy.generate_target()
        Hentropy.target.move_to(UP*2.5 + LEFT*3.5)
        Yentropy.target.move_to(UP*2.5 + RIGHT*3.5)
        self.play(MoveToTarget(Hentropy), MoveToTarget(Yentropy))

        # Venn diagram with 3 regions
        circle1 = Circle(radius=2.5, color=BLUE)
        circle2 = Circle(radius=2.5, color=YELLOW)
        circle1.shift(LEFT)
        circle2.shift(RIGHT)

        # Create the Venn diagram group
        venn = VGroup(circle1, circle2).set_fill(opacity=0.4)  
        self.play(Create(venn)) 

        # Reference the shapes for region coloring
        left_region = circle1.copy().set_fill(BLUE, opacity=0.4)
        right_region = circle2.copy().set_fill(YELLOW, opacity=0.4)
        intersection = Intersection(circle1, circle2).set_fill(ORANGE, opacity=0.6)

        self.play(Create(left_region), Create(right_region), Create(intersection))

        HgivenX_arrow = Arrow(LEFT*10,buff=0.15, color=BLUE)
        HgivenX_arrow.next_to(left_region, (LEFT+DOWN))
        HgivenX_arrow.put_start_and_end_on(LEFT*5, circle1.get_center()*0.01 + LEFT*2)
        HgivenX_arrow.rotate(PI/4)
        HgivenY.next_to(left_region, DOWN*1+LEFT*3)
        Text1 = Text("Uncertainty in X, given we know Y", color=RED).scale(0.7)

        # Shift Text1 to the bottom of the screen
        Text1.move_to(DOWN*3)
        self.play(Create(HgivenX_arrow), Write(HgivenY), Write(Text1))
        self.wait(1)
        # Fade out the arrow and transform Text1 to H(X|Y) in place
        self.play(FadeOut(HgivenX_arrow), FadeOut(Text1))
        HgivenY.generate_target()
        HgivenY.target.scale(1.2)
        HgivenY.target.move_to(DOWN*1.5 + LEFT*4.5)
        self.play(MoveToTarget(HgivenY))

        # for Y
        HgivenY_arrow = Arrow(LEFT*10,buff=0.15, color=YELLOW)
        HgivenY_arrow.next_to(right_region, (RIGHT+DOWN))
        HgivenY_arrow.put_start_and_end_on(RIGHT*5, circle2.get_center()*0.01 + RIGHT*2)
        HgivenY_arrow.rotate(-PI/4)
        YgivenH.next_to(right_region, DOWN*1+RIGHT*3)
        Text2 = Text("Uncertainty in Y, given we know X", color=RED).scale(0.7)

        # Shift Text2 to the bottom of the screen
        Text2.move_to(DOWN*3)
        self.play(Create(HgivenY_arrow), Write(YgivenH), Write(Text2))
        self.wait(1)
        # Fade out the arrow and transform Text1 to H(X|Y) in place
        self.play(FadeOut(HgivenY_arrow), FadeOut(Text2))
        YgivenH.generate_target()
        YgivenH.target.scale(1.2)
        YgivenH.target.move_to(DOWN*1.5 + RIGHT*4.5)
        self.play(MoveToTarget(YgivenH))
        
        self.play(Wiggle(intersection))
        Text3 = Text("Information between X and Y", color=RED).scale(0.7)
        Text3.move_to(DOWN*3)
        self.play(Write(Text3))
        self.play(Transform(Text3, IXY))

        self.wait(1) 