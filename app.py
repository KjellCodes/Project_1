from flask import Flask, render_template
from flask_cors import CORS
from json_background import (dump_json,
                             get_json,
                             get_json_files)

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/file_selection")
def file_selection():
    files = get_json_files()
    return render_template("file_selection.html", files=files)

@app.route("/file_edit/<string:filename>")
def file_edit(filename):
    return render_template("file_editor.html", filename=filename)

if __name__ == "__main__":
    app.run(debug=True)