from flask import Flask, render_template, redirect, request
from sklearn.externals import joblib

#__name__ == __main__
app = Flask(__name__)

model =joblib.load("model.pkl")


@app.route('/')
def hello():
    return render_template("index.html")
    # return "hello world"

@app.route('/', methods= ['POST'])
def marks():
    if request.method == 'POST':
        hours = float(request.form['hour'])
        marks= str(model.predict([[hours]])[0][0])

    return render_template("index.html", your_marks = marks)

if __name__ == '__main__':
    #app.debug = True
    app.run()