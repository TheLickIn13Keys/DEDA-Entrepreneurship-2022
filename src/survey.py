from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import pandas as pd


class Survey(Resource):
    def get(self):

        def makeDiagnosis(location, level, comment, carpal_symptoms, bursitis_symptoms, tendonitis_symptoms):
            if(int(level) > 7):    

                if(location == "wrist"):
                    for problem in comment.split(" "):
                        if(problem in carpal_symptoms):
                            return "There is a good chance you have carpal tunnel, please go back to page 1, click yes, and type in carpal"
                    return "You most likely don't have an RSI injury and your " + location + " is just sore, but you might still develop RSI in the future. This video will show you how to prevent an RSI injury fron developing: https://youtu.be/fdD7CgN5FGg."

                elif(location == "elbow"):
                    for problem in comment.split(" "):
                        if(problem in tendonitis_symptoms):
                            return "There is a good chance you have tendonitis , please go back to page 1, click yes, and type in tendonitis"
                    return "You most likely don't have an RSI injury and your " + location + " is just sore, but you might still develop RSI in the future. This video will show you how to prevent an RSI injury fron developing: https://youtu.be/fdD7CgN5FGg."

                elif(location == "knee"):
                    for problem in comment.split(" "):
                        if(problem in bursitis_symptoms):
                            return "There is a good chance you have bursitis , please go back to page 1, click yes, and type in bursitis"
                    return "You most likely don't have an RSI injury and your " + location + " is just sore, but you might still develop RSI in the future. This video will show you how to prevent an RSI injury fron developing: https://youtu.be/fdD7CgN5FGg."
                elif(location == "shoulder"):
                    for problem in comment.split(" "):
                        if(problem in tendonitis_symptoms):
                            return "There is a good chance you have tendonitis , please go back to page 1, click yes, and type in tendonitis"
                    return "You most likely don't have an RSI injury and your " + location + " is just sore, but you might still develop RSI in the future. This video will show you how to prevent an RSI injury fron developing: https://youtu.be/fdD7CgN5FGg."

                else:
                    return "There typically isn't an RSI injury that is found in the " + location + ", but if there is a lot of pain, you should consult a doctor, as you could have another form of injury."
            else:
                return "You most likely don't have an RSI injury and your " + location + " is just sore, but you might still develop RSI in the future. This video will show you how to prevent an RSI injury fron developing: https://youtu.be/fdD7CgN5FGg."

        
        injury = request.args.get('injury')
        prexisting = request.args.get('prexisting')
        location = request.args.get('location')
        level = request.args.get('level')
        comment = request.args.get('comment')

        carpal_symptoms = ["weakness", "numb", "numbness", "swollen", "swelling", "burning", "tingling"]
        bursitis_symptoms = ["can't move", "movement", "motion", "swelling", "redness", "red", "swollen"]
        tendonitis_symptoms = ["golf", "tennis", "achilles", "jump", "swimming", "swim", "inflamation", "inflamed", "swollen", "swelling"]
    
        diagnosis = makeDiagnosis(location, level, comment, carpal_symptoms, bursitis_symptoms, tendonitis_symptoms)
    
        
        return jsonify(diagnosis)
    

        
