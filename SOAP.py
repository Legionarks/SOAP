from zeep import Client
import json

url = "http://localhost:7000/ws/AcademicoWebService?wsdl"
client = Client(url)


###############
#   Student   #
###############
class Student(object):

    # The class "constructor" - It's actually an initializer 
    def __init__(self, nombre, matricula, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera

#############
#   Print   #
#############

# Create students
jorge = Student("Jorge Michelen", 20160876, "ITT")
bibi = Student("Albeily Romano", 20161066, "ITT")
danilo = Student("Danilo Medina", 11110000, "PROF")

jsonJorge = json.dumps(jorge.__dict__)
jsonBibi = json.dumps(bibi.__dict__)
jsonDanilo = json.dumps(danilo.__dict__)

print("Creating students . . .")
client.service.crearEstudiante(json.loads(str(jsonJorge)))
client.service.crearEstudiante(json.loads(str(jsonBibi)))
client.service.crearEstudiante(json.loads(str(jsonDanilo)))
print("Students created . . .")

# Listing stundents
print("Look at this... All the students :p")
print(client.service.getListaEstudiante())

# Watch student
student = client.service.getEstudiante(11110000)
print("Watch to: %s" % student.nombre)
print("He was located from another server (soap), but he is not an student")
print("Let's remove him -.-")

# Remove student
ok = client.service.eliminarEstudiante(student.matricula)
print("[Server]", ok)

# Confirmation
print("Now it looks better :D")
print(client.service.getListaEstudiante())



