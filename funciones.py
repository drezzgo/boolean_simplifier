import re
from itertools import product
from sympy.logic.boolalg import And
from sympy import simplify_logic as sl
from sympy.parsing.sympy_parser import parse_expr



def separa(expresion):
    # Inserta "*" entre letras
    expresion = re.sub(r'([A-Za-z])([A-Za-z])', r'\1*\2', expresion)
    separadores = '()+-*/'
    lista = re.findall(r"[\w]+|[" + re.escape(separadores) + "]", expresion)
    expresion = ' '.join(lista)
    return expresion

def formalizar_expresion_booleana(expresion):
    # Reemplazar operadores booleanos
    expresion = re.sub(r'\+', r' | ', expresion)  # Reemplazar "+" con " | "
    expresion = re.sub(r'\*', r' & ', expresion)  # Reemplazar "*" con " & "
    expresion = expresion.replace('*', ' & ')
    return expresion

def obtener_variables(expresion):
    return list(set(re.findall(r'\b[A-Za-z]\b', expresion)))

def evaluar_expresion(expresion, valores):
    for variable, valor in valores.items():
        expresion = expresion.replace(variable, str(valor))
    return eval(expresion)

def tabla_de_verdad(expresion):
    variables = obtener_variables(expresion)
    headers = variables + [expresion]
    print("\t".join(headers))

    for valores in product([0, 1], repeat=len(variables)):
        valores_dict = dict(zip(variables, valores))
        resultado = evaluar_expresion(expresion, valores_dict)
        fila = [str(valores_dict[var]) for var in variables] + [str(resultado)]
        print("\t".join(fila))