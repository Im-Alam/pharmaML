from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import json
from typing import Dict
from dotenv import load_dotenv


load_dotenv(override=True)


app = FastAPI()

# Load supplier scores from a JSON file
def load_supplier_scores(file_path: str) -> Dict[str, float]:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
        #formating of data
        
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Supplier scores file not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding JSON file")

# Route to fetch supplier score
@app.get("/supplier-score", response_class=JSONResponse)
async def get_supplier_score():
    scores = load_supplier_scores("state/supplier_score.json")
    if scores is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return  scores



# Route to fetch product demand for the current week
@app.get("/product-demand", response_class=JSONResponse)
async def get_product_demand():
    try:
        with open('state/demand.json', 'r') as file:
            demand = json.load(file)
        
        with open('state/medicine_inventory.json', 'r') as file:
            prod_names = json.load(file)

        if demand is None:
            raise HTTPException(status_code=404, detail="Product not found")
        
        transformed_data = {}
        for product_id, demand_value in demand.items():
            product_name = prod_names.get(product_id, "Unknown Product")
            transformed_data[product_name] = {"demand": demand_value}


        return transformed_data
    
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Demand file not found")

    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Error decoding JSON file")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
