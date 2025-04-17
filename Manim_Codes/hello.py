from manim import *

class Hellloo(Scene):
    def construct(self):
        text = Text(r"Hello, World!")
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text))
        text2 = Tex("Hello, Manim!")
        self.play(ReplacementTransform(text, text2))
        self.wait(1)
