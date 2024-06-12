import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_rendering import *
from Sprite_object import *
from object_handler import *
from weapon import *
from sounds import *
from Pathfind import *

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(0)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_rendering = ObjectRenderer(self)
        self.raycasting = Raycasting(self)
        self.object_handler = Object_handler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfind = PathFinding(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() : .1f}')

    def draw(self):
        # self.screen.fill('black')
        self.object_rendering.draw()
        self.weapon.draw()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.type == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
