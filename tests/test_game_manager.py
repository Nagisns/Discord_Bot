# Copyright (c) 2026 Nagi(Nagisns)
# Licensed under the MIT License.
# See the LICENSE file for details.

from src.game_manager import ActiveGames

def test_check_active() -> None:
    active_game: ActiveGames = ActiveGames()

    active_game.add_channel(channel_id=987654321, game_name="test")

    assert active_game.check_active(987654321) is True

def test_check_info() -> None:
    active_game: ActiveGames = ActiveGames()

    channel_id: int = 987654321

    active_game.add_channel(channel_id=channel_id, game_name="test")

    assert active_game.check_info(channel_id=channel_id) == (987654321, "test")

def test_add_channel() -> None:
    active_game: ActiveGames = ActiveGames()

    channel_id: int = 987654321

    active_game.add_channel(channel_id=channel_id, game_name="test")

    assert active_game.active_channel == {987654321: "test"}

def test_remove_channel() -> None:
    active_game: ActiveGames = ActiveGames()

    channel_id: int = 987654321

    active_game.add_channel(channel_id=channel_id, game_name="test")
    active_game.remove_channel(channel_id)

    assert active_game.check_info(channel_id=channel_id) == None
