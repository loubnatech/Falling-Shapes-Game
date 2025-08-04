from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.y_move=-10
        self.shapes_list=shapes = ["turtle", "circle", "square", "triangle"]
        self.colors_list=["blanched almond", "blue", "blue violet", "brown", "burlywood"]
        self.reset_position()
    def move(self):
        self.goto(self.xcor(),self.ycor()+self.y_move)
    def reset_position(self):
        # اختيار مكان عشوائي
        random_position=random.randint(-350,350)
        self.goto(random_position,250)
        # اختيار شكل عشوائي
        random_shape=random.choice(self.shapes_list)
        self.shape(random_shape)
        # اختيار لون عشوائي
        random_color=random.choice(self.colors_list)
        self.color(random_color)
        # فرصة10  لتكون السلحفاة بيضاء
        if random_shape=="turtle" and random.randint(1, 10)==1:
            self.color("white")
        else:
            self.color(random_color)
        # اختيار حجم عشوائي
        random_size=random.uniform(0.5,2)
        self.shapesize(stretch_wid=random_size,stretch_len=random_size)
    