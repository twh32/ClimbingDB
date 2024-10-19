from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# Sample API endpoint to get data
@app.get("/")
def read_root():
    return {"message": "Welcome to the Climbing API"}

# Load your climbing data
try:
    data = pd.read_csv('merged_demographics.csv')
    # Ensure 'Max Grades' is treated as float
    data['Max Grades'] = data['Max Grades'].astype(float)
except Exception as e:
    print(f"Error loading the data: {e}")
    data = pd.DataFrame()  # fallback if there's an issue with loading

# API endpoint to get climbing data based on grade
@app.get("/climbers-by-grade/{grade}")
def get_climbers_by_grade(grade: float):
    if data.empty:
        raise HTTPException(status_code=500, detail="Climbing data not loaded")

    # Attempt to filter the data by numeric grade
    try:
        filtered_data = data[data['Max Grades'] == grade]

        if filtered_data.empty:
            raise HTTPException(status_code=404, detail=f"No climbers found for grade {grade}")

        return filtered_data.to_dict(orient='records')

    except KeyError as e:
        raise HTTPException(status_code=500, detail=f"Column not found: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
