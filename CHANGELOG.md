# Changelog

## [1.1.0] - ####-##-##

### Added
- Introduced the `GuessGame` class to manage guessing game state.

## [1.0.3] - 2026-09-30

### Added
- Added a number range check to the guessing game. Guesses must be between 1 and 100.
- Added validation for the `TOKEN` environment variable to check whether it is set and not empty. The bot exits with an error message if the variable is missing or contains only whitespace.

### Changed
- Updated the README in English and Japanese to reflect the new input validation behavior.

## [1.0.2] - 2026-09-27

This release begins maintaining a changelog for the project.

### Added

- Added the Japanese README [`README.ja.md`](README.ja.md).
- Started the changelog in version 1.0.2; earlier release notes are included below for reference.

### Updated

- Expanded the English README with more detailed descriptions of the commands and guessing game.
- Documented the luck score result ranges, who can submit guesses, invalid input handling, the per-channel game limit, and the 20-second timeout behavior.
- Added setup guidance for the Message Content Intent and the channel permissions required by the bot.
- Fixed garbled text in the English README's luck score ranges.

### Game behavior

- The guessing game accepts guesses only from the user who started it in the same channel.
- Only one guessing game can run in a channel at a time.
- Invalid integer input does not count toward the guess total. A correct guess reports the number of valid guesses.
- The 20-second response timeout applies again after each message from the player.

## [1.0.1] - 2026-09-26

Added a 20-second time limit to the number guessing game.

- Added timeout handling using `asyncio.TimeoutError`.
- Displayed the correct number when the time runs out.
- Ended the game if the player fails to guess within 20 seconds.

### Update README.md

- Updated the Git clone instructions with the correct repository URL.
- Added instructions for navigating to the `Discord_Bot` directory.
- Documented the 20-second time limit for each guess.
- Updated the game instructions to explain that the bot reveals the correct number when time runs out.
