from paciente import consultar, altaPaciente, diagnosticar, tratar
from tools import borrarPantalla
pacientes = {}
borrarPantalla()
while True: 
    print("###############################CONSULTORIO DE LA DOCTORA GISELA SIMI#######################################"
    "\n\n\n" 
    "C) CONSULTAR\n" 
    "S) SALIR\n\n\n")
    opcion = input("Ingresa una opción: ").upper().strip()
    borrarPantalla()
    if opcion == "C":
        print("==================BUSCAR PACIENTE====================\n\n")
        rfc = input("RFC:").upper().strip()
        if rfc in pacientes:
            print("==============PACIENTE FRECUENTE=================\n\n")
        
            print("NOMBRE: ", pacientes[rfc]["NOMBRE"],pacientes[rfc]["PATERNO"],pacientes[rfc]["MATERNO"])
            print("\n\n")
        
            print("===============ULTIMA CONSULTA===================\n\n")  
        
            print("ALTURA: {}".format(pacientes[rfc]["CONSULTAS"][-1]["ALTURA"])) 
            print("PESO: {}".format(pacientes[rfc]["CONSULTAS"][-1]["PESO"])) 
            print("TEMPERATURA: {}".format(pacientes[rfc]["CONSULTAS"][-1]["TEMPERATURA"])) 
            print("PRESION: {}".format(pacientes[rfc]["CONSULTAS"][-1]["PRESION"]))
            print("\n")

            print("===============ULTIMO DIAGNÒSTICO===================\n\n")  
         
            print("SINTOMAS: {}".format(pacientes[rfc]["CONSULTAS"][-1]["SINTOMAS"])) 
            print("TRATAMIENTO: {}".format(pacientes[rfc]["CONSULTAS"][-1]["DIAGNOSTICO"])) 
            print("\n")
            
            print("==================NUEVA CONSULTA====================\n\n") 
            consulta=consultar()
            pacientes[rfc]["CONSULTAS"].append(consulta)
            sintomas=diagnosticar()
            no_consulta= len(pacientes[rfc]["CONSULTAS"])
            pacientes[rfc]["CONSULTAS"][no_consulta-1]["SINTOMAS"]=sintomas
            trato=tratar()
            pacientes[rfc]["CONSULTAS"][no_consulta-1]["DIAGNOSTICO"]=trato
        else: 
            print("==================INGRESAR NUEVO PACIENTE====================\n\n")
            paciente = altaPaciente()
            pacientes[rfc] = paciente
            pacientes[rfc]["CONSULTAS"]=[]
            print("--------------------INICIO DE CONSULTA--------------""\n\n")
            consulta=consultar()
            pacientes[rfc]["CONSULTAS"].append(consulta)

            print("--------------------INICIO DE DIAGNOSTICO--------------""\n\n")
            sintoma=diagnosticar()
            pacientes[rfc]["CONSULTAS"][0]["SINTOMAS"] = sintoma

            print("--------------------INICIO DE TRATAMIENTO--------------""\n\n")
            trato=tratar()
            pacientes[rfc]["CONSULTAS"][0]["DIAGNOSTICO"] = trato
            borrarPantalla()
    borrarPantalla()
    

