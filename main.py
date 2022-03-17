import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import json
from api.api import getNPeople

def loadLocations():
    f = open('locations.json')
    data = json.load(f)
    f.close()

    locations = dict([((i["name"]).split("EVO ")[-1],i["id"]) for i in data["Locations"]])
    return locations

locations = loadLocations()

def getLocations():
    f = open('locations.json')
    data = json.load(f)
    f.close()
    allLocations = [i["name"] for i in data["Locations"]]
    print(str(allLocations))

allLocations = str(getLocations())

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = commands.Bot(command_prefix='/')

@bot.command()
async def hello(ctx):
    await ctx.reply("response")

@bot.command()
async def evo(ctx, arg):
    try:
        location = str(locations[arg])
        response = await getNPeople(location)
        JSONResponse = json.loads(response.text)
        current = JSONResponse["current"]
        await ctx.reply(f'Det er nå {current} personer inne på EVO {arg}')
    except:
        await ctx.reply(f'{arg} finnes ikke')
    
@bot.command()
async def lokasjoner(ctx):
    await ctx.reply(allLocations)

print("Bot running")
bot.run(str(BOT_TOKEN))