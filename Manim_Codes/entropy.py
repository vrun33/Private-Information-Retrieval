from manim import *

class EntropyScene(Scene):
    def construct(self):
        Text1 = Text("For random variables X and Y").scale(0.55)
        ShannonEntropy = Tex("Shannon Entropy", color = BLUE).scale(0.9)
        Text1.move_to(UP*3.5 + LEFT*4.5)
        self.play(Write(Text1))
        #First Display Shannon Entropy, then shift it to the left and display the formula, and then take it to a top corner below Text1
        self.play(Write(ShannonEntropy))
        self.play(ShannonEntropy.animate.shift(LEFT*3))
        entropy_formula = MathTex(
            r"H(X) = - \sum_{x} P(x_i) \log_2 P(x_i)", color = BLUE
        ).scale(0.85)

        entropy_formula.next_to(ShannonEntropy, RIGHT)
        self.play(ShannonEntropy.animate.shift(UP*0.15))
        self.play(Write(entropy_formula))
        groupShannon = VGroup(ShannonEntropy, entropy_formula)
    
        self.wait(1)
        # Animation for moving and resizing
        # move to top left corner
        groupShannon.generate_target()
        groupShannon.target.scale(0.8)
        groupShannon.target.move_to(UP*2 + LEFT*2.5)
        self.play(MoveToTarget(groupShannon))

        ConditionalEntropy = Tex("Conditional Entropy", color = RED).scale(0.9)
        self.play(Write(ConditionalEntropy))
        self.play(ConditionalEntropy.animate.shift(LEFT*3.5))
        conditional_entropy_formula = MathTex(
            r"H(X|Y) = - \sum_{x,y} P(x_i, y_i) \log_2 P(x_i | y_i)", color = RED
        ).scale(0.85)

        conditional_entropy_formula.next_to(ConditionalEntropy, RIGHT)
        self.play(ConditionalEntropy.animate.shift(UP*0.15))
        self.play(Write(conditional_entropy_formula))
        groupConditional = VGroup(ConditionalEntropy, conditional_entropy_formula)
        self.wait(1)

        # Animation for moving and resizing
        # move to bottom left corner
        groupConditional.generate_target()
        groupConditional.target.scale(0.8)
        groupConditional.target.move_to(DOWN*2.7 + LEFT*2)
        self.play(MoveToTarget(groupConditional))

        Text2 = Text("Do we have any shared information between X and Y?").scale(0.75)
        self.play(Write(Text2))
        MutualInformation = Tex("Mutual Information", color = ORANGE).scale(0.9)
        self.wait(2)
        #Transform Text2 into Mutual Information
        self.play(Transform(Text2, MutualInformation))
        self.play(Text2.animate.shift(LEFT*4.5))


        mutual_information_formula = MathTex(
            r"I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X) ",  # First part
            color = ORANGE
        ).scale(0.85)

        # Positioning:
        mutual_information_formula.next_to(Text2, RIGHT)
        self.play(Write(mutual_information_formula))
        groupMutual = VGroup(Text2, mutual_information_formula)
        self.wait(1)
        # Animation for moving and resizing
        # move to middle
        groupMutual.generate_target()
        groupMutual.target.scale(0.8)
        groupMutual.target.move_to(RIGHT*0.25 + DOWN * 0.3)
        self.play(MoveToTarget(groupMutual))
        self.wait(2)
        # Use Indicate and wiggle to highlight all formulae
        self.play(Indicate(entropy_formula), wiggle = True)
        self.wait(0.7)
        self.play(Indicate(conditional_entropy_formula), wiggle = True)
        self.wait(0.7)
        self.play(Indicate(mutual_information_formula), wiggle = True)
        self.wait(5) 
