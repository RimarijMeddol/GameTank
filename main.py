import pygame
from player import *
from blocks import *
from pyganim import *
#changing


WIN_WIDTH = 800  #
WIN_HEIGHT = 640  #
BACKGROUND_COLOR = "#004400"


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)                           #
    l = max(-(camera.width - WIN_WIDTH), l)   #
    t = max(-(camera.height - WIN_HEIGHT), t)
    t = min(0, t)                           #

    return Rect(l, t, w, h)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  #
    pygame.display.set_caption("X500")  #
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  #
    #
    bg.fill(Color(BACKGROUND_COLOR))

    entities = pygame.sprite.Group()  #
    with open('level.txt', 'r') as level_map:
        lines = level_map.readlines()
        level = [string[:-2] for string in lines[1:-3]]
    all_blocks = []
    interactive = []
    timer = pygame.time.Clock()
    block_list = pygame.sprite.Group()

    x, y = 0, 0

    for row in level:
        for block_type in row:
            if block_type != ' ':
                # if block_type == '1':

                pf = GameObject(x, y, block_type)
                entities.add(pf)
                all_blocks.append(pf)
            # elif col == "+":
                # k = Key(x, y)
                # entities.add(k)
                # interactive.append(k)
                # x_key=x
                # y_key=y
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

    total_level_width = len(level[0]) * PLATFORM_WIDTH  #
    total_level_height = len(level) * PLATFORM_HEIGHT  #

    playerX = 80
    playerY = 60
    hero = Player(playerX, playerY, all_blocks)
    print('Is Player: ', isinstance(hero, Player))
    print('Is String: ', isinstance(hero, str))
    entities.add(hero)
    

    camera = Camera(camera_configure, total_level_width, total_level_height)
    position = (0, 0) # (h, v)
    myText=' '
    moving = False

    def check_button(ret_object, check):
        print('Button_pressed')
        x, y = ret_object.coord_x, ret_object.coord_y
        ret_object.kill()
        entities.add(GameObject(x, y, '2'))
    while True:  #
        timer.tick(60)
        for event in pygame.event.get():  #
            if event.type == pygame.QUIT:
                raise SystemExit('Quit')
            try:
                key, k_type = event.key, event.type
            except AttributeError:
                continue
            if k_type == pygame.KEYDOWN:
                if key == pygame.K_ESCAPE:
                    raise SystemExit('Quit')
                elif key == pygame.K_LEFT and not moving:
                    position = (-1, 0)
                    moving = True
                elif key == pygame.K_RIGHT and not moving:
                    position = (1, 0)
                    moving = True
                elif key == pygame.K_UP and not moving:
                    position = (0, -1)
                    moving = True
                elif key == pygame.K_DOWN and not moving:
                    position = (0, 1)
                    moving = True
            else:
                if k_type == pygame.KEYUP:
                    position = (0, 0)
                    moving = False
        pygame.font.init()
        myfont = pygame.font.SysFont("monospace", 30, bold=True)
        fpsData = str("FPS: ") + str(int(timer.get_fps()))
        Score = str("Score: ") + hero.func()
        label = myfont.render((fpsData), 1, (255,0,0))
        label2 = myfont.render((Score), 1, (255,0,0))
        # k = Key(x_key, y_key)
        # entities.add(k)
        # interactive.append(k)
        screen.blit(bg, (0, 0))
        ret_object, check = hero.update(position)
        if ret_object is not None:
            check_button(ret_object, check)
        camera.update(hero)  #
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        screen.blit(hero.image, camera.apply(hero))
        screen.blit(label, (0, 0))
        screen.blit(label2, (0, 40))
        pygame.display.update()
        print(hero.func())

if __name__ == "__main__":
    main()
