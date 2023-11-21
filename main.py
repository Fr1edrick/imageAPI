import os 
from predictor import Predictor
from responseSquema import ResponseSquema
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

app = FastAPI(title='Tools API predictor')

origins = ['*']
methods = ['*']
headers = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers
)

#Endpoints
@app.post('/predictImage', response_model=ResponseSquema)
def predicImage( file: UploadFile = File(...) ):
    """Params:
    \n``File`` => request body - UploadFile
    \nReturn prediction response
    \nThis function return ``response`` fron prediction
    """
    prediction = Predictor.PredictImageLoaded( file )
    return prediction

@app.get('/ping')
def ping():
    return { 'message:': 'Sucesfully Pong!'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    run(app, host='0.0.0.0', port= port)