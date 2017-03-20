from pygame import Rect, Color, Surface, sprite
from blocks import GameObject
from pyganim import PygAnimation
import pygame

XMOVE_SPEED = 5
YMOVE_SPEED = 5
WIDTH = 42
HEIGHT = 42
COLOR = "#888888"
ANIMATION_DELAY = 0.2  # скорость смены кадров
ANIMATION_RIGHT = ['player/r1..png',
                   'player/r2..png',
                   'player/r3..png']
ANIMATION_LEFT = ['player/l1..png',
                  'player/l2..png',
                  'player/l3..png']
ANIMATION_UP = ['player/u1..png',
                'player/u2..png',
                'player/u3..png']
ANIMATION_DOWN = ['player/d1..png',
                  'player/d2..png',
                  'player/d3..png']
ANIMATION_STAY = 'player/r1..png'


class Player(sprite.Sprite):

    def __init__(self, x, y, level_map):
        super().__init__()
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.i=0
        self.level_map = level_map
        self.image = Surface((WIDTH, HEIGHT))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.yvel = 0  # скорость вертикального перемещения
        self.image.set_colorkey(Color(COLOR))
        boltAnim = [(anim, ANIMATION_DELAY) for anim in ANIMATION_RIGHT]
        self.boltAnimRight = PygAnimation(boltAnim)
        self.boltAnimRight.play()
        boltAnim = [(anim, ANIMATION_DELAY) for anim in ANIMATION_LEFT]
        self.boltAnimLeft = PygAnimation(boltAnim)
        self.boltAnimLeft.play()
        self.boltAnimUp = PygAnimation(
            [(anim, ANIMATION_DELAY) for anim in ANIMATION_UP])
        self.boltAnimUp.play()
        self.boltAnimDown = PygAnimation(
            [(anim, ANIMATION_DELAY) for anim in ANIMATION_DOWN])
        self.boltAnimDown.play()

        # boltAnim = []
        # for anim in ANIMATION_LEFT:
        # boltAnim.append((anim, ANIMATION_DELAY))
        # self.boltAnimLeft = PygAnimation(boltAnim)
        # self.boltAnimLeft.play()

        # boltAnim = []
        # for anim in ANIMATION_UP:
        # boltAnim.append((anim, ANIMATION_DELAY))
        # self.boltAnimUp = PygAnimation(boltAnim)
        # self.boltAnimUp.play()

        # boltAnim = []
        # for anim in ANIMATION_DOWN:
        # boltAnim.append((anim, ANIMATION_DELAY))
        # self.boltAnimDown = PygAnimation(boltAnim)
        # self.boltAnimDown.play()
        self.key = False

        self.boltAnimStay = PygAnimation([(ANIMATION_STAY, 0.1)])
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))

    def update(self, position):
        horisontal, vertical = position
        if vertical:
            self.yvel = YMOVE_SPEED * vertical
            self.image.fill(Color(COLOR))
            if vertical < 0:
                self.boltAnimUp.blit(self.image, (0, 0))
            else:
                self.boltAnimDown.blit(self.image, (0, 0))
        if horisontal:
            self.xvel = XMOVE_SPEED * horisontal
            self.image.fill(Color(COLOR))
            if horisontal > 0:
                self.boltAnimRight.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))
        if not (horisontal or vertical):
            self.xvel = 0
            self.yvel = 0

        self.rect.y += self.yvel
        self.rect.x += self.xvel
        if self.xvel == self.yvel:
            return None, 1
        return self.collide()

    def collide(self):
        #screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # print('collide?')
        for p in self.level_map:
            if sprite.collide_rect(self, p):
                if p.object_type == 'key':
                    sprite.Sprite.kill(p)
                    p.object_type = 'button_pushed'
                    self.i=self.i+1
                    
    
                    # pygame.font.init()
                    # myfont = pygame.font.SysFont("monospace", 30, bold=True)
                    # Score = str("Score: ") + str(self.i)
                    # label = myfont.render((Score), 1, (255,0,40))
                    return None, 1
                    
                elif p.object_type == 'button_pushed':
                    return None, 1
                elif p.object_type == 'button_released':
                    return p, 1
                if self.xvel > 0:
                    self.rect.right = p.rect.left

                if self.xvel < 0:
                    self.rect.left = p.rect.right

                if self.yvel > 0:
                    self.rect.bottom = p.rect.top

                if self.yvel < 0:
                    self.rect.top = p.rect.bottom
           # screen.blit(label, (0, 0))
        return None, 1
        
    def func(self):
        myGlobal=str(self.i)
        return myGlobal

