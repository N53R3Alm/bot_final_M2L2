import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
# Dan inilah cara Kamu mengganti nama file dari variabel!
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    await ctx.send(file=picture)

organic = ['veggie', 'grass', 'sisa makanan', 'kulit buah']
anorganic = ['kaca', 'botol plastik']

@bot.command()
async def trashbag(ctx):
    await ctx.send("Input your trash:")
    msg = await bot.wait_for("message")
    if msg.content in organic:
        await ctx.send("Put into organic trash can")
    elif msg.content in anorganic:
        await ctx.send("Put into anorganic trash can")

bot.run("MTIxNjAwOTY5MDAxMDM1Mzg0Ng.GL9uGB.dBYFD66oEJWQpNJE4fdYRSrbI_z8bU1umELLa4")