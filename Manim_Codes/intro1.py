from manim import *

class Intro1(Scene):
    def construct(self):
        Title = Text("A Guided Walk Through Coded Private Information Retrieval", color=BLUE).scale(0.7)
        jumbled_text = Text("010010000110010101101100011011000110111101010001").scale(1.2)
        jumbled_text.set_color_by_gradient(GREEN, YELLOW, RED)
        author1 = Text("M.P Samartha").scale(0.55)
        author1.move_to(DOWN*2 + RIGHT*5)
        author2 = Text("Sarvesh Takbhate").scale(0.55)
        author2.move_to(DOWN*2.5 + RIGHT*5)
        author3 = Text("Varun Shastry").scale(0.55)
        author3.move_to(DOWN*3 + RIGHT*5)
        #Title on top, authors in bottom right
        self.play(Write(jumbled_text))
        self.play(jumbled_text.animate.shift(UP*1.5), Transform(jumbled_text, Title), run_time=2)
        #
        self.play(Write(author1), Write(author2), Write(author3))
        #fade out authors
        self.play(FadeOut(author1), FadeOut(author2), FadeOut(author3), FadeOut(jumbled_text), FadeOut(Title))





