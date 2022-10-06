#ejercicio_5

print("Ingrese el total de su factura sin IVA")
total = (int(input()))
print("Ingrese el porcentaje de IVA que desea aplicar, en caso de no tener uno escriba 0")
iva = int(input())

def main():
    if iva == 0:
        iva_19 = (total * 19)/ 100 
        factura_19 = total + iva_19
        print("El total de su factura es de", factura_19)
    else:
        iva_aplicado = (total * iva) / 100
        total_factura = total + iva_aplicado
        print ("El total de su factura es de", total_factura)
main()