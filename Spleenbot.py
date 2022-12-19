import discord
from discord.ext import commands
import random


#intents = discord.Intents.default()
intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='$$', intents=intents)


@bot.event 
async def on_ready():
    print('We have logged in as {0.user}'.format(bot)) #tells us that our bot is online

@bot.event #responding to messages
async def on_message(message):
    message.content = (message.content.lower()) #makes all messages lowercase, from the bot's perspective
    if message.author == bot.user: #to not respond to bots
        return
    if "hello" in message.content:
        await message.channel.send("Hi!") #response
    if "rickroll" in message.content:
        await message.channel.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    if "princesa" in message.content:
        await message.channel.send("https://www.youtube.com/watch?v=zTwgwEHiWm0&ab_channel=BlueMarbleNations")


      
    await bot.process_commands(message) #VERY IMPORTANT, if this line is not added, the bot will not respond to commands


    

@bot.command(aliases=['test2', 'testing']) #other names for the command
async def test(ctx): #test is the command name
    await ctx.send("yes, yes, I am working.") #response to the command

@bot.command(aliases = ['8ball'])
async def ball(ctx): #can't really put numbers in the command name so we have 8ball as an alias instead
    import random
    ballresponses = ['Yes', 'No']
    z = random.choice(ballresponses) #choose yes or no, randomly
    await ctx.send(z) #send either yes or no 

@bot.command()
async def givenum(ctx):

    # checks the author is responding in the same channel
    # and the message is able to be converted to a positive int
    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit() and \
               msg.channel == ctx.channel

    await ctx.send("Type a number")
    msg1 = await bot.wait_for("message", check=check)
    await ctx.send("Type a second, larger number")
    msg2 = await bot.wait_for("message", check=check)
    x = int(msg1.content)
    y = int(msg2.content)
    if x < y:
        value = random.randint(x,y)
        await ctx.send(f"You got {value}.")
    else:
        await ctx.send(":warning: Please ensure the first number is smaller than the second number.")

@bot.command()
async def rando(ctx):
    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit() and \
               msg.channel == ctx.channel

    await ctx.send("Gimme a number")
    
    msg1 = await bot.wait_for("message", check = check)
    x = int(msg1.content)

    random_value = random.choice(range(0,200))

    await ctx.send(f"numbers are {x} and {random_value} ")
  

bot.run('') #put your token here 