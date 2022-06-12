import whois
import discord
from discord.ext import commands

class Consultas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def whois(self, ctx, message):
        await ctx.send("Um momento...")
        w = whois.whois(message)
        embed=discord.Embed(title="🔎 | Whois encontrado!", description=f"{message} foi encontrado! aqui está o arquivo, mais opções nesse embed!", color=0x5865F2 )
        embed.add_field(name="Resultado do BuiltWith!", value=f"[Clique aqui!](https://builtwith.com/{message})", inline=True)
        embed.add_field(name="Resultado do Google!", value=f"[Clique aqui!](https://www.google.com/search?q={message})", inline=True)
        with open('whois_result.txt', 'w') as f:
            f.write('WHOIS RESULT BY POOOORYGON BOT' + f'{w}' + 'WHOIS RESULT BY POOOORYGON BOT')
        await ctx.author.send(embed=embed)
        await ctx.author.send(files=[discord.File('whois_result.txt')])

def setup(bot):
    bot.add_cog(Consultas(bot))

