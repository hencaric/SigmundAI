import discord
import datetime
from discord.ext import commands

class OrgManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot           

    @commands.command()
    async def fleetinfo(self, ctx):
        embed=discord.Embed(title=f"Gjallarhorn Fleet Info (Public)",description=f"- __**Flagship:**__ GNV Isaribi\n**Station:** Lorville\n**Primary Directive:** Distribution of Civilian Readiness Program Equipment Kits\n**Secondary Directive:** Protection and Escort of Gallus Corporation Ships and Personnel", color=0x00FFFF)
        embed.timestamp = datetime.datetime.now()
        await ctx.reply(embed=embed)        
        channel = self.bot.get_channel(1091976511696945182)
        author = ctx.author.name
        embed=discord.Embed(title=f"Fleet Info Accessed", color=0x00FFFF)
        embed.add_field(name="Author", value=f"{author}", inline=True)   
        embed.timestamp = datetime.datetime.now()
        await channel.send(embed=embed)

#    @commands.command()
#    async def personnelinfo(self, ctx):
#        embed=discord.Embed(title=f"Gjallarhorn Personnel Info (Public)",description=f"- __**Acting Director:**__ Ciphernaught", color=0x00FFFF)
#        embed.timestamp = datetime.datetime.now()
#        await ctx.reply(embed=embed)        
#        channel = self.bot.get_channel(1091976511696945182)
#        author = ctx.author.name
#        embed=discord.Embed(title=f"Personnel Info Accessed", color=0x00FFFF)
#        embed.add_field(name="Author", value=f"{author}", inline=True)   
#        embed.timestamp = datetime.datetime.now()
#        await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(OrgManagement(bot))