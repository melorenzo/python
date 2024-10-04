monto_total = input("Ingrese el monto total de su factura: ") 
propina = input("Ingrese el porcentaje de propina que va a entregar. Recuerde que el monto recomendado es de 10%: ")

monto_total = float(monto_total)
propina = float(propina)

cantidad_propina = (propina * monto_total) / 100 
total_a_pagar = monto_total + cantidad_propina
800
print(f"El total a pagar es: {total_a_pagar:.2f}")
print(f"La cantidad de propina es: {cantidad_propina:.2f}. Su mesero se lo agradece :)")
