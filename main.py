import sys
sys.path.append('/src')

from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import src.root as root
import src.videoReq as videoReq
import src.amazon as amazon

app = Flask(__name__)
api = Api(app)

api.add_resource(root.Root, '/')
api.add_resource(videoReq.VideoReq, '/videoReq')
api.add_resource(amazon.Amazon, '/amazon')

if __name__ == '__main__':
    app.run(debug = True)