class Test(Scene):
    def construct(self):
        image = ImageMobject("input.png")
        self.add(image)
        self.wait()