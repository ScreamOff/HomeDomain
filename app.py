from flask import Flask, render_template, url_for
from applications.file_uploader.uploader import uploader_blueprint
from applications.calculator.calculator import calculator_blueprint
from applications.notes.notes import notes_blueprint
from applications.planner.planner import planner_blueprint
from applications.snake.snake import snake_blueprint
from applications.file_downloader.downloader import downloader_blueprint
from applications.lotto import lotto_machine_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024 * 1024  # 1 GB

# Rejestracja blueprintów
app.register_blueprint(downloader_blueprint, url_prefix='/downloader')
app.register_blueprint(uploader_blueprint, url_prefix='/upload')
app.register_blueprint(calculator_blueprint, url_prefix='/calculator')
app.register_blueprint(notes_blueprint, url_prefix='/notes')
app.register_blueprint(planner_blueprint, url_prefix='/planner')
app.register_blueprint(snake_blueprint, url_prefix='/snake')
app.register_blueprint(lotto_machine_bp, url_prefix='/lotto')


@app.route('/')
def index():
    applications = [

        {'name': 'Upload', 'icon': 'upload_icon.png', 'url': url_for('uploader_blueprint.file_uploader')},
        {'name': 'Calculator', 'icon': 'calculator_icon.png', 'url': url_for('calculator.calculator')},
        {'name': 'Notes', 'icon': 'notes_icon.png', 'url': url_for('notes.notes')},
        {'name': 'Planner', 'icon': 'planner_icon.png', 'url': url_for('planner.show_planner')},
        {'name': 'Snake', 'icon': 'snake_icon.png', 'url': url_for('snake.snake_game')},
        {'name': 'Download', 'icon': 'download_icon.png', 'url': url_for('downloader.download_page')},
        {'name': 'Lotto', 'icon': 'lotto_icon.png', 'url': url_for('lotto.lotto')}
        # Możemy tutaj dodawać kolejne aplikacje
    ]
    return render_template('index.html', applications=applications)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
