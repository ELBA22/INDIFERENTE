import json
controlador = True
while controlador:
    print("---Centro medico campus---")
    print("1.  AGREGAR CITAS MEDICAS")
    print("2. BUSCAR CITAS MEDICAS")
    print("3. MODIFICAR CITAS")
    print("4. ELIMINAR CITAS")
    print("5.SALIR")
    controlador = False
                     
def agregarCita(citas):
    nombre = input("Ingrese el nombre del paciente: ")
    fechCita = input("Ingrese la fecha de su cita: ")
    horaCita = input("Ingrese la hora de su cita: ")
    motivCita = input("Ingrese el motivo de su cita: ")
    cita = {"nombre": nombre, "fechCita": fechCita, "horaCita": horaCita, "motivCita": motivCita}
    print("Cita guardada con exito.")
    
    
def buscarCitas(citas):
    criteriodBusqueda = input("Ingrese el criterio de busqueda ('nombre', 'fecha'): ")
    citasEncontrada = {}
    for cita in citas: 
        if criteriodBusqueda.lower in citas["nombre"].lower() or criteriodBusqueda.lower==cita["fecha"]:
            citasEncontrada.append(cita)
            if len(citasEncontrada)> 0:
                print("citas encontradas")
                for cita in citasEncontrada:
                    print("nombre: {}, fecha: {}, hora: {}, motivo: {}".format(cita["fecha"], cita["hora"], cita["motivo"]))
                else: 
                    print("No se encontraron citas.")
                    
def modifiCitas(citas):
    buscar_cita=(citas)
    if len(citas)>0:
        index = int(input("Ingrese el indice de la cita que desea modificar: "))
        if index >= 0 and index < len(citas):
            nombre = input("Ingrese el nuevo nombre que desea modificar: ")
            fecha = input("Ingrese la nueva fecha de su cita: ")
            hora = input("Ingrese la modificacion de la hora para su cita: ")
            motivo = input("Ingrese el motivo de su cita: ")
            citas[index][nombre]= nombre
            citas[index][fecha]= fecha
            citas[index][hora]= hora
            citas[index][motivo]= motivo
            print("cita modificada con exito")
        else:
            print("Ingrese indice valido, no hay citas para modificar.")
            
def cancelCita(citas):
    buscarCitas(citas)
    if len(citas)>0:
        index = int(input("Ingrese el indice de la cita que desea cancelar: "))
        if index >=0 and index < len (citas):
            citas.pop(index)
            guardar_citas = (citas)
            print("Cita cancelada con exito.")
        else: 
            print("indice invalido.")
            
def guardarCitas(citas):
    with open("citas.json","r") as file:
        json.dump(citas,file)

def cargarCita(citas):
    try:
        with open ("citas.json", "r") as file:
            citas= json.load(file)
            
    except FileNotFoundError:
        citas = []
        

OPCION = int(input("Ingrese la opcion que desea realizar: "))
if (OPCION ==1):
    agregarCita("citas")
        

elif (OPCION ==2):
    buscarCitas("citas")

elif (OPCION ==3):
    modifiCitas("citas")

elif (OPCION ==4):
    cancelCita("citas")

elif (OPCION ==5):
    print("Vuelve pronto.")
    
else:
    print("Opcion invalida")
        

    

    


