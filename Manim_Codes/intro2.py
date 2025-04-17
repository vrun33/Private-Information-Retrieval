from manim import *

class QuoteScene(Scene):
    def construct(self):
        quote = Tex("In an age of digital exposure, the ability to retrieve information privately is a shield against prying eyes.", color=WHITE).scale(0.8En)  # Move to top, centered

        author = Tex("- Anonymous", font_size=36, color=GRAY)
        author.to_edge(RIGHT)  # Align to right edge
        author.move_to(DOWN*1.5)
        # Display quote and author
        self.play(Write(quote), run_time = 3)  # Fade in author from right
        self.wait(1.5)  # Wait for 2 seconds
        self.play(Write(author))
        self.wait(2)  # Wait for 3 seconds
        # Fade out quote and author
        self.play(FadeOut(quote), FadeOut(author))

