import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from flask import Flask, request, render_template, jsonify

application=Flask(__name__)
app=application

#import ridge regressor and standard scaler pickle
ridge_model = pickle.load(open('models/ridge.pkl','rb'))
standard_scaler = pickle.load(open('models/scaler.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        try:
            data = request.get_json()

            Temperature = float(data.get('Temperature'))
            RH = float(data.get('RH'))
            Ws = float(data.get('Ws'))
            Rain = float(data.get('Rain'))
            FFMC = float(data.get('FFMC'))
            DMC = float(data.get('DMC'))
            ISI = float(data.get('ISI'))
            Classes = float(data.get('Classes'))
            Region = float(data.get('Region'))

            new_data = [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
            new_data_scaled = standard_scaler.transform(new_data)

            result = ridge_model.predict(new_data_scaled)

            return jsonify({'prediction': result[0]})
        except  Exception as e:
            return jsonify({'error': str(e)}), 400

    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')