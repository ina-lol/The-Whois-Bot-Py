import discord
import whois
from secret.key import *
from discord.ext import commands

bot = commands.Bot(command_prefix="$")

bot.load_extension('cogs.whois')

@bot.command()
async def ping(ctx, message):
    await  ctx.reply("Pong!")

bot.run(key)