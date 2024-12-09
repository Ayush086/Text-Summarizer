from fastapi import FastAPI 
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response 
from src.textSummarizer.pipeline.prediction import PredictionPipeline


text:str = "What is Text Summarization"
# initializin fast api
app = FastAPI()

# default route
@app.get("/", tags=['authentication'])
async def index():
    return RedirectResponse(url='/docs')


# training route
@app.get('/train')
async def training():
    try:
        os.system("python main.py")
        return Response("Training successfull !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")


# prediction route
@app.post('/predict')
async def predict_route(text):
    try:
        # prediction pipeline instance
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e


# running the application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
