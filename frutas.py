'''
Ejercicio 2: Ordenamiento de Frutas en un Salpicón
En este ejercicio, se requiere desarrollar un programa en Python que
permita registrar y organizar un conjunto de frutas con sus respectivos
precios dentro de un salpicón.
Ingreso de frutas:
El programa debe solicitar al usuario el ingreso de 10 frutas, cada una con
su nombre y precio.
Almacenar la información en una lista de diccionarios.
Ordenamiento:
Una vez ingresadas las 10 frutas, el programa deberá ordenarlas de mayor
a menor precio y mostrar la lista en pantalla.
Deben asegurarse de implementar un algoritmo de ordenamiento
adecuado para organizar las frutas correctamente y presentar los
resultados de forma clara.'
'''

# Lista para almacenar las frutas
frutas = []


for i in range(10):
    nombre = input(f"Ingrese el nombre de la fruta {i+1}: ")
    
 

    while True:
        
        precio = float(input(f"Ingrese el precio de {nombre}: "))
           
        if precio < 0:
                print("El precio no puede ser negativo. Intente nuevamente.")
        else:
                break
      
       

    frutas.append({"nombre": nombre, "precio": precio})

print(frutas)



frutas_ordenadas = sorted(frutas, key=lambda fruta: fruta["precio"], reverse=True)


print("\nFrutas ordenadas por precio (de mayor a menor):")
for fruta in frutas_ordenadas:
    print(f"{fruta['nombre']}: ${fruta['precio']:.2f}")




