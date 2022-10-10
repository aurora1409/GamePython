
import pygame
import sys


class Square():
    def __init__(self):
        self.img = pygame.image.load('square-16.jpg')

    # def ChangeColor(self):

       # self.img = pygame.Color(r, g, b)

    def GetImage(self):

        return self.img
