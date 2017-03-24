from pygame import sprite, Surface, Color, Rect, image
from main import *

PLATFORM_WIDTH = 75
PLATFORM_HEIGHT = 75
PLATFORM_COLOR = "#FF6262"
object_images = {
        "a": "block/AngleUR1.png",
        "b": "block/AngleUL1.png",
        "c": "block/AngleDR1.png",
        "d": "block/AngleDL1.png",
        "e": "block/WallR1.png",
        "f": "block/WallL1.png",
        "g": "block/WallU1.png",
        "h": "block/WallD1.png",
        "i": "block/AngleInUR1.png",
        "j": "block/AngleInUL1.png",
        "k": "block/AngleInDR1.png",
        "l": "block/AngleInDL1.png",
        "m": "block/IntersectionURLD1.png",
        "n": "block/IntersectionURD1.png",
        "o": "block/IntersectionULD1.png",
        "p": "block/IntersectionRUL1.png",
        "q": "block/IntersectionRDL1.png",
        "r": "block/IntersectionRL1.png",
        "s": "block/IntersectionUD1.png",
        "t": "block/IntersectionLR1.png",
        "u": "block/IntersectionDU1.png",
        "v": "block/EndL1.png",
        "w": "block/EndR1.png",
        "x": "block/EndU1.png",
        "y": "block/EndD1.png",
        "z": "block/Pillar1.png",
        "A": "block/WallLR1.png",
        "B": "block/WallUD1.png",
        '1': "block/Key.png",
        '0': "block/Button1.png",
        '2': "block/ButtonPushed1.png"}


class GameObject(sprite.Sprite):
    object_type = 'wall'
    coord_x = None
    coord_y = None

    def __init__(self, x, y, block_type):
        super().__init__() # 
        # sprite.Sprite.__init__(self)
        self.coord_x, self.coord_y = x, y
        self.choice_object_type(x,y,block_type)

    def choice_object_type(self, x, y, block_type):
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = image.load(object_images[block_type])
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        # a bit more correct solution?
        # self.rect = self.image.get_rect()
        # self.rect.centerx, self.rect.centery = x, y

        if block_type == '1':
            self.object_type = 'key'
        elif block_type == '0':
            self.object_type = 'button_released'
        elif block_type == '2':
            self.object_type = 'button_pushed'



#class Door(sprite.Sprite):
    #def __init__(self, x, y):
        #if :
            #sprite.Sprite.__init__(self)
            #self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
            #self.image = image.load("block/Door1.png")
            #self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        #else:
            #sprite.Sprite.__init__(self)
            #self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
            #self.image = image.load("block/Door1Open.png")
            #self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)