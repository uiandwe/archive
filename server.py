from flask import Flask, request, jsonify
from controllers import artistController
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

    return_json = {}

    if request.method == 'POST':
        print("post")
    elif request.method == 'GET':
        filed = request.args.get('filed', '')
        page = request.args.get('page', 1)

        return_json = artistController.get_artists(filed, page)
    elif request.method == 'DELETE':
        return_json = artistController.delete_all_artists()

    # return_json = {'status': "success", 'data': '', 'message': "true"}
    return jsonify(return_json)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8009)