import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("im not ready"))
    print("I am online")

@client.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@client.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)

@commands.guild_only()
@client.command()
async def nordboy(ctx):
    role = discord.utils.get(ctx.guild.roles, name="nordboy")
    if role in ctx.author.roles:
        await ctx.send(f'You already have the role {role.name}')
    else:
        await ctx.author.add_roles(role)
        await ctx.send(":white_check_mark: User is now a nordboy")

token = os.getenv("DISCORD_BOT_TOKEN")
client.run(token)