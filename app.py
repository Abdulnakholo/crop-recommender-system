from flask import Flask, render_template , request
import pickle
import sklearn
app = Flask("__name__")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/" , methods = ["POST"])
def sub():
    if request.method == 'POST':
        model = pickle.load(open("models/model.pkl" , "rb"))
        N = request.form["Nitrogen"]
        P = request.form["Phosphorous"]
        K = request.form["Potassium"]
        temp = request.form["temperature"]
        rh = request.form["Relative Humidity(%)"]
        ph = request.form["ph"]
        rf = request.form["rainfall(mm)"]

        prediction = model.predict([[N,P,K,temp,rh,ph,rf]])


    return render_template("index.html" , prediction = prediction)

if __name__ == "__main__":
    app.run(debug = True)