
from manim import *

class storage_Servers(Scene):
    def construct(self):
        server1 = ImageMobject("server.png").scale(0.5)
        server1.generate_target()
        server1.target.move_to(LEFT*5+UP*2.1)
        #self.play(MoveToTarget(server1))

        database1 = ImageMobject("Database.png").scale(0.7)
        database1.generate_target()
        database1.target.move_to(LEFT*3.9+UP*1.9)
        

        server2 = ImageMobject("server.png").scale(0.5)
        server2.generate_target()
        server2.target.move_to(RIGHT*5+UP*2.1)
        #self.play(MoveToTarget(server2))

        database2 = ImageMobject("Database.png").scale(0.7)
        database2.generate_target()
        database2.target.move_to(RIGHT*3.7+UP*1.9)
        #self.play(MoveToTarget(database2))
        self.play(MoveToTarget(server1),MoveToTarget(database1))
        self.play(MoveToTarget(server2),MoveToTarget(database2))


        man = ImageMobject("ManThinking.png").scale(0.4)
        man.generate_target()
        man.target.move_to(DOWN*2.3)
        self.play(MoveToTarget(man))

        file = ImageMobject("file_main.png").scale(0.3)
        file.generate_target()
        file.target.move_to(DOWN*2.1+RIGHT*1.5)
        self.play(MoveToTarget(file))

        #now i want a curve arrow just above file depecting a rectange
       # curve = CurvedArrow(UP*2,UP*2+RIGHT*3,color=WHITE)
        #now this curvedarrow should point to a rectangle just above the file nd file
        #should be disabled
        rectangle = RoundedRectangle(width=2.48,height=1.28,corner_radius=0.1,color=WHITE)
        rectangle.set_fill(color=YELLOW,opacity=0.85)
        rectangle.move_to(DOWN*2+RIGHT*4.3)
       # self.play(Create(curve))
        self.play(Create(rectangle))
       # self.play(FadeOut(file))

        #i want my arrow should point from file to the rectange made
        curve = CurvedArrow(DOWN*2+RIGHT*1.5,DOWN*2+RIGHT*3,color=RED)
        self.play(Create(curve))
        
        self.play(FadeOut(curve),rum_time=1)
        self.play(FadeOut(file),run_time=1)

        #now i want to write in the rectangle
        text = Text("MESSAGE",color = PURE_BLUE).scale(0.5)
        text.shift(DOWN*1.8+RIGHT*4.25)
        self.play(Write(text))
        #i want this message to be in the rectangle

        vector = Text("1000101011",color = PURE_RED).scale(0.6)
        vector.shift(DOWN*2.2+RIGHT*4.25)
        self.play(Write(vector))
       # self.wait(2)
        

        rectangle1 = RoundedRectangle(width=2.48,height=1.28,corner_radius=0.1,color=WHITE)
        rectangle1.set_fill(color=YELLOW,opacity=0.85)
        rectangle1.move_to(DOWN*2+LEFT*4.3)
       # self.play(Create(curve))
        self.play(Create(rectangle1))
        curve1 = CurvedArrow(DOWN*2+LEFT*1,DOWN*2+LEFT*3,color=RED)
        self.play(Create(curve1))
        #i want instant fade out here
        #self.play(FadeOut(rectangle1), run_time=0)
        self.play(FadeOut(curve1),run_time=1)

        text1 = Text("RANDOM",color = PURE_BLUE).scale(0.5)
        text1.shift(DOWN*1.8+LEFT*4.3)
        self.play(Write(text1))
        #i want this message to be in the rectangle

        random = Text("0101010101",color = PURE_RED).scale(0.6)
        random.shift(DOWN*2.2+LEFT*4.25)
        self.play(Write(random))
       # self.wait(2)
         
        mixed = RoundedRectangle(width=2.48,height=1.28,corner_radius=0.1,color=WHITE)
        mixed.set_fill(color=YELLOW,opacity=0.85)
        #mixed.move_to()
        self.play(Create(mixed))

        bit2 = Text("0101010101",color = PURE_RED).scale(0.6)
        #i want my bit2 should move from the random position to the left of the mixed rectangl
        #without random bit disturbing

        
        #self.play(bit2.animate.move_to(LEFT*3+DOWN*0.5)) 
        start_pos1 = np.array([-4.25,-2.2,0])
        end_pos1 = np.array([0,0,0])
        delta_pos1 = end_pos1 - start_pos1
        bit2.move_to(start_pos1)
        #self.play(bit2.animate.shift(delta_pos))  

        bit1 = Text("1000101011",color = PURE_RED).scale(0.6)

        start_pos2 = np.array([4.25,-2.2,0])
        end_pos2 = np.array([0,0,0])
        delta_pos2 = end_pos2 - start_pos2
        bit1.move_to(start_pos2)
        self.play(bit1.animate.shift(delta_pos2),bit2.animate.shift(delta_pos1))

         #i want the mod 2 opetration of bit1 + bit2  to be in the mixed rectangle
         # 1000101011 + 0101010101 = 1101111110 
        self.play(FadeOut(bit1,run_time=1))
        self.play(FadeOut(bit2,run_time=1))           
        ans = Text("1101111110",color = PURE_RED).scale(0.6)
        ans.move_to(DOWN*0.1)
        self.play(Write(ans))

        added = Text("MIXED",color=PURE_BLUE).scale(0.6)
        added.move_to(UP*0.4)
        self.play(Write(added))

        random1 = Text("0101010101",color = PURE_RED).scale(0.6)
        start_pos3 = np.array([-4.25,-2.2,0])
        end_pos3 = np.array([-4.2,0.8,0])
        delta_pos3 = end_pos3 - start_pos3
        bit2.move_to(start_pos3)
        self.play(bit2.animate.shift(delta_pos3))

        message = Text("1101111110",color=PURE_RED).scale(0.6)
        start_pos4 = np.array([0,0,0])
        end_pos4 = np.array([4.2,0.8,0])
        delta_pos4 = end_pos4 - start_pos4
        message.move_to(start_pos4)
        self.play(message.animate.shift(delta_pos4))

        
       # self.play(FadeOut(bit2,run_time=0))
        self.play(FadeOut(mixed,run_time=1))
        self.play(FadeOut(added,run_time=1))
        self.play(FadeOut(ans,run_time=1))
        self.play(FadeOut(rectangle,run_time=1))
        self.play(FadeOut(text,run_time=1))
        self.play(FadeOut(vector,run_time=1))
        self.play(FadeOut(rectangle1,run_time=1))
        self.play(FadeOut(text1,run_time=1))
        self.play(FadeOut(random,run_time=1))
        

        




        







    