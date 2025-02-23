import time
import curses
import random

from typing import List, Tuple

from src.gameoflife.cell import Cell
from src.gameoflife.error import TerminalSizeError
from src.gameoflife.constants import *

class Game:
    def __init__(self, screen):
        """
        Constructor method of the Game class.

        Args:
            screen: Curses screen object

        Raises:
            TerminalSizeError: If the terminal size is not suitable
        """
        self.screen = screen
        self.setup_game_area()
        self.initialize_grid()

    def check_terminal_size(self) -> Tuple[int, int]:
        """
        It checks the terminal size and throws an error if it is not suitable.

        Returns:
            Tuple[int, int]: Terminal height and width

        Raises:
            TerminalSizeError: If the terminal size does not meet the minimum requirements
        """
        height, width = self.screen.getmaxyx()
        current_size = (height, width)
        min_size = (MIN_HEIGHT, MIN_WIDTH)

        if height < MIN_HEIGHT or width < MIN_WIDTH:
            raise TerminalSizeError(current_size, min_size)
        
        return height, width
    
    def setup_game_area(self):
        """
        Controls terminal dimensions and adjusts the playing field.

        Raises:
            TerminalSizeError: If the terminal size is not suitable
        """
        terminal_height, terminal_width = self.check_terminal_size()

        # Limit terminal sizes
        self.height = min(terminal_height - 1, MAX_HEIGHT)
        self.width = min((terminal_width - 1) // 2, MAX_WIDTH // 2)

    def add_pattern(self, pattern: List[Tuple[int, int]], center_y: int, center_x: int):
        """Inserts a given pattern at the specified centre point."""
        for y_offset, x_offset in pattern:
            y = (center_y + y_offset) % self.height
            x = (center_x + x_offset) % self.width
            self.grid[y][x].alive = True

    def initialize_grid(self):
        """Returns the playing field to the starting position."""
        self.grid = [[Cell(x, y) for x in range(self.width)]
                     for y in range(self.height)]
        
        # Different start patterns
        glider = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        blinker = [(0, 0), (0, 1), (0, 2)]
        block = [(0, 0), (0, 1), (1, 0), (1, 1)]
        beehive = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 1), (2, 2)]

        # Place patterns in different positions
        self.add_pattern(glider, self.height // 4, self.width // 4)
        self.add_pattern(blinker, self.height // 2, self.width // 2)
        self.add_pattern(block, 3 * self.height // 4, self.width // 3)
        self.add_pattern(beehive, self.height // 3, 2 * self.width // 3)

        # Randomly add live cells
        num_random = (self.height * self.width) // 10

        for _ in range(num_random):
            y = random.randint(0, self.height - 1)
            x = random.randint(0, self.width - 1)
            self.grid[y][x].alive = True

    def count_live_neighbors(self, y: int, x: int) -> int:
        """
        Calculates the number of live neighbors at a given location.
        
        Args:
            y (int): Y coordinate
            x (int): X coordinate

        Returns:
            int: Number of alive neighbors
        """
        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue

                ny = (y + dy) % self.height
                nx = (x + dx) % self.width

                if self.grid[ny][nx].alive:
                    count += 1


        return count
    
    def update_cell_states(self):
        """Calculates the state of all cells in the next generation."""

        # Create a temporary grid
        new_grid =[[Cell(x, y) for x in range(self.width)]
                   for y in range(self.height)]
        
        for y in range(self.height):
            for x in range(self.width):
                live_neighbors = self.count_live_neighbors(y, x)
                current_state = self.grid[y][x].alive

                if current_state:
                    new_grid[y][x].alive = live_neighbors in [2, 3]
                else:
                    new_grid[y][x].alive = live_neighbors == 3

        # Copy new grid to current grid
        self.grid = new_grid

    def draw(self):
        """Draws the area on the screen."""
        self.screen.clear()

        try:
            for y in range(self.height):
                for x in range(self.width):
                    cell = self.grid[y][x]
                    char = "██" if cell.alive else "▒▒"
                    color = curses.color_pair(1) if cell.alive else curses.color_pair(2)
                    
                    if cell.alive:
                        self.screen.addstr(y, x * 2, char, curses.A_BOLD | color)
                    else:
                        self.screen.addstr(y, x * 2, char, color)
        except curses.error:
            pass

        self.screen.refresh()

    def run(self):
        """
        Starts the game loop.

        Returns:
            str: Message about how the game ended
        """
        try:
            curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)

            generation = 0
            time.sleep(1)

            while True:
                self.draw()
                self.update_cell_states()
                generation += 1

                if generation % 100 == 0:
                    alive_cells = sum(cell.alive for row in self.grid for cell in row)
                    self.screen.addstr(
                        0, 0, f"Nesil: {generation} | Canlı: {alive_cells}", 
                        curses.A_BOLD | curses.color_pair(1)
                    )

                time.sleep(0.2)

                key = self.screen.getch()
                if key == ord('q'):
                    return "Game terminated by user."
                
        except KeyboardInterrupt:
            return "The game is ended with Ctrl+C."
        except curses.error as e:
            return f"Error: {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"