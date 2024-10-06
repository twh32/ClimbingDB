import pytest
import pandas as pd
from climbing_app import load_data

# Test to check if data is loaded correctly
def test_load_data():
    # Load the data using the load_data function
    data = load_data()

    # Ensure the DataFrame is not empty
    assert not data.empty, "Data should not be empty"

    # Ensure required columns are present
    required_columns = ['Experience (yrs)', 'grade_numeric', 'success']
    for column in required_columns:
        assert column in data.columns, f"Missing required column: {column}"

# Test to check if the experience correlates with grade_numeric
def test_experience_grade_correlation():
    data = load_data()

    # Filter data to remove any null values
    filtered_data = data[['Experience (yrs)', 'grade_numeric']].dropna()

    # Assert there is some correlation between experience and grade_numeric
    correlation = filtered_data.corr().loc['Experience (yrs)', 'grade_numeric']
    assert correlation > 0, "Experience should have a positive correlation with grade_numeric"
