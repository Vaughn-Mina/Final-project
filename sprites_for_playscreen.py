# File created by Vaughn Mina
# Modeled after Mr. Cozort's code "Spritesheet.py"


# sets up file with multiple images from spritesheet
import pygame as pg
from pygame.sprite import Sprite
from os import path
from settings_for_playscreen import *

dir = path.dirname(__file__)
img_dir = path.join(dir, 'images')
SPRITESHEET = "Sprite_Sheet_for_final_project_coding.png"

class Spritesheet:
    def __init__(self,filename):
        self.spritesheet = pg.image.load(filename).convert()
    def get_image(self, x, y, width, height):
        # grabs the sprite images that would make the animation from the sprite sheet
        image = pg.Surface((width,height))
        image.blit(self.spritesheet, (0,0), (x, y, width, height))
        image = pg.transform.scale(image, (width*2, height*2))
        return image 
class Animated_sprite(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.spritesheet = Spritesheet(path.join(img_dir, "Sprite_Sheet_for_final_project_coding.png"))
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.idle = True
        self.jumping = False
        self.walking = False
        self.current_frame = 0
        self.last_update = 0
    def input(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_d]:
            self.idle = False
            self.walking = True 
            print("I am walking")
            self.current_frame +=1
    def load_images(self):
        self.standing_frames = [self.spritesheet.get_image(0, 0, 32, 32),
                                self.spritesheet.get_image(32, 0, 32, 32)]
        # self.walk_frames_r = [self.spritesheet.get_image(64, 0, 32, 32),
        #                           self.spritesheet.get_image(96, 0, 32, 32)]
        # for frame in self.standing_frames: 
        #         frame.set_colorkey(BLACK)
        # self.walk_frames_r = [self.spritesheet.get_image(0, 0, 32, 32),
        #                         self.spritesheet.get_image(32, 0, 32, 32)]
        # for frame in self.walk_frames_r:
        #     frame.set_colorkey(BLACK)
        #     self.walk_frames_r.append(pg.transform.flip(frame, True, False))
        # self.jump_frame = self.spritesheet.get_image(382, 763, 150, 181)
        # self.jump_frame.set_colorkey(BLACK)
    def animate(self):
        now = pg.time.get_ticks()
        if not self.jumping and not self.walking:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
                bottom = self.rect.bottom
                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
    def update(self):
        self.input()
        self.animate()
