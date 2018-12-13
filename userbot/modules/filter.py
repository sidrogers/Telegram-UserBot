import sqlite3
from telethon import TelegramClient, events
from userbot import bot
from userbot import LOGGER, LOGGER_GROUP
import time
import asyncio

@bot.on(events.NewMessage(outgoing=True, pattern='^.rmfilters$'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^.rmfilters$'))
async def kick_marie_filter(e):
 if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
    await e.edit("```Will be kicking away all Marie filters.```")
    time.sleep(3)
    r = await e.get_reply_message()
    filters = r.text.split('-')[1:]
    for filter in filters:
        await e.reply('/stop %s' % (filter.strip()))
        await asyncio.sleep(0.3)
    await e.respond('/filter filters @baalajimaestro kicked them all')
    await e.respond("```Successfully purged Marie filters yaay!```\n Gimme cookies @baalajimaestro")
    if LOGGER:
          await bot.send_message(LOGGER_GROUP,"I cleaned all Marie filters at "+str(e.chat_id))
