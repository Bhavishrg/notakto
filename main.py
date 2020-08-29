import pygame
import sys
import webbrowser
from pygame import mixer

#initialize
pygame.init()

#creating the screen
screen = pygame.display.set_mode((800,600))

#font
font = pygame.font.Font("fonts\chalk.ttf", 72)

#title,icon and background
pygame.display.set_caption('''Misere's Tic Tac Toe''')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
background_image = pygame.image.load("background.jpg").convert()
background_image = pygame.transform.scale(background_image , (800, 600))
help_image = pygame.image.load("help.jpg").convert()
help_image = pygame.transform.scale(help_image , (800, 600))
speakeron = pygame.image.load("speakeron.png")
speakeron = pygame.transform.scale(speakeron , (30, 30))
speakeroff = pygame.image.load("speakeroff.png")
speakeroff = pygame.transform.scale(speakeroff , (20, 30))
speaker = 1
mixer.music.load('chalksound.mp3')


#text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def draw_text2(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#draw a line
def draw_line_animate(surface, color, x1,y1, x2,y2, width):
    x = int(x1)
    y = int(y1)
    val = True
    while val:
        pygame.draw.line(surface, color, (int(x1),int(y1)),(x,y), int(width))
        if x != int(x2):
            x += 0.5
        if y!= int(y2):
            y += 0.5
        if x == x2 and y == y2:
            val = False
        pygame.display.update()
        pygame.time.Clock().tick(50000)




def game_initialize():
        screen.blit(background_image, (0, 0))
        draw_line_animate(screen, (255,255,255), 217,75, 217,275, 5)
        draw_line_animate(screen, (255,255,255), 284,75, 284,275, 5)
        draw_line_animate(screen, (255,255,255), 150,142, 350,142, 5)
        draw_line_animate(screen, (255,255,255), 150,209, 350,209, 5)
        draw_line_animate(screen, (255,255,255), 517,75, 517,275, 5)
        draw_line_animate(screen, (255,255,255), 584,75, 584,275, 5)
        draw_line_animate(screen, (255,255,255), 450,142, 650,142, 5)
        draw_line_animate(screen, (255,255,255), 450,209, 650,209, 5)
        draw_line_animate(screen, (255,255,255), 367,325, 367,525, 5)
        draw_line_animate(screen, (255,255,255), 434,325, 434,525, 5)
        draw_line_animate(screen, (255,255,255), 300,392, 500,392, 5)
        draw_line_animate(screen, (255,255,255), 300,459, 500,459, 5)

        game()




def strike_check(board):
    for row in board:
        for tile in row:
            if tile == 1:
                continue
            else:
                break
        else:
            return True

    for column in range(3):
        for row in board:
            if row[column] == 1:
                continue
            else:
                break
        else:
            return True

    for tile in range(3):
        if board[tile][tile] == 1:
            continue
        else:
            break
    else:
        return True

    for tile in range(3):
        if board[tile][2-tile] == 1:
            continue
        else:
            break
    else:
        return True



def game():
    global speaker
    running = True
    b1=[[0,0,0],[0,0,0],[0,0,0]]
    b2=[[0,0,0],[0,0,0],[0,0,0]]
    b3=[[0,0,0],[0,0,0],[0,0,0]]
    strike = [0, 0, 0]
    boards=[b1, b2, b3]
    screen.blit(background_image, (0, 0))

    pygame.draw.line(screen, (255,255,255), (217,75), (217,275), 5)
    pygame.draw.line(screen, (255,255,255), (284,75), (284,275), 5)
    pygame.draw.line(screen, (255,255,255), (517,75), (517,275), 5)
    pygame.draw.line(screen, (255,255,255), (584,75), (584,275), 5)
    pygame.draw.line(screen, (255,255,255), (367,325), (367,525), 5)
    pygame.draw.line(screen, (255,255,255), (434,325), (434,525), 5)
    pygame.draw.line(screen, (255,255,255), (150,142), (350,142), 5)
    pygame.draw.line(screen, (255,255,255), (150,209), (350,209), 5)
    pygame.draw.line(screen, (255,255,255), (450,142), (650,142), 5)
    pygame.draw.line(screen, (255,255,255), (450,209), (650,209), 5)
    pygame.draw.line(screen, (255,255,255), (300,392), (500,392), 5)
    pygame.draw.line(screen, (255,255,255), (300,459), (500,459), 5)




    b1b1 = pygame.Rect(170, 80, 50, 50)
    b1b2 = pygame.Rect(237, 80, 50, 50)
    b1b3 = pygame.Rect(304, 80, 50, 50)
    b1b4 = pygame.Rect(170, 147, 50, 50)
    b1b5 = pygame.Rect(237, 147, 50, 50)
    b1b6 = pygame.Rect(304, 147, 50, 50)
    b1b7 = pygame.Rect(170, 214, 50, 50)
    b1b8 = pygame.Rect(237, 214, 50, 50)
    b1b9 = pygame.Rect(304, 214, 50, 50)

    b2b1 = pygame.Rect(470, 80, 50, 50)
    b2b2 = pygame.Rect(537, 80, 50, 50)
    b2b3 = pygame.Rect(604, 80, 50, 50)
    b2b4 = pygame.Rect(470, 137, 50, 50)
    b2b5 = pygame.Rect(537, 137, 50, 50)
    b2b6 = pygame.Rect(604, 137, 50, 50)
    b2b7 = pygame.Rect(470, 214, 50, 50)
    b2b8 = pygame.Rect(537, 214, 50, 50)
    b2b9 = pygame.Rect(604, 214, 50, 50)

    b3b1 = pygame.Rect(320, 330, 50, 50)
    b3b2 = pygame.Rect(387, 330, 50, 50)
    b3b3 = pygame.Rect(454, 330, 50, 50)
    b3b4 = pygame.Rect(320, 397, 50, 50)
    b3b5 = pygame.Rect(387, 397, 50, 50)
    b3b6 = pygame.Rect(454, 397, 50, 50)
    b3b7 = pygame.Rect(320, 464, 50, 50)
    b3b8 = pygame.Rect(387, 464, 50, 50)
    b3b9 = pygame.Rect(454, 464, 50, 50)


    p = 1
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    mx, my = pygame.mouse.get_pos()
                    if b1b1.collidepoint((mx, my)) and b1[0][0] == 0 and strike[0] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 170, 80)
                        b1[0][0] = 1
                        if strike_check(b1):
                            strike[0] = 1
                            pygame.draw.line(screen, (255, 0, 0), (150,75), (350,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (150,275), (350,75), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b1b2.collidepoint((mx, my)) and b1[0][1] == 0 and strike[0] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 237, 80)
                        b1[0][1]= 1


                        if strike_check(b1):
                            strike[0] = 1
                            pygame.draw.line(screen, (255, 0, 0), (150,75), (350,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (150,275), (350,75), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b1b3.collidepoint((mx, my)) and b1[0][2] == 0 and strike[0] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 304, 80)
                        b1[0][2] = 1


                        if strike_check(b1):
                            strike[0] = 1
                            pygame.draw.line(screen, (255, 0, 0), (150,75), (350,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (150,275), (350,75), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b1b4.collidepoint((mx, my)) and b1[1][0] == 0 and strike[0] == 0:
                        if speaker == 1:mixer.music.play()


                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 170, 147)
                        b1[1][0] = 1
                        if strike_check(b1):
                            strike[0] = 1
                            pygame.draw.line(screen, (255, 0, 0), (150,75), (350,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (150,275), (350,75), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b1b5.collidepoint((mx, my)) and b1[1][1] == 0 and strike[0] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 237, 147)
                        b1[1][1] = 1


                        if strike_check(b1):
                            strike[0] = 1
                            pygame.draw.line(screen, (255, 0, 0), (150,75), (350,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (150,275), (350,75), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b1b6.collidepoint((mx, my)) and b1[1][2] == 0 and strike[0] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 304, 147)
                        b1[1][2] = 1


                        if strike_check(b1):
                            strike[0] = 1
                            pygame.draw.line(screen, (255, 0, 0), (150,75), (350,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (150,275), (350,75), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b1b7.collidepoint((mx, my)) and b1[2][0] == 0 and strike[0] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 170, 214)
                        b1[2][0] = 1


                        if strike_check(b1):
                            strike[0] = 1
                            pygame.draw.line(screen, (255, 0, 0), (150,75), (350,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (150,275), (350,75), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b1b8.collidepoint((mx, my)) and b1[2][1] == 0 and strike[0] == 0:
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 237, 214)
                        if speaker == 1:mixer.music.play()
                        b1[2][1] = 1


                        if strike_check(b1):
                            strike[0] = 1
                            pygame.draw.line(screen, (255, 0, 0), (150,75), (350,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (150,275), (350,75), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b1b9.collidepoint((mx, my)) and b1[2][2] == 0 and strike[0] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 304, 214)
                        b1[2][2] = 1


                        if strike_check(b1):
                            strike[0] = 1
                            pygame.draw.line(screen, (255, 0, 0), (150,75), (350,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (150,275), (350,75), 5)
                            pygame.display.update()
                        if strike == [1, 1, 1]:

                            game_over()

                    if b2b1.collidepoint((mx, my)) and b2[0][0] == 0 and strike[1] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 470, 80)
                        b2[0][0] = 1


                        if strike_check(b2):
                            strike[1] = 1
                            pygame.draw.line(screen, (255, 0, 0), (450,75), (650,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (650,75), (450,275), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b2b2.collidepoint((mx, my)) and b2[0][1] == 0 and strike[1] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 537, 80)
                        b2[0][1] = 1


                        if strike_check(b2):
                            strike[1] = 1
                            pygame.draw.line(screen, (255, 0, 0), (450,75), (650,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (650,75), (450,275), 5)
                        if strike == [1, 1, 1]:

                            game_over()
                    if b2b3.collidepoint((mx, my)) and b2[0][2] == 0 and strike[1] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 604, 80)
                        b2[0][2] = 1


                        if strike_check(b2):
                            strike[1] = 1
                            pygame.draw.line(screen, (255, 0, 0), (450,75), (650,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (650,75), (450,275), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b2b4.collidepoint((mx, my)) and b2[1][0] == 0 and strike[1] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 470, 147)
                        b2[1][0] = 1


                        if strike_check(b2):
                            strike[1] = 1
                            pygame.draw.line(screen, (255, 0, 0), (450,75), (650,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (650,75), (450,275), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b2b5.collidepoint((mx, my)) and b2[1][1] == 0 and strike[1] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 537, 147)
                        b2[1][1] = 1


                        if strike_check(b2):
                            strike[1] = 1
                            pygame.draw.line(screen, (255, 0, 0), (450,75), (650,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (650,75), (450,275), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b2b6.collidepoint((mx, my)) and b2[1][2] == 0 and strike[1] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 604, 147)
                        b2[1][2] = 1


                        if strike_check(b2):
                            strike[1] = 1
                            pygame.draw.line(screen, (255, 0, 0), (450,75), (650,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (650,75), (450,275), 5)
                            pygame.display.update()
                        if strike == [1, 1, 1]:

                            game_over()
                    if b2b7.collidepoint((mx, my)) and b2[2][0] == 0 and strike[1] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 470, 214)
                        b2[2][0] = 1


                        if strike_check(b2):
                            strike[1] = 1
                            pygame.draw.line(screen, (255, 0, 0), (450,75), (650,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (650,75), (450,275), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b2b8.collidepoint((mx, my)) and b2[2][1] == 0 and strike[1] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 537, 214)
                        b2[2][1] = 1


                        if strike_check(b2):
                            strike[1] = 1
                            pygame.draw.line(screen, (255, 0, 0), (450,75), (650,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (650,75), (450,275), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b2b9.collidepoint((mx, my)) and b2[2][2] == 0 and strike[1] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 604, 214)
                        b2[2][2] = 1


                        if strike_check(b2) and strike[1] == 0:
                            strike[1] = 1
                            pygame.draw.line(screen, (255, 0, 0), (450,75), (650,275), 5)
                            pygame.draw.line(screen, (255, 0, 0), (650,75), (450,275), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()


                    if b3b1.collidepoint((mx, my)) and b3[0][0] == 0 and strike[2] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 320, 330)
                        b3[0][0] = 1


                        if strike_check(b3):
                            strike[2] = 1
                            pygame.draw.line(screen, (255, 0, 0), (300,325), (500,525), 5)
                            pygame.draw.line(screen, (255, 0, 0), (300,525), (500,325), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b3b2.collidepoint((mx, my)) and b3[0][1] == 0 and strike[2] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 387, 330)
                        b3[0][1] = 1


                        if strike_check(b3):
                            strike[2] = 1
                            pygame.draw.line(screen, (255, 0, 0), (300,325), (500,525), 5)
                            pygame.draw.line(screen, (255, 0, 0), (300,525), (500,325), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b3b3.collidepoint((mx, my)) and b3[0][2] == 0 and strike[2] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 454, 330)
                        b3[0][2] = 1


                        if strike_check(b3):
                            strike[2] = 1
                            pygame.draw.line(screen, (255, 0, 0), (300,325), (500,525), 5)
                            pygame.draw.line(screen, (255, 0, 0), (300,525), (500,325), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b3b4.collidepoint((mx, my)) and b3[1][0] == 0 and strike[2] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 320, 397)
                        b3[1][0] = 1


                        if strike_check(b3):
                            strike[2] = 1
                            pygame.draw.line(screen, (255, 0, 0), (300,325), (500,525), 5)
                            pygame.draw.line(screen, (255, 0, 0), (300,525), (500,325), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b3b5.collidepoint((mx, my)) and b3[1][1] == 0 and strike[2] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 387, 397)
                        b3[1][1] = 1


                        if strike_check(b3):
                            strike[2] = 1
                            pygame.draw.line(screen, (255, 0, 0), (300,325), (500,525), 5)
                            pygame.draw.line(screen, (255, 0, 0), (300,525), (500,325), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b3b6.collidepoint((mx, my)) and b3[1][2] == 0 and strike[2] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 454, 397)
                        b3[1][2] = 1


                        if strike_check(b3):
                            strike[2] = 1
                            pygame.draw.line(screen, (255, 0, 0), (300,325), (500,525), 5)
                            pygame.draw.line(screen, (255, 0, 0), (300,525), (500,325), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b3b7.collidepoint((mx, my)) and b3[2][0] == 0 and strike[2] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 320, 464)
                        b3[2][0] = 1


                        if strike_check(b3):
                            strike[2] = 1
                            pygame.draw.line(screen, (255, 0, 0), (300,325), (500,525), 5)
                            pygame.draw.line(screen, (255, 0, 0), (300,525), (500,325), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b3b8.collidepoint((mx, my)) and b3[2][1] == 0 and strike[2] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 387, 464)
                        b3[2][1] = 1


                        if strike_check(b3):
                            strike[2] = 1
                            pygame.draw.line(screen, (255, 0, 0), (300,325), (500,525), 5)
                            pygame.draw.line(screen, (255, 0, 0), (300,525), (500,325), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()
                    if b3b9.collidepoint((mx, my)) and b3[2][2] == 0 and strike[2] == 0:
                        if speaker == 1:mixer.music.play()
                        draw_text2('x', pygame.font.Font(r'fonts\rd.ttf', 50), (255, 255, 255), screen, 454, 464)
                        b3[2][2] = 1


                        if strike_check(b3):
                            strike[2] = 1
                            pygame.draw.line(screen, (255, 0, 0), (300,325), (500,525), 5)
                            pygame.draw.line(screen, (255, 0, 0), (300,525), (500,325), 5)
                        if strike == [1, 1, 1]:

                            pygame.display.update()
                            game_over()


        pygame.display.update()


def game_over():
    pygame.time.wait(5000)
    global speaker

    running = True
    screen.blit(background_image, (0, 0))
    draw_text('Game over', pygame.font.Font(r'fonts\chalk.ttf', 70), (255, 255, 255), screen, 400, 300)
    draw_text('click to continue', pygame.font.Font('fonts\chalk.ttf', 30), (255, 255, 255), screen, 400, 350)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if speaker == 1:mixer.music.play()
                if event.button == 1:
                    main_menu()

        pygame.display.update()





def main_menu():
    global speaker
    click = False


    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(background_image, (0, 0))
        button_1 = pygame.Rect(300, 50, 200, 100)
        draw_text('Two Player', pygame.font.Font('fonts\chalk.ttf', 50), (255, 255, 255), screen, 400, 100)
        button_2 = pygame.Rect(300, 150, 200, 100)
        draw_text('Single Player', pygame.font.Font('fonts\chalk.ttf', 50), (255, 255, 255), screen, 400, 200)
        button_3 = pygame.Rect(300, 250, 200, 100)
        draw_text('Play Online', pygame.font.Font('fonts\chalk.ttf', 50), (255, 255, 255), screen, 400, 300)
        button_4 = pygame.Rect(300, 350, 200, 100)
        draw_text('Help', pygame.font.Font('fonts\chalk.ttf', 50), (255, 255, 255), screen, 400, 400)
        button_5 = pygame.Rect(300, 450, 200, 100)
        draw_text('Credits', pygame.font.Font('fonts\chalk.ttf', 50), (255, 255, 255), screen, 400, 500)
        speaker_button = pygame.Rect(730, 530, 40, 40)
        screen.blit(speakeroff, (740, 540))
        if speaker == 1:
            screen.blit(speakeron, (740, 540))

        if button_1.collidepoint((mx, my)):
            if click:
                if speaker == 1:mixer.music.play()
                game_initialize()
        if button_4.collidepoint((mx, my)):
            if click:
                if speaker == 1:mixer.music.play()
                help_text()
        if button_2.collidepoint((mx, my)):
            if click:
                if speaker == 1:mixer.music.play()
                coming_soon()
        if button_3.collidepoint((mx, my)):
            if click:
                if speaker == 1:mixer.music.play()
                coming_soon()
        if button_5.collidepoint((mx, my)):
            if click:
                if speaker == 1:mixer.music.play()
                credits()
        if speaker_button.collidepoint((mx, my)):
            if click:
                if speaker == 1:
                    speaker = 0
                    print(1)
                else:
                    mixer.music.play()
                    speaker = 1

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()



def help_text():
    global speaker
    screen.blit(help_image, (0, 0))
    while True:
        learn_more = pygame.Rect(300, 500, 200, 100)
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if learn_more.collidepoint((mx, my)):
                        webbrowser.open("https://www.youtube.com/watch?v=yk8nCzniSeQ&list=PLkgilrx-E5eJLoANuOWofc88Cv-tnehk6")


def coming_soon():
        global speaker
        screen.blit(background_image, (0, 0))
        while True:
            draw_text('coming soon', font, (255, 255, 255), screen, 400, 300)
            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main_menu()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        main_menu()


def credits():
        global speaker
        screen.blit(background_image, (0, 0))
        while True:
            draw_text('Bhavish', font, (255, 255, 255), screen, 400, 300)
            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main_menu()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        main_menu()


main_menu()
