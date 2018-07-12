import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import praw

bot = commands.Bot(command_prefix='#')

reddit = praw.Reddit(client_id='client_id',
                     client_secret='client_secret',
                     user_agent='user_agent')

bot.remove_command('help') # For our custom help command

@bot.event
async def on_ready():
    print ("Running with the username " + bot.user.name + " With the ID " + bot.user.id)
    await bot.change_presence(game = discord.Game(name="Try #help"), status = discord.Status("online"))

@bot.command() # Main function
async def r(subreddit):
    submissions = reddit.subreddit(subreddit).hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in submissions if not x.stickied)

    await bot.say("Retrieving a random post from r/{}...".format(subreddit))
    await bot.say(submission.url + submission.selftext)

@bot.command(pass_context=True) # Help function
async def help(ctx):
    await bot.say("Thank you for adding Argus to your server!\nArgus retreives a random post from any subreddit that you specify.\n**Syntax**: `#r (subreddit)`")

bot.run("token")
