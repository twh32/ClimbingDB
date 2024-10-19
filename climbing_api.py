from fastapi import FastAPI, HTTPException
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("climbing_api")

app = FastAPI()

# Sample API endpoint to get data
@app.get("/")
def read_root():
    return {"message": "Welcome to the Climbing API"}

# Load your climbing data
try:
    data = pd.read_csv('merged_demographics.csv')
    # Ensure 'Max Grades' is treated as float and drop rows with missing grades
    data['Max Grades'] = pd.to_numeric(data['Max Grades'], errors='coerce')
    data = data.dropna(subset=['Max Grades'])  # Remove rows with missing grades
    logger.info("Data loaded successfully.")
except Exception as e:
    logger.error(f"Error loading the data: {e}")
    data = pd.DataFrame()  # fallback if there's an issue with loading

# API endpoint to get climbing data based on grade
@app.get("/climbers-by-grade/{grade}")
def get_climbers_by_grade(grade: float):
    if data.empty:
        logger.error("Climbing data not loaded")
        raise HTTPException(status_code=500, detail="Climbing data not loaded")

    try:
        # Log the grade being queried
        logger.info(f"Querying climbers with grade: {grade}")

        # Filter the data by numeric grade
        filtered_data = data[data['Max Grades'] == grade]

        if filtered_data.empty:
            logger.warning(f"No climbers found for grade {grade}")
            # Correctly raise a 404 error if no climbers match the grade
            raise HTTPException(status_code=404, detail=f"No climbers found for grade {grade}")

        return filtered_data.to_dict(orient='records')

    except KeyError as e:
        logger.error(f"KeyError occurred: {e}")
        raise HTTPException(status_code=500, detail=f"Column not found: {e}")
    except HTTPException as e:
        # Re-raise the HTTPException directly without wrapping it again
        raise e
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
