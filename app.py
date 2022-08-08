from flask import Flask,render_template,request
import pickle

app=Flask(__name__)
model=pickle.load(open("palmerpenguin.pkl",'rb'))

@app.route('/')
def index():
    result=' '
    return render_template('index.html',**locals())


@app.route('/predict',methods=['POST','GET'])
def predict():
    culmen_length=float(request.form['culmen_length'])
    culmen_depth=float(request.form['culmen_depth'])
    flipper_length=float(request.form['flipper_length'])
    body_mass=float(request.form['body_mass'])
    result=model.predict([[culmen_length,culmen_depth,flipper_length,body_mass]])[0]
    return render_template('index.html',**locals())

if __name__=="__main__":
    app.run(debug=True)