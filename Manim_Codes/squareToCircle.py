from manim import *

class PlotGraph(Scene):
   def construct(self):
      axes = Axes(
         x_range=[0, 5, 1],
         y_range=[0, 2, 0.5],
         x_length=8,
         y_length=4,
         axis_config={"color": BLUE},
         x_axis_config={"numbers_to_include": np.arange(0, 6, 1)},
         y_axis_config={"numbers_to_include": np.arange(0, 2.5, 0.5)},
      )

      graph = axes.plot(lambda x: 2**(x-1)/((2**x)-1),color=BLUE)

         # Points on the graph
      points = VGroup([Dot(axes.coords_to_point(x, 2**(x-1)/(2**x - 1)), color=YELLOW) for x in np.arange(0.5, 5, 0.5)])

         # Dotted line
      dotted_line = DashedLine(axes.coords_to_point(0, 0.5), axes.coords_to_point(5, 0.5), stroke_width=2)

         # Animations (Modified section)
      self.play(Create(axes), Create(graph))
      self.wait(0.5)
      self.play(Create(points))  # Use 'Create' for the dots
      self.wait(0.5)
      self.play(Create(dotted_line))
      self.wait(1)
