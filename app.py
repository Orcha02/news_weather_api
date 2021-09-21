#!/usr/bin/python3
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def submit():
    text = '{}'.format(request.form['city'])
    # Proceso
    return render_template('index.html', news=text, weather=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
