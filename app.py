from flask import Flask, render_template, request, redirect
import os
import random
import shutil

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def hello_world():
    if request.method == "GET":
        name = random.choice(os.listdir('static'))
        return render_template('index.html', path=name)
    if request.method == "POST":
        if request.form['captcha'] != '':
            file = request.form['path']
            shutil.move(f'static/{file}', f'finished/{request.form["captcha"]}.jpg')
        return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
