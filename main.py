
from flask import Flask, jsonify, request, render_template
import json
import random



app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

@app.route('/', methods = ['GET'])
def home():
    with open('scrapped_data.json', 'r') as myfile:
        data = json.load(myfile)
    display_data = json.dumps(data, sort_keys = True, indent = 4, separators = (',', ': '))
    return jsonify(data)

@app.route('/data/<srno>', methods = ['GET'])
def search(srno):
    with open('scrapped_data.json', 'r') as myfile:
        data = json.load(myfile)
    
        if srno in data:
            return jsonify(data[srno])
        else:
            maxlen = len(data) - 1
            Error_data = {"Error" :  f"Please Search for another number between 1 to {maxlen}"} 
            return jsonify(Error_data)
        


if __name__ == "__main__":
    
    app.run(debug = True)
