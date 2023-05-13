from fastapi import FastAPI
from fastapi.responses import JSONResponse
from data import readDatabase
from mlforecast import MLForecast
from sklearn.linear_model import Lasso

import numpy as np

app = FastAPI()

@app.get("/prediction/{predday}/")
def predictionDays(predday : int):
    """
    Endpoint for predicting sales for a given day using machine learning.

    Args:
        day (Dayprediction): The input day to predict sales for.

    Returns:
        A dictionary containing the predicted day and sales.
    """
    # Read training data and add unique identifier.
    train = readDatabase().reset_index()[['ds', 'y']]
    train["unique_id"] = np.repeat(0, train.shape[0])
    
    # Initialize linear regression model.
    model = Lasso(fit_intercept=False)
    
    # Initialize MLForecast object with model, frequency, and lags.
    forecast = MLForecast(
        models = model,
        freq = "D",
        lags = [7, 14, 30]
    )
    
    # Fit model to training data.
    forecast.fit(train)
    
    # Predict sales for the input day.
    prediction = forecast.predict(predday)
    
    # Procesing the dataframe for the output
    prediction["ds"] = prediction["ds"].astype(str)
    prediction = prediction.drop(['unique_id'], axis=1)
    prediction = prediction.rename(columns = {'ds' : 'Day predicted',
                                              'Lasso' : 'Sales Prediction'})
    
    # Return a dictionary containing the predicted day and sales.
    return JSONResponse(content = prediction.to_dict())
