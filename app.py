# importing necessary libraries and functions
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model.pkl', 'rb')) # loading the trained model

@app.route('/') # Homepage
def home():
    return render_template('index1.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Fuel_Type = request.form['Fuel_Type']
        Seller_Type = request.form['Seller_Type']
        Transmission = request.form['Transmission']
        Owner = int(request.form['Owner'])
        Age_of_the_car = request.form['Age_of_the_car']

        prediction = model.predict(
            [[Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner, Age_of_the_car]])
        output = round(prediction[0], 2)
        return render_template('index1.html', prediction_text="You can sell your car at {} lakhs".format(output))
if __name__ == "__main__":
    app.run(debug=True)