import discord
import datetime
from discord.ext import commands

class Joinleave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 978414466892959756:
            channel = await self.bot.try_channel(978420380748365885)
            embed=discord.Embed(title="Welcome!",description=f"{member.mention} just joined the server! Make sure to give them a warm welcome!", color=0x00FFFF)
            embed.add_field(name= "", value="Thank you for joining the Gjallarhorn Server, make sure to check out <#1003443965447651359> before sending your first message!", inline=False)
            embed.timestamp = datetime.datetime.now()
            embed.set_thumbnail(url=f"{member.avatar}")
            await channel.send(embed=embed)
            channel = self.bot.get_channel(978421363884818472)
            embed=discord.Embed(title=f"User Joined",description=f"{member.mention} {member.name} just joined the server!", color=0x00FFFF)
            created_at = member.created_at.strftime("%b %d, %Y, %T")
            embed.add_field(name="Account Created", value=f"{created_at}", inline=False)
            embed.set_thumbnail(url=f"{member.avatar}")
            embed.set_footer(text=member.id)
            embed.timestamp = datetime.datetime.now()
            await channel.send(embed=embed)
            default_role = discord.utils.get(member.guild.roles, id=1081624269009715220)
            await member.add_roles(default_role)
            await member.send("Welcome to the Gjallarhorn server, we are happy to have you here! Please be sure to check out https://discord.com/channels/978414466892959756/1003443965447651359 and when you are done get with an officer or commander for next steps.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == 978414466892959756:
            channel = await self.bot.try_channel(978421363884818472)
            embed=discord.Embed(title=f"User Left",description=f"{member.mention} {member.name} just left the server!", color=0x00FFFF)
            embed.set_thumbnail(url=f"{member.avatar}")        
            embed.set_footer(text=member.id)
            embed.timestamp = datetime.datetime.now()
            await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Joinleave(bot))