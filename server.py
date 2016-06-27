from flask import Flask, request, jsonify
from controllers import artistController, ImageController
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

        name = request.form['name']
        birth_year = request.form['birth_year']
        death_year = request.form['death_year']
        country = request.form['country']
        genre = request.form['genre']

        return_json = artistController.post_artists(name, birth_year, death_year, country, genre)

    elif request.method == 'GET':
        filed = request.args.get('filed', '')
        page = request.args.get('page', 1)

        return_json = artistController.get_artists(filed, page)
    elif request.method == 'DELETE':
        return_json = artistController.delete_all_artists()

    return jsonify(return_json)


@app.route("/artists/<int:artist_id>", methods=['GET', 'PUT', 'DELETE'])
def artist(artist_id):

    return_json = {}
    if request.method == 'PUT':

        name = request.form['name']
        birth_year = request.form['birth_year']
        death_year = request.form['death_year']
        country = request.form['country']
        genre = request.form['genre']

        return_json = artistController.update_artist(artist_id, name, birth_year, death_year, country, genre)

    elif request.method == 'GET':

        filed = request.args.get('filed', '')

        return_json = artistController.get_artist(filed, artist_id)
    elif request.method == 'DELETE':
        return_json = artistController.delete_artists(artist_id)

    return jsonify(return_json)


@app.route("/artists/<int:artist_id>/images", methods=['GET', 'POST', 'DELETE'])
def artist_images(artist_id):

    return_json = {}

    if request.method == 'POST':

        image_url = request.form['image_url']
        title = request.form['title']
        year = request.form['year']
        description = request.form['description']
        print(image_url, title, year, artist_id, description)

        return_json = ImageController.post_artist_image(image_url, title, year, artist_id, description)

    elif request.method == 'GET':
        filed = request.args.get('filed', '')
        page = request.args.get('page', 1)

        return_json = ImageController.get_artist_images(artist_id, filed, page)
    elif request.method == 'DELETE':

        return_json = ImageController.delete_artist_images(artist_id)

    return jsonify(return_json)


@app.route("/artists/<int:artist_id>/images/<int:image_id>", methods=['GET', 'PUT', 'DELETE'])
def artist_image(artist_id, image_id):

    return_json = {}

    if request.method == 'PUT':

        image_url = request.form['image_url']
        title = request.form['title']
        year = request.form['year']
        description = request.form['description']

        return_json = ImageController.put_artist_image(image_id, image_url, title, year, artist_id, description)

    elif request.method == 'GET':
        filed = request.args.get('filed', '')

        return_json = ImageController.get_artist_image(artist_id, image_id, filed)
    elif request.method == 'DELETE':

        return_json = ImageController.delete_artist_images(artist_id, artist_id)

    return jsonify(return_json)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8009)