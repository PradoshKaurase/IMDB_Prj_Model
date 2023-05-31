from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin
import pickle
import numpy as np
app = Flask(__name__)

pickled_model = pickle.load(open('model.pkl','rb'))
cors = CORS(app, resources={r"/*": {"origins": "*"}})

def stringToInt(string):
    integer = 0
    #try seeing if string value given is already a number if so the output would be
    try:
        #means string value given is already a int
        integer = int(string)
    except:
        string = string.lower()
        for i in string:
            integer += ord(i)
    return integer

@app.route('/',methods=["GET"])
def test():
    return jsonify({'message' : 'it works!'})

@app.route('/movies',methods=["POST"])
def getData():
    """ director = {'director': request.get_json['director']}
    actor1 = {'actor1': request.get_json['actor1']}
    actor2 = {'actor2': request.get_json['actor2']}
    genre = {'genre': request.get_json['genre']}
    budget = {'budget': request.get_json['budget']} """

    data = request.get_json(force=True)
    print(data)
    prediction = pickled_model.predict([[stringToInt(data["exp1"].lower()),stringToInt(data["exp2"].lower()),stringToInt(data["exp3"].lower()),stringToInt(data["exp4"].lower()),data["exp5"]]])
    print(prediction)
    return jsonify({"prediction": float(prediction[0]/10)})
    

if __name__ == '__main__':
    app.run(port=8080,debug=True)
