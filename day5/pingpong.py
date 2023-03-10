import turtle as t
from functools import partial
import time

GameSpeed=2

XEdge=380                                         
yEdge=280
class Player:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
        self.t=t.Turtle()
        self.t.speed(0)
        self.t.shape("square")
        self.t.color("blue")
        self.t.shapesize(stretch_wid=5,stretch_len=1)
        self.t.penup()
        self.t.goto(self.x,self.y)

class Ball:
    def __init__(self) -> None:
        self.t=t.Turtle()
        self.t.speed(0)
        self.t.color("red")
        self.t.shape("circle")
        self.t.penup()
        self.t.goto(0,0)
        self.x_direction=GameSpeed
        self.y_direction=GameSpeed


    def move(self):
        self.t.setx(self.t.xcor()+self.x_direction)
        self.t.sety(self.t.ycor()+self.y_direction)
        if abs(self.t.ycor())>yEdge:
            self.t.sety(self.t.ycor())
            self.y_direction=self.y_direction*-1




class Game:
    def __init__(self) -> None:
        self.window=t.Screen()
        self.window.title("ping pong game")
        self.window.bgcolor("white")
        self.window.setup(width=800,height=600)
        self.window.tracer(0)
        self.__setup_ui()
        self.__bind_keys()
        self.__start()
    def __setup_ui(self):
        self.left_player=Player(-350,0)
        self.right_player=Player(350,0)
        self.ball=Ball()
        self.pen=t.Turtle()
        self.pen.color("red")
        self.pen.penup()
        self.pen.goto(0,100)
        self.pen.hideturtle()

    def __bind_keys(self):
        self.window.listen()
        self.window.onkeypress(partial(self.__move_up,self.left_player),"w")
        self.window.onkeypress(partial(self.__move_up,self.right_player),"Up")
        self.window.onkeypress(partial(self.__move_down,self.left_player),"s")
        self.window.onkeypress(partial(self.__move_down,self.right_player),"Down")

    def __move_up(self,player:Player):
        _y=player.t.ycor()+90
        if _y>yEdge:
            player.t.sety(yEdge)
            return
        player.t.sety(_y)

    def __move_down(self,player:Player):
        _y=player.t.ycor()-90
        if _y<(-yEdge):
            player.t.sety(-yEdge)
            return
        player.t.sety(_y)

    def __move_ball(self):
        self.ball.move()
        
    def __process_collision(self):
        ball_x=self.ball.t.xcor()
        ball_y=self.ball.t.ycor()
        rp_y=self.right_player.t.ycor()
        lp_y=self.left_player.t.ycor()

        if abs(ball_x-350)<GameSpeed and abs(ball_y-rp_y)<80:
            self.ball.t.setx(350)
            self.ball.x_direction=self.ball.x_direction*-1

        if abs(ball_x+350)<GameSpeed and abs(ball_y-lp_y)<80:
            self.ball.t.setx(-350)
            self.ball.x_direction=self.ball.x_direction*-1
    
    def __game_over(self):
        self.pen.write("????????????",align="center",font=("Arial",24,"normal"))

    def __count_down(self):
        for i in range(5,0,-1):
            self.pen.clear()
            self.pen.write(f"?????????????????????: {str(i)} ???",align="center",font=("Arial",24,"normal"))
            time.sleep(1)
            self.window.update()
        self.pen.clear()

    def __start(self):
        self.__count_down()
        while True:
            self.__move_ball()
            self.__process_collision()
            self.window.update()
            if abs(self.ball.t.xcor())>400:
                self.__game_over()
  


if __name__=="__main__":
    game=Game()
