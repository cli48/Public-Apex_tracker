
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.command()
async def apex(ctx, *args):
    # 'args' will contain any additional words after the command
    await ctx.send(f'Running Apex Legends command with arguments: {args}')

async def help(ctx):
    await ctx.send('Hello!')
# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token ='MTEzNTA2MDM1OTI1OTA5NTA5MA.G90GlQ.fwStjNTnvDK-aDdzvmUgRZ_lKUA8OLQJL2SNwg'
bot.run(bot_token)




