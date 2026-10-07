# Copyright (c) 2026 Nagi(Nagisns)
# Licensed under the MIT License.
# See the LICENSE file for details.

from src.games import GuessGame

def test_increment_counter() -> None:
    game = GuessGame(channel_id=123456789, user_id=987654321)
    
    game.increment_counter()

    assert game.try_counter == 1

def test_check_guess() -> None:
    game = GuessGame(channel_id=123456789, user_id=987654321)

    game.secret_number = 50

    assert game.check_guess(49) == "low"
    assert game.check_guess(50) == "correct"
    assert game.check_guess(51) == "high"
    assert game.try_counter == 3
