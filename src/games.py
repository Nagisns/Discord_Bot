# Copyright (c) 2026 Nagi(Nagisns)
# Licensed under the MIT License.
# See the LICENSE file for details.

import random
from typing import Literal

class GuessGame:

    """
    Manages the state and logic of a number guessing game.

    Game information:
    -----------------
    * channel ID
        - The ID of the channel where the game is running.

    * user ID
        - The ID of the user playing the game.

    * try counter
        - Stores the number of valid guesses made by the player.

    * secret number
        - A randomly generated integer between 1 and 100.

    Methods:
    --------
    * increment_counter
        - Increase the try counter by one.

    * check_guess
        - Compare the player's guess with the secret number.
        - Return "low", "correct", or "high".
    """

    def __init__(self, channel_id: int, user_id: int) -> None:
        self.max_value: int = 100
        self.min_value: int = 1
        self.channel_id: int = channel_id
        self.user_id: int = user_id
        self.try_counter: int = 0
        self.secret_number: int = random.randint(self.min_value, self.max_value)

    def increment_counter(self) -> None:
        self.try_counter += 1

    def check_guess(self, guess_number: int) -> Literal["low", "correct", "high"]:
        self.increment_counter()

        if guess_number < self.secret_number:
            return "low"
        elif guess_number == self.secret_number:
            return "correct"
        elif guess_number > self.secret_number:
            return "high"
        