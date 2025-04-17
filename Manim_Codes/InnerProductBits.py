from manim import *

class InnerProductBits(Scene):
    def construct(self):
        Man = ImageMobject("Man.png").scale(0.7)
        ChatBox2 = ImageMobject("ChatBox3.png").scale(0.6)
        ChatBox = ImageMobject("ChatBox2.png").scale(0.6)

        Server1 = ImageMobject("Server.png").scale(0.7)
        Server2 = ImageMobject("Server.png").scale(0.7)

        Server1.move_to(RIGHT * 5.5 + UP * 2)
        Server2.move_to(RIGHT * 5.5 + DOWN * 2)


        Man.move_to(LEFT * 5.5)
        ChatBox2.move_to(LEFT * 3.5 + DOWN * 2)
        ChatBox.move_to(LEFT * 3.5 + UP * 2)

        Message = Tex("Message", color = BLUE).scale(0.7)
        Message.next_to(ChatBox, UP*0.5)
        Random = Tex("Random", color = YELLOW).scale(0.7)
        Random.next_to(ChatBox2, DOWN*0.5)

        self.play(FadeIn(Man))
        self.wait(2)

        font_size = 0.6
        #Create bitstreams of length 9, and about 8 of them
        bitstreams = [ 
            Tex("011010101", color = BLUE).scale(font_size),
            Tex("101010101", color = BLUE).scale(font_size),
            Tex("111111111", color = BLUE).scale(font_size),
            Tex("110011001", color = BLUE).scale(font_size),
            Tex("001100110", color = BLUE).scale(font_size),
            Tex("010101010", color = BLUE).scale(font_size),
            Tex("000000010", color = BLUE).scale(font_size),
            Tex("101101101", color = BLUE).scale(font_size),
            Tex("111000111", color = BLUE).scale(font_size)
        ]

        bitstreams2 = [ 
            Tex("011010101", color = YELLOW).scale(font_size),
            Tex("101010101", color = YELLOW).scale(font_size),
            Tex("111111111", color = YELLOW).scale(font_size),
            Tex("110011001", color = YELLOW).scale(font_size),
            Tex("001100110", color = YELLOW).scale(font_size),
            Tex("010101010", color = YELLOW).scale(font_size),
            Tex("000000010", color = YELLOW).scale(font_size),
            Tex("101101101", color = YELLOW).scale(font_size),
            Tex("111000111", color = YELLOW).scale(font_size)
        ]

        rect = Rectangle(height=3.8, width=2.7, color=BLUE)
        rect.move_to(RIGHT * 3.2 + UP * 2)
        rect.scale(0.8)

        rect2 = Rectangle(height=3.8, width=2.7, color=YELLOW)
        rect2.move_to(RIGHT * 3.2 + DOWN * 2)
        rect2.scale(0.8)
        self.play(Create(rect), Create(rect2) , FadeIn(Server1), FadeIn(Server2))

        width = 0.30
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

        width = 0.30
        #Print all rows together
        bitstreams2[0].move_to(rect2.get_top() +  DOWN * width * 1)
        bitstreams2[1].move_to(rect2.get_top() +  DOWN * width * 2)
        bitstreams2[2].move_to(rect2.get_top() +  DOWN * width * 3)
        bitstreams2[3].move_to(rect2.get_top() +  DOWN * width * 4)
        bitstreams2[4].move_to(rect2.get_top() +  DOWN * width * 5)
        bitstreams2[5].move_to(rect2.get_top() +  DOWN * width * 6)
        bitstreams2[6].move_to(rect2.get_top() +  DOWN * width * 7)
        bitstreams2[7].move_to(rect2.get_top() +  DOWN * width * 8)
        bitstreams2[8].move_to(rect2.get_top() +  DOWN * width * 9)

        self.play(Write(bitstreams[0]), Write(bitstreams[1]), Write(bitstreams[2]), Write(bitstreams[3]), Write(bitstreams[4]), Write(bitstreams[5]), Write(bitstreams[6]), Write(bitstreams[7]), Write(bitstreams[8]), Write(bitstreams2[0]), Write(bitstreams2[1]), Write(bitstreams2[2]), Write(bitstreams2[3]), Write(bitstreams2[4]), Write(bitstreams2[5]), Write(bitstreams2[6]), Write(bitstreams2[7]), Write(bitstreams2[8]))
        self.wait(2)

        #Create a bitstream of length 9
        MessageBit1 = Tex("0", color = BLUE).scale(0.8)
        MessageBit2 = Tex("0", color = BLUE).scale(0.8)
        MessageBit3 = Tex("1", color = BLUE).scale(0.8)
        MessageBit4 = Tex("1", color = BLUE).scale(0.8)
        MessageBit5 = Tex("1", color = BLUE).scale(0.8)
        MessageBit6 = Tex("0", color = BLUE).scale(0.8)
        MessageBit7 = Tex("1", color = BLUE).scale(0.8)
        MessageBit8 = Tex("1", color = BLUE).scale(0.8)
        MessageBit9 = Tex("0", color = BLUE).scale(0.8)
        
        dist = 0.1
        MessageBit1.move_to(ChatBox.get_top() + DOWN*0.55 + LEFT*0.7)
        MessageBit2.next_to(MessageBit1, RIGHT*dist)
        MessageBit3.next_to(MessageBit2, RIGHT*dist)
        MessageBit4.next_to(MessageBit3, RIGHT*dist)
        MessageBit5.next_to(MessageBit4, RIGHT*dist)
        MessageBit6.next_to(MessageBit5, RIGHT*dist)
        MessageBit7.next_to(MessageBit6, RIGHT*dist)
        MessageBit8.next_to(MessageBit7, RIGHT*dist)
        MessageBit9.next_to(MessageBit8, RIGHT*dist)
        # MEssage bit is 001110110
        # Random bitstream is 101101101

        RandomBit1 = Tex("1", color = YELLOW).scale(0.8)
        RandomBit2 = Tex("0", color = YELLOW).scale(0.8)
        RandomBit3 = Tex("1", color = YELLOW).scale(0.8)
        RandomBit4 = Tex("1", color = YELLOW).scale(0.8)
        RandomBit5 = Tex("0", color = YELLOW).scale(0.8)
        RandomBit6 = Tex("1", color = YELLOW).scale(0.8)
        RandomBit7 = Tex("1", color = YELLOW).scale(0.8)
        RandomBit8 = Tex("0", color = YELLOW).scale(0.8)
        RandomBit9 = Tex("1", color = YELLOW).scale(0.8)

        RandomBit1.move_to(ChatBox2.get_top() + DOWN*1.0 + LEFT*0.7)
        RandomBit2.next_to(RandomBit1, RIGHT*dist)
        RandomBit3.next_to(RandomBit2, RIGHT*dist)
        RandomBit4.next_to(RandomBit3, RIGHT*dist)
        RandomBit5.next_to(RandomBit4, RIGHT*dist)
        RandomBit6.next_to(RandomBit5, RIGHT*dist)
        RandomBit7.next_to(RandomBit6, RIGHT*dist)
        RandomBit8.next_to(RandomBit7, RIGHT*dist)
        RandomBit9.next_to(RandomBit8, RIGHT*dist)

        MixedMessage = Tex("Mixed", color = PURE_GREEN).scale(0.7)

        #Mixed bitstream is 111100011
        MixedBit1 = Tex("1", color = PURE_GREEN).scale(0.8)
        MixedBit2 = Tex("1", color = PURE_GREEN).scale(0.8)
        MixedBit3 = Tex("1", color = PURE_GREEN).scale(0.8)
        MixedBit4 = Tex("1", color = PURE_GREEN).scale(0.8)
        MixedBit5 = Tex("0", color = PURE_GREEN).scale(0.8)
        MixedBit6 = Tex("0", color = PURE_GREEN).scale(0.8)
        MixedBit7 = Tex("0", color = PURE_GREEN).scale(0.8)
        MixedBit8 = Tex("1", color = PURE_GREEN).scale(0.8)
        MixedBit9 = Tex("1", color = PURE_GREEN).scale(0.8)
        
        MixedBit1.move_to(ChatBox.get_top() + DOWN*0.55 + LEFT*0.7)
        MixedBit2.next_to(MixedBit1, RIGHT*dist)
        MixedBit3.next_to(MixedBit2, RIGHT*dist)
        MixedBit4.next_to(MixedBit3, RIGHT*dist)
        MixedBit5.next_to(MixedBit4, RIGHT*dist)
        MixedBit6.next_to(MixedBit5, RIGHT*dist)
        MixedBit7.next_to(MixedBit6, RIGHT*dist)
        MixedBit8.next_to(MixedBit7, RIGHT*dist)
        MixedBit9.next_to(MixedBit8, RIGHT*dist)

        MessageBits = [MessageBit1,  MessageBit2, MessageBit3, MessageBit4, MessageBit5, MessageBit6, MessageBit7, MessageBit8, MessageBit9]
        RandomBits = [RandomBit1, RandomBit2, RandomBit3, RandomBit4, RandomBit5, RandomBit6, RandomBit7, RandomBit8, RandomBit9]
        MixedBits = [MixedBit1, MixedBit2, MixedBit3, MixedBit4, MixedBit5, MixedBit6, MixedBit7, MixedBit8, MixedBit9]

        self.play(FadeIn(ChatBox2),FadeIn(ChatBox),Write(Message), Write(Random))
        self.play(Write(MessageBit1), Write(MessageBit2), Write(MessageBit3), Write(MessageBit4), Write(MessageBit5), Write(MessageBit6), Write(MessageBit7), Write(MessageBit8), Write(MessageBit9), Write(RandomBit1), Write(RandomBit2), Write(RandomBit3), Write(RandomBit4), Write(RandomBit5), Write(RandomBit6), Write(RandomBit7), Write(RandomBit8), Write(RandomBit9))
        self.wait(1)

        RandomBit11 = Tex("1", color = YELLOW).scale(0.8)
        RandomBit22 = Tex("0", color = YELLOW).scale(0.8)
        RandomBit33 = Tex("1", color = YELLOW).scale(0.8)
        RandomBit44 = Tex("1", color = YELLOW).scale(0.8)
        RandomBit55 = Tex("0", color = YELLOW).scale(0.8)
        RandomBit66 = Tex("1", color = YELLOW).scale(0.8)
        RandomBit77 = Tex("1", color = YELLOW).scale(0.8)
        RandomBit88 = Tex("0", color = YELLOW).scale(0.8)
        RandomBit99 = Tex("1", color = YELLOW).scale(0.8)

        RandomBit11.move_to(ChatBox2.get_top() + DOWN*1.0 + LEFT*0.7)
        RandomBit22.next_to(RandomBit11, RIGHT*dist)
        RandomBit33.next_to(RandomBit22, RIGHT*dist)
        RandomBit44.next_to(RandomBit33, RIGHT*dist)
        RandomBit55.next_to(RandomBit44, RIGHT*dist)
        RandomBit66.next_to(RandomBit55, RIGHT*dist)
        RandomBit77.next_to(RandomBit66, RIGHT*dist)
        RandomBit88.next_to(RandomBit77, RIGHT*dist)
        RandomBit99.next_to(RandomBit88, RIGHT*dist)


        # Move the random bits to the location of the message bits
        RandomBit11.generate_target()
        RandomBit11.target.move_to(MessageBit1.get_center())
        RandomBit22.generate_target()
        RandomBit22.target.move_to(MessageBit2.get_center())    
        RandomBit33.generate_target()
        RandomBit33.target.move_to(MessageBit3.get_center())
        RandomBit44.generate_target()
        RandomBit44.target.move_to(MessageBit4.get_center())
        RandomBit55.generate_target()
        RandomBit55.target.move_to(MessageBit5.get_center())
        RandomBit66.generate_target()
        RandomBit66.target.move_to(MessageBit6.get_center())
        RandomBit77.generate_target()
        RandomBit77.target.move_to(MessageBit7.get_center())
        RandomBit88.generate_target()
        RandomBit88.target.move_to(MessageBit8.get_center())
        RandomBit99.generate_target()
        RandomBit99.target.move_to(MessageBit9.get_center())

        MixedMessage.move_to(Message.get_center())

        self.play(MoveToTarget(RandomBit11), MoveToTarget(RandomBit22), MoveToTarget(RandomBit33), MoveToTarget(RandomBit44), MoveToTarget(RandomBit55), MoveToTarget(RandomBit66), MoveToTarget(RandomBit77), MoveToTarget(RandomBit88), MoveToTarget(RandomBit99))

        Mixture1 = VGroup(MessageBit1, RandomBit11)
        Mixture2 = VGroup(MessageBit2, RandomBit22)
        Mixture3 = VGroup(MessageBit3, RandomBit33)
        Mixture4 = VGroup(MessageBit4, RandomBit44)
        Mixture5 = VGroup(MessageBit5, RandomBit55)
        Mixture6 = VGroup(MessageBit6, RandomBit66)
        Mixture7 = VGroup(MessageBit7, RandomBit77)
        Mixture8 = VGroup(MessageBit8, RandomBit88)
        Mixture9 = VGroup(MessageBit9, RandomBit99)

        self.play(ReplacementTransform(Mixture1, MixedBit1), ReplacementTransform(Mixture2, MixedBit2), ReplacementTransform(Mixture3, MixedBit3), ReplacementTransform(Mixture4, MixedBit4), ReplacementTransform(Mixture5, MixedBit5), ReplacementTransform(Mixture6, MixedBit6), ReplacementTransform(Mixture7, MixedBit7), ReplacementTransform(Mixture8, MixedBit8), ReplacementTransform(Mixture9, MixedBit9), ReplacementTransform(Message, MixedMessage))

        self.play(FadeOut(ChatBox), FadeOut(ChatBox2), FadeOut(Random), FadeOut(MixedMessage))


        shift = 1.3
        MixedBit1.generate_target()
        MixedBit1.target.move_to(rect.get_top() + DOWN * width * 1 + LEFT * shift)
        MixedBit1.target.scale(0.77)
        MixedBit2.generate_target()
        MixedBit2.target.move_to(rect.get_top() + DOWN * width * 2 + LEFT * shift)
        MixedBit2.target.scale(0.77)
        MixedBit3.generate_target()
        MixedBit3.target.move_to(rect.get_top() + DOWN * width * 3 + LEFT * shift)
        MixedBit3.target.scale(0.77)
        MixedBit4.generate_target()
        MixedBit4.target.move_to(rect.get_top() + DOWN * width * 4 + LEFT * shift)
        MixedBit4.target.scale(0.77)
        MixedBit5.generate_target()
        MixedBit5.target.move_to(rect.get_top() + DOWN * width * 5 + LEFT * shift)
        MixedBit5.target.scale(0.77)
        MixedBit6.generate_target()
        MixedBit6.target.move_to(rect.get_top() + DOWN * width * 6 + LEFT * shift)
        MixedBit6.target.scale(0.77)
        MixedBit7.generate_target()
        MixedBit7.target.move_to(rect.get_top() + DOWN * width * 7 + LEFT * shift)
        MixedBit7.target.scale(0.77)
        MixedBit8.generate_target()
        MixedBit8.target.move_to(rect.get_top() + DOWN * width * 8 + LEFT * shift)
        MixedBit8.target.scale(0.77)
        MixedBit9.generate_target()
        MixedBit9.target.move_to(rect.get_top() + DOWN * width * 9 + LEFT * shift)
        MixedBit9.target.scale(0.77)

        RandomBit1.generate_target()
        RandomBit1.target.move_to(rect2.get_top() + DOWN * width * 1 + LEFT * shift)
        RandomBit1.target.scale(0.77)
        RandomBit2.generate_target()
        RandomBit2.target.move_to(rect2.get_top() + DOWN * width * 2 + LEFT * shift)
        RandomBit2.target.scale(0.77)
        RandomBit3.generate_target()
        RandomBit3.target.move_to(rect2.get_top() + DOWN * width * 3 + LEFT * shift)
        RandomBit3.target.scale(0.77)
        RandomBit4.generate_target()
        RandomBit4.target.move_to(rect2.get_top() + DOWN * width * 4 + LEFT * shift)
        RandomBit4.target.scale(0.77)
        RandomBit5.generate_target()
        RandomBit5.target.move_to(rect2.get_top() + DOWN * width * 5 + LEFT * shift)
        RandomBit5.target.scale(0.77)
        RandomBit6.generate_target()
        RandomBit6.target.move_to(rect2.get_top() + DOWN * width * 6 + LEFT * shift)
        RandomBit6.target.scale(0.77)
        RandomBit7.generate_target()
        RandomBit7.target.move_to(rect2.get_top() + DOWN * width * 7 + LEFT * shift)
        RandomBit7.target.scale(0.77)
        RandomBit8.generate_target()
        RandomBit8.target.move_to(rect2.get_top() + DOWN * width * 8 + LEFT * shift)
        RandomBit8.target.scale(0.77)
        RandomBit9.generate_target()
        RandomBit9.target.move_to(rect2.get_top() + DOWN * width * 9 + LEFT * shift)
        RandomBit9.target.scale(0.77)

        self.play(MoveToTarget(MixedBit1), MoveToTarget(MixedBit2), MoveToTarget(MixedBit3), MoveToTarget(MixedBit4), MoveToTarget(MixedBit5), MoveToTarget(MixedBit6), MoveToTarget(MixedBit7), MoveToTarget(MixedBit8), MoveToTarget(MixedBit9), MoveToTarget(RandomBit1), MoveToTarget(RandomBit2), MoveToTarget(RandomBit3), MoveToTarget(RandomBit4), MoveToTarget(RandomBit5), MoveToTarget(RandomBit6), MoveToTarget(RandomBit7), MoveToTarget(RandomBit8), MoveToTarget(RandomBit9), FadeOut(rect), FadeOut(rect2))

        self.wait(1)

        # # Write cdot of latex
        cdot1 = Tex(".",color = WHITE).scale(0.77)
        cdot2 = Tex(".",color = WHITE).scale(0.77)
        cdot3 = Tex(".",color = WHITE).scale(0.77)
        cdot4 = Tex(".",color = WHITE).scale(0.77)
        cdot5 = Tex(".",color = WHITE).scale(0.77)
        cdot6 = Tex(".",color = WHITE).scale(0.77)
        cdot7 = Tex(".",color = WHITE).scale(0.77)
        cdot8 = Tex(".",color = WHITE).scale(0.77)
        cdot9 = Tex(".",color = WHITE).scale(0.77)
        cdot10 = Tex(".",color = WHITE).scale(0.77)
        cdot11 = Tex(".",color = WHITE).scale(0.77)
        cdot12 = Tex(".",color = WHITE).scale(0.77)
        cdot13 = Tex(".",color = WHITE).scale(0.77)
        cdot14 = Tex(".",color = WHITE).scale(0.77)
        cdot15 = Tex(".",color = WHITE).scale(0.77)
        cdot16 = Tex(".",color = WHITE).scale(0.77)
        cdot17 = Tex(".",color = WHITE).scale(0.77)
        cdot18 = Tex(".",color = WHITE).scale(0.77)

        #Keep cdot besides the first bit to the right
        cdot1.move_to(MixedBit1.get_center() + RIGHT*0.3 + DOWN*0.05)
        cdot2.move_to(MixedBit2.get_center() + RIGHT*0.3 + DOWN*0.05)
        cdot3.move_to(MixedBit3.get_center() + RIGHT*0.3 + DOWN*0.05)
        cdot4.move_to(MixedBit4.get_center() + RIGHT*0.3 + DOWN*0.05)
        cdot5.move_to(MixedBit5.get_center() + RIGHT*0.3 + DOWN*0.05)
        cdot6.move_to(MixedBit6.get_center() + RIGHT*0.3 + DOWN*0.05) 
        cdot7.move_to(MixedBit7.get_center() + RIGHT*0.3 + DOWN*0.05) 
        cdot8.move_to(MixedBit8.get_center() + RIGHT*0.3 + DOWN*0.05)
        cdot9.move_to(MixedBit9.get_center() + RIGHT*0.3 + DOWN*0.05)
        cdot10.move_to(RandomBit1.get_center() + RIGHT*0.3 + DOWN*0.05)
        cdot11.move_to(RandomBit2.get_center() + RIGHT*0.3 + DOWN*0.05)
        cdot12.move_to(RandomBit3.get_center() + RIGHT*0.3 + DOWN*0.05)
        cdot13.move_to(RandomBit4.get_center() + RIGHT*0.3 + DOWN*0.05)
        cdot14.move_to(RandomBit5.get_center() + RIGHT*0.3 + DOWN*0.05)
        cdot15.move_to(RandomBit6.get_center() + RIGHT*0.3 + DOWN*0.05)
        cdot16.move_to(RandomBit7.get_center() + RIGHT*0.3 + DOWN*0.05)
        cdot17.move_to(RandomBit8.get_center() + RIGHT*0.3 + DOWN*0.05)
        cdot18.move_to(RandomBit9.get_center() + RIGHT*0.3 + DOWN*0.05)

        self.play(Write(cdot1), Write(cdot2), Write(cdot3), Write(cdot4), Write(cdot5), Write(cdot6), Write(cdot7), Write(cdot8), Write(cdot9), Write(cdot10), Write(cdot11), Write(cdot12), Write(cdot13), Write(cdot14), Write(cdot15), Write(cdot16), Write(cdot17), Write(cdot18))

        ExplainText = Tex("We now multiply the bits together, and sum them up", color = RED).scale(0.7)
        ExplainText.move_to(UP*3.5 + LEFT*2.8)
        self.play(Write(ExplainText))
        self.wait(1)
        self.play(FadeOut(ExplainText))
        
        #Sum is 101001100
        Sum1 = Tex("1", color = ORANGE).scale(0.8)
        Sum2 = Tex("0", color = ORANGE).scale(0.8)
        Sum3 = Tex("1", color = ORANGE).scale(0.8)
        Sum4 = Tex("0", color = ORANGE).scale(0.8)
        Sum5 = Tex("0", color = ORANGE).scale(0.8)
        Sum6 = Tex("1", color = ORANGE).scale(0.8)
        Sum7 = Tex("1", color = ORANGE).scale(0.8)
        Sum8 = Tex("0", color = ORANGE).scale(0.8)
        Sum9 = Tex("0", color = ORANGE).scale(0.8)

        Sum11 = VGroup(MixedBit1, bitstreams[0], cdot1)
        Sum22 = VGroup(MixedBit2, bitstreams[1], cdot2)
        Sum33 = VGroup(MixedBit3, bitstreams[2], cdot3)
        Sum44 = VGroup(MixedBit4, bitstreams[3], cdot4)
        Sum55 = VGroup(MixedBit5, bitstreams[4], cdot5)
        Sum66 = VGroup(MixedBit6, bitstreams[5], cdot6)
        Sum77 = VGroup(MixedBit7, bitstreams[6], cdot7)
        Sum88 = VGroup(MixedBit8, bitstreams[7], cdot8)
        Sum99 = VGroup(MixedBit9, bitstreams[8], cdot9)

        Sum1.move_to(MixedBit1.get_center() + RIGHT*0.6)
        Sum2.next_to(Sum1, RIGHT*dist)
        Sum3.next_to(Sum2, RIGHT*dist)
        Sum4.next_to(Sum3, RIGHT*dist)
        Sum5.next_to(Sum4, RIGHT*dist)
        Sum6.next_to(Sum5, RIGHT*dist)
        Sum7.next_to(Sum6, RIGHT*dist)
        Sum8.next_to(Sum7, RIGHT*dist)
        Sum9.next_to(Sum8, RIGHT*dist)

        #RSum is 111011100

        RSum1 = Tex("1", color = TEAL_C).scale(0.8)
        RSum2 = Tex("1", color = TEAL_C).scale(0.8)
        RSum3 = Tex("1", color = TEAL_C).scale(0.8)
        RSum4 = Tex("0", color = TEAL_C).scale(0.8)
        RSum5 = Tex("1", color = TEAL_C).scale(0.8)
        RSum6 = Tex("1", color = TEAL_C).scale(0.8)
        RSum7 = Tex("1", color = TEAL_C).scale(0.8)
        RSum8 = Tex("0", color = TEAL_C).scale(0.8)
        RSum9 = Tex("0", color = TEAL_C).scale(0.8)


        RSum11 = VGroup(RandomBit1, bitstreams2[0], cdot10)
        RSum22 = VGroup(RandomBit2, bitstreams2[1], cdot11)
        RSum33 = VGroup(RandomBit3, bitstreams2[2], cdot12)
        RSum44 = VGroup(RandomBit4, bitstreams2[3], cdot13)
        RSum55 = VGroup(RandomBit5, bitstreams2[4], cdot14)
        RSum66 = VGroup(RandomBit6, bitstreams2[5], cdot15)
        RSum77 = VGroup(RandomBit7, bitstreams2[6], cdot16)
        RSum88 = VGroup(RandomBit8, bitstreams2[7], cdot17)
        RSum99 = VGroup(RandomBit9, bitstreams2[8], cdot18)
        
        RSum1.move_to(RandomBit1.get_center() + RIGHT*0.6)
        RSum2.next_to(RSum1, RIGHT*dist)
        RSum3.next_to(RSum2, RIGHT*dist)
        RSum4.next_to(RSum3, RIGHT*dist)
        RSum5.next_to(RSum4, RIGHT*dist)
        RSum6.next_to(RSum5, RIGHT*dist)
        RSum7.next_to(RSum6, RIGHT*dist)
        RSum8.next_to(RSum7, RIGHT*dist)
        RSum9.next_to(RSum8, RIGHT*dist)

        self.play(ReplacementTransform(Sum11, Sum1), ReplacementTransform(Sum22, Sum2), ReplacementTransform(Sum33, Sum3), ReplacementTransform(Sum44, Sum4), ReplacementTransform(Sum55, Sum5), ReplacementTransform(Sum66, Sum6), ReplacementTransform(Sum77, Sum7), ReplacementTransform(Sum88, Sum8), ReplacementTransform(Sum99, Sum9), ReplacementTransform(RSum11, RSum1), ReplacementTransform(RSum22, RSum2), ReplacementTransform(RSum33, RSum3), ReplacementTransform(RSum44, RSum4), ReplacementTransform(RSum55, RSum5), ReplacementTransform(RSum66, RSum6), ReplacementTransform(RSum77, RSum7), ReplacementTransform(RSum88, RSum8), ReplacementTransform(RSum99, RSum9))

        FinalMixedSum = VGroup(Sum1, Sum2, Sum3, Sum4, Sum5, Sum6, Sum7, Sum8, Sum9)
        FinalRandomSum = VGroup(RSum1, RSum2, RSum3, RSum4, RSum5, RSum6, RSum7, RSum8, RSum9)

        FinalMixedSum.generate_target()
        FinalMixedSum.target.move_to(LEFT * 2 + UP * 2)
        FinalRandomSum.generate_target()
        FinalRandomSum.target.move_to(LEFT * 2 + DOWN * 2)
        self.play(MoveToTarget(FinalMixedSum), MoveToTarget(FinalRandomSum))

        SubtractText = Tex("We now subtract the two", color = RED).scale(0.7)
        SubtractText.move_to(UP*3.5 + LEFT*2.8)
        self.play(Write(SubtractText))
        self.wait(1)
        FinalMixedSum.generate_target()
        FinalMixedSum.target.move_to(LEFT*1.8 + UP * 0.5)
        FinalRandomSum.generate_target()
        FinalRandomSum.target.move_to(LEFT*1.8 + UP* 0.5)

        FinalFinalBits = Tex("010010000", color = YELLOW_C).scale(0.8)
        self.play(MoveToTarget(FinalMixedSum), MoveToTarget(FinalRandomSum))
        self.wait(1)
        FinalFinal = VGroup(FinalMixedSum, FinalRandomSum)
        self.wait(1)
        self.play(FadeOut(SubtractText))
        self.wait(1)
        self.play(ReplacementTransform(FinalFinal, FinalFinalBits))
        self.play(Indicate(FinalFinalBits))
        self.wait(1)
        self.play(FadeOut(FinalFinalBits), FadeOut(Man), FadeOut(Server1), FadeOut(Server2))

        self.wait(1)