from manim import *

class MyPlotSceneAnimated(Scene):
    def construct(self):
        # Create a value tracker that updates the scene with an x-value
        vt = ValueTracker(0.001)

        # Declare x and y axes
        ax = Axes(x_range=[0, 40, 4], y_range=[0, 5, 0.5], x_length=8, y_length=6,
                  x_axis_config={"decimal_number_config": {"num_decimal_places": 0}},
                  y_axis_config={"decimal_number_config": {"num_decimal_places": 1}},
                  axis_config={"color": WHITE})
        ax.add_coordinates()

        # Define a function to create the dotted line
        def get_dotted_line(y_value):
            return DashedLine(
                ax.c2p(0, y_value), ax.c2p(ax.x_range[1], y_value), color=YELLOW
            )

        # Declare the two functions but always update their upper end to the ValueTracker
        f1 = always_redraw(lambda: ax.plot(lambda x: (2**(x-1))/((2**x)-1), color=BLUE, x_range=[0.3, vt.get_value()]))

        # Declare two dots to trace the two functions, also pointed to the ValueTracker
        f1_dot = always_redraw(lambda: Dot(
            point=ax.c2p(vt.get_value(), f1.underlying_function(vt.get_value())),
            color=BLUE
        )
        )

        # Find the saturation value (limit) of the function
        saturation_value = np.lim(lambda x: (2**(x-1))/((2**x)-1), np.inf)

        # Create the dotted line, initially hidden
        dotted_line = get_dotted_line(saturation_value)
        self.add(dotted_line)  # Add it to the scene but don't display yet

        # Animate the axis being drawn
        self.play(Write(ax))

        # Add the functions and trace dots
        self.add(f1, f1_dot)

        # Animate the ValueTracker across 6 seconds, updating the plots and tracing dots
        self.play(vt.animate.set_value(37), run_time=5)

        # Reveal the dotted line when the dot reaches x = 8
        def check_and_reveal(mob):
            if vt.get_value() >= 8:
                self.play(FadeIn(dotted_line))
                vt.remove_updater(check_and_reveal) 
                
        vt.add_updater(check_and_reveal)

        # Fade out the dots
        self.play(FadeOut(f1_dot))
        self.wait()
