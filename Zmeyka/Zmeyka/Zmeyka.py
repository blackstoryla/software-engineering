# -*- coding: cp1251 -*-
import pygame
import time
import random

pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 10
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

count_food = 200
count_bot_snake = 10

way = [
   [1,4],
   [2,5],
   [1,6],
   [2,5],
   [3,3],
   [0,16],
   [3,9],
   [2,4],
   [3,8],
   [0,8],
   [1,3],
   [2,6],
   [1,3],
   [2,9],
   [1,2],
   [2,5],
   [3,8],
   [0,6],
   [1,11],
   [0,8],
   [1,9],
   [0,6],
   [3,5],
   [2,2],
   [3,5],
   [2,8]
    ]

class My_Snake:
   def __init__(self):
      self.x1 = dis_width / 2
      self.y1 = dis_height / 2
      self.x1_change = snake_block
      self.y1_change = 0
      self.snake_List = []
      self.Length_of_snake = 1
    
   def snake_draw(self, snake_block):
      for x in self.snake_List:
         pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
      pygame.draw.rect(dis, yellow, [x[0], x[1], snake_block, snake_block])


class Bot_Snake:
   def __init__(self):
      self.b_x1 = round(random.randrange(200, dis_width - snake_block - 200) / 10.0) * 10.0
      self.b_y1 = round(random.randrange(200, dis_height - snake_block - 200) / 10.0) * 10.0
      self.b_x1_change = -snake_block
      self.b_y1_change = 0
      self.b_length_of_snake = 1
      self.b_snake_list = []
      self.go_number = random.randrange(0, 10) * 5
      self.n_way = 0
      self.len_way = 0
      self.way_count = random.randrange(0,4)
     
   def bot_snake_draw(self, snake_block):
      for x in self.b_snake_list:
         pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])
       
   def bot_go(self):
       self.len_way = self.len_way - 1
       #print(self.len_way)

       if self.len_way <= 0:
           self.n_way = (self.n_way + 1) % len(way)
           self.len_way = way[self.n_way][1]
           #print("---",way[self.n_way])
       
       dir_way = (way[self.n_way][0] + self.way_count) % 4
       if dir_way == 0:
          self.b_x1_change = snake_block
          self.b_y1_change = 0
       if dir_way == 1:
          self.b_x1_change = 0
          self.b_y1_change = -snake_block
       if dir_way == 2:
          self.b_x1_change = -snake_block
          self.b_y1_change = 0
       if dir_way == 3:
          self.b_x1_change = 0
          self.b_y1_change = snake_block

def message(msg, color):
   mesg = font_style.render(msg, True, color)
   dis.blit(mesg, [dis_width/50, dis_height/3])
   
def Score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def gameLoop():
   game_over = False
   game_close = False
   game_stop = False
   
   Snake = My_Snake()
   
   food = []
   
   bot_snake = []
   
   for x in range(count_food):
      a1 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
      a2 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
      food.append([a1, a2])
      
   for x in range(count_bot_snake):
      A = Bot_Snake()
      bot_snake.append(A)
      
   while not game_stop:
      dis.fill(blue)
      message("Нажмите любую клавишу для начала игры", red)
      pygame.display.update()
      for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
            game_stop = True

   while not game_over:
      
      while game_close == True:
         dis.fill(blue)
         message("Вы проиграли! Нажмите Q для выхода или C для повторной игры", red)
         Score(Snake.Length_of_snake - 1)
         pygame.display.update()
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               game_over = True
               game_close = False
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_q:
                  game_over = True
                  game_close = False
               if event.key == pygame.K_c:
                  gameLoop()
                  
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            game_over = True
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
               Snake.x1_change = -snake_block
               Snake.y1_change = 0
            elif event.key == pygame.K_d:
               Snake.x1_change = snake_block
               Snake.y1_change = 0
            elif event.key == pygame.K_w:
               Snake.y1_change = -snake_block
               Snake.x1_change = 0
            elif event.key == pygame.K_s:
               Snake.y1_change = snake_block
               Snake.x1_change = 0
               
      if Snake.x1 >= dis_width or Snake.x1 < 0 or Snake.y1 >= dis_height or Snake.y1 < 0:
         game_close = True
      Snake.x1 += Snake.x1_change
      Snake.y1 += Snake.y1_change
      dis.fill(blue)
      
      for x in range(len(food)):
         pygame.draw.rect(dis, green, [food[x][0], food[x][1], snake_block, snake_block])
         
      snake_Head = []
      snake_Head.append(Snake.x1)
      snake_Head.append(Snake.y1)
      Snake.snake_List.append(snake_Head)
      
      if len(Snake.snake_List) > Snake.Length_of_snake:
         del Snake.snake_List[0]
      

      Snake.snake_draw(snake_block)
      Score(Snake.Length_of_snake - 1)
      
      
      for x in range(count_bot_snake):
         bot_snake[x].bot_go()
         bot_snake[x].b_x1 += bot_snake[x].b_x1_change
         bot_snake[x].b_y1 += bot_snake[x].b_y1_change
         b_snake_Head = []
         b_snake_Head.append(bot_snake[x].b_x1)
         b_snake_Head.append(bot_snake[x].b_y1)
         bot_snake[x].b_snake_list.append(b_snake_Head)
         if len(bot_snake[x].b_snake_list) > bot_snake[x].b_length_of_snake:
            del bot_snake[x].b_snake_list[0]
         bot_snake[x].bot_snake_draw(snake_block)
      
      pygame.display.update()
      
      for x in range(len(food)):
         if Snake.x1 == food[x][0] and Snake.y1 == food[x][1]:
            food[x][0] = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food[x][1] = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Snake.Length_of_snake += 1
          
         for i in range(len(bot_snake)):
            if bot_snake[i].b_x1 == food[x][0] and bot_snake[i].b_y1 == food[x][1]:
               food[x][0] = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
               food[x][1] = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
               bot_snake[i].b_length_of_snake += 1
       
      for x in range(len(bot_snake)):
         
         for y in range(len(bot_snake)):
             if x != y:
                
                for i in bot_snake[y].b_snake_list[:-1]:
                   if bot_snake[x].b_x1 == i[0] and bot_snake[x].b_y1 == i[1]:
                      
                      for j in bot_snake[x].b_snake_list:
                         food.append(j)
                         
                      bot_snake.pop(x)
                      A = Bot_Snake()
                      bot_snake.append(A)
                      
                   if Snake.x1 == i[0] and Snake.y1 == i[1]:
                      game_close = True
                      
         for i in Snake.snake_List[:-1]:
            if bot_snake[x].b_x1 == i[0] and bot_snake[x].b_y1 == i[1]:
                
                for j in bot_snake[x].b_snake_list:
                    food.append(j)
                    
                bot_snake.pop(x)
                A = Bot_Snake()
                bot_snake.append(A)
                

      while len(food)>count_food:
         food.pop(0)
         
      clock.tick(snake_speed)
   pygame.quit()
   quit()

gameLoop()