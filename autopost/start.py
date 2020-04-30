from telethon import functions, types
from telethon.sync import TelegramClient
from telethon import TelegramClient, events, sync
from settings import api_id, api_hash

client = TelegramClient("test", api_id, api_hash)
client.start()
print("STARTED")

@client.on(events.NewMessage(chats=["https://t.me/joinchat/AAAAAEY0fM9SbvX_gEEpKg", "https://t.me/joinchat/AAAAAE6Evnojp0kGxAltxQ", "http://t.me/joinchat/AAAAAFIGEJVBjoskE_TvuA", "https://t.me/COVID19_Ukraine", "https://t.me/joinchat/AAAAAEn9-GcgeevVb3Urtg"]))
async def normal_handler(event):
    if isinstance(event.chat, types.Channel):
        username = event.chat.username
    await client.send_message("https://t.me/joinchat/AAAAAEn9-GcgeevVb3Urtg", event.message)

client.run_until_disconnected()
