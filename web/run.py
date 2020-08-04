from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from config import DB_CONFIG

app = Flask(__name__)

app.config['MYSQL_HOST'] = DB_CONFIG['host']
app.config['MYSQL_USER'] = DB_CONFIG['user']
app.config['MYSQL_PASSWORD'] = DB_CONFIG['password']
app.config['MYSQL_DB'] = DB_CONFIG['database']

mysql = MySQL(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/test', methods=['GET','POST'])
def test():
    if request.method == 'POST':
        url = request.form['url']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO image VALUES (%s,%s)",("num2",url))

        mysql.connection.commit()

        cur.close()
    return render_template('test.html',url=url)
        

if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as ex:
        print(ex)