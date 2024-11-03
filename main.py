import pygame

# setup
pygame.init()
window = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()
running = True
dt = 0

window_width, window_height = pygame.display.get_surface().get_size()

player_size = pygame.Vector2(20, 40)
player_pos = pygame.Vector2(
  window_width / 2 - (player_size.x / 2), 10)
player = pygame.Rect(player_pos, player_size)

if __name__ == "__main__":
  # main loop:
  while running:
    
    # process events:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    
    # clear screen from last frame: 
    window.fill("purple")

    # game render goes here..
    pygame.draw.rect(
      window, 
      "white", 
      pygame.Rect(player)
    )

    player.y += 50 * dt

    if player.y >= window.get_height():
      player.y = 0

    # process key inputs:
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos.y -= 300 * dt
    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * dt
    # if keys[pygame.K_a]:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
    #     player_pos.x += 300 * dt

    # double buffering:
    pygame.display.flip()

    # limit to 60fps
    # delta time used for framerate independant physics:
    dt = clock.tick(60) / 1000
  
  pygame.quit()