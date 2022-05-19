from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import pandas as pd


class VideoReq(Resource):
    def get(self):
        
        injury = request.args.get('injury')
        prexisting = request.args.get('prexisting')

        
        videos = {
            "carpal": ['Video', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', "True"], 
            "bursitis": ['Video', 'https://www.youtube.com/watch?v=dQw4w9WgXcR', "False"],
            "tendonitis": ['Video', 'https://www.youtube.com/watch?v=dQw4w9WgXcT', "True"]
        }
        
        foundVidUrls = []
        
        
        for key, value in videos.items():  
            if(injury == key):
                if(prexisting == value[2]):
                    foundVidUrls.append(value[1])

        
    
        

        
        data = {
            # 'injury': injury,
            # 'prexisting': prexisting,
            'videos: ': foundVidUrls
        }
    
        
        return jsonify(foundVidUrls)