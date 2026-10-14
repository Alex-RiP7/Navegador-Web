"""
Simulador de Navegador Web usando estructura de datos tipo Lifo
"""

historial = []  

def visitar_pagina():
    url = input("Ingresa la URL o nombre de la página a visitar: ").strip()
    if url:
        historial.append(url)
        print(f"\nVisitando: {url}")
    else:
        print("\nURL vacía, no se registró nada.")

def regresar_anterior():
    if len(historial) <= 1:
        print("\nNo hay página anterior a la que regresar.")
        return
    pagina_actual = historial.pop()
    print(f"\nRegresando desde: {pagina_actual}")
    print(f"Ahora estás en: {historial[-1]}")

def mostrar_actual():
    if not historial:
        print("\nNo hay página actual. El historial está vacío.")
    else:
        print(f"\nPágina actual: {historial[-1]}")

def mostrar_historial():
    if not historial:
        print("\nEl historial está vacío.")
        return
    print("\n=== Historial de páginas (más reciente primero) ===")
    for i, pagina in enumerate(reversed(historial), 1):
        print(f"{i}. {pagina}")

def verificar_o_limpiar():
    if not historial:
        print("\nEl historial está vacío.")
    else:
        respuesta = input("El historial tiene páginas. ¿Deseas eliminar todo el historial? (s/n): ").strip().lower()
        if respuesta == 's':
            historial.clear()
            print("Historial eliminado.")
        else:
            print("Historial conservado.")

def menu():
    while True:
        print("\n" + "="*45)
        print("     SIMULADOR DE NAVEGADOR WEB (PILA LIFO)")
        print("="*45)
        print("1. Visitar una página web")
        print("2. Regresar a la página anterior")
        print("3. Mostrar la página actual")
        print("4. Mostrar el historial (orden descendente)")
        print("5. Verificar si el historial está vacío / Eliminar")
        print("6. Salir del programa")
        print("="*45)

        opcion = input("Selecciona una opción (1-6): ").strip()

        if opcion == '1':
            visitar_pagina()
        elif opcion == '2':
            regresar_anterior()
        elif opcion == '3':
            mostrar_actual()
        elif opcion == '4':
            mostrar_historial()
        elif opcion == '5':
            verificar_o_limpiar()
        elif opcion == '6':
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
