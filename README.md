# Discord Bot

A simple Discord bot built with Python and `discord.py`. This project was
created as a learning project to practice Python and Discord bot development.

## Features

- **Ping:** Shows the bot's latency in milliseconds.
- **Luck:** Generates a random luck score from 1 to 100 and displays a result:
  - 70-100: `Good luck!`
  - 40-69: `Average luck.`
  - 1-39: `Bad luck...`
- **Guess the Number:** Starts a game in which the bot chooses a number from 1
  to 100. Only the user who started the game can submit guesses, and only one
  game can run in a channel at a time.

## Commands

| Command | Description |
|---|---|
| `::ping` | Displays the bot's latency in milliseconds. |
| `::list` | Displays an embed listing the bot's commands. |
| `::luck` | Generates and reports a random luck score. |
| `::guess` | Starts a number guessing game. |

Unknown commands receive a response saying that the command does not exist.

## Requirements

- Python 3.10 or later
- A Discord bot application
- `discord.py`
- `python-dotenv`

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Nagisns/Discord_Bot.git
cd Discord_Bot
```

### 2. Install the dependencies

```bash
pip install discord.py python-dotenv
```

### 3. Create and configure a Discord bot

1. Visit the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create an application and add a bot.
3. Copy the bot token.
4. Enable **Message Content Intent** in the bot settings. The bot needs this
   intent to read command messages and guesses.
5. Invite the bot to your server with permission to view channels and send
   messages.

### 4. Configure the environment

Create a file named `.env` in the project directory:

```env
TOKEN=your_bot_token_here
```

Replace `your_bot_token_here` with your bot token. Keep the token private and
do not commit `.env` to Git.

If the `TOKEN` environment variable is missing or empty, the bot will display
an error message and exit. Whitespace-only values are also rejected.

### 5. Run the bot

```bash
python src/bot.py
```

Once the bot is running, use its commands in a server where it is present.

## Guessing Game

Use `::guess` to start. The bot chooses a number between 1 and 100, then waits
for guesses from the user who started the game in the same channel.

- If a guess is too high, the bot replies `Too high!`.
- If a guess is too low, the bot replies `Too low!`.
- If the guess is correct, the bot replies `Correct!` and reports the number
  of valid integer guesses.
- Non-integer messages prompt the user to enter a valid integer and do not
  count as guesses.
- Integer guesses outside the 1-100 range prompt the user to enter a number in
  range and do not count as guesses.
- The bot waits up to 20 seconds for each message from the player. If no
  message arrives in that time, the game ends and the bot reveals the number.
- Only one game can run in each channel at a time.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE)
file for details.

## Acknowledgements

- [discord.py](https://discordpy.readthedocs.io/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

This README was written with assistance from ChatGPT.
