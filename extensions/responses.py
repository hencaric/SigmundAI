import discord
import datetime
from discord.ext import commands

class Responses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if self.bot.user.mentioned_in(message):
            await message.channel.send(f"Hello! I am Sigmund, the Gjallarhorn AI, say `?gencommand` for more info on what I can do! If you are having any issues with my functions please tag Ian `<@288522211164160010>`.")
            
    @commands.command(description='Ping?')
    async def ping(self, ctx):
        await ctx.reply("Pong!")            

    @commands.command()
    async def gencommands(self, ctx):
        embed=discord.Embed(title=f"General Command List",description=f"__All commands use ? prefix__ \n**ping** - check the status of Gjallarhorn Bot\n", color=0x00FFFF)
        embed.timestamp = datetime.datetime.now()
        await ctx.reply(embed=embed)        
        channel = self.bot.get_channel(1091976511696945182)
        author = ctx.author.name
        embed=discord.Embed(title=f"General Command List Accessed",description=f"General command list was summoned.", color=0x00FFFF)
        embed.add_field(name="Author", value=f"{author}", inline=True)   
        embed.timestamp = datetime.datetime.now()
        await channel.send(embed=embed)
    @commands.command()
    async def enforcer(self, ctx):
        channel = self.bot.get_channel(1091976511696945182)
        author = ctx.author.name
        embed=discord.Embed(title=f"Admin Command List Accessed",description=f"Admin command list was summoned.", color=0x00FFFF)
        embed.add_field(name="Author", value=f"{author}", inline=True)   
        embed.timestamp = datetime.datetime.now()
        await channel.send(embed=embed)
        role = discord.utils.get(ctx.guild.roles, name="Enforcer")
        if role in ctx.author.roles:
            embed=discord.Embed(title=f"Moderation Command List",description=f"__All commands use ? prefix__ \n**kick (@user)** - kicks the mentioned user\n**ban (@user)** - bans mentioned user, must manually unban through server settings currently \n**mute (@user)** - adds muted role to user which keeps them from chatting or seeing any channels except #muted\n**purge (number)** - removes the indicated amount of messages from channel command was used in", color=0x00FFFF)
            embed.timestamp = datetime.datetime.now()
            await ctx.reply(embed=embed)        
        else:
            await ctx.reply("Sorry, you dont have the required permissions to perform this command! If you think this was in error please tag Ian `<@288522211164160010>`.")    

    @commands.command()
    async def whereami(self,ctx):
        owner=str(ctx.guild.owner.name)
        icon=str(ctx.guild.icon.url)
        guild_id = str(ctx.guild.id)
        memberCount = str(ctx.guild.member_count)
        desc=ctx.guild.description
        
        embed = discord.Embed(
            title=ctx.guild.name + " Server Information",
            description=desc,
            color=discord.Color.blue()
        )
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=guild_id, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)
        embed.set_thumbnail(url=icon)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Responses(bot))