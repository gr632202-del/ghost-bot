import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} online ho gaya!')
    print('------')

@bot.event
async def on_message(message):
    if message.author == bot:
        return
    
    if message.content.lower() == 'hi':
        await message.channel.send('Hello bhai 👋')
    
    await bot.process_commands(message)

bot.run(os.getenv('TOKEN'))
