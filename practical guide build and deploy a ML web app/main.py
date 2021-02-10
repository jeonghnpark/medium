from flask import Flask, render_template, request, redirect, url_for, send_file
import os


from iris_model import predict_iris

import pandas as pd

app = Flask('what')


app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def uploadFiles():
    uploaded_file=request.files['file']

    if uploaded_file.filename !='':
        file_path=("file.csv")
        uploaded_file.save(file_path)
    return redirect(url_for('downloadFile'))

@app.route('/download')
def downloadFile():
    path="file.csv"
    predictions=predict_iris(pd.)

app.run(host="localhost")

