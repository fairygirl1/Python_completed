"""
Напишите скрипт который получает системный ввод от пользователя и выводит надпись "команда принята" если ввод начинается
с sys.in.
"""
import sys
import os

user_input = input('команда: ')

if user_input.lower().startswith('sys.in'):
    print('команда принята')
else:
    print('неверный ввод')