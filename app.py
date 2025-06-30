from flask import Flask, render_template, request, redirect, url_for
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
    content = get_json(filename)
    terms = [i for i in content.keys()]
    defs = [i for i in content.values()]
    return render_template("file_editor.html", filename=filename, terms=terms, defs=defs)

@app.route("/submit/td", methods=["POST"])
def submit_td():
    filename = request.form.get("filename")
    print(filename)
    terms = request.form.getlist("terms")
    defs = request.form.getlist("defs")
    content = {}
    for i, term in enumerate(terms):
        content[term] = defs[i]
    print(content)
    dump_json(content, filename)
    return redirect(url_for("file_selection"))

if __name__ == "__main__":
    app.run(debug=True)