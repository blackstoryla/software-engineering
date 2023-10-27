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
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

count_food = 100
count_bot_snake = 5

class Bot_Snake:
   def __init__(self):
      self.b_x1 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
      self.b_y1 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
      self.b_x1_change = -snake_block
      self.b_y1_change = 0
      self.b_length_of_snake = 1
      self.b_snake_list = []
      self.go_number = random.randrange(0, 100)
     
   def bot_snake_draw(self, snake_block):
      for x in self.b_snake_list:
         pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])
         
   def bot_go(self):
      if self.go_number % 5 == 0:
          self.b_x1_change = -snake_block
          self.b_y1_change = 0
      elif self.go_number % 7 == 0:
          self.b_x1_change = snake_block
          self.b_y1_change = 0
      elif self.go_number % 11 == 0:
          self.b_y1_change = -snake_block
          self.b_x1_change = 0
      elif self.go_number % 13 == 0:
          self.b_y1_change = snake_block
          self.b_x1_change = 0
      self.go_number += random.randrange(0, 10)

def Your_score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
   for x in snake_list:
      pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
   mesg = font_style.render(msg, True, color)
   dis.blit(mesg, [dis_width/50, dis_height/3])

def gameLoop():
   game_over = False
   game_close = False
   
   x1 = dis_width / 2
   y1 = dis_height / 2
   x1_change = 0
   y1_change = 0
   
   snake_List = []
   Length_of_snake = 1
   
   food = []
   
   bot_snake = []
   
   for x in range(count_food):
      a1 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
      a2 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
      food.append([a1, a2])
      
   for x in range(count_bot_snake):
      A = Bot_Snake()
      bot_snake.append(A)

   while not game_over:
      
      while game_close == True:
         dis.fill(blue)
         message("Вы проиграли! Нажмите Q для выхода или C для повторной игры", red)
         Your_score(Length_of_snake - 1)
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
            if event.key == pygame.K_LEFT:
               x1_change = -snake_block
               y1_change = 0
            elif event.key == pygame.K_RIGHT:
               x1_change = snake_block
               y1_change = 0
            elif event.key == pygame.K_UP:
               y1_change = -snake_block
               x1_change = 0
            elif event.key == pygame.K_DOWN:
               y1_change = snake_block
               x1_change = 0
               
      if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
         game_close = True
      x1 += x1_change
      y1 += y1_change
      dis.fill(blue)
      
      for x in range(len(food)):
         pygame.draw.rect(dis, green, [food[x][0], food[x][1], snake_block, snake_block])
         
      snake_Head = []
      snake_Head.append(x1)
      snake_Head.append(y1)
      snake_List.append(snake_Head)
      
      if len(snake_List) > Length_of_snake:
         del snake_List[0]
         
      # for x in snake_List[:-1]:
      #    if x == snake_Head:
      #       game_close = True

      
      our_snake(snake_block, snake_List)
      Your_score(Length_of_snake - 1)
      
      #Обработка ботов 
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
         if x1 == food[x][0] and y1 == food[x][1]:
            food[x][0] = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food[x][1] = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            
      clock.tick(snake_speed)
   pygame.quit()
   quit()

gameLoop()