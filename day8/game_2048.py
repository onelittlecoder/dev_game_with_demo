import pygame
import sys
import random

def getRandomPos():
    return [random.choice(range(0,1200)),random.choice(range(0,500))]
class Game:
    def __init__(self,name) -> None:
        pygame.init()
        pygame.display.set_caption(name)
        self.screen = pygame.display.set_mode((1280, 600))
        pygame.mouse.set_visible(False)
        self.start()


    def start(self):
        player=Ball(2,0,0,self.screen,"player")
        correct=Ball(2,getRandomPos()[0],getRandomPos()[1],self.screen,"correct")
        wrong=Ball(1,getRandomPos()[0],getRandomPos()[1],self.screen,"wrong")
        group=pygame.sprite.Group()
        group.add(player)
        group.add(correct)
        group.add(wrong)

        while True:
            for envent in pygame.event.get():
                if envent.type == pygame.QUIT:
                    sys.exit()
                self.screen.fill((0,0,0))
                group.update()

                if abs(correct.x-player.x)<=25 and abs(correct.y-player.y)<=25:
                    player.value+=1
                    correct.value+=1
                    wrong.value+=1
                    correct.update_pos(getRandomPos()[0],getRandomPos()[1])
                    wrong.update_pos(getRandomPos()[0],getRandomPos()[1])

                pygame.display.update()

class Ball(pygame.sprite.Sprite):
    def __init__(self,value,x,y,screen,role) -> None:
        super(Ball,self).__init__()
        self.font = pygame.font.SysFont('pingfang',20)
        self.value=value
        self.x=x
        self.y=y
        self.screen=screen
        self.role=role
        # self.setup_ui()
        
    
    def setup_ui(self):
        self.img=pygame.image.load("day8/ball.png").convert_alpha()
        self.circle=pygame.transform.scale(self.img, (50, 50))
        self.screen.blit(self.circle, (self.x, self.y)) 
        text = self.font.render(str(self.value), True, (255, 255, 255))
        self.screen.blit(text, (self.x+20, self.y+10))

    def update(self):
        if self.role=="player":
            (x,y)=pygame.mouse.get_pos()
            self.x=x
            self.y=y
        self.setup_ui()

    def update_value(self,value):
        self.value=value

    def update_pos(self,x,y):
        self.x=x
        self.y=y

if __name__=="__main__":
    game=Game("2048")
    game.start()  