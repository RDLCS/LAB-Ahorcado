from typing import Dict,DefaultDict,List,Tuple,Optional,Set
import csv
from random import choice

def cargar_palabras(ruta:str)->List[str]:
    lista=list()
    with open(ruta,'rt',encoding='utf-8') as f:
        iter=csv.reader(f)
        for palabra in iter:
            palabra=palabra[0]
            lista.append(palabra)
    return lista

def elegir_palabra(palabras:List[str])->str:
    return choice(palabras)

def enmascarar_palabra(palabra:str,letras:set)->str:
    lista=list()
    nueva=list()
    for letra in palabra:
        lista.append(letra)
    for letra in lista:
        if letra in letras:
            nueva.append(letra)
        else:
            nueva.append('_')
    return ' '.join(nueva)

def pedir_letra(letras:set)->Tuple[set,str]:
    letra=str(input('Adivine una letra: ')).lower()
    while letra in letras:
        letra=str(input('Ya has probado con esa letra. Intenta con otra: ')).lower()
    print(f'Letra introducida: {letra}')
    letras.add(letra)
    return letras,letra

def comprobar_letra(palabra:str,letra:str)->bool:
    conj=set()
    for p in palabra:
        conj.add(p)
    if letra in conj:
        return True
    elif letra not in conj:
        return False
    
def comprobar_palabra_completa(palabra:str,letras:set)->bool:
    conj=set()
    for p in palabra:
        conj.add(p)
    if conj==letras:
        return True,letras
    elif conj!=letras:
        return False
    
def ejecutar_turno(palabra:str,letras:set)->Tuple[bool,set]:
    enmascarada=enmascarar_palabra(palabra,letras)
    print(f"Palabra: {enmascarada}")
    nuevas_letras,letra=pedir_letra(letras)
    return comprobar_letra(palabra,letra),nuevas_letras

def jugar(max_intentos:int,palabras:List[str])->None:
    print('Está jugando al ahorcado.')
    palabra=elegir_palabra(palabras)
    letras=set()
    errores=0
    while errores<max_intentos:
        res,letras=ejecutar_turno(palabra,letras)
        if res==True:
            print('¡Bien hecho! Esa letra está en la palabra.')
            termina=comprobar_palabra_completa(palabra,letras)
            if termina==True:
                break
        elif res==False:
            print('Lo siento, esa letra no está en la palabra.')
            errores+=1
    if comprobar_palabra_completa(palabra,letras)==True:
        print(f'¡Felicidades! Adivinaste que la palabra es {palabra}. :D')
    elif errores==max_intentos:
        print(f"¡Lo siento! Has llegado al número máximo de intentos. :(\nLa palabra era {palabra}.")