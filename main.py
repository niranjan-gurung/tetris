import pygame

# setup
pygame.init()
window = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(
  window.get_width() / 2, 
  window.get_height() / 2
)

if __name__ == "__main__":
  print("hello from local machine!")

  # main loop:
  while running:
    
    # process events:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    
    # clear screen from last frame: 
    window.fill("purple")

    # game render goes here..
    pygame.draw.circle(window, "white", player_pos, 5)

    # process key inputs:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # double buffering:
    pygame.display.flip()

    # limit to 60fps
    # delta time used for framerate independant physics:
    dt = clock.tick(60) / 1000
  
  pygame.quit()