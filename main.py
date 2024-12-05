#Proyecto clase 13 Repaso Final
#Autor Andres Morales
import csv
import pandas as pd
import os
# Lista para almacenar datos de ventas
ventas = []

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Ingresar datos de ventas")
        print("2. Guardar datos en un archivo CSV")
        print("3. Analizar los datos guardados")
        print("4. Salir del sistema")
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            ingresar_datos()
        elif opcion == '2':
            guardar_datos_csv()
        elif opcion == '3':
            analizar_datos()
        elif opcion == '4':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def ingresar_datos():
    print("\n--- Ingreso de Datos de Venta ---")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad vendida: "))
    precio = float(input("Ingrese precio por unidad: "))
    fecha = input("Ingrese la fecha de la venta (YYYY-MM-DD): ")
    cliente = input("Ingrese el nombre del cliente: ")
    
    venta = {
        "Producto": producto,
        "Cantidad": cantidad,
        "Precio": precio,
        "Fecha": fecha,
        "Cliente": cliente
    }
    ventas.append(venta)
    print("¡Venta registrada exitosamente!")

def guardar_datos_csv():
    if not ventas:
        print("No hay datos para guardar.")
        return

    with open("ventas.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Producto", "Cantidad", "Precio", "Fecha", "Cliente"])
        writer.writeheader()
        writer.writerows(ventas)
    
    print("Datos guardados en ventas.csv")

def analizar_datos():
    try:
        df = pd.read_csv("ventas.csv")
        print("\n--- Análisis de Datos ---")
        
        print("1. Total de ingresos generados:")
        ingresos_totales = (df["Cantidad"] * df["Precio"]).sum()
        print(f"   {ingresos_totales:.2f}")
        
        print("2. Producto más vendido:")
        producto_mas_vendido = df.groupby("Producto")["Cantidad"].sum().idxmax()
        print(f"   {producto_mas_vendido}")
        
        print("3. Cliente con más compras:")
        cliente_top = df.groupby("Cliente")["Cantidad"].sum().idxmax()
        print(f"   {cliente_top}")
        
        print("4. Ventas por fecha:")
        ventas_por_fecha = df.groupby("Fecha")["Cantidad"].sum()
        print(ventas_por_fecha)
    except FileNotFoundError:
        print("El archivo ventas.csv no existe. Guarda datos antes de analizarlos.")
    except Exception as e:
        print(f"Error al analizar los datos: {e}")



#VAlidar la ejecucuion del archivo principal
if __name__ == "__main__":
    print('Bienvenido al sistema de Gestion de Ventas')
    menu()
