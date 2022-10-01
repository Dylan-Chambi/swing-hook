import pygame

class App:
    def __init__(self, screen_width, screen_height, max_fps = 60, bg_color=(39, 185, 245, 0.8)):
        self.width = screen_width
        self.height = screen_height
        self.max_fps = max_fps
        self.bg_color = bg_color
        pygame.init()
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.is_running = False
        self.clock = pygame.time.Clock()


    def update(self, keys):
        self.screen.fill(self.bg_color)
        pygame.display.flip()

        self.clock.tick(self.max_fps)
        pygame.display.set_caption(f"FPS: {self.clock.get_fps():.2f}")

    def run(self):
        self.is_running = True
        
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
            
            keys = pygame.key.get_pressed()
            self.update(keys)
        pygame.quit()