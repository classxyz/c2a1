# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 12:22:46 2021

@author: jp
"""

import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 400))

dino_rect = pygame.Rect(100, 250, 64, 64)
cactus_rect = pygame.Rect(1100, 300, 32, 32)
ground_rect = pygame.Rect(0, 330, 1200, 2)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    cactus_rect.x = cactus_rect.x-1     # Replace "--" to reduce 1 from cactus_rect.x.
    if cactus_rect.x <= -30:      # Replace "--" to make the line a conditional statement.
        cactus_rect.x = 1200      # Replace "--" with the coordinate you want.
    
    pygame.draw.rect(screen, (100, 100, 100), dino_rect)
    pygame.draw.rect(screen, (100, 100, 100), cactus_rect)
    pygame.draw.rect(screen, (100, 100, 100), ground_rect)
    
    pygame.display.update()

