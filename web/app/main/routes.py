from flask import Blueprint, request, render_template, redirect, url_for
from flask import current_app as current_app

#index 파일에 들어갔을 때 이름 어떻게 설정할지 결정
main = Blueprint('main',__name__,url_prefix='/')

#파일 내부에서의 경로
@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

