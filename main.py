from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class ModelData(BaseModel):
    document: str

class TestData(BaseModel):
    id:int
    message:str

@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.post("/predict")
# async def predict(d:ModelData):
#     nlp_updated = spacy.load('tmp_model')
#     results = nlp_updated(d.document)
#     data = {}
#     for ent in results.ents:
#         data.update({
#             ent.label_: ent.text
#         })
#     return data

@app.post("/test")
def test(data:TestData):
    return {'message':data.message,'id':data.id}