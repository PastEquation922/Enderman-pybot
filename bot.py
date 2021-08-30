import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '=')

@client.event
async def on_ready():
    print('Bot is ready and set up to go!')

@client.command(aliases=['information', 'about'])
async def info(ctx):
    await ctx.send('Hello! Im enderman and im from python! my brother is mr.creeper. Past#6854 created me!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['question'])
async def trivia(ctx, *, question):
    responses = ["Don't count on it.",
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.',
                "Reply hazy, try again.",
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                "As I see it, yes.",
                'Most likely.',
                'Outlook good',
                'Yes.',
                'Signs point to yes.',
                'It is Certain.',
                'It is decidedly so.',
                'Without a doubt.',
                 'Yes definitely.',
                'You may rely on it.']
    await ctx.send(f'{random.choice(responses)}')

client.run('ODgxNTYwMjgzNTg2MzkyMDk0.YSum_g.K3JNRc1xNgZQwQfYEQAJGxlBseg')
