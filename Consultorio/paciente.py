def consultar():
    altura = float(input("ALTURA: " ))
    peso = float(input("PESO: "))
    temp = float(input("TEMPERATURA: "))
    presion = (input("PRESION: "))
    alergias =input("ALERGIAS: ")
    datos_paciente = {"ALTURA":altura, "PESO":peso, "TEMPERATURA":temp, "PRESION":presion, "ALERGIAS":alergias}
    return (datos_paciente)

def diagnosticar():
    sintoma  = input("SINTOMAS: ")
    return sintoma
def tratar():
    tratamieto = input("TRATAMIENTO: ")
    return tratamieto 

def altaPaciente():
    nombre = input("NOMBRE: ").upper().strip()
    apellido_pat = input("PATERNO: ").upper().strip()
    apellido_mat = input("MATERNO: ").upper().strip()
    alta_paciente = {"NOMBRE":nombre, "PATERNO":apellido_pat, "MATERNO":apellido_mat}
    return alta_paciente


