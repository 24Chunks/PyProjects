import pygame, sys
import utls
from pygame.locals import *
import random
import os

WIDTH, HEIGHT = 360, 240

pygame.display.set_caption("Snake by Los v3.0")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 30

GREEN = pygame.Color((0, 255, 0))
BLUE = pygame.Color(0, 0, 255)

pygame.init()
pygame.mixer.init()
fps_clock = pygame.time.Clock()

txt_box = utls.TextBoxInput(WIDTH / 2 - 75, HEIGHT / 2, 150, 50)
print(screen)

high_score = 0

eat_sound = pygame.mixer.Sound("assets/sounds/eat.mp3")
advance_level_sound = pygame.mixer.Sound("assets/sounds/advance_level_2.wav")
arcade_music = pygame.mixer.Sound("assets/sounds/arcade.mp3")
game_over_sound = pygame.mixer.Sound("assets/sounds/game_over.wav")

play_button = utls.Button("assets/play_button.png", WIDTH / 2, HEIGHT / 2 - 25, "assets/play_button_pressed.png")
quit_button = utls.Button("assets/quit_button.png", WIDTH / 2, HEIGHT / 2 + 50, "assets/quit_button_pressed.png")

player = utls.Snake(0, 20)
apple = utls.Food((random.randint(1, WIDTH / 10) * 10 - 10), (random.randint(1, HEIGHT / 10) * 10 - 10), "assets/apple.png")


def prompt():
    text = ""
    fps_count = 0
    while True:
        events = pygame.event.get()

        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == 13:
                    return txt_box.content
        screen.fill((60, 60, 60))
        screen.blit(utls.draw_text("Enter Name:", 40), (txt_box.x - 50, txt_box.y - 50))
        txt_box.render(screen, events)

        fps_clock.tick(FPS)
        pygame.display.update()
        fps_count += 1


def save(name, score):
    # THIS IS A MESS
    temp = open("temp.txt", "w")
    found = False

    with open("saves/stats.txt", "r") as f:
        data = f.readlines()
        i = 0
        while i < len(data):
            if data[i] == (name.upper() + "\n"):
                temp.write(data[i] + str(score) + "\n")
                i += 2
                found = True
            else:
                temp.write(data[i])
                i += 1

    if not found:
        temp.write(name.upper() + "\n" + str(score) + "\n")

    temp.close()

    temp = open("temp.txt", "r")
    with open("saves/stats.txt", "w") as f:
        for line in temp.readlines():
            f.write(line)
    temp.close()
    os.remove("temp.txt")


def run():
    score = 0
    fps_counter = 0
    next_level = 1
    passiveness = 4.5

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                key = pygame.key.get_pressed()
                if key[K_d] or key[K_RIGHT]:
                    player.dir_right()
                if key[K_s] or key[K_DOWN]:
                    player.dir_down()
                if key[K_w] or key[K_UP]:
                    player.dir_up()
                if key[K_a] or key[K_LEFT]:
                    player.dir_left()
                if key[K_F1]:
                    player.length += 50
                    score += 500

        screen.fill((50, 50, 50))

        fps_counter += 1
        if fps_counter >= passiveness:
            player.update()
            fps_counter = 0

        # collision handling
        if player.collides(apple.rect):
            eat_sound.play()
            apple.rect.x, apple.rect.y = (random.randint(1, WIDTH / 10) * 10 - 10), (
                    random.randint(1, HEIGHT / 10) * 10 - 10)
            player.grow()
            score += 10

        if player.pixels[-1] in player.pixels[:-1]:
            game_over_sound.play()
            if score > high_score:
                name = prompt()
                save(name, score)
                txt_box.clear()
            player.reset_stats()
            main()
        if player.x < 0 or player.x > (WIDTH - 10) or player.y < 0 or player.y > (HEIGHT - 10):
            game_over_sound.play()
            if score > high_score:
                name = prompt()
                save(name, score)
                txt_box.clear()
            player.reset_stats()
            main()
        # check score:
        if score / 100 == next_level:
            passiveness -= 0.25
            advance_level_sound.play()
            next_level += 1

        player.render(screen)
        screen.blit(apple.surface, apple.rect)
        screen.blit(utls.draw_text("Score: " + str(score), 12), [10, 10])

        pygame.display.update()
        fps_clock.tick(FPS)


def main():
    name = ""
    with open("saves/stats.txt", mode="r") as f:
        global high_score
        data = f.readlines()

        for index, line in enumerate(data):
            try:
                if int(line) >= high_score:
                    high_score = int(line)
                    name = data[index - 1][:-1]
            except ValueError:
                continue
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if play_button.rect.collidepoint(pos):
                    play_button.pressed = True
                if quit_button.rect.collidepoint(pos):
                    quit_button.pressed = True
            if event.type == MOUSEBUTTONUP:
                if play_button.pressed:
                    play_button.pressed = False
                    run()
                if quit_button.pressed:
                    quit_button.pressed = False
                    pygame.quit()
                    sys.exit()

        screen.fill((0, 0, 0))

        screen.blit(utls.draw_text(("{0}HIGH SCORE: {1}".format((name + "'s ") if name else "", high_score)), 15), [10, 10])
        screen.blit(play_button.get_surface(), play_button.rect)
        screen.blit(quit_button.get_surface(), quit_button.rect)

        pygame.display.update()
        fps_clock.tick(FPS)

arcade_music.play(999)
main()
