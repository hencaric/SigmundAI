import discord
import datetime
from discord.ext import commands

class Joinleave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = await self.bot.try_channel(978420390748365885)
        embed=discord.Embed(title="Welcome!",description=f"{member.mention} just joined the server! Make sure to give them a warm welcome!", color=0x00FFFF)
        embed.add_field(name= "", value="Thank you for joining the Gjallarhorn Server, make sure to check out #server-rules before sending your first message!", inline=False)
        embed.timestamp = datetime.datetime.now()
        embed.set_thumbnail(url="https://i.imgur.com/kQOJjQf.jpg")
        await channel.send(embed=embed)
        channel = self.bot.get_channel(978421363884818472)
        embed=discord.Embed(title=f"User Joined",description=f"{member} just joined the server!", color=0x00FFFF)
        embed.set_footer(text=member.id)
        embed.set_thumbnail(url= "https://i.imgur.com/6anFs9h.jpg")
        embed.timestamp = datetime.datetime.now()
        await channel.send(embed=embed)
        default_role = discord.utils.get(member.guild.roles, id=978420390748365885)
        await member.add_roles(default_role)
        await member.send("Welcome to the Gjallarhorn server, we are happy to have you here! Please be sure to read all the rules before agreeing and when you are done get with an officer or commander for next steps.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = await self.bot.try_channel(978421363884818472)
        embed=discord.Embed(title=f"User Left",description=f"{member} just left the server!", color=0x00FFFF)
        embed.set_footer(text=member.id)
        embed.set_thumbnail(url= "https://i.imgur.com/2pohyKU.png")
        embed.timestamp = datetime.datetime.now()
        await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Joinleave(bot))