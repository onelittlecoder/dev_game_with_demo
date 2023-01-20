import turtle as t
from functools import partial
GameSpeed=5

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
        self.x_edge=380
        self.y_edge=280
    def move(self):
        print(self.t.xcor(),self.t.ycor())
        if abs(self.t.ycor())>self.y_edge:
            self.t.sety(self.t.ycor())
            self.y_direction=self.y_direction*-1
        if abs(self.t.xcor())>self.x_edge:
            self.t.setx(self.t.xcor())
            self.x_direction=self.x_direction*-1

        self.t.setx(self.t.xcor()+self.x_direction)
        self.t.sety(self.t.ycor()+self.y_direction)

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

    def __bind_keys(self):
        self.window.listen()
        self.window.onkeypress(partial(self.__move_up,self.left_player),"w")
        self.window.onkeypress(partial(self.__move_up,self.right_player),"Up")
        self.window.onkeypress(partial(self.__move_down,self.left_player),"s")
        self.window.onkeypress(partial(self.__move_down,self.right_player),"Down")

    def __move_up(self,player:Player):
        player.t.sety(player.t.ycor()+90)

    def __move_down(self,player:Player):
        player.t.sety(player.t.ycor()-90)

    def __move_ball(self):
        self.ball.move()

    def __start(self):
        while True:
            self.__move_ball()
            self.window.update()
            pass


if __name__=="__main__":
    game=Game()
