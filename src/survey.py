from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import pandas as pd


class Survey(Resource):
    def get(self):
        
        injury = request.args.get('injury')
        prexisting = request.args.get('prexisting')
        location = request.args.get('location')
        level = request.args.get('level')
        comment = request.args.get('comment')
    
        diagnosis = "NA"

        

        
        data = {
            'injury': injury,
            'prexisting': prexisting,
            'location': location,
            'level': level,
            'comment': comment,
            'diagnosis': diagnosis
        }
    
        
        return jsonify({'data': data})

        