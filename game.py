import gamebox
import pygame
import random

camera = gamebox.Camera(800, 600)
counter = 0
asteroids = [gamebox.from_image(100, 0,
                "greyasteroid.png"), gamebox.from_image(150, 0,
                "greyasteroid.png"), gamebox.from_image(300, 0,
                "greyasteroid.png"), gamebox.from_image(450, 0,
                "greyasteroid.png")]
health = 5
healthy = 30
time = 0
endy = 300

character = gamebox.from_image(400, 550, "player.png")
enemy = gamebox.from_image(100, 0, "ufo.png")
background = gamebox.from_image(400, 300, "background.jpg")

top_wall = gamebox.from_color(400, camera.y-300, "black", 800, 1)
bottom_wall = gamebox.from_color(400, camera.y+300, "black", 800, 1)

starting_screen_names = gamebox.from_text(400, 100, "Welcome", 40, "black")
starting_screen_instructions_1 = gamebox.from_text(400, 250, "Use the arrow keys to move.", 40, "black")
starting_screen_instructions_2 = gamebox.from_text(400, 300, "Avoid the asteroids and the enemy!", 40, "black")
starting_screen_instructions_3 = gamebox.from_text(400, 350, "You have 5 health; asteroids take away 1, ", 40, "black")
starting_screen_instructions_4 = gamebox.from_text(400, 400, "the enemy takes away 5.", 40, "black")
starting_screen_instructions_5 = gamebox.from_text(400, 450, "Press SPACE to start", 40, "black")
starting_screen_instructions_6 = gamebox.from_text(400, 500, "tip: try moving to the side of the screen!", 30, "black")

# frame = 0
# counter = 0
# number_of_frames_for_explosion = 38
# sheet = gamebox.load_sprite_sheet("explosion sprite sheet.png", 1, number_of_frames_for_explosion)

game_on = False

def tick(keys):
    global counter
    global health
    global healthy
    global score
    global endy
    global game_on
    global time
    # global frame
    # global counter

    if not game_on:
        camera.draw(gamebox.from_image(400, 300, "starting_bg.jpg"))
        camera.draw(starting_screen_names)
        camera.draw(starting_screen_instructions_1)
        camera.draw(starting_screen_instructions_2)
        camera.draw(starting_screen_instructions_3)
        camera.draw(starting_screen_instructions_4)
        camera.draw(starting_screen_instructions_5)
        camera.draw(starting_screen_instructions_6)
        if pygame.K_SPACE in keys:
            game_on = True

    if game_on:
        camera.clear("black")

        if pygame.K_RIGHT in keys:
            character.x += 10
        if pygame.K_LEFT in keys:
            character.x -= 10
        if pygame.K_UP in keys:
            character.y -= 10
        if pygame.K_DOWN in keys:
            character.y += 10

        camera.draw(background)
        camera.draw(character)
        camera.draw(enemy)

        background.y -= 3
        camera.y -= 3
        character.y -= 3
        counter += 1
        healthy -= 3
        time += 1
        endy -= 3


        if character.x >= 800:
            character.x = 0
        elif character.x <= 0:
            character.x = 800

        top_wall = gamebox.from_color(400, camera.y - 300, "black", 800, 1)
        bottom_wall = gamebox.from_color(400, camera.y + 300, "black", 800, 1)

        if character.touches(top_wall):
            character.move_to_stop_overlapping(top_wall)
        if character.touches(bottom_wall):
            character.move_to_stop_overlapping(bottom_wall)


        if counter % 20 == 0:
            new_asteroid = gamebox.from_image(random.randint(0, 600), camera.y-300,
                                          "greyasteroid.png")
            asteroids.append(new_asteroid)


        for asteroid in asteroids:
            if character.touches(asteroid):
                asteroids.remove(asteroid)
                health -= 1
            camera.draw(asteroid)

        if character.x < enemy.x:
            enemy.x -= 4
        elif character.x > enemy.x:
            enemy.x += 4
        if character.y < enemy.y:
            enemy.y -= 7
        elif character.y > enemy.y:
            enemy.y += 4

        if character.touches(enemy):
            health = 0

        score = str(int((time/ticks_per_second))).zfill(3)
        score_box = gamebox.from_text(700, healthy, "Score: "+str(score), 24, "yellow")
        camera.draw(score_box)
        ending_message = gamebox.from_text(400, endy, "GAMEOVER: Your Score is "+str(score), 50, "white")

        health_meter = gamebox.from_text(100, healthy, "Health: "+str(health), 24, "white")
        camera.draw(health_meter)

        if health <= 0:
            time -= 1
            # for frame in (1, 39):
            #     character.image = sheet[frame]
            camera.draw(gamebox.from_image(400, camera.y, "ending_background.jpg"))

            camera.draw(ending_message)

    camera.display()

ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)


# Citing:
#
# http://gushh.net/blog/wp-content/uploads/2011/06/explosion_3_40_128.png for the explosion
# https://pixabay.com/en/milky-way-starry-sky-night-sky-star-2695569/ for background
# https://pixabay.com/en/rocket-missile-space-ship-lift-off-153227/ for rocket
# https://dumielauxepices.net/wallpaper-3416929 for asteroids
# https://www.kisspng.com/png-emoji-unidentified-flying-object-flying-saucer-squ-1027796/download-png.html for enemy
# https://no.wikipedia.org/wiki/Fil:STS-125_Atlantis_Liftoff.jpg for starting background
# http://factslist.net/2013/02/coming-in-2015-asteroid-miners/ for ending background

