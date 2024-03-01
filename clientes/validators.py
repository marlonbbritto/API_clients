import re

def cpf_valido(numero_cpf):
    return len(numero_cpf) == 11

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9  

def celular_valido(celular):
    """redux para validar o telefone"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta =  re.findall(modelo,celular)
    return resposta
   
    
        
    
        