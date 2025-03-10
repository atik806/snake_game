import pygame
import sys
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Load sounds
try:
    game_over_sound = pygame.mixer.Sound(r"AUDIO\1.wav")  # Game over sound
    eat_sound = pygame.mixer.Sound(r"AUDIO\2.wav")  # Eating sound
except pygame.error as e:
    print(f"Error loading sound files: {e}")

# Colors
BACKGROUND = (255, 255, 204)  # Light yellow
SNAKE_COLOR = (34, 139, 34)   # Green
APPLE_COLOR = (255, 0, 0)     # Red
BLACK = (0, 0, 0)

# Game variables
snake_pos = []
snake_direction = [10, 0]
food_pos = []
food_spawn = True
score = 0
top_score = 0
game_active = False

# Game settings
clock = pygame.time.Clock()

def draw_snake(snake_pos):
    for pos in snake_pos:
        pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], 10, 10))
    
    # Draw eye
    eye_pos = (snake_pos[0][0] + 7, snake_pos[0][1] + 3)
    pygame.draw.circle(screen, BLACK, eye_pos, 2)

def move_snake(snake_pos, snake_direction):
    new_head = [snake_pos[0][0] + snake_direction[0], snake_pos[0][1] + snake_direction[1]]
    snake_pos.insert(0, new_head)
    return snake_pos

def check_collision(snake_pos):
    if snake_pos[0][0] >= width or snake_pos[0][0] < 0 or snake_pos[0][1] >= height or snake_pos[0][1] < 0:
        return True
    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            return True
    return False

def draw_start_screen():
    screen.fill(BACKGROUND)
    font = pygame.font.SysFont('arial', 50)
    title_surface = font.render('Snake Game', True, BLACK)
    title_rect = title_surface.get_rect(center=(width / 2, height / 4))
    screen.blit(title_surface, title_rect)

    start_button = pygame.Rect(width / 2 - 100, height / 2 - 50, 200, 100)
    pygame.draw.rect(screen, BLACK, start_button)
    start_text = font.render('Start', True, BACKGROUND)
    start_text_rect = start_text.get_rect(center=start_button.center)
    screen.blit(start_text, start_text_rect)

    pygame.display.flip()

    return start_button

def draw_game_over_screen():
    screen.fill(BACKGROUND)
    font = pygame.font.SysFont('arial', 35)
    game_over_surface = font.render('Game Over', True, BLACK)
    game_over_rect = game_over_surface.get_rect(center=(width / 2, height / 4))
    screen.blit(game_over_surface, game_over_rect)

    score_surface = font.render('Your Score: ' + str(score), True, BLACK)
    score_rect = score_surface.get_rect(center=(width / 2, height / 2))
    screen.blit(score_surface, score_rect)

    restart_button = pygame.Rect(width / 2 - 100, height / 2 + 50, 200, 50)
    pygame.draw.rect(screen, BLACK, restart_button)
    restart_text = font.render('Restart', True, BACKGROUND)
    restart_text_rect = restart_text.get_rect(center=restart_button.center)
    screen.blit(restart_text, restart_text_rect)

    exit_button = pygame.Rect(width / 2 - 100, height / 2 + 120, 200, 50)
    pygame.draw.rect(screen, BLACK, exit_button)
    exit_text = font.render('Exit', True, BACKGROUND)
    exit_text_rect = exit_text.get_rect(center=exit_button.center)
    screen.blit(exit_text, exit_text_rect)

    pygame.display.flip()

    return restart_button, exit_button

def draw_scoreboard():
    font = pygame.font.SysFont('arial', 24)
    score_surface = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_surface, (10, 10))
    top_score_surface = font.render(f'Top Score: {top_score}', True, BLACK)
    screen.blit(top_score_surface, (width - 150, 10))

def reset_game():
    global snake_pos, snake_direction, food_pos, food_spawn, score, game_active
    snake_pos = [[100, 50], [90, 50], [80, 50]]
    snake_direction = [10, 0]
    food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
    food_spawn = True
    score = 0
    game_active = True

# Main game loop
while True:
    if not game_active:
        start_button = draw_start_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    reset_game()

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != [0, 10]:
                    snake_direction = [0, -10]
                if event.key == pygame.K_DOWN and snake_direction != [0, -10]:
                    snake_direction = [0, 10]
                if event.key == pygame.K_LEFT and snake_direction != [10, 0]:
                    snake_direction = [-10, 0]
                if event.key == pygame.K_RIGHT and snake_direction != [-10, 0]:
                    snake_direction = [10, 0]

        snake_pos = move_snake(snake_pos, snake_direction)

        # Snake eating food
        if snake_pos[0][0] == food_pos[0] and snake_pos[0][1] == food_pos[1]:
            score += 1
            eat_sound.play()  # Play eating sound
            food_spawn = False
            if score > top_score:
                top_score = score
        else:
            snake_pos.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
        food_spawn = True

        # Fill the screen with background color
        screen.fill(BACKGROUND)

        # Draw food
        pygame.draw.rect(screen, APPLE_COLOR, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        # Draw snake
        draw_snake(snake_pos)

        # Draw scoreboard
        draw_scoreboard()

        # Game Over conditions
        if check_collision(snake_pos):
            game_over_sound.play()  # Play the game over sound
            restart_button, exit_button = draw_game_over_screen()
            game_active = False
            while not game_active:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_button.collidepoint(event.pos):
                            reset_game()
                        if exit_button.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()

        pygame.display.flip()
        clock.tick(15)  # Controls the speed of the snake
