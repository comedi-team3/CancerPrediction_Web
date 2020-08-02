from app.main import blueprint
from flask import Blueprint, request, render_template, redirect, url_for
from flask import current_app as current_app
from jinja2 import TemplateNotFound

#파일 내부에서의 경로
@blueprint.route('/index')
def main():
    return render_template('index.html')

@blueprint.route('/<template>')
def route_template(template):
    try:
        if not template.endswith('.html'):
            template += '.html'
        return render_template(template)
    except Exception as ex:
        print(ex)