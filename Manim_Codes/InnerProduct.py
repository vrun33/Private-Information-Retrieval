from manim import *

class InnerProduct(Scene):
    def construct(self):
        # Create vectors
        v1 = np.array([3, 1, 0])
        v2 = np.array([1, 2, 1])
        vector1 = Vector(v1, color=BLUE)
        vector2 = Vector(v2, color=BLUE)
        dot_product = np.dot(v1, v2)
        dot_text = MathTex(r"\vec{v}_1 \cdot \vec{v}_2 = ", str(dot_product)).to_corner(UL)
        dot_text[1].set_color(YELLOW)

        # Display vectors
        self.play(Create(vector1), Create(vector2))
        self.wait(1)

        # Display dot product
        self.play(Write(dot_text))
        self.wait(1)

        # Remove vectors and dot product
        self.play(FadeOut(vector1), FadeOut(vector2), FadeOut(dot_text))
        self.wait(1)

        # Create vectors
        v1 = np.array([3, 1, 0])
        v2 = np.array([1, 2, 1])
        vector1 = Vector(v1, color=BLUE)
        vector2 = Vector(v2, color=BLUE)
        dot_product = np.dot(v1, v2)
        dot_text = MathTex(r"\vec{v}_1 \cdot \vec{v}_2 = ", str(dot_product)).to_corner(UL)
        dot_text[1].set_color(YELLOW)

        # Display vectors
        self.play(Create(vector1), Create(vector2))
        self.wait(1)

        # Display dot product
        self.play(Write(dot_text))
        self.wait(1)

        # Remove vectors and dot product
        self.play(FadeOut(vector1), FadeOut(vector2), FadeOut(dot_text))
        self.wait(1)

        # Create vectors
        v1 = np.array([3, 1, 0])
        v2 = np.array([1, 2, 1])
        vector1 = Vector(v1, color=BLUE)
        vector2 = Vector(v2, color=BLUE)
        dot_product = np.dot(v1, v2)
        dot_text = MathTex(r"\vec{v}_1 \cdot \vec{v}_2 = ", str(dot_product)).to_corner(UL)
        dot_text[1].set_color(YELLOW)

        # Display vectors
        self.play(Create(vector1), Create(vector2))
        self.wait(1)
        