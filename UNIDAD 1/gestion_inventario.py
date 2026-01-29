"""
Programa: Calculadora de Inventario de Tienda
Funcionalidad: Calcula el valor total de un producto en stock, aplica un descuento
               si es necesario y verifica si hay disponibilidad.
"""
def calcular_valor_inventario():
    # --- Definición de variables con distintos tipos de datos ---

    nombre_producto = "Monitor Gaming"  # String (Texto)
    cantidad_stock = 15  # Integer (Entero)
    precio_unitario = 299.99  # Float (Decimal)
    tiene_descuento = True  # Boolean (Booleano)
    porcentaje_descuento = 0.10  # Float (10% de descuento)

    # --- Lógica del programa ---

    # Calculamos el precio total bruto
    valor_total_bruto = cantidad_stock * precio_unitario

    # Aplicamos descuento si la variable tiene_descuento es verdadera
    if tiene_descuento:
        descuento_aplicado = valor_total_bruto * porcentaje_descuento
        valor_final = valor_total_bruto - descuento_aplicado
    else:
        valor_final = valor_total_bruto

    # Verificamos si hay suficiente stock para una alerta (boolean dinámico)
    necesita_reabastecer = cantidad_stock < 5

    # --- Mostrar resultados ---
    print(f"--- Resumen de Producto: {nombre_producto} ---")
    print(f"Cantidad en bodega: {cantidad_stock} unidades")
    print(f"Precio por unidad: ${precio_unitario}")
    print(f"Valor total del inventario: ${valor_final:.2f}")
    print(f"¿Requiere compra urgente?: {necesita_reabastecer}")


# Ejecutar la función
if __name__ == "__main__":
    calcular_valor_inventario()
