from flask import Flask
from app.main.routes import main as main

#추가적인 모듈 / config 추가

app=Flask(__name__)

# 2번 라인에서 추가한 파일 연동해줌
app.register_blueprint(main)
