pruebas_atl= [200, 100, 400] #lista
tiempos=(29.3, 13.9, 58)  #tupla

print(pruebas_atl)
print(tiempos)

print("\n")

print(pruebas_atl[2:])
print(tiempos[1])

print("\n")
print(pruebas_atl)
print(tiempos)
pruebas_atl[2]=300 #para reemplazar el elemento 2 por 300
print(pruebas_atl)
print("Las tuplas no son modificables")

print("\n")

print(len(pruebas_atl))
print(len(tiempos))

print("\n")
print (200 in pruebas_atl)
print(30 in tiempos)

print("\n")

pruebas_atl.append('longitud')
print(pruebas_atl)
print("No se pueden añadir datos en una tupla")

print("\n")

pruebas_atl.pop(2)
print(pruebas_atl)
print("Las tuplas no son modificables")

print("\n\n\n")

comidaset = {"cocido", "fabada", "salmorejo"}
print(comidaset)
futbolistas = {
  5: "Zinedine Zidane",
  1: "Iker Casillas",
  9: "Karim Benzema",
  7: "Cristiano Ronaldo"
}
print(futbolistas)
print("\n")
print("En los sets no se puede mostrar un elemento especifico(por ejemplo, el segundo valor del set) ya que va cambiando cada vez el orden ")
print(next(iter(futbolistas)))

print("\n")
print("El set no permite realizar cambios")
futbolistas[4]=futbolistas.pop(7)
futbolistas[4]= 'Sergio Ramos'
print(futbolistas)

print("\n")
print(len(futbolistas))
print(len(comidaset))

print("\n")
print('paella' in comidaset)
print(7 in futbolistas)

print("\n")
comidaset.add('ensalada')
futbolistas[20]='Vinícus Junior'
print(comidaset)
print(futbolistas)

print("\n")
futbolistas.pop(1)
print(futbolistas)

comidaset.discard('salmorejo')
print(comidaset)

print("\n\n\n")

numero_1= int(float(input("Escribe un número:")))
numero_2= int(float(input("Escribe un número:")))
numero_3= int(float(input("Escribe un número:")))
numeros=[numero_1, numero_2, numero_3]
print(numeros)
sumatorio= sum(numeros)
print(sumatorio)

print("\n\n\n")
media=sumatorio/len(numeros)
print(media)