from flask import Flask
from flask_cors import CORS
from json_background import (dump_json,
                             get_json,
                             get_json_files,
                             temp_select_file)

app = Flask(__name__)

@app.route("/")
def index():
    pass
