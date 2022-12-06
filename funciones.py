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

mi_lista=['martina',1,2,3,4,5,6,7,8,9,10]
print(mi_lista)
print(len(mi_lista))
print(mi_lista[0])
print(mi_lista[2:])
primeralista=[1,2,3]
segundalista=[4,5,6]
lista=primeralista+segundalista
lista[0]='mar'
print(lista)
lista.append(7)
print(lista)
intem_eliminado= lista.pop()
print(intem_eliminado)
print(lista)
lista.pop(3)
nuevalista1=print(lista)
mi_nuevalista=['a','b','c']