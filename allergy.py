# functions for creating an allegry resource for FHIR and sending it to a FHIR server.
from fhir.resources.allergyintolerance import AllergyIntolerance
from fhir.resources.reference import Reference as Reference
from base2 import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir

def create_allergy(patient_id, substance, reaction, severity):
    allergy = AllergyIntolerance(patient=Reference(reference=f"Patient/{patient_id}"),
                                    code={"text": substance},
                                    reaction=[{"manifestation": [{"text": reaction}],
                                                "severity": severity,
                                                "substance": {"text": substance}}])
    return allergy


if __name__ == '__main__':
    allergy = create_allergy("45151396", "Yerba Mate", "Rash", "severe")
    allergy_id = send_resource_to_hapi_fhir(allergy, "AllergyIntolerance")
    if allergy_id:
        print(f"ID del recurso Allergy Intolerance creado: {allergy_id}")
        get_resource_from_hapi_fhir(allergy_id, "AllergyIntolerance")
