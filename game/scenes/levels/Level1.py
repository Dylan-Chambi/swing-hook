from game.scenes.Scene import Scene

from game.items.actors.Player import Player
from game.items.staticItems.Boundarie import Boundarie
from game.items.staticItems.Platform import Platform
from game.items.staticItems.Spike import Spike


from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, DT


'''
Level 1
-1 = Player
0 = Nothing
1 = Boundarie
2 = Platform
3 = Spikes
'''

TILES_MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
    [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
    [1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
    [1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1],
    [1, 0, -1, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

NRO_TILES_X = len(TILES_MAP[0])
NRO_TILES_Y = len(TILES_MAP)

TILE_HEIGHT = SCREEN_HEIGHT // NRO_TILES_Y
TILE_WIDTH = SCREEN_WIDTH // NRO_TILES_X

MIN_TILE_SIZE = min(TILE_HEIGHT, TILE_WIDTH)

PLAYER_SIZE = min(TILE_HEIGHT, TILE_WIDTH) * 0.9

class Level1(Scene):
    def __init__(self):
        super().__init__()
    
    def pre_loads(self) -> None:
        for i in range(NRO_TILES_Y):
            for j in range(NRO_TILES_X):
                if TILES_MAP[i][j] == -1:
                    player = Player(j * TILE_WIDTH + TILE_WIDTH // 2, i * TILE_HEIGHT + TILE_HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)
                    self.add_static_item(player)
                    self.player = player
                elif TILES_MAP[i][j] == 1:
                    self.add_static_item(Boundarie(j * TILE_WIDTH + TILE_WIDTH // 2, i * TILE_HEIGHT + TILE_HEIGHT // 2, TILE_WIDTH, TILE_HEIGHT))
                elif TILES_MAP[i][j] == 2:
                    self.add_grabbable_item(Platform(j * TILE_WIDTH + TILE_WIDTH // 2, i * TILE_HEIGHT + TILE_HEIGHT // 2, TILE_WIDTH, TILE_HEIGHT))
                elif TILES_MAP[i][j] == 3:
                    self.add_dangerous_item(Spike(j * TILE_WIDTH + TILE_WIDTH // 2, i * TILE_HEIGHT + TILE_HEIGHT // 2, MIN_TILE_SIZE, MIN_TILE_SIZE))
