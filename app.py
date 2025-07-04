from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from json_background import (dump_json,
                             get_json,
                             get_json_files, create_json, delete_json)

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/file_selection/edit")
def file_selection_edit():
    files = get_json_files()
    return render_template("file-selection-edit.html", files=files)

@app.route("/file_selection/guess")
def file_selection_guess():
    files = get_json_files()
    return render_template("file-selection-guess.html", files=files)

@app.route("/file_create")
def file_create():
    return render_template("file_creator.html")

@app.route("/file_delete", methods=["POST"])
def file_delete():
    filename = request.form.get("filename")
    delete_json(filename)
    return redirect(url_for("file_selection_edit"))

@app.route("/guess")
def guess():
    return render_template("guess.html")

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
        if term == "" or defs[i] == "":
            continue
        content[term] = defs[i]
    print(content)
    dump_json(content, filename)
    return redirect(url_for("file_selection"))

@app.route("/submit/fc", methods=["POST"])
def submit_fc():
    filename = request.form.get("file_name")
    create_json(filename)
    return redirect(url_for("file_edit", filename=filename))

if __name__ == "__main__":
    app.run(debug=True)