import discord 
client = discord.Client()

bot_ka_token=''

@client.event
async def on_ready():
    print('Bot is connected to Discord!')

@client.command(name='$ping')
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(bot_ka_token)
