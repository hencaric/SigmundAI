#Gjallarhorn AI Version 1.4-Build 
#Production Date: 3/19/23
#Creator: ian#5555

import os
import discord
import discord.ext
from discord.utils import get
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
intents.message_content = True
intents.members = True 

extensions = ("embed","joinleave","moderation","responses",)
bot = commands.Bot(command_prefix="?", intents=intents)
ALLOWED_GUILDS = (978414466892959756,)
bot.add_check(lambda ctx: ctx.guild.id in ALLOWED_GUILDS)

@bot.event
async def setup_hook():
    for extension in extensions:
        await bot.load_extension(extension)

@bot.event
async def on_ready():
    print("The Gjallarhorn AI is online and watching!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Stanton"))

bot.run(TOKEN)