import pickle
import requests
from flask import Flask, request


app = Flask(__name__)

#import model
model = open('./classifier.pkl', 'rb')
clf = pickle.load(model)


@app.route("/ping")
def hello_world():
    return "<h1>Pinging the model file</h1>"

@app.route("/predict", methods=["Post"] )
def prediction ():
    loan_req=request.get_json()

    if loan_req['Gender']=="Male":
        gender=0
    else:
        gender=1


    if loan_req['Married']=="Unmarried":
        marital_status=0
    else:
        marital_status=1


    applicant_income = loan_req['ApplicantIncome']
    loan_amt = loan_req['LoanAmount']/1000
    credit_history = loan_req['Credit_History']

    input_data=[[gender ,marital_status, applicant_income, loan_amt, credit_history]]

    prediction = clf.predict(input_data)

    if prediction == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return {"loan_approval_status: ": pred   }


@app.route("/get_params", methods=["Get"] )
def get_params ():
    parameters = {
                "Gender":"Male",
                "Married": "Unmarried",
                "ApplicantIncome": 50000,
                "Credit_History": 1.0,
                "LoanAmount": 500000
        }

    return parameters