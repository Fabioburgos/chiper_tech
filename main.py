from fastapi import FastAPI
from data import readDatabase
from pydantic import BaseModel
from mlforecast import MLForecast
from sklearn.linear_model import LinearRegression

import numpy as np


class Dayprediction(BaseModel):
    """Pydantic model representing the request body for the prediction endpoint."""
    day : int

app = FastAPI()

@app.post('/prediction')
def predictionDays(day : Dayprediction):
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
    model = LinearRegression(fit_intercept=False)
    
    # Initialize MLForecast object with model, frequency, and lags.
    forecast = MLForecast(
        models = model,
        freq = "D",
        lags = [7, 14, 30]
    )
    
    # Fit model to training data.
    forecast.fit(train)
    
    # Predict sales for the input day.
    prediction = forecast.predict(day.day)
    
    # Return a dictionary containing the predicted day and sales.
    return {"Day predicted" : f"{prediction['ds']}",
            "Sale prediction" : f"{prediction['LinearRegression']}"}
