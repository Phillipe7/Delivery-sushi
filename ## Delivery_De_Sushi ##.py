## Delivery_De_Sushi ##

# menú #
precioPikachu = 4500
precioOtaku = 5000
precioPulpo = 5200
precioAnguila = 4800

## contadores de cantidad ##
cantidadPikachu = 0
cantidadOtaku = 0
cantidadPulpo = 0  
cantidadAnguila = 0

# Totales #
subtotal = 0
descuento = 0  
total = 0

# Programa # 
pedidoCompleto = False
otroPedido = "si"

while otroPedido == "si":
    print("Bienvenido a la entrega de sushi, por favor ingresa tu pedido:")
    print("1. Pikachu - $4500")
    print("2. Otaku - $5000")
    print("3. Pulpo - $5200")
    print("4. Anguila - $4800")
    
    opcion = int(input("Selecciona el número del sushi que deseas ordenar: "))
    
    if opcion == 1:
        cantidadPikachu += 1
        subtotal += precioPikachu
    elif opcion == 2:
        cantidadOtaku += 1
        subtotal += precioOtaku
    elif opcion == 3:
        cantidadPulpo += 1
        subtotal += precioPulpo
    elif opcion == 4:
        cantidadAnguila += 1
        subtotal += precioAnguila
    else:
        print("Opción no válida, por favor selecciona un número del menú.")
    
    otroPedido = input("¿Deseas agregar otro sushi a tu pedido? (si/no): ").lower()

tieneDescuento = input("¿Tienes un código de descuento? (si/no): ").lower()

if tieneDescuento == "si":
    codigoValido = False

    while codigoValido == False:
        codigo = input("Ingresa tu código de descuento: "). lower()
        if codigo == "soyotaku":
            descuento = subtotal * 0.10
            codigoValido = True
            print("Código de descuento aplicado correctamente.")
        else:
            print("Código de descuento no válido.")
            opcionCodigo = input("presiona xpara volver al menú o cualquier tecla para intentar nuevamente: ").lower()
            if opcionCodigo == "x":
                codigoValido = True
                pedidoTerminado = False
else:
    pedidoTerminado = True

total = subtotal - descuento
totalProductos = cantidadPikachu + cantidadOtaku + cantidadPulpo + cantidadAnguila

print(f"TOTAL PRODUCTOS: {totalProductos}")
print("*****************")
print(f"Pikachu Roll: {cantidadPikachu}")
print(f"Otaku Roll: {cantidadOtaku}")
print(f"Pulpo Roll: {cantidadPulpo}")
print(f"Pulpo Venenoso Roll: {cantidadPulpo}")
print(f"Anguila Roll: {cantidadAnguila}")
print("*****************")
print("*****************")
print(f"Subtotal por pagar: ${subtotal}")
print(f"Descuento aplicado por codigo: ${int(descuento)}")
print(f"Total a pagar: ${int(total)}")

programaActivo = input("¿Desea realizar otro pedido completo o salir? (si/no): ").lower()

print("Gracias por tu pedido, ¡que disfrutes tu sushi!")