from flask import Flask, request, jsonify, make_response
from platformApp import platform
import json

app = Flask(__name__)


@app.route("/")
@app.route("/index")
@app.route("/<path:url>")
def home(url=None):
    try:
        return make_response(platform.index(), 200)
    except Exception as e:
        print("Error in home view:", str(e))
        return make_response("An error occurred while processing the request.", 500)


@app.route("/perform-action", methods=["POST"])
def perform_action():
    try:
        action_data = request.get_json(force=True)
        if action_data is None:
            return make_response("Invalid JSON", 400)
        result = platform.perform_action(
            action_data.get("Action Name"),
            action_data.get("payload"),
            action_data.get("Plugin Name") or None,
        )
        return make_response(result, 200)
    except (json.JSONDecodeError, TypeError):
        return make_response("Invalid JSON", 400)
    except Exception:
        return make_response("An error occurred while processing the request.", 500)


@app.route("/plugins", methods=["GET"])
def get_plugins():
    try:
        request_action_name = request.args.get("Action Name")
        print("Received request for plugins with Action Name:", request_action_name)
        plugins = platform.get_plugins(request_action_name)
        print("Returning plugins:", plugins)
        json_plugins = [plugin.to_dict() for plugin in plugins]
        return jsonify(json_plugins)
    except Exception as e:
        print("Error in get_plugins:", str(e))
        return jsonify({"error": "An error occurred while fetching plugins."}), 500


if __name__ == "__main__":
    app.run(debug=True, port=8000)