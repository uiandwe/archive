from flask import Flask, request, jsonify


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

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8009)