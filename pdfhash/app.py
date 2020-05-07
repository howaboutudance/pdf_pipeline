from flask import Flask, request
import json
import hash_files

app = Flask(__name__)

with open("../config/revision.json", "r") as file:
    rev_dict = json.load(file)

@app.route("/")
def root():
    return {"status": "ok", **rev_dict}

@app.route("/metadata", methods=["GET"])
@app.route("/hash", methods=["GET"])
def get_upload_error():
    return {"status": "error", 
    "message": "invalid path or method", **rev_dict}, 404

@app.route("/hash", methods=["POST"])
def upload():
    if "file" in request.files:
        print(request.files["file"])
        return {"status": "ok", "data": hash_files.get_hashes([request.files["file"]]), **rev_dict}
    else:
        return {"status": "error", **rev_dict}

@app.route("/metadata", methods=["POST"])
def metadata():
    return {"status": "error", **rev_dict}