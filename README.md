# Discord Bot

A simple Discord bot built with Python and discord.py.
This project was created as a learning project to practice Python
and Discord bot development.

## Features

- **Ping** — Check the bot's latency.
- **Luck** — Get a random luck score from 1 to 100.
- **Guess the Number** — Try to guess a randomly generated number
  between 1 and 100.

## Commands

| Command | Description |
|---|---|
| `::ping` | Displays the bot's latency in milliseconds. |
| `::luck` | Generates a random luck score. |
| `::guess` | Starts a number guessing game. |

## Requirements

- Python 3.10 or later
- A Discord bot application
- The following Python packages:
  - discord.py
  - python-dotenv

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Replace `YOUR_USERNAME` and `YOUR_REPOSITORY` with your
GitHub username and repository name.

### 2. Install the dependencies

```bash
pip install discord.py python-dotenv
```

### 3. Create a Discord bot

1. Visit the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create an application and add a bot.
3. Copy your bot token.
4. Enable the **Message Content Intent** in the bot settings.
5. Invite the bot to your Discord server with the required permissions.

### 4. Configure the environment

Create a file named `.env` in the project directory:

```env
TOKEN=your_bot_token_here
```

Replace `your_bot_token_here` with your actual bot token.

**Never share your bot token or commit your `.env` file to Git.**

### 5. Run the bot

```bash
python bot.py
```

Once the bot is running, you can use its commands in a
Discord server where the bot is present.

## How to Play

Use `::guess` to start the number guessing game.

The bot will choose a number between 1 and 100.
Send your guesses in the same channel.

- If your guess is too high, the bot will say `Too high!`.
- If your guess is too low, the bot will say `Too low!`.
- If you guess correctly, the bot will say `Correct!`.

The game counts your valid integer guesses.

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [discord.py](https://discordpy.readthedocs.io/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

---

This project is a work in progress as I continue learning Python
and Discord bot development.

- The README was written with assistance from ChatGPT.