paciente = {"BUME": {"NOMBRE:":"ELIUD", 
            "PATERNO":"BUENO",
            "CONSULTAS":[{"TEMP":36.5, 
                          "ESTATURA":1.80, 
                          "PESO":83,
                          "DIAGNOSTICO":"Inflacion",
                          "TRATAMIENTO":"Aspirina"
                          },
                          {"TEMP":36, 
                          "ESTATURA":1.82, 
                          "PESO":84}
                        ]
                    }
            }
print(paciente["BUME"]["CONSULTAS"][0])
print(paciente["BUME"]["CONSULTAS"][1])
print(len(paciente["BUME"]["CONSULTAS"]))
paciente["BUME"]["CONSULTAS"].append({"TEMP":35, "ESTATURA":1.85, "PESO":85})
#paciente["BUME"]["CONSULTAS"][].append({"TEMP":35, "ESTATURA":1.85, "PESO":85})
print(len(paciente["BUME"]["CONSULTAS"]))
print((paciente["BUME"]["CONSULTAS"]))
print(paciente["BUME"]["CONSULTAS"][-1])
print(paciente["BUME"]["CONSULTAS"][-2])
print(paciente["BUME"]["CONSULTAS"][-3])