#1 Crear líneas de código en Python que calcule el promedio de los valores contenidos en una lista.

mi_lista = [5,6,10,13,3,4]

x = mi_lista[0] + mi_lista[1] + mi_lista[2] + mi_lista[3] + mi_lista[4] + mi_lista[5]

print(x/len(mi_lista))

#2 Escriba un código en python que determine cual grupo de personas contiene la mayor de todas las alturas de todas las personas

todos = [[177,145,167,190,140,150,180,130],
         [165,176,145,189,170,189,159,190],
         [145,136,178,200,123,145,145,134],
         [201,110,187,175,156,165,156,135]]

a=max(todos[0])
b=max(todos[1])
c=max(todos[2])
d=max(todos[3])

for i in todos:
    if a>b:
        i=a
    else:
        i=b
    if i>c:
        i=i
    else:
        i=c
    if i>d:
        i=i
    else:
        i=d

print('la persona con la mayor altura esta en el elemento', todos.index(max(todos)))














