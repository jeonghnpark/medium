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
    uploaded_file = request.files['file']

    if uploaded_file.filename != '':
        file_path = os.path.join(os.getcwd(),"file.csv")
        uploaded_file.save(file_path)
    return redirect(url_for('downloadFile'))


@app.route('/download')
def downloadFile():
    path = os.path.join(os.getcwd(), "file.csv")
    predictions = predict_iris(pd.read_csv(path, header=None))
    print(predictions)
    predictions.to_csv(os.path.join(os.getcwd(),'predictions.csv'), index=False)
    return send_file('predictions.csv', as_attachment=True)


app.run(host="localhost")

