from app import create_app
from flask_mysqldb import MySQL

app=create_app()

mysql = MySQL(app)


if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as ex:
        print(ex)