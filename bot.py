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

# This global variable is used in the guess function.
active_games: set[int] = set()

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
    secret_number: int = random.randint(1, 100)

    channel_id: int = ctx.channel.id

    try_counter: int = 0

    if channel_id not in active_games:
        active_games.add(channel_id)
    else:
        await ctx.send("A game is already running in this channel!")
        return

    def check_message(message: discord.Message) -> bool:
        check_user: bool = ctx.author == message.author
        check_channel: bool = ctx.channel == message.channel

        return check_user and check_channel

    try:
        await ctx.send("I'm thinking of a number between 1 and 100. Guess the number!")

        while True:
            try:
                message: discord.Message = await bot.wait_for("message", check=check_message, timeout=20.0)
            except asyncio.TimeoutError:
                await ctx.send(f"Time's up! The correct number was {secret_number}.")
                return

            try:
                guess_number: int = int(message.content)
                if not 1 <= guess_number <= 100:
                    await ctx.send("Please enter a number between 1 and 100.")
                    continue
            except ValueError:
                await ctx.send("Please enter a valid integer.")
                continue

            try_counter += 1

            if guess_number > secret_number:
                await ctx.send("Too high!")
            elif guess_number < secret_number:
                await ctx.send("Too low!")
            else:
                await ctx.send("Correct!")
                break

        await ctx.send(f"Your try counter is {try_counter}")
    finally:
        active_games.discard(channel_id)
    
bot.run(TOKEN)