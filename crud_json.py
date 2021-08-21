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
actualizar_archivo(palabras)