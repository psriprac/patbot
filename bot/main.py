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

@client.command()
async def nordboy(ctx, member:discord.Member, nordboy: discord.Role): #pass user and role
    if nordboy in member.roles: #checks all roles the member has
        await member.remove_roles(nordboy) #removes the role
    else:
        await member.add_roles(nordboy) #adds the role

token = os.getenv("DISCORD_BOT_TOKEN")
client.run(token)