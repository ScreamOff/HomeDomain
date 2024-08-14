from flask import Blueprint, render_template

lotto_machine_bp = Blueprint('lotto', __name__, template_folder='templates')


@lotto_machine_bp.route('/lotto')
def lotto():
    return render_template('lotto.html')
