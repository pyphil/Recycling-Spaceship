import pygame
from random import randint

try:
    with open('score'):
        pass
except FileNotFoundError:
    with open('score', 'a') as f:
        f.write('-- - ---\n')
        f.write('-- - ---\n')
        f.write('-- - ---\n')
        f.write('-- - ---\n')

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# set up font
font = pygame.font.Font(None, 30)
title_font = pygame.font.Font(None, 50)


def get_random_velocity(points=None):
    if points:
        vel = randint(2, 5) + points/5
    else:
        vel = randint(2, 5)
    print(vel)
    return vel


def startscreen(result=None):
    navigation = "keyboard"

    # text and button
    title = title_font.render("Recycling Spaceship Game", 1, "green")
    subtitle = font.render("Sammle mit deinem Raumschiff den Weltraumschrott ein. Aber Vorsicht:", 1, "white")
    subtitle_2 = font.render("Asteroiden könnten dein Raumschiff beschädigen.", 1, "white")
    name_label = font.render("NAME:", 1, "white")

    with open('score') as f:
        lines = f.readlines()
        lines.sort(reverse=True)
    highscore = font.render("HIGHSCORE", 1, "green")
    highscore_1 = font.render(f"1. {lines[0].strip()}", 1, "white")
    highscore_2 = font.render(f"2. {lines[1].strip()}", 1, "white")
    highscore_3 = font.render(f"3. {lines[2].strip()}", 1, "white")
    highscore_4 = font.render(f"4. {lines[3].strip()}", 1, "white")

    button = pygame.Rect(screen.get_width()/2 - 50, 400, 100, 50)
    buttontext = font.render("START", 1, "white")
    input = pygame.Rect(screen.get_width()/2 - 100, 300, 200, 50)
    user_text = ""

    keyboard_nav = pygame.Rect(screen.get_width()/2 - 200, 500, 130, 50)
    keyboard_nav_text = font.render("KEYBOARD", 1, "white")
    mouse_nav = pygame.Rect(screen.get_width()/2 + 70, 500, 130, 50)
    mouse_nav_text = font.render("MOUSE", 1, "white")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # check button press
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    if user_text != "":
                        play(user_text, navigation)
                        break
                if keyboard_nav.collidepoint(event.pos):
                    if navigation == "mouse":
                        navigation = "keyboard"
                if mouse_nav.collidepoint(event.pos):
                    if navigation == "keyboard":
                        navigation = "mouse"


            # input
            if event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                # remove Enter/Return-Key char
                elif event.key == pygame.K_RETURN:
                    if user_text != "":
                        play(user_text, navigation)
                        break
                # Unicode standard is used for string formation
                else:
                    user_text += event.unicode
        screen.fill('purple')
        # draw title, subtitle, input box and button
        screen.blit(title, (screen.get_width()/2 - title.get_width()/2, 100))
        screen.blit(subtitle, (screen.get_width()/2 - subtitle.get_width()/2, 150))
        screen.blit(subtitle_2, (screen.get_width()/2 - subtitle.get_width()/2, 180))
        screen.blit(name_label, (input.x, input.y - 30))
        pygame.draw.rect(screen, "blue", button)
        screen.blit(buttontext, (button.x + 18, button.y + 17))
        pygame.draw.rect(screen, "blue", input)
        inputtext = font.render(user_text, True, (255, 255, 255))
        screen.blit(inputtext, (input.x + 5, input.y + 17))
        screen.blit(highscore, (900, 250))
        screen.blit(highscore_1, (900, 280))
        screen.blit(highscore_2, (900, 300))
        screen.blit(highscore_3, (900, 320))
        screen.blit(highscore_4, (900, 340))
        if navigation == "keyboard":
            pygame.draw.rect(screen, "green", keyboard_nav)
        else:
            pygame.draw.rect(screen, "black", keyboard_nav)
        screen.blit(keyboard_nav_text, (keyboard_nav.x + 7, keyboard_nav.y + 17))
        if navigation == "mouse":
            pygame.draw.rect(screen, "green", mouse_nav)
        else:
            pygame.draw.rect(screen, "black", mouse_nav)
        screen.blit(mouse_nav_text, (mouse_nav.x + 27, mouse_nav.y + 17))

        if result:
            feedback = font.render(f"Game over! You collected {result} points.", 1, "white")
            screen.blit(feedback, (screen.get_width()/2 - feedback.get_width()/2, 650))

        pygame.display.update()

        clock.tick(60)


def play(user, navigation):
    # load background
    background = pygame.image.load("stars.png")
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

    # load and position spaceship and spacetrash
    asteroid = pygame.image.load("asteroid.png")
    asteroid_1_pos = asteroid.get_rect()
    asteroid_2_pos = asteroid.get_rect()
    asteroid_3_pos = asteroid.get_rect()
    spaceship = pygame.image.load("spaceship.png")
    spaceship_pos = spaceship.get_rect()
    spaceship_pos.center = screen.get_width() / 2, screen.get_height() / 2
    spacetrash = pygame.image.load("spacetrash_1.png")
    spacetrash_pos = spacetrash.get_rect()

    # set up player and object positions
    PLAYER_VELOCITY = 8
    # player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    # object_1_pos = pygame.Vector2(randint(5, 1275), 0)
    # object_2_pos = pygame.Vector2(randint(5, 1275), 0)
    # object_3_pos = pygame.Vector2(randint(5, 1275), 0)
    # object_4_pos = pygame.Vector2(randint(5, 1275), 0)
    asteroid_1_pos.center = randint(5, 1275), 0
    asteroid_2_pos.center = randint(5, 1275), 0
    asteroid_3_pos.center = randint(5, 1275), 0

    # set velocity
    # object_1_vel = get_random_velocity()
    # object_2_vel = get_random_velocity()
    # object_3_vel = get_random_velocity()
    # object_4_vel = get_random_velocity()
    asteroid_1_vel = get_random_velocity()
    asteroid_2_vel = get_random_velocity()
    asteroid_3_vel = get_random_velocity()
    spacetrash_vel = get_random_velocity()

    points = 0
    while True:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # fill the screen with a color to wipe away anything from last frame
        # screen.fill("purple")
        screen.blit(background, (0, 0))
        caption = font.render(f"USER: {user} / POINTS: {points}", 1, "white")
        screen.blit(caption, (10, 10))

        # create players and objects
        screen.blit(spaceship, spaceship_pos)
        # player = pygame.draw.circle(screen, "red", player_pos, 40)
        # object_1 = pygame.draw.circle(screen, "green", object_1_pos, 10)
        # object_2 = pygame.draw.circle(screen, "red", object_2_pos, 10)
        # object_3 = pygame.draw.circle(screen, "red", object_3_pos, 10)
        # object_4 = pygame.draw.circle(screen, "red", object_4_pos, 10)
        asteroid_obj_1 = screen.blit(asteroid, asteroid_1_pos)
        asteroid_obj_2 = screen.blit(asteroid, asteroid_2_pos)
        asteroid_obj_3 = screen.blit(asteroid, asteroid_3_pos)
        spacetrash_obj = screen.blit(spacetrash, spacetrash_pos)

        # let objects come down and set new position and velocity when they
        # reach the bottom
        # object_1_pos.y += object_1_vel
        # if object_1_pos.y > 720:
        #     object_1_pos = pygame.Vector2(randint(5, 1275), 0)
        #     object_1_vel = get_random_velocity(points)
        # object_2_pos.y += object_2_vel
        # if object_2_pos.y > 720:
        #     object_2_pos = pygame.Vector2(randint(5, 1275), 0)
        #     object_2_vel = get_random_velocity(points)
        # object_3_pos.y += object_3_vel
        # if object_3_pos.y > 720:
        #     object_3_pos = pygame.Vector2(randint(5, 1275), 0)
        #     object_3_vel = get_random_velocity(points)
        # object_4_pos.y += object_4_vel
        # if object_4_pos.y > 720:
        #     object_4_pos = pygame.Vector2(randint(5, 1275), 0)
        #     object_4_vel = get_random_velocity(points)

        asteroid_1_pos.y += asteroid_1_vel
        if asteroid_1_pos.y > 720:
            asteroid_1_pos.center = randint(5, 1275), 0
            asteroid_1_vel = get_random_velocity(points)

        asteroid_2_pos.y += asteroid_2_vel
        if asteroid_2_pos.y > 720:
            asteroid_2_pos.center = randint(5, 1275), 0
            asteroid_2_vel = get_random_velocity(points)

        asteroid_3_pos.y += asteroid_3_vel
        if asteroid_3_pos.y > 720:
            asteroid_3_pos.center = randint(5, 1275), 0
            asteroid_3_vel = get_random_velocity(points)

        spacetrash_pos.y += spacetrash_vel
        if spacetrash_pos.y > 720:
            spacetrash = pygame.image.load(f'spacetrash_{ randint(1,4) }.png')
            spacetrash_pos.center = randint(5, 1275), 0
            spacetrash_vel = get_random_velocity(points)

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP]:
        #     player_pos.y -= PLAYER_VELOCITY
        # if keys[pygame.K_DOWN]:
        #     player_pos.y += PLAYER_VELOCITY
        # if keys[pygame.K_LEFT]:
        #     player_pos.x -= PLAYER_VELOCITY
        # if keys[pygame.K_RIGHT] and player_pos.x <= screen.get_width() - player.width:
        #     player_pos.x += PLAYER_VELOCITY

        # Follow Mouse
        if navigation == "mouse":
            spaceship_pos.x = pygame.mouse.get_pos()[0]
            spaceship_pos.y = pygame.mouse.get_pos()[1]

        # Use Arrow-Keys
        if navigation == "keyboard":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and spaceship_pos.y >= 0:
                spaceship_pos.y -= PLAYER_VELOCITY
            if keys[pygame.K_DOWN] and spaceship_pos.y <= screen.get_height() - spaceship.get_rect().height:
                spaceship_pos.y += PLAYER_VELOCITY
            if keys[pygame.K_LEFT] and spaceship_pos.x >= 0:
                spaceship_pos.x -= PLAYER_VELOCITY
            if keys[pygame.K_RIGHT] and spaceship_pos.x <= screen.get_width() - spaceship.get_rect().width:
                spaceship_pos.x += PLAYER_VELOCITY

        # let spaceship come in on the other side of the screen (also remove 'and' operator in sequence above)
        # if spaceship_pos.x >= screen.get_width() - spaceship.get_rect().width:
        #     spaceship_pos.x = 0
        # if spaceship_pos.x < 0:
        #     spaceship_pos.x = screen.get_width() - spaceship.get_rect().width
        # if spaceship_pos.y >= screen.get_height() - spaceship.get_rect().height:
        #     spaceship_pos.y = 0
        # if spaceship_pos.y < 0:
        #     spaceship_pos.y = screen.get_height() - spaceship.get_rect().height

        # if object_1.colliderect(player):
        #     points += 1
        #     object_1_pos.y = 721

        # if object_1.colliderect(spaceship_pos):
        #     points += 1
        #     object_1_pos.y = 721

        if spacetrash_obj.colliderect(spaceship_pos):
            points += 1
            spacetrash_pos.y = 721

        # if object_2.colliderect(player) or object_3.colliderect(player) or object_4.colliderect(player):
        #     feedback = font.render(f"Game over! You collected {points} points.", 1, "white")
        #     screen.blit(feedback, (screen.get_width()/2, screen.get_height()/2))

        if (asteroid_obj_1.colliderect(spaceship_pos)
                or asteroid_obj_2.colliderect(spaceship_pos)
                or asteroid_obj_3.colliderect(spaceship_pos)):
            with open('score', 'a') as f:
                if points < 10:
                    f.write(f'0{points} - {user}\n')
                else:
                    f.write(f'{points} - {user}\n')
            startscreen(result=points)
            break

        # update display
        pygame.display.update()

        # limits FPS to 60
        clock.tick(60)


startscreen()

pygame.quit()
