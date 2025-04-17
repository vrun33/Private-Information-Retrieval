from manim import *

class VennDiagram(Scene):
    def construct(self):
        # Configuration
        set_labels = ["X", "Y", "Z"]
        label_positions = [LEFT, UP, RIGHT * 2]  
        colors = [BLUE, GREEN, YELLOW] 

        # Create circles / sets
        circles = VGroup(*[
            Circle(radius=2).set_fill(color, opacity=0.5).set_stroke(color, width=3)
            for color in colors
        ]) 
        circles.arrange_submobjects(RIGHT, buff=1)

        # Add set labels
        labels = VGroup(*[
            Text(label).next_to(circle, direction)
            for label, circle, direction in zip(set_labels, circles, label_positions)
        ])

        # Mutual information area 
        mi_area = Intersection(circles[0], circles[1])
        mi_label = Tex("I(X;Y)").move_to(mi_area)

        # H(X) area (excluding mutual information)
        hx_area = Difference(circles[0], circles[1])
        hx_label = Tex("H(X)").move_to(hx_area)

        # H(Y) area (excluding mutual information)
        hy_area = Difference(circles[1], circles[0])
        hy_label = Tex("H(Y)").move_to(hy_area)

        # Play animations - adjust as needed
        self.play(Create(circles), Write(labels))
        self.play(FadeIn(mi_area), Write(mi_label))
        self.play(FadeIn(hx_area), Write(hx_label))
        self.play(FadeIn(hy_area), Write(hy_label))
