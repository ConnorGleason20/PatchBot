import requests
import json
import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv


def get_patch_notes(url):
    """gets patch notes from url"""
    page = requests.get(url)
    patches = page.json()
    notes = patches.get("appnews", {}).get("newsitems", [])
    for patch in notes:
        title = patch.get("title")
    try:
        with open('patch_notes.json', 'r') as f:
            patch_notes = json.load(f)
    except FileNotFoundError:
        print("patch_notes.json not found")
    if title in patch_notes:
        print('Patch note already exists')
        return False
    else:
        patch_notes.insert(0, title)
        with open('patch_notes.json', 'w') as f:
            json.dump(patch_notes, f)
        return True



#Discord bot set up
load_dotenv(".env")
token = os.getenv("DISCORD_TOKEN")
server_name = os.getenv("SERVER_ID")
channel_name = os.getenv("CHANNEL_ID")
intents = discord.Intents.all()
intents.message_content = True
intents.guilds = True
bot = commands.Bot(command_prefix='!', intents=intents)
#main program
@bot.event
async def on_ready():
    print("Patch Bot Ready")
    await bot.wait_until_ready()
    channel = bot.get_channel(int(channel_name))
    await channel.send("Patch Bot Ready")
    patch_notes_updates.start(channel)
@tasks.loop(hours=1.0)
async def patch_notes_updates(channel):
    """commands for the discord bot"""
    url1 = os.getenv("URL1")
    url2 = os.getenv("URL2")
    url3 = os.getenv("URL3")
    try:
        if get_patch_notes(url1) is True:
            await channel.send('https://store.steampowered.com/news/app/2767030')
        else:
            print('No patch notes found')
        if get_patch_notes(url2) is True:
            await channel.send('https://store.steampowered.com/news/app/1384160')
        else:
            print('No patch notes found')
        if get_patch_notes(url3) is True:
            await channel.send('https://store.steampowered.com/news/app/2357570')
        else:
            print('No patch notes found')
    except Exception as e:
        print(e)
bot.run(token)
