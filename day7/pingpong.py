import turtle as t
from functools import partial
import time
import random
GameSpeed=10

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
        self.x_direction=GameSpeed+random.randint(1,10)/10
        self.y_direction=GameSpeed+random.randint(1,10)/10


    def move(self):
        self.t.setx(self.t.xcor()+self.x_direction)
        self.t.sety(self.t.ycor()+self.y_direction)
        if abs(self.t.ycor())>yEdge:
            self.t.sety(self.t.ycor())
            self.y_direction=self.y_direction*-1




class Game:
    def __init__(self) -> None:
        self.balls=[]
        self.stop=False
        self.ai_mode=True
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
        self.balls.append(Ball())

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
        self.window.onkeypress(self.__add_ball,"a")
        self.window.onkeypress(self.__toggle_AI_mode,"t")

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
        for ball in self.balls:
            ball.move()
    def __add_ball(self):
        self.balls.append(Ball())
    
    def __toggle_AI_mode(self):
        self.ai_mode = not self.ai_mode

    def __print_time(self):
        self.pen.clear()
        self.t_game=round(time.time()-self.__start_time)
        self.pen.write(f"已开始游戏{self.t_game}秒",align="center",font=("Arial",24,"normal"))

    def __process_collision(self):
        for ball in self.balls:
            ball_x=ball.t.xcor()
            ball_y=ball.t.ycor()
            rp_y=self.right_player.t.ycor()
            lp_y=self.left_player.t.ycor()

            if abs(ball_x-350)<GameSpeed:
                if self.ai_mode:
                    self.right_player.t.sety(ball_y)
                    rp_y=self.right_player.t.ycor()


                if abs(ball_y-rp_y)<80:
                    ball.t.setx(350)
                    ball.x_direction=ball.x_direction*-1


            if abs(ball_x+350)<GameSpeed:
                if self.ai_mode:
                    self.left_player.t.sety(ball_y)
                    lp_y=self.left_player.t.ycor()

                if abs(ball_y-lp_y)<80:
                    ball.t.setx(-350)
                    ball.x_direction=ball.x_direction*-1
    
    def __game_over(self):
        self.pen.clear()
        self.pen.write(f"游戏结束: [{self.t_game}]秒",align="center",font=("Arial",24,"normal"))
        self.stop=True

    def __count_down(self):
        for i in range(5,0,-1):
            self.pen.clear()
            self.pen.write(f"游戏开始倒计时: {str(i)} 秒",align="center",font=("Arial",24,"normal"))
            time.sleep(1)
            self.window.update()
        self.__start_time=time.time()
        self.pen.clear()

    def __start(self):
        self.__count_down()
        while True:
            if not self.stop:
                self.__move_ball()
                self.__process_collision()
                self.__print_time()
                self.window.update()
                for ball in self.balls:
                    if abs(ball.t.xcor())>400:
                        self.__game_over()
            else:
                input()


if __name__=="__main__":
    game=Game()
