from fastapi import FastAPI
from pydantic import BaseModel
from comparator import compare_prices

app = FastAPI()

class Query(BaseModel):
    country: str
    query: str

@app.post("/search")
def search(input: Query):
    results = compare_prices(input.country, input.query)
    return sorted(results, key=lambda x: float(x["price"]))
