import pygame
import random

def display_mole(screen, mole_image, x, y):
    screen.blit(mole_image, mole_image.get_rect(topleft=(x*32, y*32)))

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))

        mole_x, mole_y = 0, 0
        clock = pygame.time.Clock()
        running = True
        while running:
            screen.fill("light green")
            display_mole(screen, mole_image, mole_x, mole_y)
            for i in range(0, 640, 32):
                # Horizontal lines
                pygame.draw.line(screen, 'black', (i,0), (i, 512))
            for i in range(0, 512, 32):
                # Vertical lines
                pygame.draw.line(screen, 'black', (0, i), (640, i))
            pygame.display.flip()
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if mole_x*32 < mouse_x < mole_x*32+32 and mole_y*32 < mouse_y < mole_y*32+32:
                        mole_x = random.randrange(0, 20)
                        mole_y = random.randrange(0, 16)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
