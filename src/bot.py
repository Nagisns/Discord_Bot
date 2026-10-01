# Copyright (c) 2026 Nagi(Nagisns)
# Licensed under the MIT License.
# See the LICENSE file for details.

import asyncio
import os
import random
import sys

import discord
from discord.ext import commands
from dotenv import load_dotenv

from games import GuessGame
from game_manager import ActiveGames

load_dotenv()
try:
    TOKEN: str = os.environ["TOKEN"]
    if not TOKEN.strip():
        print("The TOKEN environment variable is empty.")
        sys.exit(1)
except KeyError:
    print("The TOKEN environment variable is not set.")
    sys.exit(1)
    
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="::", intents=intents)

active_game = ActiveGames()

@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user}")

@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError) -> None:
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("This command does not exist.")
    else:
        raise error

@bot.command()
async def ping(ctx: commands.Context) -> None:
    latency = round(bot.latency * 1000)
    await ctx.send(f"Pong! {latency} ms")

@bot.command()
async def list(ctx: commands.Context) -> None:
    embed = discord.Embed(
        title="Commands List",
        description="ping - Shows the bot's latency in milliseconds.\n " \
                    "luck - Generates and reports a random luck score.\n" \
                    "guess - Starts a number guessing game.",
        colour=discord.Colour.blue()
        )

    await ctx.send(embed=embed)

@bot.command()
async def luck(ctx: commands.Context) -> None:
    luck_score: int = random.randint(1, 100)

    if luck_score >= 70:
        result: str = "Good luck!"
    elif luck_score >= 40:
        result: str = "Average luck."
    else:
        result: str = "Bad luck..."

    await ctx.send(f"Your luck score is {luck_score}/100!\n{result}")

@bot.command()
async def guess(ctx: commands.Context) -> None:
    game = GuessGame(channel_id=ctx.channel.id, user_id=ctx.author.id)

    if active_game.check_active(game.channel_id) is False:
        active_game.add_channel(game.channel_id, "guess")
    else:
        await ctx.send("A game is already running in this channel!")
        return

    def check_message(message: discord.Message) -> bool:
        return game.user_id == message.author.id and game.channel_id == message.channel.id

    try:
        await ctx.send("I'm thinking of a number between 1 and 100. Guess the number!")

        while True:
            try:
                message: discord.Message = await bot.wait_for("message", check=check_message, timeout=20.0)
            except asyncio.TimeoutError:
                await ctx.send(f"Time's up! The correct number was {game.secret_number}.")
                return

            try:
                guess_number: int = int(message.content)
                if not 1 <= guess_number <= 100:
                    await ctx.send("Please enter a number between 1 and 100.")
                    continue
            except ValueError:
                await ctx.send("Please enter a valid integer.")
                continue

            result: str = game.check_guess(guess_number)

            if result == "high":
                await ctx.send("Too high!")
            elif result == "low":
                await ctx.send("Too low!")
            elif result == "correct":
                await ctx.send("Correct!")
                break

        await ctx.send(f"Your try counter is {game.try_counter}")
    finally:
        active_game.remove_channel(game.channel_id)

bot.run(TOKEN)
