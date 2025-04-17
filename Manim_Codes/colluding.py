from manim import *

class Colluding(Scene):
    def construct(self):

        #start writting from here
        # ManThinking = ImageMobject("ManThinking.png").scale(0.8)
        #now bringing a man
        text = Text("Assume there is a vault with three keys")
        self.play(Write(text))
        self.play(FadeOut(text))
        #in this i want that my lock should be in the top and then one men below to left 
        lock = ImageMobject("Picture1.jpg").scale(1)
        lock.generate_target()
        lock.target.move_to(UP*2)
        self.play(MoveToTarget(lock))
        

        men1 = ImageMobject("ManThinking.png").scale(0.5)
        men1.generate_target()
        men1.target.move_to(LEFT*3+DOWN*2)
        self.play(MoveToTarget(men1))
       # self.wait(1)
        men2 = ImageMobject("ManThinking.png").scale(0.5)
        men2.generate_target()
        men2.target.move_to(DOWN*2)
        self.play(MoveToTarget(men2))
       # self.wait(1)
        men3 = ImageMobject("ManThinking.png").scale(0.5)
        men3.generate_target()
        men3.target.move_to(RIGHT*3+DOWN*2)
        self.play(MoveToTarget(men3))

        #till here i have added men
         
        #done for key 1
        key = ImageMobject("keyfinal.png").scale(1.6)
        key.generate_target()
        key.target.move_to(LEFT*3)
        self.play(MoveToTarget(key))
        key.target.move_to(UP*2+LEFT*2.8)
        self.play(MoveToTarget(key))
        together = Group(lock,key)
        self.play(Wiggle(together))
        self.wait(1)
        key.target.move_to(LEFT*3)
        self.play(MoveToTarget(key))


        #doing for key 3
        key3 = ImageMobject("keyfinal.png").scale(1.6)
        key3.generate_target()
        key3.target.move_to(RIGHT*3)
        self.play(MoveToTarget(key3))
        key3.target.move_to(UP*2+RIGHT*1.8)
        self.play(MoveToTarget(key3))
        together = Group(lock,key3)
        self.play(Wiggle(together))
        self.wait(1)
        key3.target.move_to(RIGHT*3)
        self.play(MoveToTarget(key3))
         
        #doing for key 2
        key2 = ImageMobject("keyfinal.png").scale(1.6)
        key2.generate_target()
       #key2.target.move_to(LEFT*3)
        self.play(MoveToTarget(key2))
        key2.target.move_to(UP*2+LEFT*0.6)
        self.play(MoveToTarget(key2))
        together = Group(lock,key2)
        self.play(Wiggle(together))
        self.wait(1)
        key2.target.move_to(DOWN*0.001)
        self.play(MoveToTarget(key2))

        #now i have to move all the keys to the lock
        key.generate_target()
        key.target.move_to(UP*2+LEFT*2.8)
      #  self.play(MoveToTarget(key))

        #my key is going behind the value so i have to bring it to front
       # key.bring_to_front(key)

        key2.generate_target()
        key2.target.move_to(UP*2+LEFT*0.6)
        key3.generate_target()
        key3.target.move_to(UP*2+RIGHT*1.8)
        self.bring_to_front(key,key2,key3)

        self.play(MoveToTarget(key),MoveToTarget(key2),MoveToTarget(key3))

        self.wait(1)
        money = ImageMobject("money.png").scale(0.75)
        money.move_to(UP*1.3)
        self.play(FadeOut(key),FadeOut(key2),FadeOut(key3),run_time=1)
        self.play(FadeOut(lock),FadeIn(money),run_time=1)

        

