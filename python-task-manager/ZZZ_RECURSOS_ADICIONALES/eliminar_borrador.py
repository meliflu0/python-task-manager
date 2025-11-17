import ast
import sys

def Eliminar():
    while True:
        print("\n==============================")
        elimino = input("\n¿Deseas eliminar una tarea?: ").strip().lower()

        if elimino == "si":
            print("\n==============================")
            indice = int(input("\nNúmero de tarea a eliminar (empezando desde 0): "))

            # Leer todas las líneas
            with open("1.4.ARCHIVOS\\tareas.txt", 'r', encoding="UTF-8") as archivo:
                lineas = archivo.readlines()

            # Convertir líneas en diccionarios reales
            tareas = [ast.literal_eval(linea.strip()) for linea in lineas]

            # Verificar que el índice sea válido
            if 0 <= indice < len(tareas):
                tarea_eliminada = tareas.pop(indice)

                # Reescribir el archivo con las tareas restantes
                with open("1.4.ARCHIVOS\\tareas.txt", 'w', encoding="UTF-8") as archivo:
                    for tarea in tareas:
                        archivo.write(str(tarea) + "\n")

                print(f"\nTarea '{tarea_eliminada}' ha sido eliminada correctamente.")
            else:
                print("\n⚠️ Índice inválido. Intenta con un número existente.")

        elif elimino == "no":
            print("\n1. Volver al menú principal")
            print("2. Salir de la aplicación")
            que_hacer = input("\n¿Qué quieres hacer?: ").strip()
            match que_hacer:
                case "1":
                    break
                case "2":
                    print("\n¡Hasta pronto!\n")
                    sys.exit()

Eliminar()
