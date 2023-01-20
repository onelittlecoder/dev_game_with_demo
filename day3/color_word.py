import pygame
import sys
import random
import subprocess
audios=["/Users/super/work/projects/python_src/day3/what_color.wav","/Users/super/work/projects/python_src/day3/what_word.wav"]
words=["红","黑","白","黄","绿","蓝"]
colors=[(255,0,0),
        (255,255,255),
        (255,255,0),
        (255,0,255),
        (0,0,255)
    ]
pygame.init()
pygame.display.set_caption("color game")
screen = pygame.display.set_mode((500, 500))
font = pygame.font.SysFont('pingfang', 100)
while 1:
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            sys.exit()
        if envent.type==771:
            screen.fill((0,0,0))
            text = font.render(random.choice(words), True, random.choice(colors))
            screen.blit(text, (200, 160))
            pygame.display.update()
            num = random.randint(1,1000)
            random.seed(num) 
            return_code = subprocess.call(["afplay", random.choice(audios)])