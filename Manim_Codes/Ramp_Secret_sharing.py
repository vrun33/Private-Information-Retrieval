from manim import *


class ramp_secret_sharing(Scene):
    def construct(self):
        text1 = Tex("Ramp Sharing Scheme").scale(1)
        text1.set_color(ORANGE)
        
        text = Tex("Now we discuss", color=WHITE).scale(1)
        text.shift(LEFT*2)
        text1.next_to(text,RIGHT)
        # text4.add(text5)
        self.play(Write(text))
        self.play(Write(text1))
        self.play(FadeOut(text),FadeOut(text1),run_time = 1)

        text22 = Tex("$f(t) = S + R_{1} \cdot t + R_{2} \cdot t^{2}$ ").scale(1)
        text22.set_color(ORANGE)
        text2 = Tex("In the (5,3) Threshold Secret Sharing,the polynomial used is").scale(0.7)
        text2.shift(ORIGIN)
        text22.next_to(text2,DOWN)
        self.play(Write(text2))
        self.play(Write(text22))
        
        self.play(FadeOut(text2),FadeOut(text22),run_time = 1)

        text33 = Tex("$g(t) = S_{1} +S_{2} \cdot t + S_{3} \cdot t^{2} + R_{1} \cdot t^{3} + R_{2} \cdot t^{4}$").scale(1)
        text33.set_color(ORANGE)
        text3 = Tex("In the Ramp Sharing Scheme, we consider").scale(1)
        text3.shift(ORIGIN)
        text33.next_to(text3,DOWN)
        self.play(Write(text3))
        self.play(Write(text33))
        self.play(FadeOut(text3),FadeOut(text33),run_time = 1)

        #r"$\text{Download Rate} = \frac{1}{7}$"
        #, which is an improvement over the (N, T + 1)-threshold secret sharing scheme at the cost of noise resilience.$").scale(0.7)
        text44 = Tex(r"$\text{, which is an improvement over the (N, T + 1)-threshold secret sharing}$").scale(0.75)
        text4 = Tex(r"$\text{This Results in a communication rate } $=$ $").scale(1)
        rate = Tex("$\\frac{3}{5}$")
        rate.color = ORANGE
        text4.shift(UP*1.5)
        rate.next_to(text4,RIGHT)
        text45 = Tex("scheme at the cost of noise resilience.").scale(1)
        text4.shift(ORIGIN)
        text44.next_to(text4,DOWN)
        text45.next_to(text44,DOWN)
        self.play(Write(text4))
        self.play(Wiggle(rate))
        self.play(Write(text44))
        self.play(Write(text45))
        self.wait(4)
        self.play(FadeOut(text4),FadeOut(text44),FadeOut(text45),FadeOut(rate),run_time = 1)

        ramp = Tex("The General ramp secret sharing scheme is as follows")
        ramp.shift(UP*3.5)
        self.wait(1)
        main = Tex("(N,B,T+1)- Ramp Secret Sharing").scale(0.8)
        main.set_color(ORANGE)
        main.next_to(ramp,DOWN)
        self.wait(1)
        #now i want to add bullet points one by one
        #there is no gap between the text in bullet points please correct

        b1 = Tex("1.The secrets are elements $S_{1},S_{2}.......,S_{B-T+1}$").scale(0.7)
        b1.shift(UP*1.5)
        b2 = Tex("2.The number of shareholders is N (N $<$ q)").scale(0.7)
        b2.next_to(b1,DOWN)
        b3 = Tex("3.The minimum threshold required to learn something about secrets is T+1").scale(0.7)
        b3.next_to(b2,DOWN)
        b4 = Tex("4.The threshold to uniquely determine all secrets is B+1 .$(T \\leq b < N)$").scale(0.7)
        b4.next_to(b3,DOWN)
        b5 = Tex("Step 1: Choose T random keys $R_{1},R_{2}....,R{T} \\in F_{q}$ uniformly at random").scale(0.7)
        b5.next_to(b4,DOWN)
        b6 = Tex("Step 2: Define the polynomial $f(t) = S_{1} + S_{2} \\cdot t +....+ S_{B-T+1} \\cdot t^{B-T} + R_{1} \\cdot t^{B-T} +....+ R_{T} \\cdot t^{B}$.").scale(0.7)
        b6.next_to(b5,DOWN)
        b7 = Tex("Step 3: Each shareholder i receives the share f(i)").scale(0.7)
        b7.next_to(b6,DOWN)
        self.wait(7)
        self.play(Write(ramp),run_time=0.3)
        self.play(Write(main),run_time=0.3)
        self.play(Write(b1),run_time=0.3)
        self.play(Write(b1),run_time=0.3)
        self.play(Write(b2),run_time=0.3)
        self.play(Write(b3),run_time=0.3)
        self.play(Write(b4),run_time=0.3)
        self.play(Write(b5),run_time=0.3)
        self.play(Write(b6),run_time=0.3)
        self.play(Write(b7),run_time=0.3)
        self.play(FadeOut(ramp),FadeOut(main),FadeOut(b1),FadeOut(b2),FadeOut(b3),FadeOut(b4),FadeOut(b5),FadeOut(b6),FadeOut(b7),run_time=0.3)
        
        random1 = Tex("we can ensure privacy against any T colluding servers,").scale(1)
        random = Tex("Using an (N,B,T+1)-Ramp Secret Sharing Scheme,").scale(1)
        random.shift(UP*1.5)
        random1.next_to(random,DOWN)
        random11 = Tex("achieve tolerance to B-T erasures,").scale(1)
        random11.next_to(random1,DOWN)
        random2 = Tex("and correct up to $\\frac{B - T}{2}$ errors").scale(1)
        random2.next_to(random11,DOWN)

        self.play(Write(random),run_time=0.3)
        self.play(Write(random1),run_time=0.3)
        self.play(Write(random11),run_time=0.3)
        self.play(Write(random2),run_time=0.3)
        self.play(FadeOut(random),FadeOut(random1),FadeOut(random11),FadeOut(random2),run_time=0.3)

        random3 = Tex("When this scene is applied to a classical PIR setting , the PIR capacity i observed to be").scale(0.75)
        random4 = Tex("$= \\frac{N-T \\cdot N^{M-1}}{N^{M}-T^{M}}$").scale(1)
        random4.color = ORANGE
        random4.shift(UP*1.5)
        random3.next_to(random4,UP)
        random5 = Tex("which depends on the number of messages M").scale(1)
        random5.next_to(random4,DOWN)
        random6 = Tex("Thus we look upon Refining and Lifting Schemes,").scale(1)
        random6.next_to(random5,DOWN)
        random7 = Tex("wherein optimal capacity can be achieved.").scale(1)
        random7.next_to(random6,DOWN)
        self.wait(2)
        self.play(Write(random3),run_time=0.3)
        self.play(Wiggle(random4),run_time=0.3)
        self.play(Write(random5),run_time=0.3)
        self.play(Write(random6),run_time=0.3)
        self.play(Write(random7),run_time=0.3)
        self.play(FadeOut(random3),FadeOut(random4),FadeOut(random5),FadeOut(random6),FadeOut(random7),run_time=0.3)
        self.wait(1)
        



        



