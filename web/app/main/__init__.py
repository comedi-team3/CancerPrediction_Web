# main 화면을 위한 blueprint 작성
from flask import Blueprint

blueprint = Blueprint(
    'main_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)