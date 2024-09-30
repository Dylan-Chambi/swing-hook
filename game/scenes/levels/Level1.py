import pygame
import sys
from game.scenes.Scene import Scene

from game.items.actors.Player import Player
from game.items.staticItems.Boundarie import Boundarie
from game.items.staticItems.Grab import Grab
from game.items.staticItems.Spike import Spike
from game.items.staticItems.Goal import Goal

from utils.utils import get_font, get_assets_path


from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, DT, LOSE_EVENT, WIN_EVENT


'''
Level 1
-2 = Goal
-1 = Player
0 = Nothing
1 = Boundarie
2 = Grass Boundarie
3 = Grab
4 = Spike
'''

P = -1

TILES_MAP = [
    [1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 1],
    [1, -2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 1],
    [1, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3,
        3, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2,
        2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
        1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1, 1,
        1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 1, 1,
        1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1],
    [1, 0, P, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 1, 1,
        1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

NRO_TILES_X = len(TILES_MAP[0])
NRO_TILES_Y = len(TILES_MAP)

TILE_HEIGHT = SCREEN_HEIGHT / NRO_TILES_Y
TILE_WIDTH = SCREEN_WIDTH / NRO_TILES_X

MIN_TILE_SIZE = min(TILE_HEIGHT, TILE_WIDTH)

PLAYER_SIZE = min(TILE_HEIGHT, TILE_WIDTH) * 0.9

floor = pygame.image.load(get_assets_path('assets/sprites/floor.png'))
floor_grass = pygame.image.load(
    get_assets_path('assets/sprites/floor_grass.png'))
grap_brick = pygame.image.load(get_assets_path('assets/sprites/grap.png'))
spikes = pygame.image.load(get_assets_path('assets/sprites/spikes.png'))
goal = pygame.image.load(get_assets_path('assets/sprites/portal_yellow.png'))
player_sprite = pygame.image.load(get_assets_path('assets/sprites/player.gif'))

# background = pygame.image.load(get_assets_path('assets/level1_back.png'))


class Level1(Scene):
    def __init__(self, app, lose_scene: Scene = None, win_scene: Scene = None, menu_scene: Scene = None):
        super().__init__(bg_color=(0, 0, 0))
        self.app = app
        self.lose_scene = lose_scene
        self.win_scene = win_scene
        self.menu_scene = menu_scene

    def pre_loads(self) -> None:
        pygame.mixer.music.stop()
        self.grabbable_items = pygame.sprite.Group()
        self.dangerous_items = pygame.sprite.Group()
        self.static_items = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.item_list = []
        self.goal = None
        for i in range(NRO_TILES_Y):
            for j in range(NRO_TILES_X):
                if TILES_MAP[i][j] == -1:
                    player = Player(j * TILE_WIDTH + TILE_WIDTH / 2, i * TILE_HEIGHT +
                                    TILE_HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE, img=player_sprite)
                    self.add_player(player)
                elif TILES_MAP[i][j] == -2:
                    self.set_goal(Goal(j * TILE_WIDTH + TILE_WIDTH / 2, i * TILE_HEIGHT +
                                  TILE_HEIGHT // 2, TILE_WIDTH, TILE_HEIGHT, img=goal))
                elif TILES_MAP[i][j] == 1:
                    self.add_static_item(Boundarie(j * TILE_WIDTH + TILE_WIDTH / 2, i *
                                         TILE_HEIGHT + TILE_HEIGHT // 2, TILE_WIDTH, TILE_HEIGHT, img=floor))
                elif TILES_MAP[i][j] == 2:
                    self.add_static_item(Boundarie(j * TILE_WIDTH + TILE_WIDTH / 2, i *
                                         TILE_HEIGHT + TILE_HEIGHT // 2, TILE_WIDTH, TILE_HEIGHT, img=floor_grass))
                elif TILES_MAP[i][j] == 3:
                    self.add_grabbable_item(Grab(j * TILE_WIDTH + TILE_WIDTH / 2, i *
                                            TILE_HEIGHT + TILE_HEIGHT // 2, TILE_WIDTH, TILE_HEIGHT, img=grap_brick))
                elif TILES_MAP[i][j] == 4:
                    self.add_dangerous_item(Spike(j * TILE_WIDTH + TILE_WIDTH / 2, i *
                                            TILE_HEIGHT + TILE_HEIGHT // 2, MIN_TILE_SIZE, MIN_TILE_SIZE, img=spikes))
        pygame.mixer.music.load(get_assets_path('assets/music/play_song.ogg'))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

    def on_event(self, event: pygame.event) -> None:
        super().on_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.app.change_scene(self.menu_scene)
        if event.type == LOSE_EVENT:
            self.app.change_scene(self.lose_scene)
        if event.type == WIN_EVENT:
            self.app.change_scene(self.win_scene)

    def update(self, pressed_keys: list) -> None:
        super().update(pressed_keys)
        self.draw_lives()

    def draw_lives(self) -> None:
        screen = pygame.display.get_surface()

        text = get_font(20).render(
            f'Lives: {self.players.sprites()[0].lives}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, 30)
        screen.blit(text, text_rect)
