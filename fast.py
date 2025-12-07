# Simple FastAPI Hospital Management System.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title=" Welcome To Simple Hospital Management API")

# -----------------------------
# Pydantic Model
# -----------------------------
class Patient(BaseModel):
    id: int
    name: str
    age: int
    disease: str

# In-memory "database"
patients_db: List[Patient] = []

#...............
from fastapi import FastAPI

app = FastAPI( title="Hospital Management System " )

# -----------------------------
# Create Patient
# -----------------------------
@app.post("/patients/", response_model=Patient)
def create_patient(patient: Patient):
    # Check duplicate ID
    for p in patients_db:
        if p.id == patient.id:
            raise HTTPException(status_code=400, detail="Patient ID already exists")
    patients_db.append(patient)
    return patient

# -----------------------------
# Get All Patients
# -----------------------------
@app.get("/patients/", response_model=List[Patient])
def get_patients():
    return patients_db

# -----------------------------
# Get Single Patient
# -----------------------------
@app.get("/patients/{patient_id}", response_model=Patient)
def get_patient(patient_id: int):
    for p in patients_db:
        if p.id == patient_id:
            return p
    raise HTTPException(status_code=404, detail="Patient not found")

# -----------------------------
# Update Patient
# -----------------------------
@app.put("/patients/{patient_id}", response_model=Patient)
def update_patient(patient_id: int, updated: Patient):
    for index, p in enumerate(patients_db):
        if p.id == patient_id:
            patients_db[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Patient not found")

# -----------------------------
# Delete Patient
# -----------------------------
@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):
    for p in patients_db:
        if p.id == patient_id:
            patients_db.remove(p)
            return {"message": "Patient deleted"}
    raise HTTPException(status_code=404, detail="Patient not found")


