config = open('config.py', 'w')
config.write(f'token = {input('Telegram bot token: ')}')
icon = input('Use default file icon or your own icon (D for default, path to file for use your local icon):')
if icon == 'D':
    config.write('icon = "bot.py"')
else:
  config.write(f'icon = {icon}')
