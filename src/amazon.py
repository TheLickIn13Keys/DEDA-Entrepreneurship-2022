from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import pandas as pd


class Amazon(Resource):
    def get(self):
        
        injury = request.args.get('injury')
        prexisting = request.args.get('prexisting')
        
        products = {
            "carpal": ['https://amz.run/5bs4', 'https://amz.run/5bs6', 'https://amz.run/5bs7'], 
            "bursitis": ['https://amz.run/5brw', 'https://amz.run/5brx'],
            "tendonitis": ['https://amz.run/5bs8', 'https://amz.run/5brx'],
        }
        
        foundProdUrls = []
        
        
        for key in products:  
            if(key == injury):
                for link in products.get(key):
                    foundProdUrls.append(link)


        
        data = {
            # 'injury': injury,
            # 'prexisting': prexisting,
            'products': foundProdUrls
        }
    
        
        return jsonify(foundProdUrls)

        