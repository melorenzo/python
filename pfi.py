print("Bienvenido al sistema de Inventario de MEL Store")
print("-"*50)
inventario = {}
while True : 
    print("Ingrese la opción que quiere ejecutar: ")
    print()
    print("1. Cargar Producto \n2. Buscar Producto \n3. Informes \n4. Modificar un Producto \n5. Salir del Sistema")
    primera_opcion = input("Elija su menú (1, 2, 3, 4 o 5): ")

    if primera_opcion == '1': 
        producto_nombre = input("Ingrese el nombre del producto: ")
        producto_cantidad = input("Ingrese la cantidad del producto: ")
        inventario[producto_nombre.strip()] = producto_cantidad
       
        print(f"El producto se guardó correctamente: {producto_nombre} - Cantidad: {producto_cantidad}")
    elif primera_opcion == "2":
        valor_buscar=input("Ingrese el nombre del producto: ")
        if valor_buscar in inventario:
            print(f"{valor_buscar.strip()} - Cantidad: {inventario[valor_buscar]}")
        else:
            print("Producto no encontrado.", inventario)
    elif primera_opcion == "3" :
        print()
        print("Ingrese la opción que quiere ejecutar: ")
        print()
        print("1. Cantidad de Productos en el Inventario \n2. Listado de Productos y Cantidades \n3.  ")
        print()
        print("*"*60)
        print()
        segunda_opcion = input("Ingrese la opción que quiere ejecutar: ")
        if segunda_opcion == "1" : 
            suma_cantidades = 0
            for cantidad in inventario.values() :
                suma_cantidades += int(cantidad) 
            espacio_total = 100
            total_productos = len(inventario)
            mensaje = f"Total de productos por tipo en el inventario: {total_productos}"
            mensaje2 = f"Total de productos por cantidad en el inventario: {suma_cantidades}"
            espacios_izquierda = (espacio_total - len(mensaje)) // 2
            print("_"*100)
            print(" " * espacios_izquierda + mensaje)
            print(" " * espacios_izquierda + mensaje2)
            print("_"*100)
            print()
        elif segunda_opcion == "2" :
             print("_" * 40)
             print(f"{'Producto':<20} | {'Cantidad':<10}")
             print("_" * 40)
             for producto, cantidad in inventario.items():
                print(f"{producto.title():<20} | {cantidad:<10}")
                print("_" * 40)
                print()
    elif primera_opcion == "4":
         print()
         print("Ingrese la opción que quiere ejecutar: ")
         print()
         print("1. Modificar Nombre \n2. Modificar Cantidad ")
         print()
         print("*"*60)
         print()
         tercera_opcion = input("Ingrese la opción que quiere ejecutar: ")
         if tercera_opcion == "1" :
            valor_buscar = input("Ingrese el nombre del producto: ").strip()  
            if valor_buscar in inventario:
                print(f"Producto encontrado: {valor_buscar} - Cantidad actual: {inventario[valor_buscar]}")
                nuevo_nombre = input("Ingrese el nuevo nombre del producto: ").strip()
                inventario[valor_buscar] = nuevo_nombre
                cantidad_actual = inventario[valor_buscar]
                del inventario[valor_buscar]
                inventario[nuevo_nombre] = cantidad_actual
                print(f"El nombre del producto {valor_buscar} se actualizó a {nuevo_nombre}.") 
                print()
         elif tercera_opcion == "2":   
            valor_buscar = input("Ingrese el nombre del producto: ").strip()  
            if valor_buscar in inventario:
                print(f"Producto encontrado: {valor_buscar} - Cantidad actual: {inventario[valor_buscar]}")
                nueva_cantidad = input("Ingrese la nueva cantidad del producto: ")
                inventario[valor_buscar] = nueva_cantidad
                print(f"La cantidad del producto {valor_buscar} se actualizó a {nueva_cantidad}.")
        
    elif primera_opcion == "5":
        print("Saliendo del sistema.")
        break             

    else :
        print("Opción no válida. Por favor, elija una opción válida.")    
    




#Funciones que voy a usar: cargar_producto actualizar_producto borrar_producto generar_informe buscar_producto