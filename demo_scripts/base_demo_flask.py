from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    if not request.is_json:
        return {"error": True, "message": "Request is not JSON"}

    data = request.get_json()
    print(json.dumps(data, indent=4))
    return {"error": False}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)
