from manim import *

class Database(Scene):
    def construct(self):
        ManWithComputer = ImageMobject("1.png").scale(0.8)
        User = Tex("User").scale(0.8)
        # Keep user with computer below the image
        User.next_to(ManWithComputer, DOWN)
        self.play(FadeIn(ManWithComputer), Write(User))
        UserComp = Group(ManWithComputer, User)
        UserComp.generate_target()
        UserComp.target.move_to(LEFT * 4)
        self.play(MoveToTarget(UserComp))

        Database1 = ImageMobject("Database.png").scale(0.75)
        DataBase2 = ImageMobject("Database.png").scale(0.75)
        DataBase3 = ImageMobject("Database.png").scale(0.75)


        DataBase1Text = Tex("Database 2").scale(0.8)
        DataBase2Text = Tex("Database 1").scale(0.8)
        DataBase3Text = Tex("Database 3").scale(0.8)

        #Play the images of the three databases on the right side of the screen
        Database1.move_to(RIGHT * 3.5)
        Database2 = Database1.copy()
        Database3 = Database1.copy()
        Database2.move_to(RIGHT * 3 + UP * 2.5)
        Database3.move_to(RIGHT * 3 + DOWN * 2.5)
        
        #Play the text of the three databases on the right side of the screen beside the images
        DataBase1Text.next_to(Database1, RIGHT)
        DataBase2Text.next_to(Database2, RIGHT)
        DataBase3Text.next_to(Database3, RIGHT)

        self.play(FadeIn(Database1), FadeIn(Database2), FadeIn(Database3))
        self.play(Write(DataBase1Text), Write(DataBase2Text), Write(DataBase3Text))

        # Draw an arrow from the user to the databases with the Labels "Query" 
        # Arrow1 = Arrow(start=User.get_right(), end=Database1.get_left(), color=GREEN)
        # Arrow2 = Arrow(start=User.get_right(), end=Database2.get_left(), color=GREEN)
        # Arrow3 = Arrow(start=User.get_right(), end=Database3.get_left(), color=GREEN)
        Query1 = Tex("Query 2", color = GREEN).scale(0.65)
        Query2 = Tex("Query 1", color = GREEN).scale(0.65)
        Query3 = Tex("Query 3", color = GREEN).scale(0.65)
        # Query2 = Query1.copy()
        # Query3 = Query1.copy()
        # Query1.next_to(Arrow1, UP*0.25)
        # Query2.next_to(Arrow2, UP*3)
        # Query3.next_to(Arrow3, DOWN*1.5)
        # self.play(GrowArrow(Arrow1), GrowArrow(Arrow2), GrowArrow(Arrow3))
        # self.play(Write(Query1))
        Response = Tex("Response 2", color = RED).scale(0.65)
        Response2 = Tex("Response 1", color = RED).scale(0.65)
        Response3 = Tex("Response 3", color = RED).scale(0.65)

        l_arrow = LabeledArrow(Query1, start= ManWithComputer.get_right(), end= Database1.get_left(), label_position=0.5, label_frame = False, color=GREEN, stroke_width=1.5, tip_shape=StealthTip)
        l_arrow2 = LabeledArrow(Query2, start= ManWithComputer.get_right(), end= Database2.get_left(), label_position=0.5, label_frame = False, color=GREEN, stroke_width=1.5, tip_shape=StealthTip)
        l_arrow3 = LabeledArrow(Query3, start= ManWithComputer.get_right(), end= Database3.get_left(), label_position=0.5, label_frame = False, color=GREEN, stroke_width=1.5, tip_shape=StealthTip)

        self.play(GrowArrow(l_arrow),GrowArrow(l_arrow2),GrowArrow(l_arrow3))

        l_arrow4 = LabeledArrow(Response, start= Database1.get_left(), end= ManWithComputer.get_right() + RIGHT*0.2  , label_position=0.5, label_frame = False, color=RED, stroke_width=1.5, tip_shape=StealthTip)
        l_arrow5 = LabeledArrow(Response2, start= Database2.get_left(), end= ManWithComputer.get_right() + RIGHT*0.20 + UP*0.2, label_position=0.5, label_frame = False, color=RED, stroke_width=1.5, tip_shape=StealthTip)
        l_arrow6 = LabeledArrow(Response3, start= Database3.get_left(), end= ManWithComputer.get_right() + RIGHT*0.20 + DOWN* 0.2, label_position=0.5, label_frame = False, color=RED, stroke_width=1.5, tip_shape=StealthTip)

        self.wait(3)
        #Transform the arrows to the response arrows
        self.play(Transform(l_arrow, l_arrow4), Transform(l_arrow2, l_arrow5), Transform(l_arrow3, l_arrow6))
        self.wait(3)


        
