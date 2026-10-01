# Copyright (c) 2026 Nagi(Nagisns)
# Licensed under the MIT License.
# See the LICENSE file for details.

class ActiveGames:

    """
    Manages active games by channel ID.

    Active game information:
    ------------------------
    * channel ID
        - Used as the key for each active game.

    * game name
        - Stored as the value associated with the channel ID.

    Methods:
    --------
    * check_active
        - Check whether a game is active in a channel.

    * check_info
        - Get information about an active game.

    * add_channel
        - Add a game to the active game list.

    * remove_channel
        - Remove a game from the active game list.
    """

    def __init__(self) -> None:
        self.active_channel: dict[int, str] = {}

    def check_active(self, check_id: int) -> bool:
        if check_id in self.active_channel:
            return True
        else:
            return False
        
    def check_info(self, channel_id: int) -> tuple[int, str] | None:
        if self.check_active(channel_id):
            game_name = self.active_channel[channel_id]
            return channel_id, game_name

    def add_channel(self, channel_id: int, game_name: str) -> None:
        if self.check_active(channel_id) is False:
            self.active_channel[channel_id] = game_name

    def remove_channel(self, channel_id: int) -> None:
        if self.check_active(channel_id):
            self.active_channel.pop(channel_id)      
   