
from asyncio.windows_events import NULL
from os.path import join
from discord.voice_client import VoiceClient
from tokens import *    # TODO use ENV-variables later
import freesound
import discord

fs = freesound.FreesoundClient()
fs.set_token(freesound_client_secret)

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if not message.content.startswith('&'):
        return

    string :str = message.content
    splstr = string.split()
    command = splstr[0][1]
    if command=='p':
        sounds = fs.text_search(query=splstr[1])
        sounds[0].retrieve_preview('./tmp', splstr[1])
        with open('./tmp/'+splstr[1]) as f :
            channel = message.author.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(executable='C:/ffmpeg/bin/ffmpeg.exe', source='./tmp/lambs'))
    elif command=='s':
        channel = message.author.voice.channel
        if vc.is_playing():
            vc.disconnect()
    elif command=='l':
        await bot.login(discord_token)
    elif command=='q':
        # for vc in bot.voice_clients:
        #     await vc.disconnect()
        await bot.logout()
        
bot.run(discord_token)
