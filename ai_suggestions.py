import ast
import os
import collections
from collections import defaultdict


def extrair_valores_de_testes():
    
    return [
        ("int", 0), ("int", 1), ("int", -1),
        ("str", ""), ("str", "abc"), ("str", "hello"),
        ("bool", True), ("bool", False),
        ("float", 0.0), ("float", 3.14), ("float", -2.5),
    ]

def valores_mais_frequentes(valores):
    contador = defaultdict(lambda: defaultdict(int))

    for tipo, valor in valores:
        chave = repr(valor)  
        contador[tipo][chave] += 1

    mais_frequentes = {}
    for tipo, valores_dict in contador.items():
        mais_frequentes[tipo] = [
            k for k, _ in sorted(valores_dict.items(), key=lambda item: item[1], reverse=True)[:3]
        ]

    return mais_frequentes
