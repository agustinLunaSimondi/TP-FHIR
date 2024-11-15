import requests

# Función genérica para enviar un recurso FHIR al servidor HAPI FHIR
def send_resource_to_hapi_fhir(resource, resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}"
    headers = {"Content-Type": "application/fhir+json"}
    resource_json = resource.json()

    response = requests.post(url, headers=headers, data=resource_json)

    if response.status_code == 201:
        print(f"Recurso {resource_type} creado exitosamente.")
        return response.json()["id"]  # Devuelve el ID del recurso creado
    else:
        print(f"Error al crear el recurso {resource_type}: {response.status_code}")
        print(response.json())
        return None

# Función genérica para recuperar un recurso FHIR del servidor HAPI FHIR por ID
def get_resource_from_hapi_fhir(resource_id, resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}/{resource_id}"
    headers = {"Accept": "application/fhir+json"}
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(f"Recurso {resource_type} encontrado:")
        return response.json()  # Devuelve el recurso completo en formato JSON
    else:
        print(f"Error al obtener el recurso {resource_type}: {response.status_code}")
        print(response.json())
        return None

# Función genérica para buscar recursos FHIR en el servidor HAPI FHIR (Punto 3.b)
def search_resource_in_hapi_fhir(resource_type, search_params):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}"
    headers = {"Accept": "application/fhir+json"}

    response = requests.get(url, headers=headers, params=search_params)

    if response.status_code == 200:
        resources = response.json().get("entry", [])
        if resources:
            print(f"Se encontraron {len(resources)} recurso(s) {resource_type} que coinciden con los criterios de búsqueda.")
            return [entry["resource"] for entry in resources]  # Devuelve una lista de recursos
        else:
            print(f"No se encontraron recursos {resource_type} que coincidan con los criterios de búsqueda.")
            return []
    else:
        print(f"Error al buscar recursos {resource_type}: {response.status_code}")
        print(response.json())
        return []
