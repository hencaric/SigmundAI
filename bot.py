import subprocess
from discord.ext import commands
import discord
from utils import Config

VERSION = "1.0.0"
INTENTS = discord.Intents.all()
INTENTS.message_content = True
INTENTS.members = True


class Bot(commands.Bot):
    def __init__(self, config: Config, /) -> None:
        super().__init__(
            intents=INTENTS,
            command_prefix=commands.when_mentioned_or(config.prefix),
            allowed_mentions=discord.AllowedMentions(everyone=False),
            case_insensitive=True,
            activity=discord.Activity(
                type=discord.ActivityType.watching, name="Stanton"
            ),
        )
        self.config = config
        self.version = VERSION

    async def setup_hook(self) -> None:
        for extension in self.config.extensions:
            await self.load_extension(extension)

        await self.add_cog(CoreCog(self))


class CoreCog(commands.Cog, name="Core"):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.hybrid_command(description="Shows you some info about the bot.")
    async def info(self, ctx: commands.Context) -> None:
        embed = discord.Embed(
            color=self.bot.config.embed_color,
            description="The GjallarhornAI is a Discord bot created for the Gjallarhorn Organization Discord server to provide info and help with org/fleet management.",
        )
        embed.add_field(
            name="Version", value=f"v{VERSION}"
        )
        view = discord.ui.View()
        await ctx.reply(embed=embed, view=view, mention_author=False)