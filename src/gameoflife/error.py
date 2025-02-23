from typing import Tuple

class TerminalSizeError(Exception):
    """
    Error class related to terminal size.

    Attributes:
        current_size (Tuple[int, int]): Current terminal size (height, width)
        min_size (Tuple[int, int]): Minimum terminal size (height, width)
        message (str): Error message
    """
    def __init__(
        self,
        current_size: Tuple[int, int],
        min_size: Tuple[int, int]
    ):
        self.current_size = current_size
        self.min_size = min_size
        self.message = self._create_error_message()
        super().__init__(self.message)

    def _create_error_message(self) -> str:
        """Creates a detailed error message."""
        messages = [
            "\nERROR: The terminal size is too small!",
            f"\nMinimum Requirements:",
            f"- Height: {self.min_size[0]} row (current: {self.current_size[0]})",
            f"- Width: {self.min_size[1]} col (current: {self.current_size[1]})",
            "\nPlease maximise your terminal window and try again."
        ]
        return "\n".join(messages)
