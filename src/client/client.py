import pygame
import client.src.entity.player as player
import client.src.entity.entity as entity


class Client:
    fps = 60
    dim = (400, 450)

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode(self.dim)
        self.set_name("StickMario: Remastered")
        self.player = player.Player()

        self.otherPlayers = entity.Entities()
        self.enemies = entity.Entities()

    def set_name(self, name: str = "Game"):
        pygame.display.set_caption(name)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.display.fill((0, 0, 0))

            for entity in [*self.otherPlayers, *self.enemies]:
                # more to think on here
                entity.render(self.display)

            pygame.display.update()
            self.clock.tick(self.fps)
        pygame.quit()
