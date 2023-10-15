import funciones as f


expresion = input("Inserte la expresion : ")
separada = f.separa(expresion)
print("La expresion se separo correctamente en " + str(separada))

formal = f.formalizar_expresion_booleana(separada)
print("La expresion se formalizo y quedo " + formal)


simplificada = f.sl(formal)
print("Se simplifico y quedo " + str(simplificada))

f.tabla_de_verdad(str(simplificada))
