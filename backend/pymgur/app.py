from flask import Flask, send_file, flash, request, abort, jsonify
from flask_cors import CORS
from os import listdir
from sys import argv

APP = Flask(__name__, static_url_path='/')
CORS(APP)

APP.config['UPLOAD_FOLDER'] = './static'


@APP.route('/<filename>', methods=['GET'])
def get_image(filename):
    try:
        return send_file('./static/{}'.format(filename), mimetype='image/gif')
    except FileNotFoundError:
        return abort(400, 'File not found')


@APP.route('/', methods=['POST'])
def post_image():
    try:
        image = request.files['image']
    except KeyError:
        return abort(400, 'No file sent')

    filename = image.filename
    extension = filename.split('.')[1]
    if extension not in ['jpg', 'jpeg', 'png', 'bmp', 'gif']:
        return abort(400, 'Bad file name')

    if filename in listdir('./static'):
        return abort(400, 'File already exists')

    image.save('./static/{}'.format(filename))

    return jsonify({'img_url': request.base_url+filename})


if __name__ == '__main__':
    if argv[1]:
        APP.run(host='0.0.0.0', port=int(argv[1]))
    else:
        APP.run()
