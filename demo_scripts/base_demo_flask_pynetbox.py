from flask import Flask, request
import json
import pynetbox

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    if not request.is_json:
        return {"error": True, "message": "Request is not JSON"}

    data = request.get_json()
    if data["model"] != "device":
        return {"error": True, "message": "only device model is supported"}
    if data["event"] not in ["created", "updated"]:
        return {"error": True, "message": "only created and updated are supported"}

    device_id = data["data"]["id"]
    nb = pynetbox.api(
        'http://192.168.0.16:32768', # Your Netbox Host URL
        token='838e37d04d68a2a3eeb3a08904b27ac1d52004b0' # Your Netbox API Token generated in the Admin view
    )
    device_object = nb.dcim.devices.get(device_id)
    device_interfaces = nb.dcim.interfaces.filter(device=device_object)
    print(device_interfaces)
    return {"error": False}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)
