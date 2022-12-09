x='hola mundo'
X=x.split() #divide la cadena en una lista
print(X)

x='hola mundo'
x=x.upper() #convierte la cadena a mayuscula

a="martina"
print(len(a))#nos da la longitud de la cadena


micadena="hola mundo"
print(micadena[2]) #nos da la letra que esta en la posicion 2
print(micadena[4])
print(micadena[0:3]) #nos da la cadena desde la posicion 0 hasta la 3
print(micadena[:3]) #nos da la cadena desde la posicion 0 hasta la 3Ç
print(micadena[0:4])
print(micadena[0:4:2]) #nos da la cadena desde la posicion 0 hasta la 4 de 2 en 2
name="martina"
 #no se puede cambiar el valor de una cadena las cadenas son inmutables

a=7%4 #nos da el resto de la division

print('estudio {} y mi asignatura favorita es {}'.format('informatica','calculo'))
print('mi nombre es {x} y mi apellido es {y}'.format(x="martina",y='garcia'))
print('mi comida favorita ed {p}'.format(p='pizza'))
resultados=500/78
print('los resultados son {} '.format(resultados))
nombre='martina'
edad='22'
print(f'mi nombre es {nombre} y tengo {edad} años')





milista=[1,2,3]
for num in range(10):  #va desde 0 hasta 9
    print(num)
print('------------------')
for num in range(0,12,2): #va desde 0 hasta 11 de 2 en 2
    print(num)
print('------------------')
print(list(range(0,20,5)))  #nos da una lista con los numeros que estan en el rango
print('------------------')
contador_indice=0
palabra='hola'
for letra in palabra:
    print(palabra[contador_indice])
    contador_indice+=1
print('------------------')
#otra manera de saber la posicion de cada letra
for letra in enumerate(palabra):
    print(letra)
print('------------------')
milista1=[1,2,3,]
milista2=['a','b','c']
for intem in zip(milista1,milista2):
    print(intem)
lista_nombres=['martina','jose','bea']
lista_apellidos=['garcia','perez','gomez']
for item in zip(lista_nombres, lista_apellidos):
    print(item)
print('------------------')
lista_nombres=['martina','jose','bea']
lista_apellidos=['garcia','perez','gomez']
edades=[18,54,23]
datos=list(zip(lista_nombres,lista_apellidos,edades))
print(datos)
print('------------------')
#ahora imaginate que tenemos un diccionario y queremos saber si tenemos una clave
diccionario={'a':1,'b':2,'c':3}
if 1 in diccionario.values():
    print('existe')
print('------------------')
from random import shuffle
lista=[1,2,3,4,5,6,7,8,9,10]
lista=shuffle(lista) #desordena la lista
print('------------------')
from random import randint
print(randint(0,100)) #nos da un numero aleatorio entre 0 y 100 entero

#nos permite crear una lista con las letras de un nombre
minombre='martina'
lista=[]
for letra in minombre:
    lista.append(letra)
print(lista)