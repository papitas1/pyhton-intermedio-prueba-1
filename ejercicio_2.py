#ejercicio_2


print ("Ingrese su renta anual porfavor")
renta_anual = int(input())

if renta_anual >= 10000:
    renta_1 = (renta_anual * 5)/100
    total_1 = renta_1 + renta_anual
    print("Su renta sera de ", total_1)

elif renta_anual >= 20000:
    renta_2 = (renta_anual * 5)/100
    total_2 = renta_2 + renta_anual
    print("Su renta sera de ", total_2)

elif renta_anual >= 35000:
    renta_3 = (renta_anual * 5)/100
    total_3 = renta_3 + renta_anual
    print("Su renta sera de ", total_3)

elif renta_anual >= 60000:
    renta_4 = (renta_anual * 5)/100
    total_4 = renta_4 + renta_anual
    print("Su renta sera de ", total_4)

elif renta_anual < 60000:
    renta_5 = (renta_anual * 5)/100
    total_5 = renta_5 + renta_anual
    print("Su renta sera de ", total_5)

