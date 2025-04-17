from manim import *


class DataRetrieval(Scene):
    def construct(self):
        text = Tex("Now we extend the (5,3) example to the case of data retrieval").scale(0.6)
        text.shift(ORIGIN)
        self.play(Write(text))

        self.play(FadeOut(text))
        self.wait()

        text1 = Tex(r"$f(t) = e_{i} + R_{1} \cdot t + R_{2} \cdot t^{2}$").scale(0.7)
        text1.shift(UP*3.5)
        self.play(Write(text1))

        boy = ImageMobject("ManThinking.png").scale(0.4)
        boy.shift(DOWN*2.5)
        self.play(FadeIn(boy))

        server1 = ImageMobject("server.png").scale(0.3)
        server1.shift(UP*2+RIGHT*6)
        self.play(FadeIn(server1))

        #-------------------------------rectangle

        font_size = 0.3
        #Create bitstreams of length 9, and about 8 of them
        bitstreams = [ 
            Tex("61003", color = BLUE).scale(font_size),
            Tex("46223", color = BLUE).scale(font_size),
            Tex("03145", color = BLUE).scale(font_size),
            Tex("14465", color = BLUE).scale(font_size),
            Tex("51013", color = BLUE).scale(font_size),
        ]

        rect = Rectangle(height=2.2, width=1.2, color=BLUE)
        rect.move_to(RIGHT *4.8 + UP * 2)
        rect.scale(0.65)
        self.play(Create(rect))



        width = 0.25
        #Print all rows together
        bitstreams[0].move_to(rect.get_top() +  DOWN * width * 1)
        bitstreams[1].move_to(rect.get_top() +  DOWN * width * 2)
        bitstreams[2].move_to(rect.get_top() +  DOWN * width * 3)
        bitstreams[3].move_to(rect.get_top() +  DOWN * width * 4)
        bitstreams[4].move_to(rect.get_top() +  DOWN * width * 5)

        self.play(Write(bitstreams[0]), Write(bitstreams[1]), Write(bitstreams[2]), Write(bitstreams[3]), Write(bitstreams[4]))
        self.wait(2)


        # #-----------------------------------

        

        server2 = ImageMobject("server.png").scale(0.3)
        server2.shift(UP*2+LEFT*6)
        self.play(FadeIn(server2))

        #------------------rect 2

        font_size = 0.3
        #Create bitstreams of length 9, and about 8 of them
        bitstreams1 = [ 
            Tex("61003", color = BLUE).scale(font_size),
            Tex("46223", color = BLUE).scale(font_size),
            Tex("03145", color = BLUE).scale(font_size),
            Tex("14465", color = BLUE).scale(font_size),
            Tex("51013", color = BLUE).scale(font_size),
        ]

        rect1 = Rectangle(height=2.2, width=1.2, color=BLUE)
        rect1.move_to(LEFT *4.8 + UP * 2)
        rect1.scale(0.65)
        self.play(Create(rect1))



        width = 0.25
        #Print all rows together
        bitstreams1[0].move_to(rect1.get_top() +  DOWN * width * 1)
        bitstreams1[1].move_to(rect1.get_top() +  DOWN * width * 2)
        bitstreams1[2].move_to(rect1.get_top() +  DOWN * width * 3)
        bitstreams1[3].move_to(rect1.get_top() +  DOWN * width * 4)
        bitstreams1[4].move_to(rect1.get_top() +  DOWN * width * 5)

        self.play(Write(bitstreams1[0]), Write(bitstreams1[1]), Write(bitstreams1[2]), Write(bitstreams1[3]), Write(bitstreams1[4]))
        self.wait(2)


        #--------------------------

        
        server3 = ImageMobject("server.png").scale(0.3)
        server3.shift(UP*2+LEFT*0.2)
        self.play(FadeIn(server3))

        #------------------rect 3

        font_size = 0.3
        #Create bitstreams of length 9, and about 8 of them
        bitstreams3 = [ 
            Tex("61003", color = BLUE).scale(font_size),
            Tex("46223", color = BLUE).scale(font_size),
            Tex("03145", color = BLUE).scale(font_size),
            Tex("14465", color = BLUE).scale(font_size),
            Tex("51013", color = BLUE).scale(font_size),
        ]

        rect3 = Rectangle(height=2.2, width=1.2, color=BLUE)
        rect3.move_to(RIGHT *1 + UP * 2)
        rect3.scale(0.65)
        self.play(Create(rect3))



        width = 0.25
        #Print all rows together
        bitstreams3[0].move_to(rect3.get_top() +  DOWN * width * 1)
        bitstreams3[1].move_to(rect3.get_top() +  DOWN * width * 2)
        bitstreams3[2].move_to(rect3.get_top() +  DOWN * width * 3)
        bitstreams3[3].move_to(rect3.get_top() +  DOWN * width * 4)
        bitstreams3[4].move_to(rect3.get_top() +  DOWN * width * 5)

        self.play(Write(bitstreams3[0]), Write(bitstreams3[1]), Write(bitstreams3[2]), Write(bitstreams3[3]), Write(bitstreams3[4]))
        self.wait(2)


        #--------------------------



        

        server4 = ImageMobject("server.png").scale(0.3)
        server4.shift(DOWN*2+RIGHT*6)
        self.play(FadeIn(server4))

        #------------------rect 4

        font_size = 0.3
        #Create bitstreams of length 9, and about 8 of them
        bitstreams4 = [ 
            Tex("61003", color = BLUE).scale(font_size),
            Tex("46223", color = BLUE).scale(font_size),
            Tex("03145", color = BLUE).scale(font_size),
            Tex("14465", color = BLUE).scale(font_size),
            Tex("51013", color = BLUE).scale(font_size),
        ]

        rect4 = Rectangle(height=2.2, width=1.2, color=BLUE)
        rect4.move_to(RIGHT *4.8 + DOWN * 2)
        rect4.scale(0.65)
        self.play(Create(rect4))



        width = 0.25
        #Print all rows together
        bitstreams4[0].move_to(rect4.get_top() +  DOWN * width * 1)
        bitstreams4[1].move_to(rect4.get_top() +  DOWN * width * 2)
        bitstreams4[2].move_to(rect4.get_top() +  DOWN * width * 3)
        bitstreams4[3].move_to(rect4.get_top() +  DOWN * width * 4)
        bitstreams4[4].move_to(rect4.get_top() +  DOWN * width * 5)

        self.play(Write(bitstreams4[0]), Write(bitstreams4[1]), Write(bitstreams4[2]), Write(bitstreams4[3]), Write(bitstreams4[4]))
        self.wait(2)


        #--------------------------


        server5 = ImageMobject("server.png").scale(0.3)
        server5.shift(DOWN*2+LEFT*6)
        self.play(FadeIn(server5))

         #------------------rect 4

        font_size = 0.3
        #Create bitstreams of length 9, and about 8 of them
        bitstreams5 = [ 
            Tex("61003", color = BLUE).scale(font_size),
            Tex("46223", color = BLUE).scale(font_size),
            Tex("03145", color = BLUE).scale(font_size),
            Tex("14465", color = BLUE).scale(font_size),
            Tex("51013", color = BLUE).scale(font_size),
        ]

        rect5 = Rectangle(height=2.2, width=1.2, color=BLUE)
        rect5.move_to(LEFT *4.8 + DOWN * 2)
        rect5.scale(0.65)
        self.play(Create(rect5))



        width = 0.25
        #Print all rows together
        bitstreams5[0].move_to(rect5.get_top() +  DOWN * width * 1)
        bitstreams5[1].move_to(rect5.get_top() +  DOWN * width * 2)
        bitstreams5[2].move_to(rect5.get_top() +  DOWN * width * 3)
        bitstreams5[3].move_to(rect5.get_top() +  DOWN * width * 4)
        bitstreams5[4].move_to(rect5.get_top() +  DOWN * width * 5)

        self.play(Write(bitstreams5[0]), Write(bitstreams5[1]), Write(bitstreams5[2]), Write(bitstreams5[3]), Write(bitstreams5[4]))
        self.wait(2)

        
        #--------------------------
        
        R1 = Tex("$R_{1} = 26331$").scale(0.65)
        R2 = Tex("$R_{2} = 41125$").scale(0.65)
        ei = Tex("$e_{i} = 14155$").scale(0.65)

        R1.shift(DOWN*2.5 + RIGHT*1.5)
        R2.shift(DOWN*3 + RIGHT*1.5)
        ei.shift(DOWN*3.5 + RIGHT*1.5)

        self.play(Write(R1),Write(R2),Write(ei))  
        



         
        #done for t = 1 -----------------------------------------------------------------
        #now generate f(1) = ei + R1*1 + R2*(1)^2
        f_1 = Tex("$f(1) = e_{i} + R_{1} \cdot 1 + R_{2} \cdot 1^{2}$").scale(0.5)
        f_1.shift(DOWN*1)
        self.play(Write(f_1))
        self.wait()
        #calculate the value of f(1) = ei + R1 + R2
        f_11 = Tex("04530").scale(0.65)
        self.play(FadeOut(f_1),run_time=1)
        f_11.shift(DOWN*1+LEFT*1)
        
        f11bit1 = Tex("0").scale(0.65)
        f11bit2 = Tex("4").scale(0.65)
        f11bit3 = Tex("5").scale(0.65)
        f11bit4 = Tex("3").scale(0.65)
        f11bit5 = Tex("0").scale(0.65)
        f11bit1.move_to(DOWN*1 + LEFT*0.15)
        f11bit2.next_to(f11bit1, RIGHT*0.1)
        f11bit3.next_to(f11bit2, RIGHT*0.1)
        f11bit4.next_to(f11bit3, RIGHT*0.1)
        f11bit5.next_to(f11bit4, RIGHT*0.1)
        self.play(Write(f11bit1), Write(f11bit2), Write(f11bit3), Write(f11bit4), Write(f11bit5))
        self.wait(1)

        #now i have all the bits i want to transform it to each server in column wise
        #this bit will go to top left server i.e 1
        f11bit1.generate_target()
        f11bit1.target.move_to(rect.get_top() + DOWN * width * 1 + LEFT*0.75)
        f11bit2.generate_target()
        f11bit2.target.move_to(rect.get_top() + DOWN * width * 2 + LEFT*0.75)
        f11bit3.generate_target()
        f11bit3.target.move_to(rect.get_top() + DOWN * width * 3 + LEFT*0.75)
        f11bit4.generate_target()
        f11bit4.target.move_to(rect.get_top() + DOWN * width * 4 + LEFT*0.75)
        f11bit5.generate_target()
        f11bit5.target.move_to(rect.get_top() + DOWN * width * 5 + LEFT*0.75)

        self.play(MoveToTarget(f11bit1),MoveToTarget(f11bit2),MoveToTarget(f11bit3),MoveToTarget(f11bit4),MoveToTarget(f11bit5))
        #-----------------------------------------------------------------------------------------------------------------------

        #done for t = 2-----------------------------------------------------------------
        #now generate f(2) = ei + R1*2 + R2*(2)^2
        f_2 = Tex("$f(2) = e_{i} + R_{1} \cdot 2 + R_{2} \cdot 2^{2}$").scale(0.5)
        f_2.shift(DOWN*1)
        self.play(Write(f_2))
        self.wait()
        #calculate the value of f(1) = ei + R1 + R2
        f_12 = Tex("06456").scale(0.65)
        self.play(FadeOut(f_2),run_time=1)
        f_12.shift(DOWN*1+LEFT*1)
        
        f12bit1 = Tex("0").scale(0.65)
        f12bit2 = Tex("6").scale(0.65)
        f12bit3 = Tex("4").scale(0.65)
        f12bit4 = Tex("5").scale(0.65)
        f12bit5 = Tex("6").scale(0.65)
        f12bit1.move_to(DOWN*1 + LEFT*0.15)
        f12bit2.next_to(f12bit1, RIGHT*0.1)
        f12bit3.next_to(f12bit2, RIGHT*0.1)
        f12bit4.next_to(f12bit3, RIGHT*0.1)
        f12bit5.next_to(f12bit4, RIGHT*0.1)
        self.play(Write(f12bit1), Write(f12bit2), Write(f12bit3), Write(f12bit4), Write(f12bit5))
        self.wait(1)

        #now i have all the bits i want to transform it to each server in column wise
        #this bit will go to top left server i.e 1
        f12bit1.generate_target()
        f12bit1.target.move_to(rect1.get_top() + DOWN * width * 1 + RIGHT*0.75)
        f12bit2.generate_target()
        f12bit2.target.move_to(rect1.get_top() + DOWN * width * 2 + RIGHT*0.75)
        f12bit3.generate_target()
        f12bit3.target.move_to(rect1.get_top() + DOWN * width * 3 + RIGHT*0.75)
        f12bit4.generate_target()
        f12bit4.target.move_to(rect1.get_top() + DOWN * width * 4 + RIGHT*0.75)
        f12bit5.generate_target()
        f12bit5.target.move_to(rect1.get_top() + DOWN * width * 5 + RIGHT*0.75)

        self.play(MoveToTarget(f12bit1),MoveToTarget(f12bit2),MoveToTarget(f12bit3),MoveToTarget(f12bit4),MoveToTarget(f12bit5))

        #done for server2----------------------------------------------------------------------

        
        #done for t = 3-----------------------------------------------------------------
        #now generate f(3) = ei + R1*3 + R2*(3)^2
        f_3 = Tex("$f(3) = e_{i} + R_{1} \cdot 3 + R_{3} \cdot 3^{2}$").scale(0.5)
        f_3.shift(DOWN*1)
        self.play(Write(f_3))
        self.wait()
        #calculate the value of f(1) = ei + R1 + R2
        f_13 = Tex("13544").scale(0.65)
        self.play(FadeOut(f_3),run_time=1)
        f_13.shift(DOWN*1+LEFT*1)
        
        f13bit1 = Tex("1").scale(0.65)
        f13bit2 = Tex("3").scale(0.65)
        f13bit3 = Tex("5").scale(0.65)
        f13bit4 = Tex("4").scale(0.65)
        f13bit5 = Tex("4").scale(0.65)
        f13bit1.move_to(DOWN*1 + LEFT*0.15)
        f13bit2.next_to(f13bit1, RIGHT*0.1)
        f13bit3.next_to(f13bit2, RIGHT*0.1)
        f13bit4.next_to(f13bit3, RIGHT*0.1)
        f13bit5.next_to(f13bit4, RIGHT*0.1)
        self.play(Write(f13bit1), Write(f13bit2), Write(f13bit3), Write(f13bit4), Write(f13bit5))
        self.wait(1)

        #now i have all the bits i want to transform it to each server in column wise
        #this bit will go to top left server i.e 1
        f13bit1.generate_target()
        f13bit1.target.move_to(rect3.get_top() + DOWN * width * 1 + RIGHT*0.75)
        f13bit2.generate_target()
        f13bit2.target.move_to(rect3.get_top() + DOWN * width * 2 + RIGHT*0.75)
        f13bit3.generate_target()
        f13bit3.target.move_to(rect3.get_top() + DOWN * width * 3 + RIGHT*0.75)
        f13bit4.generate_target()
        f13bit4.target.move_to(rect3.get_top() + DOWN * width * 4 + RIGHT*0.75)
        f13bit5.generate_target()
        f13bit5.target.move_to(rect3.get_top() + DOWN * width * 5 + RIGHT*0.75)

        self.play(MoveToTarget(f13bit1),MoveToTarget(f13bit2),MoveToTarget(f13bit3),MoveToTarget(f13bit4),MoveToTarget(f13bit5))

        #done for server3----------------------------------------------------------------------



        #doing for server4-----------------------------------------------------------------------
         #now generate f(3) = ei + R1*3 + R2*(3)^2
        f_4 = Tex("$f(4) = e_{i} + R_{1} \cdot 4 + R_{3} \cdot 4^{2}$").scale(0.5)
        f_4.shift(DOWN*1)
        self.play(Write(f_4))
        self.wait()
        #calculate the value of f(1) = ei + R1 + R2
        f_14 = Tex("32005").scale(0.65)
        self.play(FadeOut(f_4),run_time=1)
        f_14.shift(DOWN*1+LEFT*1)
        
        f14bit1 = Tex("3").scale(0.65)
        f14bit2 = Tex("2").scale(0.65)
        f14bit3 = Tex("0").scale(0.65)
        f14bit4 = Tex("0").scale(0.65)
        f14bit5 = Tex("5").scale(0.65)
        f14bit1.move_to(DOWN*1 + LEFT*0.15)
        f14bit2.next_to(f14bit1, RIGHT*0.1)
        f14bit3.next_to(f14bit2, RIGHT*0.1)
        f14bit4.next_to(f14bit3, RIGHT*0.1)
        f14bit5.next_to(f14bit4, RIGHT*0.1)
        self.play(Write(f14bit1), Write(f14bit2), Write(f14bit3), Write(f14bit4), Write(f14bit5))
        self.wait(1)

        #now i have all the bits i want to transform it to each server in column wise
        #this bit will go to top left server i.e 1
        f14bit1.generate_target()
        f14bit1.target.move_to(rect4.get_top() + DOWN * width * 1 + LEFT*0.75)
        f14bit2.generate_target()
        f14bit2.target.move_to(rect4.get_top() + DOWN * width * 2 + LEFT*0.75)
        f14bit3.generate_target()
        f14bit3.target.move_to(rect4.get_top() + DOWN * width * 3 + LEFT*0.75)
        f14bit4.generate_target()
        f14bit4.target.move_to(rect4.get_top() + DOWN * width * 4 + LEFT*0.75)
        f14bit5.generate_target()
        f14bit5.target.move_to(rect4.get_top() + DOWN * width * 5 + LEFT*0.75)

        self.play(MoveToTarget(f14bit1),MoveToTarget(f14bit2),MoveToTarget(f14bit3),MoveToTarget(f14bit4),MoveToTarget(f14bit5))

        #done for server 4--------------------------------------------------------------------------------


        #doing for the server 5----------------------------------------------------------------------------
        f_5 = Tex("$f(5) = e_{i} + R_{1} \cdot 5 + R_{3} \cdot 5^{2}$").scale(0.5)
        f_5.shift(DOWN*1)
        self.play(Write(f_5))
        self.wait()
        #calculate the value of f(1) = ei + R1 + R2
        f_15 = Tex("63642").scale(0.65)
        self.play(FadeOut(f_5),run_time=1)
        f_15.shift(DOWN*1+LEFT*1)
        
        f15bit1 = Tex("6").scale(0.65)
        f15bit2 = Tex("3").scale(0.65)
        f15bit3 = Tex("6").scale(0.65)
        f15bit4 = Tex("4").scale(0.65)
        f15bit5 = Tex("2").scale(0.65)
        f15bit1.move_to(DOWN*1 + LEFT*0.15)
        f15bit2.next_to(f15bit1, RIGHT*0.1)
        f15bit3.next_to(f15bit2, RIGHT*0.1)
        f15bit4.next_to(f15bit3, RIGHT*0.1)
        f15bit5.next_to(f15bit4, RIGHT*0.1)
        self.play(Write(f15bit1), Write(f15bit2), Write(f15bit3), Write(f15bit4), Write(f15bit5))
        self.wait(1)

        #now i have all the bits i want to transform it to each server in column wise
        #this bit will go to top left server i.e 1
        f15bit1.generate_target()
        f15bit1.target.move_to(rect5.get_top() + DOWN * width * 1 + RIGHT*0.75)
        f15bit2.generate_target()
        f15bit2.target.move_to(rect5.get_top() + DOWN * width * 2 + RIGHT*0.75)
        f15bit3.generate_target()
        f15bit3.target.move_to(rect5.get_top() + DOWN * width * 3 + RIGHT*0.75)
        f15bit4.generate_target()
        f15bit4.target.move_to(rect5.get_top() + DOWN * width * 4 + RIGHT*0.75)
        f15bit5.generate_target()
        f15bit5.target.move_to(rect5.get_top() + DOWN * width * 5 + RIGHT*0.75)

        self.play(MoveToTarget(f15bit1),MoveToTarget(f15bit2),MoveToTarget(f15bit3),MoveToTarget(f15bit4),MoveToTarget(f15bit5))

        #done for all the servers ----------------------------------------------------------------------------------------------

        #now i have replace the servers and databases and bits with a new set of bits

        ser1 = Group(rect,bitstreams[0],bitstreams[1],bitstreams[2],bitstreams[3],bitstreams[4],f11bit1,f11bit2,f11bit3,f11bit4,f11bit5)
        ser2 = Group(rect1,bitstreams1[0],bitstreams1[1],bitstreams1[2],bitstreams1[3],bitstreams1[4],f12bit1,f12bit2,f12bit3,f12bit4,f12bit5)
        ser3 = Group(rect3,bitstreams3[0],bitstreams3[1],bitstreams3[2],bitstreams3[3],bitstreams3[4],f13bit1,f13bit2,f13bit3,f13bit4,f13bit5)
        ser4 = Group(rect4,bitstreams4[0],bitstreams4[1],bitstreams4[2],bitstreams4[3],bitstreams4[4],f14bit1,f14bit2,f14bit3,f14bit4,f14bit5)
        ser5 = Group(rect5,bitstreams5[0],bitstreams5[1],bitstreams5[2],bitstreams5[3],bitstreams5[4],f15bit1,f15bit2,f15bit3,f15bit4,f15bit5)

        h1 = Tex("h(1) = 46411").scale(0.85)
        h2 = Tex("h(2) = 14114").scale(0.85)
        h3 = Tex("h(3) = 05656").scale(0.85)
        h4 = Tex("h(4) = 26422").scale(0.85)
        h5 = Tex("h(5) = 64006").scale(0.85)

        self.play(FadeOut(R1),FadeOut(R2),FadeOut(ei),run_time=1)

        
        
       
        
        boy.shift(LEFT*1.5)
        self.play(FadeIn(boy))

        self.play(ReplacementTransform(ser1,h1),FadeOut(server1),run_time = 1)
        h1.generate_target()
        h1.target.move_to(DOWN*1+ RIGHT*1.5)
        self.play(MoveToTarget(h1))


        self.play(ReplacementTransform(ser2,h2),FadeOut(server2),run_time = 1)
        h2.generate_target()
        h2.target.move_to(DOWN*1.5 + RIGHT*1.5)
        self.play(MoveToTarget(h2))


        self.play(ReplacementTransform(ser3,h3),FadeOut(server3),run_time = 1)
        h3.generate_target()
        h3.target.move_to(DOWN*2 + RIGHT*1.5)
        self.play(MoveToTarget(h3))


        self.play(ReplacementTransform(ser4,h4),FadeOut(server4),run_time = 1)
        h4.generate_target()
        h4.target.move_to(DOWN*2.5 + RIGHT*1.5)
        self.play(MoveToTarget(h4))


        self.play(ReplacementTransform(ser5,h5),FadeOut(server5),run_time = 1)
        h5.generate_target()
        h5.target.move_to(DOWN*3 + RIGHT*1.5)
        self.play(MoveToTarget(h5))

        # final = Tex(r"$\text{Download Rate} = \frac{1}{7}$").scale(0.7)
        # final.shift(UP*1)
        # self.play(Write(final))
        rate = Tex("$\\frac{1}{7}$")
        rate.color = ORANGE
        final = Tex("Download Rate $=$").scale(0.9)
        rate.next_to(final,RIGHT)
        self.play(Write(final))
        self.play(Wiggle(rate))

        final11 = Tex("4 erasures and 2 errors").scale(0.7)
        final11.set_color(ORANGE)
        
        final1 = Tex("Further This scheme also offers resilience to up to").scale(0.7)
        final1.shift(UP*2+LEFT*2)
        final11.next_to(final1,RIGHT)
        self.play(Write(final1),Write(final11))
        self.play(Wiggle(final11),run_time = 2)
        

        self.wait(2)

        



















        

           
        



        


