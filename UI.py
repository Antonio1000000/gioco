import pygame

class UI:
    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    padding = 20

    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.start = False
        self.quit = False

        self.font = pygame.font.SysFont("Arial", 40)

        self.start_menu_title = self.font.render("Gioco", True, self.color)
        self.start_button_text = self.font.render("Inizia", True, self.color)
        self.quit_button_text = self.font.render("Esci", True, self.color)

        self.game_over_title = self.font.render('Game Over', True, self.color)

    def draw_start_menu(self):
        self.screen.fill((0, 0, 0))

        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        self.screen.blit(self.start_menu_title, (screen_width / 2 - self.start_menu_title.get_width() / 2, screen_height / 2 - self.start_menu_title.get_height() / 2 - 100))

        mouse = pygame.mouse.get_pos()

        start_button_width = screen_width / 2 - self.start_button_text.get_width() / 2 - self.padding / 2
        start_button_height = screen_height / 2 + self.start_button_text.get_height() / 2 - 50

        if start_button_width <= mouse[0] <= start_button_width + self.padding + self.start_button_text.get_width() and start_button_height <= mouse[1] <= start_button_height + self.padding + self.start_button_text.get_height():
            pygame.draw.rect(self.screen, self.color_light, [start_button_width, start_button_height, self.start_button_text.get_width() + self.padding, self.start_button_text.get_height() + self.padding])
            self.start = True
        else:
            pygame.draw.rect(self.screen, self.color_dark, [start_button_width, start_button_height, self.start_button_text.get_width() + self.padding, self.start_button_text.get_height() + self.padding])
            self.start = False

        self.screen.blit(self.start_button_text, (start_button_width + self.padding / 2, start_button_height + self.padding / 2))

        quit_button_width = screen_width / 2 - self.quit_button_text.get_width() / 2 - self.padding / 2
        quit_button_height = screen_height / 2 + self.quit_button_text.get_height() / 2 + 50

        if quit_button_width <= mouse[0] <= quit_button_width + self.padding + self.quit_button_text.get_width() and quit_button_height <= mouse[1] <= quit_button_height + self.padding + self.quit_button_text.get_height():
            pygame.draw.rect(self.screen, self.color_light, [quit_button_width, quit_button_height, self.quit_button_text.get_width() + self.padding, self.quit_button_text.get_height() + self.padding])
            self.quit = True
        else:
            pygame.draw.rect(self.screen, self.color_dark, [quit_button_width, quit_button_height, self.quit_button_text.get_width() + self.padding, self.quit_button_text.get_height() + self.padding])
            self.quit = False

        self.screen.blit(self.quit_button_text, (quit_button_width + self.padding / 2, quit_button_height + self.padding / 2))

        pygame.display.update()

    def draw_game_over_screen(self):
        self.screen.fill((0, 0, 0))

        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        self.screen.blit(self.game_over_title, (screen_width / 2 - self.game_over_title.get_width() / 2, screen_height / 2 - self.game_over_title.get_height() / 2 - 100))

        mouse = pygame.mouse.get_pos()

        quit_button_width = screen_width / 2 - self.quit_button_text.get_width() / 2 - self.padding / 2
        quit_button_height = screen_height / 2 + self.quit_button_text.get_height() / 2

        if quit_button_width <= mouse[0] <= quit_button_width + self.padding + self.quit_button_text.get_width() and quit_button_height <= mouse[1] <= quit_button_height + self.padding + self.quit_button_text.get_height():
            pygame.draw.rect(self.screen, self.color_light, [quit_button_width, quit_button_height, self.quit_button_text.get_width() + self.padding, self.quit_button_text.get_height() + self.padding])
            self.quit = True
        else:
            pygame.draw.rect(self.screen, self.color_dark, [quit_button_width, quit_button_height, self.quit_button_text.get_width() + self.padding, self.quit_button_text.get_height() + self.padding])
            self.quit = False

        self.screen.blit(self.quit_button_text, (quit_button_width + self.padding / 2, quit_button_height + self.padding / 2))

        pygame.display.update()
