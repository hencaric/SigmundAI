import discord
from discord.ext import commands

class Responses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if self.bot.user.mentioned_in(message):
            print("Turlington has been mentioned.")
            await message.channel.send(f"Hello! I am Sigmund, the Gjallarhorn AI, say `?gencommand` for more info on what I can do! If you are having any issues with my functions please tag ian `<@288522211164160010>`.")

    @commands.command()
    async def gencommands(self, ctx):
        await ctx.send("__All commands use ? prefix__ \n**ping** - check the status of Gjallarhorn Bot\n")
        channel = self.bot.get_channel(1091976511696945182)
        author = ctx.author.name
        await channel.send(f"Command list access by {author}")

    @commands.command()
    async def enforcer(self, ctx):
        channel = self.bot.get_channel(1091976511696945182)
        author = ctx.author.name
        await channel.send(f"Admin command list access by {author}")
        role = discord.utils.get(ctx.guild.roles, name="Enforcer")
        if role in ctx.author.roles:
            await ctx.send("__All commands use ? prefix__ \n**kick (@user)** - kicks the mentioned user\n**ban (@user)** - bans mentioned user, must manually unban through server settings currently \n**mute (@user)** - adds muted role to user which keeps them from chatting or seeing any channels except #muted\n**purge (number)** - removes the indicated amount of messages from channel command was used in")
        else:
            await ctx.send("Sorry, you dont have the required permissions to perform this command!")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Hello! I am here.")

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
        embed.add_field(name="Icon", value=icon, inline=True)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Responses(bot))