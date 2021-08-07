from flask import Flask,render_template,request
from PredictDiabates import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')


@app.route("/predict")
def Predict():
    return render_template('index.html')


@app.route("/prediction",methods = ['POST'])
def Prediction():
    l = []
    if request.method == 'POST':
        
        l.append(request.form['age'])
        l.append(request.form['gender'])
        l.append(request.form['polyuria'])
        l.append(request.form['polydipsia'])
        l.append(request.form['wl'])
        l.append(request.form['weakness'])
        l.append(request.form['Polyphagia'])
        l.append(request.form['gt'])
        l.append(request.form['vb'])
        l.append(request.form['itching'])
        l.append(request.form['irritable'])
        l.append(request.form['heal'])
        l.append(request.form['muscle'])
        l.append(request.form['stifness'])
        l.append(request.form['alopecia'])
        l.append(request.form['obecity'])
        
        pd = PredictDiabetes(l)
        if pd.predict_diab() > 0.68:
            return render_template("pred.html",prediction = "You have High risk of having Diabetes. Your probability of being diabetic is "+str((pd.predict_diab())*100)+"%")
        else:
            return render_template("pred.html",prediction = "You have Low risk of having Diabetes. Your probability of being diabetic is "+str(pd.predict_diab()*100)+"%")
            



if __name__ == "__main__":
    app.run()