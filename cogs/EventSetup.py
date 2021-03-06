import discord
from discord.ext import commands
from discord import  Role, TextChannel
from utils import Configuration, Permission


class EventSetup(commands.Cog):
    def __init__(self, bot):
        pass

    @commands.guild_only()
    @commands.group(hidden=True)
    async def configure(self, ctx: commands.Context):
        """Configure server specific settings."""
        if ctx.subcommand_passed is None:
            await ctx.send("See the subcommands (+help configure) for configurations.")

    @configure.command(hidden=True)
    async def fanart(self, ctx:commands.Context, channel:TextChannel):
        """Sets the FanArt channel."""
        mods = discord.utils.get(ctx.guild.roles, id=590955362106998784)
        if 590955362106998784 not in [role.id for role in ctx.author.roles]:
            return
        else:
            Configuration.setConfigVar(ctx.guild.id, "FAN_ART_CHANNEL", channel.id)
            await ctx.send(f"The Fan Art category channel is now {channel.mention}")

    @configure.command(hidden=True)
    async def emoji(self, ctx:commands.Context, channel:TextChannel):
        """Sets the Emoji Art channel."""
        mods = discord.utils.get(ctx.guild.roles, id=590955362106998784)
        if 590955362106998784 not in [role.id for role in ctx.author.roles]:
            return
        else:
            Configuration.setConfigVar(ctx.guild.id, "EMOJIS_CHANNEL", channel.id)
            await ctx.send(f"The Emoji Art category channel is now {channel.mention}")

    @configure.command(hidden=True)
    async def merch(self, ctx:commands.Context, channel:TextChannel):
        """Sets the Merch Art channel."""
        mods = discord.utils.get(ctx.guild.roles, id=590955362106998784)
        if 590955362106998784 not in [role.id for role in ctx.author.roles]:
            return
        else:
            Configuration.setConfigVar(ctx.guild.id, "MERCH_CHANNEL", channel.id)
            await ctx.send(f"The Merch Art category channel is now {channel.mention}")

    @configure.command(hidden=True)
    async def music(self, ctx:commands.Context, channel:TextChannel):
        mods = discord.utils.get(ctx.guild.roles, id=590955362106998784)
        if 590955362106998784 not in [role.id for role in ctx.author.roles]:
            return
        else:
            Configuration.setConfigVar(ctx.guild.id, "MUSIC_CHANNEL", channel.id)
            await ctx.send(f"The Music category channel is now {channel.mention}")

    @configure.command(hidden=True)
    async def story(self, ctx:commands.Context, channel:TextChannel):
        mods = discord.utils.get(ctx.guild.roles, id=590955362106998784)
        if 590955362106998784 not in [role.id for role in ctx.author.roles]:
            return
        else:
            Configuration.setConfigVar(ctx.guild.id, "STORY_CHANNEL", channel.id)
            await ctx.send(f"The Stories category channel is now {channel.mention}")

    @configure.command(hidden=True)
    async def productivity(self, ctx:commands.Context, channel:TextChannel):
        mods = discord.utils.get(ctx.guild.roles, id=590955362106998784)
        if 590955362106998784 not in [role.id for role in ctx.author.roles]:
            return
        else:
            Configuration.setConfigVar(ctx.guild.id, "PRODUCTIVITY", channel.id)
            await ctx.send(f"The Functional Bot category channel is now {channel.mention}")

    @configure.command(hidden=True)
    async def entertainment(self, ctx:commands.Context, channel:TextChannel):
        mods = discord.utils.get(ctx.guild.roles, id=590955362106998784)
        if 590955362106998784 not in [role.id for role in ctx.author.roles]:
            return
        else:
            Configuration.setConfigVar(ctx.guild.id, "ENTERTAINMENT", channel.id)
            await ctx.send(f"The Entertainment Bot category channel is now {channel.mention}")

    @configure.command(hidden=True)
    async def shitpost(self,ctx:commands.Context, channel:TextChannel):
        mods = discord.utils.get(ctx.guild.roles, id=590955362106998784)
        if 590955362106998784 not in [role.id for role in ctx.author.roles]:
            return
        else:
            Configuration.setConfigVar(ctx.guild.id, "SHITPOST", channel.id)
            await ctx.send(f"The Shitpost Bot category channel is now {channel.mention}")

    @configure.command(hidden=True)
    async def moderation(self,ctx:commands.Context, channel:TextChannel):
        mods = discord.utils.get(ctx.guild.roles, id=590955362106998784)
        if 590955362106998784 not in [role.id for role in ctx.author.roles]:
            return
        else:
            Configuration.setConfigVar(ctx.guild.id, "MODERATION", channel.id)
            await ctx.send(f"The Shitpost Bot category channel is now {channel.mention}")

    @configure.command(hidden=True)
    async def social(self,ctx:commands.Context, channel:TextChannel):
        mods = discord.utils.get(ctx.guild.roles, id=590955362106998784)
        if 590955362106998784 not in [role.id for role in ctx.author.roles]:
            return
        else:
            Configuration.setConfigVar(ctx.guild.id, "SOCIAL", channel.id)
            await ctx.send(f"The Shitpost Bot category channel is now {channel.mention}")

    @configure.command(hidden=True)
    async def censored(self,ctx:commands.Context, channel:TextChannel):
        mods = discord.utils.get(ctx.guild.roles, id=590955362106998784)
        if 590955362106998784 not in [role.id for role in ctx.author.roles]:
            return
        else:
            Configuration.setConfigVar(ctx.guild.id, "CENSORED_LOGS", channel.id)
            await ctx.send(f"The censored channel is now {channel.mention}")


def setup(bot):
    bot.add_cog(EventSetup(bot))
