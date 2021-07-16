# author: stanley
# crated date: 2021/6/25
# -*- coding:utf-8 -*-
from telethon import TelegramClient, events
import time

api_id = 6627460
api_hash = '27a53a0965e486a2bc1b1fcde473b1c4'
channel_id = 'https://t.me/hao1238'  # group identifier - channel id or joining link
substring = '海阔天空'

client = TelegramClient('PyMon', api_id, api_hash)


@client.on(events.NewMessage(chats=(channel_id)))
async def event_handler(event):
    print("="*20)
    # print('{}'.format(event))
    sender = await event.get_sender()
    # print(sender)
    print('time received: %s' % time.strftime("%H:%M:%S", time.localtime()))
    print('Sender: %s %s' % (sender.first_name, sender.last_name or ''))
    print(event.raw_text)
    if str(event.raw_text).lower().find(substring) != -1:
        print("海阔天空 message found")
        client.send_message(str(event.raw_text).lower() + '?')
        client.send_message(sender, 'sender')
        # winsound.Beep(2500, 20000)
    else:
        print("not go message")
    print("=" * 20)
    print("\n")
with client:
    client.start()
    client.run_until_disconnected()