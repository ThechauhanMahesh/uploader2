from telethon import events
from main.plugins.uploader import upload
from main.plugins.downloader import weburl
from .. import bot
@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def u(event):
    edit = await event.reply("dl...")
    file = weburl(event.text)
    await edit.edit(uploading)
    await upload(file, event, edit)
