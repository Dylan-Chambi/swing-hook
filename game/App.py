import pygame
# import pymunk.pygame_util
# import pymunk

from game.scenes.Scene import Scene

class App:
    def __init__(self, screen_width: int, screen_height: int, max_fps: int = 60, init_scene: Scene = None, bg_color: tuple = (39, 185, 245, 0.8)) -> None:
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode([screen_width, screen_height])
        self.width: int = pygame.display.get_surface().get_size()[0]
        self.height: int = pygame.display.get_surface().get_size()[1]
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.is_running: bool = False
        self.scene = init_scene
        if self.scene is not None:
            self.scene.pre_loads()
        self.max_fps: int = max_fps
        self.bg_color: tuple = bg_color
        # self.draw_options: pymunk.pygame_util.DrawOptions = pymunk.pygame_util.DrawOptions(self.screen)


    def update(self, keys: list) -> None:
        if self.scene is not None:
            self.screen.fill(self.scene.bg_color)
            self.scene.update(keys)
            # self.scene.space.step(1/self.max_fps)

        self.clock.tick(self.max_fps)
        pygame.display.set_caption(f"FPS: {self.clock.get_fps():.2f}")
        pygame.display.flip()

    def change_scene(self, scene: Scene) -> None:
        self.scene = scene
        if self.scene is not None:
            self.scene.pre_loads()

    def run(self):
        self.is_running = True
        
        while self.is_running:
            for event in pygame.event.get():
                self.scene.on_event(event)
            keys = pygame.key.get_pressed()
            self.update(keys)
        pygame.quit()
