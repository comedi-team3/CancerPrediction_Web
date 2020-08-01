from app import app

if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as ex:
        print(ex)