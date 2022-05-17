from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import pandas as pd


class Amazon(Resource):
    def get(self):
        
        injury = request.args.get('injury')
        prexisting = request.args.get('prexisting')
        
        products = {
            "carpal": ['Product', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', "True"], 
            "bursitis": ['Product', 'https://www.youtube.com/watch?v=dQw4w9WgXcR', "False"],
            "tendonitis": ['Product', 'https://www.youtube.com/watch?v=dQw4w9WgXcT', "True"]
        }
        
        foundProdUrls = []
        
        
        for key, value in products.items():  
            if(injury == key):
                if(prexisting == value[2]):
                    foundProdUrls.append(value[1])

        
    
        

        
        data = {
            'injury': injury,
            'prexisting': prexisting,
            'products': foundProdUrls
        }
    
        
        return jsonify({'data': data})

        