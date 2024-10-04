print("Bienvenido al sistema de Inventario de MEL Store")
print("Ingrese la opción que quiere ejecutar: ")
print("1. Cargar Producto \n2. Buscar Producto \n3. Informes")

primera_opcion = input("Elija su menú (1, 2 o 3): ")

if primera_opcion == '1': 
    producto_nombre = input("Ingrese el nombre del producto: ")
    producto_cantidad = input("Ingrese la cantidad del producto: ")
    1    
    producto_info = f"{producto_nombre} - Cantidad: {producto_cantidad}"
       
    print(f"El producto se guardó correctamente: {producto_info}")
else:
    print("Opción no válida. Por favor, elija una opción válida.")




#Funciones que voy a usar: cargar_producto actualizar_producto borrar_producto generar_informe buscar_producto