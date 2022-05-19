from flask import Flask, jsonify, request
from flask_restful import Resource, Api

class Root(Resource):
    def get(self):
        return jsonify({'message': 'welcome to root :)'})