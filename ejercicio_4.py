#ejercicio_4

lista = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

for i in range (len(lista)-1,-1,-1):
    promedio = float (input("Que nota sacaste en" + lista[i] + "?"))
    if promedio >= 4:
        lista.pop(i)
print("Tienes uqe repetir" + str(lista))

