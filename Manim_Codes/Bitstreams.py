from manim import *
import random

class Bitstreams(Scene):
    def construct(self):
        Man = ImageMobject("Man.png").scale(0.7)
        # Create Man
        self.play(FadeIn(Man))
        Man.generate_target()
        Man.target.move_to(LEFT * 5)
        self.play(MoveToTarget(Man))
       
        # Create a rectangle on the right side of the screen which contains 12 bitstreams of length 25
        rect = Rectangle(height=7.5, width=4.7, color=BLUE)
        rect.move_to(RIGHT * 4)
        self.play(Create(rect))
        
        # Create the 14 bitstreams
        bitstreams = [ 
            Tex("0110101011101001101").scale(0.8),
            Tex("1010101010101011010").scale(0.8),
            Tex("1111111111111101010").scale(0.8),
            Tex("1100110011001100000").scale(0.8),
            Tex("0011001100110011001").scale(0.8),
            Tex("0101010101010101101").scale(0.8),
            Tex("0000000100000010110").scale(0.8),
            Tex("1011011011011011011").scale(0.8),
            Tex("1110001110001111101").scale(0.8),
            Tex("0001110001110011111").scale(0.8),
            Tex("1101101101101110101").scale(0.8),
            Tex("0010010010010011000").scale(0.8),
            Tex("0110101011101001101").scale(0.8),
            Tex("0010010010010000000").scale(0.8)
        ]
        # 
        # for i in range(14):
        #     bitstreams[i].move_to(rect.get_top() +  DOWN * width * i)
        #     self.play(Write(bitstreams[i]), run_time = 0.1)
        # self.wait(3)
        
        #declare an integer variable
        width = 0.50
        #Print all rows together
        bitstreams[0].move_to(rect.get_top() +  DOWN * width * 1)
        bitstreams[1].move_to(rect.get_top() +  DOWN * width * 2)
        bitstreams[2].move_to(rect.get_top() +  DOWN * width * 3)
        bitstreams[3].move_to(rect.get_top() +  DOWN * width * 4)
        bitstreams[4].move_to(rect.get_top() +  DOWN * width * 5)
        bitstreams[5].move_to(rect.get_top() +  DOWN * width * 6)
        bitstreams[6].move_to(rect.get_top() +  DOWN * width * 7)
        bitstreams[7].move_to(rect.get_top() +  DOWN * width * 8)
        bitstreams[8].move_to(rect.get_top() +  DOWN * width * 9)
        bitstreams[9].move_to(rect.get_top() +  DOWN * width * 10)
        bitstreams[10].move_to(rect.get_top() +  DOWN * width * 11)
        bitstreams[11].move_to(rect.get_top() +  DOWN * width * 12)
        bitstreams[12].move_to(rect.get_top() +  DOWN * width * 13)
        bitstreams[13].move_to(rect.get_top() +  DOWN * width * 14)
        self.play(Write(bitstreams[0]), Write(bitstreams[1]), Write(bitstreams[2]), Write(bitstreams[3]), Write(bitstreams[4]), Write(bitstreams[5]), Write(bitstreams[6]), Write(bitstreams[7]), Write(bitstreams[8]), Write(bitstreams[9]), Write(bitstreams[10]), Write(bitstreams[11]), Write(bitstreams[12]), Write(bitstreams[13]))
       

        # Change the color of the 5th bitstream to red
        self.play(bitstreams[4].animate.set_color(RED))
        
        #  Wiggle the 5th bitstream
        self.play(Wiggle(bitstreams[4]))
        self.wait(1)

        # Group the rectangle and bitstreams and reduce its opacity, and move it to the left and shrink a little in size
        bitstreams_group = Group(rect, bitstreams[0], bitstreams[1], bitstreams[2], bitstreams[3], bitstreams[4], bitstreams[5], bitstreams[6], bitstreams[7], bitstreams[8], bitstreams[9], bitstreams[10], bitstreams[11], bitstreams[12], bitstreams[13])
       
        # Copy this group and move it to the left, while the original group is still on the right, and reduces in opacity
        bitstreams_group2 = bitstreams_group.copy()
        bitstreams_group2.generate_target()
        bitstreams_group2.target.move_to(LEFT * 2)
        bitstreams_group2.target.scale(0.6)

        # Draw two lines with opacity 0.4, one from the top of the original rectangle and bottom, to the new rectangle
        line1 = Line(start=rect.get_top() , end=bitstreams_group2.target.get_top(), color=WHITE, stroke_width=1.5)
        line2 = Line(start=rect.get_bottom() , end=bitstreams_group2.target.get_bottom(), color=WHITE, stroke_width=1.5)      
        self.play(Create(line1), Create(line2), MoveToTarget(bitstreams_group2), rect.animate.set_stroke(opacity=0.3),bitstreams[0].animate.set_opacity(0.3), bitstreams[1].animate.set_opacity(0.3), bitstreams[2].animate.set_opacity(0.3), bitstreams[3].animate.set_opacity(0.3), bitstreams[4].animate.set_opacity(0.3), bitstreams[5].animate.set_opacity(0.3), bitstreams[6].animate.set_opacity(0.3), bitstreams[7].animate.set_opacity(0.3), bitstreams[8].animate.set_opacity(0.3), bitstreams[9].animate.set_opacity(0.3), bitstreams[10].animate.set_opacity(0.3), bitstreams[11].animate.set_opacity(0.3), bitstreams[12].animate.set_opacity(0.3), bitstreams[13].animate.set_opacity(0.3)) 
        
        self.wait(3)
        self.play(FadeOut(bitstreams_group), FadeOut(line1), FadeOut(line2))
        # Completely remove the original group, and remove all bitstreams except the red one in the new group
        self.remove(bitstreams_group)

        # Shuffle indices for bitstreams_group2 
        indices = list(range(len(bitstreams_group2))) 
        random.shuffle(indices)

        # Fade out with randomization
        self.play(FadeOut(bitstreams_group2[0]), run_time=0.5)
        for i in indices:
            if i != 5 and i!=0 :
                self.play(FadeOut(bitstreams_group2[i]), run_time=0.4)  # Adjust run_time if desired

        self.wait(2)
        # Move the red bitstream to the right and expand
        bitstreams_group2[5].generate_target()
        bitstreams_group2[5].target.move_to(RIGHT * 2)
        bitstreams_group2[5].target.scale(3)
        self.play(MoveToTarget(bitstreams_group2[5]))
        self.play(Indicate(bitstreams_group2[5]))

        self.wait(2)
        # Reduce opacity of bitstream and Man
        self.play(bitstreams_group2[5].animate.set_opacity(0.1), Man.animate.set_opacity(0.1))

        # Write text over the faded screen
        text = Tex("This procedure incurs a lot of download cost ", font_size=48).set_color(BLUE)
        text2 = Tex("and is thus inefficient!", font_size=48).set_color(BLUE)
        Wifi = ImageMobject("Wifi.png").scale(0.9)
        Wifi.move_to(DOWN * 2)
        text.next_to(text2, UP)
        self.play(Write(text), Write(text2), FadeIn(Wifi))
        
        self.wait(2)
        self.play(FadeOut(text), FadeOut(bitstreams_group2[5]), FadeOut(Man), FadeOut(text2), FadeOut(Wifi))


      