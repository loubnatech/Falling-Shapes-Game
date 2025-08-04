from turtle import Turtle,Screen
from paddle import Paddle
from score import Score
import time
from ball import Ball
import random
window=Screen()
window.setup(width=800,height=600)
window.bgcolor("black")
window.tracer(0)
paddle=Paddle((0,-250))
score=Score()
ball=Ball()
window.listen()
window.onkey(paddle.move_right,"Right")
window.onkey(paddle.move_left,"Left")
GAME_ON=True
time_sleep=0.1
while GAME_ON:
    window.update()
    time.sleep(time_sleep)
    # قم بانتزال الاشكال من اعلى الشاشة
    ball.move()
    if ball.distance(paddle)<50 and ball.ycor()> -330:
        shape_type=ball.shape()
        color_type=ball.color()[0]
        if shape_type=="turtle":
            if color_type=="white":
                GAME_ON=False
                score.game_over()
            else:
                
                score.incresse_score(5)
        if shape_type=="circle":
            score.incresse_score(1)
        if shape_type=="square":
            score.incresse_score(2)
        if shape_type=="triangle":
            score.reset_score()
        ball.reset_position()
        time_sleep*=0.9
    if ball.ycor() < -230:
        ball.reset_position()
    
window.exitonclick()
