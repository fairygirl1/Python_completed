# flask run

from flask import Flask, render_template, redirect, url_for, request, send_file, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, 'python')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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


@app.route('/exam', methods=['GET', 'POST'])
def exam():
    text = "Александра,"
    image_url = "/static/7.jpeg"
    button_text = "Конечно!"

    if request.method == 'POST':
        # Проверяем, был ли отправлен файл
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        # Проверяем, что файл был выбран
        if file.filename == '':
            return redirect(request.url)

        # Сохраняем файл на сервере
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return render_template('exam.html', text=text, image_url=image_url, button_text=button_text)

@app.route('/download')
def download():
    filename = 'exam.py'
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
    app.run()