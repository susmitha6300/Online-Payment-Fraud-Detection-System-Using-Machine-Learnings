from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))   # make sure model.pkl is in same folder


# ---------- HOME PAGE ----------
@app.route('/')
def home():
    return render_template("home.html")


# ---------- PREDICT PAGE ----------
@app.route('/predict')
def predict():
    return render_template("predict.html")


# ---------- SUBMIT FORM ----------
@app.route('/submit', methods=['POST'])
def submit():
    try:
        step = float(request.form['step'])
        type_t = float(request.form['type'])
        amount = float(request.form['amount'])
        oldbalanceOrg = float(request.form['oldbalanceOrg'])
        newbalanceOrig = float(request.form['newbalanceOrig'])

        # Features order must match training order
        features = np.array([[step, type_t, amount, oldbalanceOrg, newbalanceOrig]])

        # Use probability instead of direct predict
        prob = model.predict_proba(features)[0][1]

        if amount > 100000 and newbalanceOrig == 0:
            result = 1      # Fraud
        elif amount < 5000 and (oldbalanceOrg - amount) == newbalanceOrig:
            result = 0      # Safe
        else:
            if prob > 0.40:
                result = 1  # Fraud
            else:
                result = 0  # Safe

        print("Fraud Probability:", prob)
        return render_template("submit.html", result=result)

    except Exception as e:
        return f"Error occurred: {e}"


# ---------- RUN APP ----------
if __name__ == "__main__":
    app.run(debug=True)
