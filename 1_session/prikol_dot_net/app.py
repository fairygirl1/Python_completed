# flask run

from flask import Flask, render_template, redirect, url_for, request, send_file, send_from_directory
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def index():
    text = "Доброе утро, Олег Юрьевич!"  
    image_url = "/static/1.jpeg"  
    button_text = "Погладить котика"  
    return render_template('morning.html', text=text, image_url=image_url, button_text=button_text)

@app.route('/preparation')
def preparation():
    text = "А это вот мы с ребятами к сессии готовились"  
    image_url = "/static/2.png"  
    button_text = "Молодцы"  
    return render_template('preparation.html', text=text, image_url=image_url, button_text=button_text)


@app.route('/eye')
def eye():
    text = "Мы пытаемся угадать, что будет на экзамене, не имея билетов"  
    image_url = "/static/3.jpg"  
    button_text = "Я все вовремя скинул"  
    return render_template('eye.html', text=text, image_url=image_url, button_text=button_text)


@app.route('/me')
def me():
    text = "Я в коворке в 2 ночи, когда вы скинули билеты"  
    image_url = "/static/4.jpeg"  
    button_text = "Спать надо в такое время"  
    return render_template('me.html', text=text, image_url=image_url, button_text=button_text)


@app.route('/sea')
def sea():
    text = "Мы на пляже, пока никто не заметил"  
    image_url = "/static/5.jpg"  
    button_text = "И вы 5 хотите?"  
    return render_template('sea.html', text=text, image_url=image_url, button_text=button_text)


@app.route('/aaa')
def aaa():
    text = "Ну я правда готовилась"  
    image_url = "/static/6.jpeg"  
    button_text = "..."  
    return render_template('aaa.html', text=text, image_url=image_url, button_text=button_text)


@app.route('/exam')
def exam():
    text = "Александра,"
    image_url = "/static/7.jpeg"
    button_text = "Конечно!"
    return render_template('exam.html', text=text, image_url=image_url, button_text=button_text)

@app.route('/redirect', methods=['GET'])
def redirect_page():
    redirect_url = 'https://www.programiz.com/python-programming/online-compiler/'

    with open('./python/exam.py', 'r') as file:
        file_content = file.read()

    response = requests.get(redirect_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    form = soup.find('form', {'id': 'editorForm'})
    if form is None:
        return "Форма не найдена"

    code_textarea = form.find('textarea', {'name': 'code'})
    if code_textarea is None:
        return "Текстовое поле для кода не найдено"

    code_textarea.string=file_content

    form_data = {input_field['name']: input_field.get('value', '') for input_field in form.find_all('input')}

    response = requests.post(redirect_url, data=form_data)

    return response.content

if __name__ == '__main__':
    app.run()