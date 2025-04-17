from manim import *

class BulbScene(Scene):
    def construct(self):
        # Define the dimensions of the rectangle
        width = 3
        height = 4
        
        # Create a white rectangle
        rectangle = Rectangle(width=width, height=height, color=WHITE, fill_opacity=1)
        
        # Define the number of lines and the spacing between them
        num_lines = 10
        line_spacing = height / (num_lines + 1)
        
        # Generate equidistant black parallel lines inside the rectangle
        lines = VGroup()
        for i in range(num_lines):
            y_position = -height / 2 + (i + 1) * line_spacing
            line = Line(start=LEFT * width / 2 , end=RIGHT * width / 2 , color=BLACK)
            line.shift(UP * y_position)
            lines.add(line)
        
        # Shift the paper to the left of the screen
        #rectangle.shift(LEFT * 4)
        #lines.shift(LEFT * 4)
        

        #IMAGES
        ManThinking = ImageMobject("ManThinking.png").scale(0.8)
        BulbGlow = ImageMobject("BulbGlow.png").scale(0.8)


        self.play(FadeIn(ManThinking))
        self.wait(3)
        #Replace ManThinking with BulbGlow
        self.play(FadeOut(ManThinking), run_time = 0.01)
        self.play(FadeIn(BulbGlow))

        BulbGlow.generate_target()
        BulbGlow.target.move_to(LEFT * 2)
        self.play(MoveToTarget(BulbGlow)) 

        # Define the dimensions of the rectangle
        # XYZ.animate.shift(LEFT * 4)
        # XYZ.generate_target()
        # XYZ.target.shift(LEFT * 4)
        # self.play(MoveToTarget(XYZ))
        width = 3
        height = 4
        
        # Create a white rectangle
        rectangle = Rectangle(width=width, height=height, color=WHITE, fill_opacity=1)
        
        # Define the number of lines and the spacing between them
        num_lines = 10
        line_spacing = height / (num_lines + 1)
        
        # Generate equidistant black parallel lines inside the rectangle
        lines = VGroup()
        for i in range(num_lines):
            y_position = -height / 2 + (i + 1) * line_spacing
            line = Line(start=LEFT * width / 2 , end=RIGHT * width / 2 , color=BLACK)
            line.shift(UP * y_position)
            lines.add(line)
        
        # Shift the paper to the left of the screen
        #rectangle.shift(LEFT * 4)
        #lines.shift(LEFT * 4)
        
        # Assemble the scene
        #self.add(rectangle, lines)
        together = VGroup(rectangle,lines)
        together.shift(RIGHT * 2)
        self.play(Create(together))

        #rectangle.shift(LEFT * 4)
        #lines.shift(LEFT * 4)

        #FadeOut Image
        self.play(FadeOut(BulbGlow))
        #shifting to target
        together.generate_target()
        together.target.move_to(LEFT * 4)
        self.play(MoveToTarget(together))

        self.wait(2)

       #Create a computer using shapes
        border = RoundedRectangle(width=6, height=4, corner_radius=0, color=WHITE)
        screen = RoundedRectangle(width=5.5, height=3.5, corner_radius=0, color=WHITE)
        # fill screen with white color
        screen.set_fill(color=WHITE,opacity=1)

        computer = VGroup(border, screen)
        computer.shift(RIGHT*3)
        self.play(Create(computer))
        self.wait(2)

        search_bar = RoundedRectangle(width=4,height=1,corner_radius=0.1,color=GREY)
        search_bar.set_fill(color=GREY,opacity=1)
        search_bar.shift(RIGHT*3)
     #   search_bar.shift(UP*1)
        self.play(Create(search_bar))
        #typed google on top of search bar
        googleText = Tex("Google",color=RED).scale(1.2)
        googleText.move_to(search_bar.get_top()+UP*0.65)
        self.play(Write(googleText))
        
        self.wait(1)
         #search bar searching text
        research = Tex("Research works on…",color=BLACK).scale(0.65)
        research.move_to(search_bar.get_top()+DOWN*0.5)
        self.play(Write(research))

        self.wait(2)
        remove = VGroup(search_bar,googleText,research)
        self.play(FadeOut(together), FadeOut(computer), FadeOut(remove))
        

