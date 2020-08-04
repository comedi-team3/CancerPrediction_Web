#from app import create_app
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as ex:
        print(ex)