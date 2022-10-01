import pygame

class App:
    def __init__(self, screen_width, screen_height, max_fps = 60, bg_color=(39, 185, 245, 0.8)):
        self.max_fps = max_fps
        self.bg_color = bg_color
        pygame.init()
        self.screen = pygame.display.set_mode([screen_width, screen_height], pygame.FULLSCREEN)
        self.width, self.height = pygame.display.get_surface().get_size()
        self.is_running = False
        self.clock = pygame.time.Clock()


    def update(self, keys):
        self.screen.fill(self.bg_color)

        poly = pygame.draw.rect(self.screen, (255, 0, 0), (0, 0, 100, 100))
        poly.center = (self.width/2, self.height/2)

        x, y = pygame.mouse.get_pos()
        pygame.draw.circle(self.screen, (255, 0, 0), (x, y), 10)
        pygame.mouse.set_visible(False)

        self.clock.tick(self.max_fps)
        pygame.display.set_caption(f"FPS: {self.clock.get_fps():.2f}")

        pygame.display.flip()

    def run(self):
        self.is_running = True
        
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.is_running = False
            keys = pygame.key.get_pressed()
            self.update(keys)
        pygame.quit()


    def hiddeMouse(self):
        pygame.mouse.set_visible(False)