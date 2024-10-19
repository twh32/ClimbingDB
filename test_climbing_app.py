import pytest
from fastapi.testclient import TestClient
from climbing_api import app

# Set up a TestClient for the FastAPI app
client = TestClient(app)

# Test for the root endpoint
def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Climbing API"}

# Test to check if the climbers-by-grade endpoint works for a specific grade
@pytest.mark.parametrize("grade", [4, 5])
def test_climbers_by_grade(grade):
    response = client.get(f"/climbers-by-grade/{grade}")
    assert response.status_code == 200
    climbers = response.json()

    # Ensure climbers are returned for the given grade
    assert len(climbers) > 0, f"No climbers found for grade {grade}"

    # Check that all returned climbers have the correct grade
    for climber in climbers:
        assert climber["Max Grades"] == grade, f"Incorrect grade returned for climber: {climber}"

# Test for a non-existent grade (expecting a 404 error)
def test_climbers_by_grade_not_found():
    response = client.get("/climbers-by-grade/11")
    assert response.status_code == 404
    assert response.json() == {"detail": "No climbers found for grade 11.0"}
