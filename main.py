import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

description = 'grgrgrgrgrgrgrggr'
bot = commands.Bot(command_prefix='$', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

bot.run("MTE2MzA1NDIxMjAwODEyNDUzNg.GkdjoY.1vEAz94T1nubYLitH9-PVQUe1lIf3RTkrJlxjg")