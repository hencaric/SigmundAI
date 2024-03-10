import discord
import asyncio
import datetime
from discord.ext import commands
import asyncio
import re

with open("bad_words.txt") as file:
    bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]

time_units = {
    "second": 1,
    "minute": 60,
    "hour": 3600,
    "day": 86400,
}

def convert_to_seconds(duration: str):
    try:
        match = re.match(r'(\d+)\s*(\w+)', duration)
        if match:
            amount, unit = match.groups()
            seconds = int(amount) * time_units.get(unit.lower(), 0)
            return seconds
    except ValueError:
        pass
    return None

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= 'purge')
    async def purge(self, ctx, num):
        channel = self.bot.get_channel(1091976511696945182)
        author = ctx.author.name
        embed=discord.Embed(title=f"Messages have been purged",description=f"{num} messages have been deleted from {channel}.", color=0x00FFFF)
        embed.add_field(name="Author", value=f"{author}", inline=True)   
        embed.timestamp = datetime.datetime.now()
        await channel.send(embed=embed)
        role = discord.utils.get(ctx.guild.roles, id=1197608181526966313)
        if role in ctx.author.roles:
            msg = []
            async for x in ctx.channel.history(limit=int(num)):
                msg.append(x)
            await ctx.channel.delete_messages(msg)
            print(num + ' messages removed from the channel')
            channel = self.bot.get_channel(978421363884818472)
            embed=discord.Embed(title=f"Messages have been purged",description=f"{num} messages have been deleted from {channel} by {author}.", color=0x00FFFF)
            embed.timestamp = datetime.datetime.now()
            await channel.send(embed=embed)
            warning = await ctx.send(num + ' messages removed from the channel')

            await asyncio.sleep(3)
            await warning.delete()
        else:
            await ctx.reply("Sorry, you dont have the required permissions to perform this command! If you think this was in error please tag Ian `<@288522211164160010>`.")

    @commands.command()
    async def kick(self, ctx, user: discord.Member, *, reason: str = "No reason provided."):
        role = discord.utils.get(ctx.guild.roles, id=1197608181526966313)
        if role in ctx.author.roles:
# reporting server message
            author = ctx.author.name
            channel = self.bot.get_channel(1091976511696945182)
            embed=discord.Embed(title=f"User has been kicked",description=f"{user.mention} has been kicked from the server by **{author}**.\n\n**Username:** {user}\n**ID:** {user.id}\n**Reason:** {reason}", color=0x00FFFF) 
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=f"{user.avatar}")
            await channel.send(embed=embed)
# in-server message
            await user.send(f"You have been kicked from the Gjallarhorn server for {reason}.")
            await user.kick()
            channel = self.bot.get_channel(978421363884818472)
            embed=discord.Embed(title=f"User has been kicked",description=f"{user.mention} has been kicked from the server by **{author}**.\n\n**Username:** {user}\n**ID:** {user.id}\n**Reason:** {reason}", color=0x00FFFF)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=f"{user.avatar}")
            await channel.send(embed=embed)
            print('A user has been kicked')
        else:
            await ctx.reply("Sorry, you dont have the required permissions to perform this command! If you think this was in error please tag Ian `<@288522211164160010>`.")

    @commands.command()
    async def ban(self, ctx, user: discord.Member, *, reason: str = "No reason provided."):
        role = discord.utils.get(ctx.guild.roles, id=1197608181526966313)
        if role in ctx.author.roles:
# reporting server message
            author = ctx.author.name
            channel = self.bot.get_channel(1091976511696945182)
            embed=discord.Embed(title=f"User has been banned",description=f"{user.mention} has been banned from the server by **{author}**.\n\n**Username:** {user}\n**ID:** {user.id}\n**Reason:** {reason}", color=0x00FFFF) 
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=f"{user.avatar}")
            await channel.send(embed=embed)
# in-server message
            await user.send(f"You have been banned from the Gjallarhorn server for {reason}.")
            await user.ban()
            channel = self.bot.get_channel(978421363884818472)
            embed=discord.Embed(title=f"User has been banned",description=f"{user.mention} has been banned from the server by **{author}**.\n\n**Username:** {user}\n**ID:** {user.id}\n**Reason:** {reason}", color=0x00FFFF)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=f"{user.avatar}")
            await channel.send(embed=embed)
            print('A user has been banned')
        else:
            await ctx.reply("Sorry, you dont have the required permissions to perform this command! If you think this was in error please tag Ian `<@288522211164160010>`.") 

#    @commands.command()
#    async def mute(self, ctx, member: discord.Member, duration: str):
#    async def mute(self,ctx, user: discord.Member):
#        seconds = convert_to_seconds(duration)
#        role = discord.utils.get(ctx.guild.roles, id=1197608181526966313)
#        if role not in ctx.author.roles:
#            await ctx.reply("Sorry, you dont have the required permissions to perform this command! If you think this was in error please tag Ian `<@288522211164160010>`.")
#            return
#        if seconds is None:
#            await ctx.send("Invalid duration specified. Please use a valid format (e.g., '1 hour').")
#            return
#        role = discord.utils.get(ctx.guild.roles, id=1081630634289668208)
#        await member.add_roles(role)
#        channel = self.bot.get_channel(1091976511696945182)
#        author = ctx.author.name
#        embed=discord.Embed(title=f"User has been muted",description=f"{member} has been muted for {seconds}.", color=0x00FFFF)
#        embed.add_field(name="Author", value=f"{author}", inline=True)   
#        embed.timestamp = datetime.datetime.now()
#        await ctx.send(f"{member.mention} has been muted for {duration} seconds.")
#        await asyncio.sleep(duration)
#        await member.remove_roles(role)
#        await ctx.send(f"{member.mention} has been unmuted.")
#        channel = self.bot.get_channel(1091976511696945182)
#        author = ctx.author.name
#        embed=discord.Embed(title=f"User has been muted",description=f"{member} has been muted for {duration}.", color=0x00FFFF)
#        embed.add_field(name="Author", value=f"{author}", inline=True)   
#        embed.timestamp = datetime.datetime.now()



#        role = discord.utils.get(ctx.guild.roles, id=1197608181526966313)
#        if role in ctx.author.roles:
#            role = discord.utils.get(ctx.guild.roles, id=1081630634289668208)
#            mutedrole = discord.utils.get(ctx.guild.roles, id= 1081630634289668208)
#            member = discord.utils.get(ctx.guild.roles, id= 978416622270283787)
#            await user.add_roles(mutedrole)
#            await user.remove_roles(member)
#            channel = self.bot.get_channel(978421363884818472)
#            embed=discord.Embed(title=f"User has been muted",description=f"{user} has been muted by {author}.", color=0x00FFFF)
#            embed.timestamp = datetime.datetime.now()
#            await channel.send(embed=embed)
#            print('A user has been muted')
#        else:
#            await ctx.reply("Sorry, you dont have the required permissions to perform this command! If you think this was in error please tag Ian `<@288522211164160010>`.")

#    @commands.command()
#    async def unmute(self, ctx, user: discord.Member):
#        channel = self.bot.get_channel(1091976511696945182)
#        author = ctx.author.name
#        embed=discord.Embed(title=f"User has been unmuted",description=f"{user} has been unmuted.", color=0x00FFFF)
#        embed.add_field(name="Author", value=f"{author}", inline=True)   
#        embed.timestamp = datetime.datetime.now()
#        role = discord.utils.get(ctx.guild.roles, id=1197608181526966313)
#        if role in ctx.author.roles:
#            mutedrole = discord.utils.get(ctx.guild.roles, id= 1081630634289668208)
#            member = discord.utils.get(ctx.guild.roles, id= 978416622270283787)
#            await user.remove_roles(mutedrole)
#            await user.add_roles(member)
#            channel = self.bot.get_channel(978421363884818472)
#            embed=discord.Embed(title=f"User has been unmuted",description=f"{user} has been unmuted by {author}.", color=0x00FFFF)
#            embed.timestamp = datetime.datetime.now()
#            await channel.send(embed=embed)
#            print('A user has been unmuted')
#        else:
#            await ctx.reply("Sorry, you dont have the required permissions to perform this command! If you think this was in error please tag Ian `<@288522211164160010>`.")

    @commands.Cog.listener() 
    async def on_message(self, message):
        for bad_word in bad_words:
            if bad_word in message.content:
                print("Banned words scrubbed from chat.")
                await message.delete()
                await message.channel.send("That terminology is not permitted here.")
                channel = self.bot.get_channel(978421363884818472)
                embed=discord.Embed(title=f"A censored word has been scrubbed.",description=f"{message.author} has used the censored term, {bad_word}, and it has been scrubbed from the server.", color=0x00FFFF)
                embed.timestamp = datetime.datetime.now()
                await channel.send(embed=embed)
                channel = self.bot.get_channel(1091976511696945182)
                embed=discord.Embed(title=f"A censored word has been scrubbed.",description=f"{message.author} has used the censored term, {bad_word}, and it has been scrubbed from the server.", color=0x00FFFF)
                embed.timestamp = datetime.datetime.now()

async def setup(bot):
    await bot.add_cog(Moderation(bot))