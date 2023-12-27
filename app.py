from flask import Flask,render_template,request
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder


model = pickle.load(open('classifier1.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    Nitrogen = (request.form.get('Nitrogen'))
    Phosphorus = (request.form.get('Phosphorus'))
    Potassium = (request.form.get('Potassium'))
    pH = float(request.form.get('pH'))
    Rainfall = (request.form.get('Rainfall'))
    Temperature = (request.form.get('Temperature'))
    

    # prediction
    result = model.predict(np.array([[Nitrogen,Phosphorus,Potassium,pH ,Rainfall ,Temperature]]))
    if(result == 0):
        result = "12:32:16 NPK"	
    elif(result == 1):
        result = "13:32:26 NPK"
    elif(result == 2):
        result = "DAP"
    elif(result == 3):
        result = "Magnesium Sulphate"




    return render_template('index.html',result=str(result))


if __name__ == '__main__':
    app.run(debug=True)