from flask import Flask, render_template, url_for
from applications.file_uploader.uploader import uploader_blueprint
from applications.calculator.calculator import calculator_blueprint
from applications.notes.notes import notes_blueprint

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024 * 1024  # 1 GB

# Rejestracja blueprintów
app.register_blueprint(uploader_blueprint, url_prefix='/upload')
app.register_blueprint(calculator_blueprint, url_prefix='/calculator')
app.register_blueprint(notes_blueprint, url_prefix='/notes')
@app.route('/')
def index():
    applications = [
        {'name': 'Upload', 'icon': 'upload_icon.png', 'url': url_for('uploader_blueprint.file_uploader')},
        {'name': 'Calculator', 'icon': 'calculator_icon.png', 'url': url_for('calculator.calculator')},
        {'name': 'Notes', 'icon': 'notes_icon.png', 'url': url_for('notes.notes')}
        # Możemy tutaj dodawać kolejne aplikacje
    ]
    return render_template('index.html', applications=applications)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
