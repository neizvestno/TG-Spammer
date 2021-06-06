from pyrogram import Client, filters
from pyrogram.types import Message, Chat
from pyrogram.errors import FloodWait
import time
from time import sleep
from random import randint

app = Client("my_account")

def outtext(l):
	s = l[1:len(l)-1]
	return ' '.join(s)
	
@app.on_message(filters.command("help", prefixes=".") & filters.me)
def help(_, msg):
	helpm = "☆Инструкция пользования☆\n Чтоб отправлять сообщения в чате котором пишите:\n`.sp r [текст] [количество]`\n Для того чтоб отправить определенному пользователю:\n`.sp [id, номер, username] [текст] [количество]`\nНа этом всё. Советую не злоупотреблять этим инструментом, так как тг заблокирует аккаунты которые отправляют подозрительные запросы :)"
	app.send_message(msg.chat.id, helpm)

#spamchik :)
@app.on_message(filters.command("sp", prefixes=".") & filters.me)
def type(_, msg):
	orig_text = msg.text.split(".sp ", maxsplit=1)[1]
	t = orig_text.split()
	n = int(t[len(t)-1]) + 1
	text = outtext(t)
	cl = t[0]
	app.delete_messages(msg.chat.id, msg.message_id)
	if cl == "r":
		for i in range(1, n):
			sleep(0.05)
			app.send_message(msg.chat.id, text)
	else:
		for i in range(1, n):
			sleep(0.05)
			app.send_message(cl, text)

app.run()