from random import randint
from pygame import*
init()

win_width = 1280
win_height = 720

class GameSprite(sprite.Sprite):
     def __init__(self, player_imag, player_x, player_y, size_x, size_y, player_speed):
         sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
   
class Player(GameSprite):
    def update_l_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_height - 80:
            self.rect.x += self.speed
    def update_a_d(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < win_height - 80:
            self.rect.x += self.spee

      
class Enemy(GameSprite):
  def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, side='left'):
      GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y, player_speed)        
      self.side = side
        
   def update(self):
    global side
    if self.side == 'right':
        self.rect.x -= self.speed
    if self.side == 'left':
        self.rect.x += self.speed
window = display.set_mode((win_width, win_height))
display.set_caption("Arcada")      
      
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
display.update()
    clock.tick(FPS)
