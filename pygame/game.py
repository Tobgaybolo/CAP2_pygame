import pygame
import os
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display dimensions
WIDTH, HEIGHT = 900, 780
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Egg")
# Get the absolute path to the image file
current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, "farm-background-with-barn-and-windmill-free-vector.jpg")

# Load the background image
background = pygame.image.load(image_path)

# Get the absolute path to the image file
current_directory = os.path.dirname(os.path.abspath(__file__))
basket_path = os.path.join(current_directory, "wicker-basket.png")

# Load the basket image
basket_image = pygame.image.load(basket_path)

# Get the absolute path to the image file
current_directory = os.path.dirname(os.path.abspath(__file__))
chicken_path = os.path.join(current_directory, "back-camera.png")

# Load the chicken image
chicken_image = pygame.image.load(chicken_path)

# Get the absolute path to the image file
current_directory = os.path.dirname(os.path.abspath(__file__))
chicken2_path = os.path.join(current_directory, "back-camera.png")

# Load the chicken2 image
chicken2_image = pygame.image.load(chicken2_path)

# Get the absolute path to the image file
current_directory = os.path.dirname(os.path.abspath(__file__))
chicken3_path = os.path.join(current_directory, "back-camera.png")

# Load the chicken3 image
chicken3_image = pygame.image.load(chicken3_path)

# Get the absolute path to the image file
current_directory = os.path.dirname(os.path.abspath(__file__))
chicken4_path = os.path.join(current_directory, "back-camera.png")

# Load the chicken4 image
chicken4_image = pygame.image.load(chicken4_path)

# Get the absolute path to the image file
current_directory = os.path.dirname(os.path.abspath(__file__))
chicken5_path = os.path.join(current_directory, "back-camera.png")

# Load the chicken4 image
chicken5_image = pygame.image.load(chicken5_path)

# Resize the basket and chicken images to the desired dimensions
basket_image = pygame.transform.scale(basket_image, (100, 100))  # Adjust the dimensions as needed
chicken_image = pygame.transform.scale(chicken_image, (180, 180))  # Adjust the dimensions as needed
chicken2_image = pygame.transform.scale(chicken2_image, (180, 180))  # Adjust the dimensions as needed
chicken3_image = pygame.transform.scale(chicken3_image, (180, 180))  # Adjust the dimensions as needed
chicken4_image = pygame.transform.scale(chicken4_image, (180, 180))  # Adjust the dimensions as needed
chicken5_image = pygame.transform.scale(chicken5_image, (180, 180))  # Adjust the dimensions as needed

# Define the initial coordinates for the basket
basket_x = 400
basket_y = 650

# Define the initial coordinates for the chicken
chicken_x = 30
chicken_y = 10

# Define the initial coordinates for the chicken
chicken2_x = 200
chicken2_y = 10

# Define the initial coordinates for the chicken
chicken3_x = 370
chicken3_y = 10

# Define the initial coordinates for the chicken
chicken4_x = 540
chicken4_y = 10

# Define the initial coordinates for the chicken
chicken5_x = 710
chicken5_y = 10

# Define the speed of the basket movement
basket_speed = 5

# Get the absolute path to the image file for the chicken poop
current_directory = os.path.dirname(os.path.abspath(__file__))
poop_path = os.path.join(current_directory, "poop.png")

# Load the chicken poop image
poop_image = pygame.image.load(poop_path)
poop_image = pygame.transform.scale(poop_image, (30, 30))  # Adjust the dimensions as needed

# Define the list to store chicken poops
poops = []

# Define the initial number of lives
lives = 3

# Function to generate chicken poop at a random position
def poop_randomly():
    chicken_positions = [(chicken_x, chicken_y), (chicken2_x, chicken2_y), (chicken3_x, chicken3_y), (chicken4_x, chicken4_y), (chicken5_x, chicken5_y)]
    for pos in chicken_positions:
        if random.random() < 0.003:  # Adjust the probability as needed
            poops.append({'x': pos[0] + 50, 'y': pos[1] + 150, 'falling': True})

# Function to check collision between poop and basket
def check_poop_collision(poop):
    if basket_x < poop['x'] < basket_x + basket_image.get_width() and basket_y < poop['y'] < basket_y + basket_image.get_height():
        return True
    return False

# Set a clock to control the frame rate
clock = pygame.time.Clock()

# Scale the background image to fit the screen size
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Define the color for the rope
rope_color = (139, 69, 19)  # Brown color

# Define the list to store eggs
eggs = []

# Get the absolute path to the image file
current_directory = os.path.dirname(os.path.abspath(__file__))
egg_path = os.path.join(current_directory, "holidays.png")

# Load the egg image
egg_image = pygame.image.load(egg_path)
egg_image = pygame.transform.scale(egg_image, (40, 40))  # Adjust the dimensions as needed

# Get the absolute path to the image file for the second egg
current_directory = os.path.dirname(os.path.abspath(__file__))
egg2_path = os.path.join(current_directory, "holidays copy 2.png")

# Load the second egg image
egg2_image = pygame.image.load(egg2_path)
egg2_image = pygame.transform.scale(egg2_image, (40, 40))  # Adjust the dimensions as needed

# Define the list to store eggs of the second type
eggs2 = []

# Function to generate the second type of egg at a random position
def lay_second_egg_randomly():
    chicken_positions = [(chicken_x, chicken_y), (chicken2_x, chicken2_y), (chicken3_x, chicken3_y), (chicken4_x, chicken4_y), (chicken5_x, chicken5_y)]
    for pos in chicken_positions:
        if random.random() < 0.001:  # Adjust the probability as needed
            eggs2.append({'x': pos[0] + 50, 'y': pos[1] + 150, 'falling': True})

# Get the absolute path to the image file for the third egg
current_directory = os.path.dirname(os.path.abspath(__file__))
egg3_path = os.path.join(current_directory, "holidays copy 3.png")

# Load the third egg image
egg3_image = pygame.image.load(egg3_path)
egg3_image = pygame.transform.scale(egg3_image, (40, 40))  # Adjust the dimensions as needed

# Define the list to store eggs of the third type
eggs3 = []

# Function to generate the third type of egg at a random position
def lay_third_egg_randomly():
    chicken_positions = [(chicken_x, chicken_y), (chicken2_x, chicken2_y), (chicken3_x, chicken3_y), (chicken4_x, chicken4_y), (chicken5_x, chicken5_y)]
    for pos in chicken_positions:
        if random.random() < 0.001:  # Adjust the probability as needed
            eggs3.append({'x': pos[0] + 50, 'y': pos[1] + 150, 'falling': True})

# Define the score counter
score = 0

# Function to generate an egg at a random position
def lay_egg_randomly():
    chicken_positions = [(chicken_x, chicken_y), (chicken2_x, chicken2_y), (chicken3_x, chicken3_y), (chicken4_x, chicken4_y), (chicken5_x, chicken5_y)]
    for pos in chicken_positions:
        if random.random() < 0.001:  # Adjust the probability as needed
            eggs.append({'x': pos[0] + 50, 'y': pos[1] + 150, 'falling': True})

# Function to check collision between eggs and basket
def check_collision(egg):
    if basket_x < egg['x'] < basket_x + basket_image.get_width() and basket_y < egg['y'] < basket_y + basket_image.get_height():
        return True
    return False

# Function to render the score
def display_score(score_value, font, color, x, y):
    score = font.render("Score: " + str(score_value), True, color)
    screen.blit(score, (x, y))

# Define the font for the scoreboard
score_font = pygame.font.Font(None, 36)

# Function to render the score
def display_score(score_value, font, color, x, y):
    score = font.render("Score: " + str(score_value), True, color)
    screen.blit(score, (x, y))

# Define the font for the scoreboard
score_font = pygame.font.Font(None, 36)

# Load the heart image
heart_path = os.path.join(current_directory, "love-always-wins.png")
heart_image = pygame.image.load(heart_path)
heart_image = pygame.transform.scale(heart_image, (40, 40))  # Adjust the dimensions as needed

# Load the image for the homepage
# homepage_image_path = os.path.join(current_directory, "hintergrund-der-roten-scheune-mit-hand-gezeichneten-schoenen-hennen_23-2147625230.jpg")
# homepage_image = pygame.image.load(homepage_image_path)
# homepage_image = pygame.transform.scale(homepage_image, (300, 300))  # Adjust the dimensions as needed


# Function to display the home page
def display_home_page(screen, font):
    title_font = pygame.font.Font(None, 70)
    title_text = title_font.render("Chicken Egg Game", True, (255, 255, 255))
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

    start_font = pygame.font.Font(None, 36)
    start_text = start_font.render("Press any key to Start", True, (255, 255, 255))
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))

    # Blit the homepage image onto the screen
    #screen.blit(homepage_image, (WIDTH // 2 - homepage_image.get_width() // 2, HEIGHT // 2 - homepage_image.get_height() // 2))

    pygame.display.update()

    # Wait for any key press
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

# Function to display the exit page
def display_exit_page(screen, font):
    exit_font = pygame.font.Font(None, 60)
    exit_text = exit_font.render("Game Over! Press Q to quit or R to retry", True, (0, 0, 0))
    screen.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, HEIGHT // 4))
    pygame.display.update()

    # Wait for the user to choose an option
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    return

# Define the duration of the game in seconds
game_duration_seconds = 60  # Change this to the desired duration in seconds

# Define the duration of the game in seconds
game_duration_seconds = 60  # Change this to the desired duration in seconds

# Define the start time of the game
start_time = pygame.time.get_ticks()

# Main game loop
running = True
display_home_page(screen, score_font)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False

    # Start the game loop only when the home page is not being displayed
    if not running:
        break

    # Blit the background image onto the screen
    screen.blit(background, (0, 0))

    # Draw the rope
    rope_start = (0, 180)
    rope_end = (900, 180)
    pygame.draw.line(screen, rope_color, rope_start, rope_end, 5)

    # Draw the basket image at the specified position
    screen.blit(basket_image, (basket_x, basket_y))

    # Draw the chicken image at the specified position
    screen.blit(chicken_image, (chicken_x, chicken_y))

    # Draw the chicken image at the specified position
    screen.blit(chicken2_image, (chicken2_x, chicken2_y))

    # Draw the chicken image at the specified position
    screen.blit(chicken3_image, (chicken3_x, chicken3_y))

    # Draw the chicken image at the specified position
    screen.blit(chicken4_image, (chicken4_x, chicken4_y))

    # Draw the chicken image at the specified position
    screen.blit(chicken5_image, (chicken5_x, chicken5_y))

     # Display the remaining lives
    # lives_font = pygame.font.Font(None, 36)
    # lives_text = lives_font.render(f"Lives: {lives}", True, (255, 255, 255))
    # screen.blit(lives_text, (10, 60))

    # Display the hearts for lives
    heart_padding = 10
    for i in range(lives):
        screen.blit(heart_image, (heart_padding + i * (heart_image.get_width() + 5), 50))

    # Call the function to lay eggs randomly
    lay_egg_randomly()

    # Draw the eggs and handle collisions
    for egg in eggs:
        screen.blit(egg_image, (egg['x'], egg['y']))
        if egg['falling']:
            egg['y'] += 2  # Adjust the falling speed as needed
            if check_collision(egg):
                eggs.remove(egg)
                score += 5
    

    # Inside the main game loop, call the function to lay the second type of eggs randomly
    lay_second_egg_randomly()

    # Draw the second type of eggs and handle collisions
    for egg in eggs2:
        screen.blit(egg2_image, (egg['x'], egg['y']))
        if egg['falling']:
            egg['y'] += 2  # Adjust the falling speed as needed
            if check_collision(egg):
                eggs2.remove(egg)
                score += 3  # Update this with the actual score value

    # Inside the main game loop, call the function to lay the third type of eggs randomly
    lay_third_egg_randomly()

    # Draw the third type of eggs and handle collisions
    for egg in eggs3:
        screen.blit(egg3_image, (egg['x'], egg['y']))
        if egg['falling']:
            egg['y'] += 2  # Adjust the falling speed as needed
            if check_collision(egg):
                eggs3.remove(egg)
                score += 1  # Update this with the actual score value


    # Handling key presses for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_image.get_width():
        basket_x += basket_speed


    # Call the function to generate chicken poop
    poop_randomly()

    # Draw the chicken poop and handle collisions
    for poop in poops:
        screen.blit(poop_image, (poop['x'], poop['y']))
        if poop['falling']:
            poop['y'] += 5  # Adjust the falling speed as needed
            if check_poop_collision(poop):
                poops.remove(poop)
                lives -= 1

    # Display the scoreboard
    display_score(score, score_font, (255, 255, 255), 10, 10)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)  # Adjust the frame rate as needed

    # Check if lives are exhausted
    if lives <= 0:
        display_exit_page(screen, score_font)
        # Reset the game state if the user chooses to retry
        lives = 3
        score = 0
        poops.clear()
        eggs.clear()
        eggs2.clear()
        eggs3.clear()
        basket_x = 400
        basket_y = 650
        continue  # Restart the game loop


# Quit Pygame
pygame.quit()
