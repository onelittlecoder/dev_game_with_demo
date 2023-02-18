import pygame
import sys
import random

# 初始化
pygame.init()

# 设置窗口大小
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)

# 设置标题
pygame.display.set_caption("贪吃蛇游戏")

# 设置帧率
clock = pygame.time.Clock()
FPS = 10

# 设置蛇的颜色
snake_color = (255, 255, 255)

# 设置食物的颜色
food_color = (255, 0, 0)

# 设置蛇的初始位置
snake_x = 50
snake_y = 50
snake_size = 10
snake_list = []
snake_length = 1

# 设置食物的位置
food_x = random.randint(0, window_size[0] // snake_size) * snake_size
food_y = random.randint(0, window_size[1] // snake_size) * snake_size

# 设置移动的方向
direction = "right"

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "up"
            elif event.key == pygame.K_DOWN:
                direction = "down"
            elif event.key == pygame.K_LEFT:
                direction = "left"
            elif event.key == pygame.K_RIGHT:
                direction = "right"

    # 移动蛇
    if direction == "right":
        snake_x += snake_size
    elif direction == "left":
        snake_x -= snake_size
    elif direction == "up":
        snake_y -= snake_size
    elif direction == "down":
        snake_y += snake_size

    # 增加蛇的长度
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # 如果蛇碰到边界或自身，则退出游戏
    if snake_x >= window_size[0] or snake_x < 0 or snake_y >= window_size[1] or snake_y < 0:
        pygame.quit()
        sys.exit()
    for segment in snake_list[:-1]:
        if segment == snake_head:
            pygame.quit()
            sys.exit()

    # 如果蛇吃到食物，则增加蛇的长度并重新生成食物
    if snake_x == food_x and snake_y == food_y:
        snake_length += 1
        food_x = random.randint(0, window_size[0] // snake_size) * snake_size
        food_y = random.randint(0, window_size[1] // snake_size) * snake_size

    # 更新屏幕
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, food_color, [food_x, food_y, snake_size, snake_size])
    for segment in snake_list:
        pygame.draw.rect(screen, snake_color, [segment[0], segment[1], snake_size, snake_size])
    pygame.display.update()
    clock.tick(FPS)
