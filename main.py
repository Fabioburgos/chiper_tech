from fastapi import FastAPI
from data import readDatabase
from sklearn.linear_model import LinearRegression
import numpy as np
from pydantic import BaseModel
from mlforecast import MLForecast

class Dayprediction(BaseModel):
    day : int

app = FastAPI()

@app.post('/prediction')
def predictionDays(day : Dayprediction):

    train = readDatabase().reset_index()[['ds', 'y']]
    train["unique_id"] = np.repeat(0, train.shape[0])
    
    model = LinearRegression(fit_intercept=False)
    
    forecast = MLForecast(
        models = model,
        freq = "D",
        lags = [7, 14, 30]
    )
    
    forecast.fit(train)
    prediction = forecast.predict(day.day)
    
    return {"Day predicted" : f"{prediction['ds']}",
            "sale prediction" : f"{prediction['LinearRegression']}"}
