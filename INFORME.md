# Trabajo Práctico N°6
![image](Imagenes/logoitba.png)

## _Autores:_ 
* Gonzalo Grau
* Agustín Luna Simondi

## **PARTE 1:** HAPI FHIR
![image](Imagenes/pagina_inicial_hapifhir.png)
Ingresamos a la pagina de HAPI FHIR a traves del link otorgada por la catedra. Lo primero que debemos hacer es 
dirigirnos a la solapa de paciente y de ahi a la solapa de CRUD operations que nos permitira manejar las
diferentes herramientas de una API del tipo REST

### 1. a. Crear un recurso patient utilizando la UI del servidor de HAPI FHIR. Leer el recurso patient creado.
Una vez ya marcada la solapa anterior tenemos varias opciones en donde en este caso debemos ir a la sección de "Create", en donde nos permitira crear un recurso de tipo "Paciente"

![image](Imagenes/crear_recurso_1a.png)

Elegimos un ID para identificarlo de manera univoca en donde seleccionamos uno de fantasia "DOC124". Ademas de esto debemos
agregar información del paciente dentro de "Contents" en donde se debe crear un body con formato JSON en donde se debe respetar los atributos especificos del tipo de recurso. Por ejemplo le agregamos a nuestro paciente el año de nacimiento bajo el atributo "birthdate", su genero "genre" y asi se puedo ir creando un perfil mucho mas extenso



![image](Imagenes/recurso_request_1a.png)

Podemos ver el uso de la funcionalidad del API REST al hacer el POST del nuevo endpoint que hemos creado del recurso Paciente. También vemos el "Result Body" con datos propios que hemos metido en el JSON asi como otros que los proporciona la creación mediante HAPI FHIR como es el "system"

![image](Imagenes/recurso_generado_1a.png)
Aca ya tenemos el recurso generado, en donde vemos la creación correcta del paciente incluyendo datos como el nombre, fecha de nacimiento y genero.

Ademas de esto podemos ver el "Result Body" en donde encontramos datos adicionales que se inicializan al crean un nuevo recursco como puede ser su "id" siendo este 45151339 , algo que tendremos que tener en consideración cuando queramos hacer una busqueda


### 2. b. Describir brevemente las propiedades del mismo.

![image](Imagenes/solicitar_lectura_1b.png)
![image](Imagenes/lectura_generada_1b.png)

## **PARTE 2:** POSTMAN

### 1. a.  Repetir lo anterior utilizando postman online. Luego, leer el recurso creado.
Repetimos el mismo proceso en POSTMAN

![image](Imagenes/recurso_postman_2.png)
![image](Imagenes/lectura_postman_2.png)

## **PARTE 3:** PYTHON

## 3. a. ~

