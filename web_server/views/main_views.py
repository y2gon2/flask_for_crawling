from flask import Blueprint, request, render_template
from web_server import db_controller
from web_server.stock_crawling import stock_crawling
from web_server.mailing import send
from web_server.file_control import save_file

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('menu.html')

@bp.route('/stock', methods=['POST'])
def stock():
    email = request.form['email']
    stock_code = request.form['stock_code']

    if len(stock_code) != 6:
        return '종목 코드 6자리를 모두 입력해주시기 바랍니다.'
    else:
        result = stock_crawling(stock_code)

        if result.get('code') == 'None':
            return '입력하신 종목 코드에 대한 주식을 찾을수 없습니다. 코드를 재학인 해주시기 바랍니다.'
        else:
            code = result.get('code')
            save_file(result, code)
            send(email, code)
            return '입력하신 메일 주소로 해당 파일을 송부하였습니다. 이용해 주셔서 감사합니다.'


@bp.route('/add')
def add():
    return render_template('add.html')

@bp.route('/del')
def delete():
    return render_template('del.html')

@bp.route('/del_all')
def del_all():
    return render_template('del_all.html')

@bp.route('/end', methods=['POST'])
def success():
    mode = request.form['mode']
    email = request.form['email']
    word = request.form['word']
    time = request.form['time']
    print(time)

    if db_controller.identify_email(email):
        if mode == "add":
            db_controller.push_word(email, word, time)
        elif mode == "del":
            db_controller.pull_word(email, word)
        else:
            db_controller.del_email(email)
    else:
        if mode == "add":
            db_controller.new_email(email, word, time)
        else:
            return '입력하신 e-mail 대한 기존 등록 정보가 없습니다.'

    return '요청이 성공적으로 등록되었습니다. 이용해주셔서 감사합니다.'

