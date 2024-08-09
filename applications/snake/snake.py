from flask import Blueprint, render_template

snake_blueprint = Blueprint('snake', __name__, template_folder='templates')

@snake_blueprint.route('/snake')
def snake_game():
    """Wyświetla grę Snake."""
    return render_template('snake.html')
