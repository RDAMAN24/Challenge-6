import numpy as np
import pandas as pd
from flask import Flask, render_template,request
import pickle

app=Flask(__name__,template_folder='templates')

model = pickle.load(open('RandomForestClassifier_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    features_name = ['mean smoothness', 'mean compactness', 'mean symmetry',
       'mean fractal dimension', 'texture error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error', 'fractal dimension error',
       'worst texture', 'worst area', 'worst smoothness', 'worst compactness',
       'worst concavity', 'worst concave points', 'worst symmetry',
       'worst fractal dimension']
    
    df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict(df)
    
    if output == 0:
        res_val= "* breast cancer *"
    else:
        res_val= "no breast cancer"
        

    return render_template('index.html', prediction_text='Patient has {}'.format(res_val))

if __name__ == "__main__":
    app.run(debug=True)