from flask import Flask, request, jsonify
from controllers import DbController, artistController
dc = DbController.DbController()
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST', 'DELETE', 'PUT'])
def index():
    if request.method == 'POST':
        print("post")
    elif request.method == 'GET':
        print("GET")
    elif request.method == 'DELETE':
        print("DELETE")
    elif request.method == 'PUT':
        print("PUT")

    return_json = {'status': "success", 'data': '', 'message': "true"}
    return jsonify(return_json)


@app.route("/artists", methods=['GET', 'POST', 'DELETE'])
def artists():
    if request.method == 'POST':
        print("post")
    elif request.method == 'GET':
        filed = request.args.get('filed', '')
        page = request.args.get('page', 1)

        return jsonify(artistController.get_artists(dc, filed, page))

    elif request.method == 'DELETE':
        print("DELETE")

    return_json = {'status': "success", 'data': '', 'message': "true"}
    return jsonify(return_json)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8009)