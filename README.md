# Snake Game

A classic Snake game implemented in Python using Pygame. Control a snake as it moves around the screen, eat food to grow longer, and try to achieve the highest score without hitting the walls or yourself!

## Features

- Smooth snake movement with keyboard controls
- Score tracking with top score display
- Sound effects for eating and game over
- Clean and simple user interface
- Start screen and game over screen with restart option
- Eye detail on the snake for better visuals

## Requirements

- Python 3.x
- Pygame library

To install the required dependencies:

```bash
pip install pygame
```

## Game Controls

- **↑ (Up Arrow)**: Move snake up
- **↓ (Down Arrow)**: Move snake down
- **← (Left Arrow)**: Move snake left
- **→ (Right Arrow)**: Move snake right

## Directory Structure

```
Snake game/
│
├── snake_game.py
├── AUDIO/
│   ├── 1.wav    # Game over sound
│   └── 2.wav    # Eating sound
└── README.md
```

## How to Play

1. Run the game:
   ```bash
   python snake_game.py
   ```
2. Click the "Start" button to begin
3. Use arrow keys to control the snake
4. Eat the red food to grow and increase your score
5. Avoid hitting the walls and yourself
6. When game is over, choose to restart or exit

## Game Features

- **Score System**: Current score and top score display
- **Sound Effects**: Audio feedback for eating and game over
- **Smooth Controls**: Responsive keyboard input
- **Clean UI**: Light yellow background with clear visuals
- **Game States**: Start screen, gameplay, and game over screen

## Technical Details

- Screen Resolution: 800x600 pixels
- Snake Speed: 15 FPS
- Colors:
  - Background: Light Yellow (255, 255, 204)
  - Snake: Green (34, 139, 34)
  - Food: Red (255, 0, 0)

## License

This project is open source and available for personal and educational use.

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project. You can also open issues for bugs or feature requests.
