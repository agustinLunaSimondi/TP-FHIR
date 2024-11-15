from patient2 import create_patient_with_identifier as create_patient
from base2 import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir, search_resource_in_hapi_fhir


if __name__ == "__main__":
    # Crear tres pacientes
    patient1 = create_patient("Smith", "John", "male", "1990-01-01", "DOC123")
    patient2 = create_patient("Doe", "James", "male", "1985-05-15", "DOC456")
    patient3 = create_patient("Brown", "Emily", "female", "2000-03-10", "DOC789")
    
    # Enviar pacientes a HAPI FHIR
    patient1_id = send_resource_to_hapi_fhir(patient1, "Patient")
    patient2_id = send_resource_to_hapi_fhir(patient2, "Patient")
    patient3_id = send_resource_to_hapi_fhir(patient3, "Patient")
    
    # Buscar un paciente por su ID en FHIR
    if patient1_id:
        print("\nBuscando al primer paciente por ID:")
        get_resource_from_hapi_fhir(patient1_id, "Patient")
    
    # Buscar todos los pacientes masculinos
    print("\nBuscando pacientes masculinos:")
    male_patients = search_resource_in_hapi_fhir("Patient", {"gender": "male"})
    if male_patients:
        for patient in male_patients:
            print(f"ID: {patient['id']}, Nombre: {patient.get('name', 'Sin nombre')}")
