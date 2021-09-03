'''
import json
#read
def actualizar_archivo(lista):
   f=open('datos_almacenados.json', 'w')
   escribir=json.dumps(lista)
   f.write(escribir)
   f.close()
#agregar 
def agregar_string():
   month=input('Escriba valor a agregar')
   lista:list=[]
   try:
       lista=json.load(open('datos_almacenados.json', 'r'))
   except:
       lista:list=[]
   """ with open('datos_almacenados.json', 'w') as f:
       lista.append(month)
       escribir=json.dumps(lista)
       f.write(escribir) """
   lista.append(month)
   actualizar_archivo(lista)
#read
def leer_json()->list:
    read=open('datos_almacenados.json', 'r')
    leyendo=read.read()
    leido_formato_python=json.loads(leyendo)
    read.close()
    return leido_formato_python
leer_json()
#updates
palabras=leer_json()
print(palabras)
palabra_reemplazar=input('Cual desea actualizar: ')
for palabra in palabras:
   if palabra== palabra_reemplazar:
       indice=palabras.index(palabra)
       palabras[indice]=input('Ingrese nueva palabra: ')
       break
print(palabras)
actualizar_archivo(palabras)
#Borrar
string_a_remover=input('Cual desea remover: ')
palabras.remove(string_a_remover)
actualizar_archivo(palabras)'''

import json
from os import remove
#read
def escribir_json(subir):
    dato:list=[]
    file=open(archivo_json, 'w')
    dato.append(subir)
    file.write(json.dumps(dato))
    file.close()
archivo_json='datos_almacenados.json'
def leer():
    lista_leer=open(archivo_json, 'r')
    compatibilidad_python=json.loads(lista_leer.read())
    lista_leer.close()
    return compatibilidad_python
leer()
#agregar
def agregar_strings():
    leer=[]
    try:
        leer=json.load(open(archivo_json))
        print(leer)
    except:
        leer:list=[]
    nombre=input('Escribe un nombre: ')
    leer.append(nombre)
    escribir_json=open(archivo_json, 'w')
    escribir_json.write(json.dumps(leer))
    escribir_json.close()
    

def updates():
    leer_json:list=leer()
    print(leer_json)
    nombre_a_actualizar=input('Escribe el nombre que quiere actualizar: ')
    for x in leer_json:
        if nombre_a_actualizar ==x: 
           index_input=leer_json.index(nombre_a_actualizar)
           leer_json[index_input]=input('Nombre por el que lo va a actualizar: ')
           escribir_json(leer_json)    
def delete():
    leer_json:list=leer()
    print(leer_json)
    print('______________________________________')
    string_a_borrar=input('Escribe el nombre a borrar aqui: ')
    if string_a_borrar in leer_json:
      leer_json.remove(string_a_borrar)
      escribir_json(leer_json)     
    else:
         print('No esta ese estudiante')
    print(f'Estudiantes actuales: {leer_json}')
delete()