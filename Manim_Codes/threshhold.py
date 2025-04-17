from manim import *

#write a function which take in the surrounding rectangle, and animates to change its stroke width to 10 and then to 2
def change_stroke_width(self, square, colour):
        rect1 = SurroundingRectangle(square, color=colour, buff=0)
        rect1.stroke_width=3.5
        self.play(Create(rect1))

        rect2 = SurroundingRectangle(square, color=colour, buff=0)
        rect2.stroke_width=10
        self.play(Transform(rect1,rect2))

        rect3 = SurroundingRectangle(square, color=colour, buff=0)
        rect3.stroke_width=3.5
        self.play(Transform(rect1,rect3))

class threshhold(Scene):
    def construct(self):
        floppy = ImageMobject("floppy.png").scale(0.5)
        floppy.move_to(ORIGIN)
        rect1 = SurroundingRectangle(floppy, color=PURE_RED, buff=0)
        rect1.stroke_width=3.5
        self.play(FadeIn(floppy))
        
        self.play(Create(rect1))
        
   
        #Now i have to generate 8 small squares at 45 degree each of the floppy
        square1 = Square(side_length=1.2, fill_color=BLUE, fill_opacity=1)
        square1.move_to(UP*2.5+LEFT*4.5)

        square2 = Square(side_length=1.2, fill_color=BLUE, fill_opacity=1)
        square2.move_to(UP*2.5+RIGHT*4.5)
       
        square3 = Square(side_length=1.2, fill_color=BLUE, fill_opacity=1)
        square3.move_to(UP*2.5)
    
        square4 = Square(side_length=1.2, fill_color=BLUE, fill_opacity=1)
        square4.move_to(DOWN*2.5)

        square5 = Square(side_length=1.2, fill_color=BLUE, fill_opacity=1)
        square5.move_to(DOWN*2.5+LEFT*4.5)

        square6 = Square(side_length=1.2, fill_color=BLUE, fill_opacity=1)
        square6.move_to(DOWN*2.5+RIGHT*4.5)

        square7 = Square(side_length=1.2, fill_color=BLUE, fill_opacity=1)
        square7.move_to(RIGHT*4.5)
    
        square8 = Square(side_length=1.2, fill_color=BLUE, fill_opacity=1)
        square8.move_to(LEFT*4.5)

        self.play(Create(square1),Create(square2),Create(square3),Create(square4),Create(square5),
                  Create(square6),Create(square7),Create(square8))

        #now i want borders to each square created just like floppy
        rect2 = SurroundingRectangle(square1, color=PURE_RED, buff=0)
        rect2.stroke_width=3.5

        rect3 = SurroundingRectangle(square2, color=PURE_RED, buff=0)
        rect3.stroke_width=3.5
       
        rect4 = SurroundingRectangle(square3, color=PURE_RED, buff=0)
        rect4.stroke_width=3.5
       
        rect5 = SurroundingRectangle(square4, color=PURE_RED, buff=0)
        rect5.stroke_width=3.5

        rect6 = SurroundingRectangle(square5, color=PURE_RED, buff=0)
        rect6.stroke_width=3.5

        rect7 = SurroundingRectangle(square6, color=PURE_RED, buff=0)
        rect7.stroke_width=3.5

        rect8 = SurroundingRectangle(square7, color=PURE_RED, buff=0)
        rect8.stroke_width=3.5

        rect9 = SurroundingRectangle(square8, color=PURE_RED, buff=0)
        rect9.stroke_width=3.5

        self.play(Create(rect2),Create(rect3),Create(rect4),Create(rect5),
                  Create(rect6),Create(rect7),Create(rect8),Create(rect9))

        # send the required shape and color in the parameters
        #change_stroke_width(self, floppy, PURE_RED)
        change_stroke_width(self, square1, PURE_GREEN)
        change_stroke_width(self, square8, PURE_GREEN)
        change_stroke_width(self, square5, PURE_GREEN)
        change_stroke_width(self, square4, PURE_GREEN)

        #now from each of the square i want to draw a dotted line to the floppy
        line1 = DashedLine(start=square1.get_center(), end=floppy.get_center(), color=PURE_GREEN)
        line2 = DashedLine(start=square8.get_center(), end=floppy.get_center(), color=PURE_GREEN)
        line3 = DashedLine(start=square5.get_center(), end=floppy.get_center(), color=PURE_GREEN)
        line4 = DashedLine(start=square4.get_center(), end=floppy.get_center(), color=PURE_GREEN)
        #and as soon as my line4 reaches floppy, i want to change the color of floppy to green
        self.play(Create(line1),Create(line2),Create(line3),Create(line4))
        #now i want one arrow on each dotted line
        

        #self.wait()
        #self.play(FadeOut(rect1),FadeOut(rect2),FadeOut(rect3),FadeOut(rect4),FadeOut(rect5),FadeOut(rect6),FadeOut(rect7),FadeOut(rect8),FadeOut(rect9))
        change_stroke_width(self, floppy, PURE_GREEN)
        
        #i want to remove my dotted lines
        self.play(FadeOut(line1),FadeOut(line2),FadeOut(line3),FadeOut(line4),run_time =1)
        #now i want my floppy an squares to get red color again as soon as the floppy changes to green
        #i want them to turn red immidiately

        rect10 = SurroundingRectangle(floppy, color=PURE_RED, buff=0)
        rect10.stroke_width=3.5

        rect11 = SurroundingRectangle(square1, color=PURE_RED, buff=0)
        rect11.stroke_width=3.5

        rect12 = SurroundingRectangle(square8, color=PURE_RED, buff=0)
        rect12.stroke_width=3.5

        rect13 = SurroundingRectangle(square5, color=PURE_RED, buff=0)
        rect13.stroke_width=3.5

        rect14 = SurroundingRectangle(square4, color=PURE_RED, buff=0)
        rect14.stroke_width=3.5

        self.play(Create(rect10),Create(rect11),Create(rect12),Create(rect13),Create(rect14))

        # change_stroke_width(self, square2, PURE_GREEN)
        # change_stroke_width(self, square3, PURE_GREEN)
        # change_stroke_width(self, square6, PURE_GREEN)
        # change_stroke_width(self, square8, PURE_GREEN)
        
        # line5 = DashedLine(start=square2.get_center(), end=floppy.get_center(), color=PURE_GREEN)
        # line6 = DashedLine(start=square3.get_center(), end=floppy.get_center(), color=PURE_GREEN)
        # line7 = DashedLine(start=square6.get_center(), end=floppy.get_center(), color=PURE_GREEN)
        # line8 = DashedLine(start=square8.get_center(), end=floppy.get_center(), color=PURE_GREEN)
        # self.play(Create(line5),Create(line6),Create(line7),Create(line8))
        
        # change_stroke_width(self, floppy, PURE_GREEN)
        # self.play(FadeOut(line5),FadeOut(line6),FadeOut(line7),FadeOut(line8),run_time =1)
        


        





    