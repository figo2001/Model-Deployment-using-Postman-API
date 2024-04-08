from flask import Flask,request, jsonify
import joblib
import pandas as pd

# 1. Create Fask Apllication
app=Flask(__name__)


# 2. Connect Post API Call --> Predict() function

## a) http://localhost:5000/predict
## b) It means if you go to predict (http://localhost:5000/predict), then you should be able to post some information a ## api call
@app.route('/classification',methods=['POST'])  
def classification():

    # Get the JSON request
    feature_data=request.json

    # Convert the JSON into pandas df (col names)
    df=pd.DataFrame(feature_data)
    df=df.reindex(columns=col_names)

    # Predict
    prediction =list(model.predict(df))
    
    
    return jsonify({'prediction': str(prediction)})

    
# 3.Load my Model and Load Column names
if __name__ == '__main__':

    model=joblib.load('logistc_model.pkl')
    col_names=joblib.load('col_names.pkl')

    app.run(debug=True)

