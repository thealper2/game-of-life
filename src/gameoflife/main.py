import curses
import sys

from src.gameoflife.game import Game
from src.gameoflife.error import TerminalSizeError

def main():
    try:
        screen = curses.initscr()
        curses.start_color()
        curses.curs_set(0)
        screen.nodelay(1)
        
        game = Game(screen)
        exit_message = game.run()
        
    except TerminalSizeError as e:
        if 'screen' in locals():
            curses.endwin()
        print(e.message)
        sys.exit(1)
    except Exception as e:
        if 'screen' in locals():
            curses.endwin()
        print(f"\nError: {str(e)}")
        sys.exit(1)
    finally:
        if 'screen' in locals():
            curses.endwin()
        if 'exit_message' in locals():
            print("\n" + exit_message)
        #print("\nGame terminated.")