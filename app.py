from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("house_price_model.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

print("MODEL LOADED")
print("FEATURES:", features)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        print("POST REQUEST RECEIVED")
        print("FORM DATA:", request.form)

        values = [float(request.form[f]) for f in features]
        print("VALUES:", values)

        prediction = model.predict([values])[0]
        print("PREDICTION:", prediction)

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
