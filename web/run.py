from flask import Flask, render_template, request
#from flask_mysqldb import MySQL
#from config import DB_CONFIG
from werkzeug.utils import secure_filename

app = Flask(__name__)

# app.config['MYSQL_HOST'] = DB_CONFIG['host']
# app.config['MYSQL_USER'] = DB_CONFIG['user']
# app.config['MYSQL_PASSWORD'] = DB_CONFIG['password']
# app.config['MYSQL_DB'] = DB_CONFIG['database']

# mysql = MySQL(app)
        

@app.route('/')
def main():
    # cur = mysql.connection.cursor()
    # resultValue = cur.execute("SELECT * FROM image")
    # if resultValue > 0:
    #     res = cur.fetchall()
    # return render_template('index.html', resData=res)
  
    return render_template('/home/index.html')

@app.route('/index')
def index():
    return render_template('/home/index.html')

@app.route('/<template>')
def route_template(template):
    if not template.endswith('.html'):
        template+='.html'
    if "performance" in template:
        return render_template('/home/'+template)
    if "basic" or "buttons" or "chartjs" or "dropdowns" or "tpography" in template:
        return render_template(template)

    return render_template('/cancer_result/'+template)

# @app.route('/<template>')
# def route_template(template):
#     if not template.endswith('.html'):
#         template+='.html'
#     return render_template(template)


@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      #저장할 경로 + 파일명
      f.save(secure_filename(f.filename))
      return 'uploads 디렉토리 -> 파일 업로드 성공!'


# @app.route('/test', methods=['GET','POST'])
# def test():
#     if request.method == 'POST':
#         url = request.form['url']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO image VALUES (%s,%s)",("num2",url))

#         mysql.connection.commit()

#         cur.close()
#     return render_template('test.html',url=url)


if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as ex:
        print(ex)