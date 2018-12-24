import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 125)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (350, 350)
screen = pygame.display.set_mode(size)

pos_XO = [(20,12),(145,12),(270,12),(20,137),(145,137),(270,137),(20,265),(145,265),(270,265)]
font = pygame.font.SysFont('Calibri', 100, True, False)
text1 = font.render("O", True, RED)
text2 = font.render("X", True, RED)

table =[0,0,0,0,0,0,0,0,0]
user = 1
select = 0
game_end = 0
x_c = 0
o_c = 0

pygame.display.set_caption("XO")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            select = 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                x_c = 0
                o_c = 0
                table =[0,0,0,0,0,0,0,0,0]
                select = 0
                user = 1
                game_end = 0

    # background image.
    screen.fill(WHITE)
    
    # --- score
    if game_end != 1:
        if (table[0] == table[1]) & (table[1]==table[2]):
            if table[0] == 1:
                print ("O WIN")
                game_end = 1
            elif table[0] == 2:
                print ("X WIN")
                game_end = 1
        elif (table[3]==table[4]) & (table[4]==table[5]):
            if table[3] == 1:
                print ("O WIN")
                game_end = 1
            elif table[3] == 2:
                print ("X WIN")
                game_end = 1
        elif (table[6]==table[7]) & (table[7]==table[8]):
            if table[6] == 1:
                print ("O WIN")
                game_end = 1
            elif table[6] == 2:
                print ("X WIN")
                game_end = 1
        elif (table[0]==table[3]) & (table[3]==table[6]):
            if table[0] == 1:
                print ("O WIN")
                game_end = 1
            elif table[0] == 2:
                print ("X WIN")
                game_end = 1
        elif (table[1]==table[4]) & (table[4]==table[7]):
            if table[1] == 1:
                print ("O WIN")
                game_end = 1
            elif table[1] == 2:
                print ("X WIN")
                game_end = 1
        elif (table[2]==table[5]) & (table[5]==table[8]):
            if table[2] == 1:
                print ("O WIN")
                game_end = 1
            elif table[2] == 2:
                print ("X WIN")
                game_end = 1
        elif (table[0]==table[4]) & (table[4]==table[8]):
            if table[0] == 1:
                print ("O WIN")
                game_end = 1
            elif table[0] == 2:
                print ("X WIN")
                game_end = 1
        elif (table[2]==table[4]) & (table[4]==table[6]):
            if table[2] == 1:
                print ("O WIN")
                game_end = 1
            elif table[2] == 2:
                print ("X WIN")
                game_end = 1
        # game end
        elif x_c == 4:
            if o_c == 5:
                game_end = 1
                print ("DRAW")
    
    # --- Game logic 
    while (select == 1)&(game_end != 1):
        # --- y pos
        if (pos[1]<=112):
            put = 0
        elif (pos[1]<=237):
            put = 3
        else:
            put = 6

        # --- x pos
        if (pos[0]<=112):
            put += 0
        elif (pos[0]<=237):
            put += 1
        else:
            put += 2

        # --- check empty
        if table[put] == 0:
            # --- x or o
            if user == 1:
                table[put] = user
                user = 2
                o_c = o_c + 1
                print (o_c)
            else:
                table[put] = user
                user = 1
                x_c = x_c + 1
                print (x_c)
        print(table)
        print(pos)
        select = 0
   
    
    # --- Drawing Table
    pygame.draw.line(screen, BLACK, [0,112], [350, 112], 25)
    pygame.draw.line(screen, BLACK, [0,237], [350, 237], 25)
    pygame.draw.line(screen, BLACK, [112,0], [112, 350], 25)
    pygame.draw.line(screen, BLACK, [237,0], [237, 350], 25)

    # --- Draw X
    count = 0
    for i in table:
        if i == 1:
            screen.blit(text1, pos_XO[count])
        elif i == 2:
            screen.blit(text2, pos_XO[count])
        count +=1
    

    # --- Grid table
       
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

