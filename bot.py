# Copyright (c) 2026 Nagi(Nagisns)
# Licensed under the MIT License.
# See the LICENSE file for details.

import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN: str = os.environ["TOKEN"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="::", intents=intents)

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

    await ctx.send("I'm thinking of a number between 1 and 100. Guess the number!")

    def check_message(message: discord.Message) -> bool:
        check_user: bool = ctx.author == message.author
        check_channel: bool = ctx.channel == message.channel

        return check_user and check_channel

    try_counter: int = 0

    while True:
        message: discord.Message = await bot.wait_for("message", check=check_message, timeout=20.0)

        try:
            guess_number: int = int(message.content)
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
    
bot.run(TOKEN)