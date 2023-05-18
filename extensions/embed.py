import discord
from discord.ext import commands


class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def embed(self, ctx):
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        await ctx.send('Waiting for a title')
        title = await self.bot.wait_for('message', check=check)
  
        await ctx.send('Waiting for a description')
        desc = await self.bot.wait_for('message', check=check)

        embed = discord.Embed(title=title.content, description=desc.content, color=0x1ABC9C)
        embed.set_author(name="Gjallarhorn Fleet AI", icon_url="https://i.imgur.com/j31QvVm.png")
    
        await ctx.send(embed=embed)

    @commands.command()
    async def embednoauthor(self, ctx):
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        await ctx.send('Waiting for a title')
        title = await self.bot.wait_for('message', check=check)
  
        await ctx.send('Waiting for a description')
        desc = await self.bot.wait_for('message', check=check)

        embed = discord.Embed(title=title.content, description=desc.content, color=0x1ABC9C)
    
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Embed(bot))