import pygame
from src import hero

class HealthBars(pygame.sprite.Sprite):
    def __init__(self, img_file, hero, num):
        #initialize all the Sprite functionality
      pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
      self.image = pygame.image.load(img_file).convert_alpha()
      self.hero = hero
      self.image = pygame.transform.scale(self.image,(600,250))
        #get the rectangle for positioning
      self.num = num
      self.rect = self.image.get_rect()
      self.rect.x = 30
      self.rect.y = -85
        #set other attributes

    def update(self):
      if self.hero.health == 2 and self.num == 3:
        self.kill()
      elif self.hero.health == 1 and self.num == 2:
        self.kill()
      elif self.hero.health == 0 and self.num == 1:
        self.kill()
    