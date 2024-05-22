from flask import render_template
from flask_login import current_user

def list_patients(patients):
    return render_template("patients.html", patients=patients, title="Lista de patients", current_user=current_user,)

def create_patient():
    return render_template("create_patients.html", title="Creando patient....", current_user=current_user)

def update_patient(patient):
    return render_template("update_patient.html", title="Actualizar patient", patient=patient, current_user=current_user,)