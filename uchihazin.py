import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ">", case_insensitive = True)

@client.event
async def on_ready():
  print('entramos como {0.user}' .format(client))

@client.command()
async def ola(ctx):
  await ctx.send(f'olá, {ctx.author}')

@client.command()
async def nome(ctx):
  await ctx.send(f'seu nome é {ctx.author}')

@client.command()
async def potencia(ctx):
  await ctx.send('é a potencia não tem com muleke nem se mexe')

@client.command()
async def mhzin(ctx):
  await ctx.send('sabe que é o mhzin')

client.run('ODUyMzA2NTgxNDc5NDg5NTQx.YME6XA.CItPl3MuSI4He9IbxXZcCb2fUes')
