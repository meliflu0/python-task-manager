
import ast  # para convertir texto -> diccionario real

def marcar_tarea(nombre_tarea):
    nuevas_lineas = []

    # 1️⃣ Leer todas las líneas
    with open("1.4.ARCHIVOS\\tareas.txt", "r", encoding="UTF-8") as archivo:
        lineas = archivo.readlines()

    # 2️⃣ Revisar cada línea y modificar si hay coincidencia
    for linea in lineas:
        dic = ast.literal_eval(linea.strip())  # convierte str a dict real

        for tarea in dic:
            if tarea == nombre_tarea:
                dic[tarea] = True  # cambiar el valor a True

        nuevas_lineas.append(str(dic) + "\n")

    # 3️⃣ Sobrescribir con los cambios
    with open("1.4.ARCHIVOS\\tareas.txt", "w", encoding="UTF-8") as archivo:
        archivo.writelines(nuevas_lineas)

    print(f"✅ Tarea '{nombre_tarea}' marcada como completada.")

# Ejemplo de uso
marcar_tarea("papu")
