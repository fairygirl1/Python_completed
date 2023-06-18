from flask import Flask, render_template, redirect, url_for

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

if __name__ == '__main__':
    app.run()