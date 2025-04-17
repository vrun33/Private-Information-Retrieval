from manim import *
class Exponential(Scene):
    def construct(self):
        plane=NumberPlane(
            x_range =[0.3, 26, 2],
            y_range=[0, 26, 2],
            x_length= 10,
            y_length=7,
            background_line_style={
                "stroke_color": TEAL_C,
                "stroke_width": 0.5,
                "stroke_opacity": 0.4
            }
        )
        axes = Axes(
            x_range=[0.1, 26, 2],
            y_range=[0, 26, 2],
            x_length=10,
            y_length=7,
            tips=True,
            axis_config={
                "tip_shape": StealthTip,
                "color": GREEN
            },
        ).add_coordinates()

        axis_labels = axes.get_axis_labels(x_label="x", y_label="y")
        graph = axes.plot(lambda x: 2**(x-1)/((2**x)-1),x_range=[0.001,24.5], color=BLUE, stroke_opacity=0.8)
        graph_label = MathTex("y = \\frac{2^{x-1}}{2^x-1}").move_to(axes.coords_to_point(20, 20))

        dot1 = Dot(axes.coords_to_point(1, 1), color=RED)
        dot2 = Dot(axes.coords_to_point(2, 0.666666666667), color=RED)
        dot3 = Dot(axes.coords_to_point(3, 0.571428571429), color=RED)
        dot4 = Dot(axes.coords_to_point(4, 0.516129032258), color=RED)

        #animation
        self.wait()
        self.play(DrawBorderThenFill(plane), Write(axes), Write(axis_labels), run_time=5)
        self.play(Write(axis_labels))
        self.play(FadeIn(VGroup(dot1, dot2, dot3, dot4)), run_time=2)
        self.play(Create(graph), run_time=2)
        self.play(Write(graph_label))
        self.wait()