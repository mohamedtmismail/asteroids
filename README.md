# Asteroids
A simple remake of the classic arcade game written with [Pygame](https://www.pygame.org/). The codebase contains lightweight modules for the player ship, asteroids and projectiles. The main game loop lives in `main.py` which sets up sprite groups and handles updates and drawing each frame.

<img width="1392" alt="Asteroids_Screenshot" src="https://github.com/user-attachments/assets/fa7c0402-d72a-452b-b255-17b8e7fb5d49" />


## Project Structure

- `constants.py` – game tuning values such as screen size and speeds
- `circleshape.py` – base sprite used by the player, asteroids and shots
- `player.py` – logic for controlling the ship and firing
- `asteroid.py` – behaviour for individual asteroids
- `asteroidfield.py` – spawns new asteroids over time
- `shot.py` – projectile behaviour
- `main.py` – entry point that runs the game loop

## How to Run

### UV
1. Install [UV](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)
2. Run this command in the root of the directory:
   ```bash
   uv run main.py
   ```

### manually
1. Install Python 3.13 or newer.
2. Install dependencies (only Pygame is required):
   ```bash
   pip install pygame==2.6.1
   ```
3. Launch the game from the repository root:
   ```bash
   python main.py
   ```

Use **W/A/S/D** to thrust and rotate the ship and **SPACE** to fire. When your ship collides with an asteroid the program exits with "Game over!" in the console.
