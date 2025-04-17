from manim import *
import random

class Communications(Scene):
    def construct(self):
        Man = ImageMobject("Man.png").scale(0.7)
        Man2 = ImageMobject("Man2.png").scale(1.2)
        ChatBox = ImageMobject("ChatBox.png").scale(0.8)
        ChatBox2 = ImageMobject("ChatBox2.png").scale(1.0)
        # Flip ChatBox about vertical axis

        Man.move_to(LEFT * 5)
        Man2.move_to(RIGHT * 5)
        ChatBox2.move_to(LEFT * 2.5 + UP * 2)
        
        text1 = Tex("Message", color = BLUE).scale(0.7)
        text1.next_to(ChatBox2, UP*0.5)
        t2 = Tex("Random", color = YELLOW).scale(0.7)
        # Write text1 inside the chatbox
        # text1.move_to(LEFT * 2.5 + UP * 2)
        self.play(FadeIn(Man), FadeIn(Man2))
        self.wait(2)
        text2 = Tex("Nobody can beat").scale(0.7)
        text3 = Tex("Thala Dhoni").scale(0.7)
        text2.move_to(ChatBox2.get_top() + DOWN*0.7)
        text3.move_to(ChatBox2.get_top() + DOWN*1.2)
        textGroup = VGroup(text2, text3)
        self.play(FadeIn(ChatBox2), Write(textGroup), Write(text1))
        bits1 = Tex("0110101011101001101", color = BLUE).scale(0.8)
        self.wait(2)
        #Transform textGroup into bits1 and keep it in that location
        bits1.move_to(ChatBox2.get_top() + DOWN*1.0 + RIGHT*0.05)
        self.play(ReplacementTransform(textGroup, bits1), run_time = 0.8)
        self.wait(1)
        Chatbox3 = ImageMobject("ChatBox3.png").scale(1.0)
        Chatbox3.move_to(LEFT * 2.5 + DOWN * 2)
        t2.next_to(Chatbox3, DOWN*0.5)

        bits2 = Tex("0011101100000100011", color = YELLOW).scale(0.8)
        bits100 = bits2.copy()
        bits100.move_to(Chatbox3.get_top() + DOWN*1.6 + RIGHT*0.05)
        bits2.move_to(Chatbox3.get_top() + DOWN*1.6 + RIGHT*0.05)
        self.play(FadeIn(Chatbox3), Write(bits2), Write(t2))

        # Fade out chatboxes, and merge the two bits in the center into "1234567"
        self.wait(2)
        self.play(FadeOut(ChatBox2), FadeOut(Chatbox3), FadeOut(text1))
        self.play(t2.animate.next_to(bits2, DOWN*0.5))
        # Sum of bits1 and bits2 (mod 2 sum) = 1010010111101110000
        bits1.generate_target()
        bits100.generate_target()
        bits1.target.move_to(LEFT * 2)
        bits100.target.move_to(LEFT * 2)

        self.play(MoveToTarget(bits1), MoveToTarget(bits100))

        bits_group = VGroup(bits1, bits100)
        bits3 = Tex("1010010111101110000", color = PURE_GREEN).scale(0.8)
        bits3.move_to(LEFT * 2)
        subtitle = Tex("Bit Addition (mod 2 operation) gives us M+R", color = RED).scale(0.9)
        subtitle.move_to(UP*3.0)
        self.play(ReplacementTransform(bits_group, bits3), Write(subtitle))
        
        self.play(FadeOut(subtitle))

        mPlusR = Tex("M+R", color = PURE_GREEN).scale(0.6)
        mPlusR.next_to(bits3, DOWN*0.5)

# Create the arrow first
        arrow2 = CurvedArrow(bits2.get_bottom(), Man2.get_bottom(), color = YELLOW, stroke_width = 1.5)
        arrow = CurvedArrow(bits3.get_top(), Man2.get_top(), color=PURE_GREEN, stroke_width=1.5)
        self.play(Create(arrow), Create(arrow2), run_time=1) 

# Now write the text
        self.play(Write(mPlusR))

# Move the text along the arrow
        Group2 = VGroup(bits3, mPlusR) 
        Group3 = VGroup(bits2, t2)
        self.play(MoveAlongPath(Group2, arrow), MoveAlongPath(Group3, arrow2), run_time=2) 
        self.play(FadeOut(arrow), FadeOut(arrow2), Group2.animate.next_to(Man2.get_top() + LEFT * 3 + UP * 0.5), Group3.animate.next_to(Man2.get_bottom() + LEFT* 3 + DOWN* 0.5))

        bits4 = Tex("1010010111101110000", color = PURE_GREEN).scale(0.8)
        bits5 = Tex("0011101100000100011", color = YELLOW).scale(0.8)
        bits4.move_to(RIGHT * 2 + UP * 1)
        bits5.move_to(RIGHT * 2 + DOWN * 1)
        self.play(ReplacementTransform(Group2, bits4), ReplacementTransform(Group3, bits5))
      
        subtitle2 = Tex("We now subtract the two, to retrieve the original message", color = ORANGE)
        subtitle2.move_to(UP*3.0)
        Group8 = VGroup(bits4, bits5)

        bits4.generate_target()
        bits5.generate_target()
        bits4.target.move_to(RIGHT * 2)
        bits5.target.move_to(RIGHT * 2)
        bits9 = Tex("0110101011101001101", color = ORANGE).scale(0.8)
        bits9.move_to(RIGHT*2)
        self.play(Write(subtitle2), ReplacementTransform(Group8, bits9), run_time = 1)
        self.wait(1)
        
        text100 = Tex("Nobody can beat", color = ORANGE).scale(0.7)
        text100.move_to(RIGHT* 2)
        text101 = Tex("Thala Dhoni", color = ORANGE).scale(0.7)
        text101.next_to(text100,DOWN)
        textGroup2 = VGroup(text100, text101)
        self.play(ReplacementTransform(bits9, textGroup2))
        self.play(ApplyWave(textGroup2))

# Additional actions if needed
       
        self.play(FadeOut(textGroup2), FadeOut(Man), FadeOut(Man2), FadeOut(subtitle2))
        text8 = Tex("Well there's no secret about this message:) Thala is always unbeatable!", color= WHITE).scale(0.7)
        self.play(Write(text8))
        
        self.play(FadeOut(text8))
        


        
