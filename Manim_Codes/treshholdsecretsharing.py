from manim import *

class threshholdsecretsharing(Scene):
    def construct(self):
        #in the below text i want n-degree in orange color and n+1 distinct in aslo orange and rest in white


        text = Text("We will now show that for any n-degree Polynomial,we need exactly n+1 distinct point on the plane to pinpoint the curve.").scale(0.35)
        self.play(Write(text))
        self.play(FadeOut(text),run_time=1)

        self.wait(2)

        #i want to create a graph with xlim and ylim
        #xlim = (-5,5) and ylim = (-5,5)

        #hre i want to label my axis as x and y with proper location

        #i want to show the plane in blue color

        
        
        plane = NumberPlane(x_range=[-7, 7], y_range=[-7, 7])
        plane.add_coordinates()

        #in this can you add the x and y label with proper location
        #i want to show the x label in the upper right corner of the x-axis
        #i want to show the y label in the upper right corner of the y-axis

        

        # Label the x and y axes
        x_label = Text("x", font_size=24).next_to(plane.get_x_axis(), UR)
        y_label = Text("y", font_size=24).next_to(plane.get_y_axis(), UR)
        self.play(Create(plane), Write(x_label), Write(y_label))

        # Define the points
        points = [(0.5, 1.25), (4,3), (2,-1)]

        # Create dots for the points
        dot_labels = VGroup()
        dots = VGroup()
        for point in points:
            dot = Dot(plane.coords_to_point(*point), color=ORANGE)
            dots.add(dot)
            label = Text(f"({point[0]}, {point[1]})", font_size=16).next_to(dot, UP)
            dot_labels.add(label)

        self.play(Create(dots), Write(dot_labels))

        # Quadratic function through the points
        def quadratic_function(x):
            return x**2 - 4*x + 3

        # Graph of the quadratic function
        graph = FunctionGraph(quadratic_function, x_range=[-7, 7], color=PURE_GREEN)
        self.play(Create(graph))

        self.wait()

        #now i have to wiggle all the dots

        self.play(Wiggle(dots[0]),Wiggle(dots[1]),Wiggle(dots[2]))

       # self.play(Wiggle(point1),Wiggle(point2),Wiggle(point3))


        #now i want to create a graph y = x^2 - 4x +3
        #i want to show this graph in red color
        #i want to show this graph only in the range of -5 to 5
        #i want to show this graph in the plane




        #self.wait(2)

        self.wait(2)







           