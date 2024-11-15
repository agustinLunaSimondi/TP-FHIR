#Cargar librerias propias del estandar FHIR
from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.contactpoint import ContactPoint
from fhir.resources.identifier import Identifier


# Crear el recurso FHIR de paciente con número de documento
def create_patient_with_identifier(family_name=None, given_name=None, birth_date=None, gender=None, phone=None, document_number=None):
    patient = Patient()
    
    # Agregar identifier (número de documento)
    if document_number:
        identifier = Identifier()
        identifier.system = "http://example.org/national-id"
        identifier.value = document_number
        patient.identifier = [identifier]
    
    # Agregar el nombre del paciente
    if family_name or given_name:
        name = HumanName()
        if family_name:
            name.family = family_name
        if given_name:
            name.given = [given_name]
        patient.name = [name]
    
    # Agregar la fecha de nacimiento
    if birth_date:
        patient.birthDate = birth_date

    # Agregar el género
    if gender:
        patient.gender = gender

    # Agregar información de contacto
    if phone:
        contact = ContactPoint()
        contact.system = "phone"
        contact.value = phone
        contact.use = "mobile"
        patient.telecom = [contact]

    return patient
