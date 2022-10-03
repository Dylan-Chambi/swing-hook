import pygame
import sys
from game.App import App
from game.scenes.Scene import Scene
from game.scenes.ui.Button import Button
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, FPS
from utils.utils import get_font

class MainMenu(Scene):
    def __init__(self, app: App, play_scene: Scene = None, credits_scene: Scene = None) -> None:
        super().__init__()
        self.bg_color = (39, 185, 245, 0.8)
        self.app = app
        self.play_scene = play_scene
        self.credits_scene = credits_scene
        self.menu_tittle = get_font(100).render("Swing Hook", True, "#D3D3D3")
        self.menu_rect = self.menu_tittle.get_rect(center=(SCREEN_WIDTH / 2, 130))
        self.background = pygame.transform.scale(pygame.image.load("assets/back_blue.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.play_button = Button(image=pygame.image.load("assets/play_rect.png"), pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150),
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        self.credits_button = Button(image=pygame.image.load("assets/credits_rect.png"), pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
                            text_input="CREDITS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        self.quit_button = Button(image=pygame.image.load("assets/quit_rect.png"), pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150),
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

    def play(self):
        self.app.change_scene(self.play_scene)

    def credits(self):
        self.app.change_scene(self.credits_scene)

    def pre_loads(self) -> None:
        pass

    def update(self, screen: pygame.Surface, pressed_keys: list) -> None:
        screen.blit(self.background, (0, 0))

        mouse_pos = pygame.mouse.get_pos()


        screen.blit(self.menu_tittle, self.menu_rect)

        for button in [self.play_button, self.credits_button, self.quit_button]:
            button.changeColor(mouse_pos)
            button.update(screen)
        

    def on_event(self, event: pygame.event) -> None:
        super().on_event(event)
        if event.type == pygame.QUIT:
            self.app.is_running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.app.is_running = False
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.play_button.checkForInput(mouse_pos):
                self.play()
            if self.credits_button.checkForInput(mouse_pos):
                self.credits()
            if self.quit_button.checkForInput(mouse_pos):
                self.app.is_running = False
                pygame.quit()
                sys.exit()
