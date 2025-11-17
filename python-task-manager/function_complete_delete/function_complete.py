import ast    # para convertir texto -> diccionario real
import sys

from colors import green, yellow, blue, cyan, white, reset 
def Completar():
    new_lines = []
    
    while True:
        print(f"\n{blue}=============================={reset}")
        complete = input(f"\n{white}Did you {yellow}complete{reset} a task? y/n:{reset} ")
    
        if complete == "y":
            print(f"\n{blue}=============================={reset}")
            completed = str(input(f"\n{white}Task name:{reset} "))
            # Leer todas las líneas
            with open("storage_file\\tasks.txt",'r',encoding="UTF-8") as archivos:
                lineas = archivos.readlines()
            # Revisar cada línea y modificar si hay coincidencia
            for linea in lineas:
                dic = ast.literal_eval(linea.strip())   # convierte str a dict real
                for tarea in dic:
                    
                    if tarea == completed:
                        dic[completed] = True  # cambiar el valor a True
                        
                new_lines.append(str(dic) + "\n")
                
            # Sobrescribir con los cambios         
            with open("storage_file\\tasks.txt",'w', encoding="UTF-8") as archivo:
                archivo.writelines(new_lines)
            # Elimina la lista para cada bucle no generar valores de anteriores bucles
            new_lines.clear()

            print(f"\n{white}Task '{completed}'{reset} {green}marked as completed.{reset}")
        elif complete == "n":   
            print(f"\n{cyan}1.{reset} {white}Return to the main menu{reset}")
            print(f"{cyan}2.{reset} {white}Exit the application{reset}") 
            selection = input(f"\n{white}What would you like to do?:{reset} ")
            match selection:
                case "1":
                    break
                case "2":
                    print(f"\n{yellow}See you soon!{reset}\n")
                    sys.exit()
        
if __name__ == "__main__":
    Completar()        