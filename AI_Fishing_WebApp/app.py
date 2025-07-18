from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from illegal_fishing_ai import run_detection

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    result_path = None
    status_text = None

    if request.method == 'POST':
        file = request.files.get('image')
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            result_path, status_text = run_detection(filepath)
        else:
            status_text = "⚠️ No image uploaded."

    return render_template('index.html', result_path=result_path, status_text=status_text)

if __name__ == '__main__':
    import webbrowser
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=False)
