import pygame
def draw_grid(screen):
    for row in range(10):
        for col in range(10):
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(col * 50, row * 50, 50, 50), 1)


def draw_wall(screen,x,y,dir):
    if dir==1:
        pygame.draw.line(screen, (0, 0, 0), (y * 50, x * 50), ((y+1) * 50, x * 50), 7)
    elif dir==2:
        pygame.draw.line(screen, (0, 0, 0), ((y+1) * 50, x * 50), ((y+1) * 50, (x+1) * 50), 7)
    elif dir==3:
        pygame.draw.line(screen, (0, 0, 0), (y * 50, (x+1) * 50), ((y+1) * 50, (x+1) * 50), 7)
    elif dir==4:
        pygame.draw.line(screen, (0, 0, 0), ((y) * 50, x * 50), ((y) * 50, (x+1) * 50), 7)
    



def draw(screen, position, vaccum,dirt):
    if vaccum == True:
        char='o>'
        angle=90
        color = (255, 0, 0)
    if dirt == True:
        char='X'
        angle=0
        color = (0, 0, 0)

    rect = pygame.Rect(position[1] * 50,  position[0] * 50, 50, 50)
    font = pygame.font.Font(None, 36) 
    text = font.render(char, True, color)
    text = pygame.transform.rotate(text, angle)
    text_rect = text.get_rect(center=(rect.centerx, rect.centery)) 
    screen.blit(text, text_rect) 

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        #Create Initial Playground
        screen.fill((255, 255, 255))
        draw_grid(screen)
        draw_wall(screen,4,0,3)
        draw_wall(screen,4,1,3)
        draw_wall(screen,4,2,3)
        draw_wall(screen,4,3,3)
        draw_wall(screen,4,4,3)
        draw_wall(screen,4,5,3)
        draw_wall(screen,1,6,2)
        draw_wall(screen,2,6,2)
        draw_wall(screen,3,6,2)
        draw_wall(screen,4,6,2)
        draw_wall(screen,6,6,2)
        draw_wall(screen,7,6,2)



        p_vaccum=(9,0)
        draw(screen, p_vaccum , True,False)
        pygame.display.flip()
