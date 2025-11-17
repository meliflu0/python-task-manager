import ast
import sys

from colors import red, yellow, blue, cyan, white, reset 

def Eliminar():
    new_lines = []
    
    while True:
        print(f"\n{blue}=============================={reset}")
        print(f"\n{cyan}1.{reset} {white}Delete a single task{reset}")
        print(f"{cyan}2.{reset} {white}Delete {reset}{yellow}all{reset} {white}tasks{reset}") 
        print(f"{cyan}3.{reset} {white}Return to the main menu{reset}")
        all_or_one = input(f"\n{white}What would you like to do?:{reset}")
        match all_or_one:
            case "1":
            
                print(f"\n{blue}=============================={reset}")
                delete_1 = input(f"\n{white}Do you want to {yellow}delete{reset} a task? y/n:{reset} ")
            
                if delete_1 == "y":
                    try:
                        print(f"\n{blue}=============================={reset}")
                        eliminando = int(input(f"\n{white}Delete task by index{reset} {yellow}(starting from 0):{reset} "))
                        # Leer todas las líneas
                        with open("storage_file\\tasks.txt",'r',encoding="UTF-8") as archivos:
                            lineas = archivos.readlines()
                        # Revisar cada línea y modificar si hay coincidencia
                        for linea in lineas:
                            dic = ast.literal_eval(linea.strip())   # convierte str a dict real

                            new_lines.append(str(dic) + "\n")
                        
                        
                        new_lines.pop(eliminando)
                            
                            
                        # Sobrescribir con los cambios         
                        with open("storage_file\\tasks.txt",'w', encoding="UTF-8") as archivo:
                            archivo.writelines(new_lines)
                        # Elimina la lista para cada bucle no generar valores de anteriores bucles
                        new_lines.clear()

                        print(f"\n{white}The task '{eliminando}' has been{reset} {red}deleted.{reset}")
                        break
                    except (IndexError, ValueError):
                        print(f"\n{white}That Task(Index) does not exist or is invalid, try again{reset}")
                elif delete_1 == "n":   
                    print(f"\n{cyan}1.{reset} {white}Return to the main menu{reset}")
                    print(f"{cyan}2.{reset} {white}Exit the application{reset}") 
                    selection = input(f"\n{white}What would you like to do?:{reset} ")
                    match selection:
                        case "1":
                            break
                        case "2":
                            print(f"\n{yellow}See you soon!{reset}\n")
                            sys.exit()
            case "2":
                seguro = input(f"\n{white}Are you sure you want to{reset} {red}delete{reset} everything? y/n:{reset} ")
                if seguro == "y":
                    print(f"\n{white}All tasks have been{reset} {red}deleted{reset}{white}.{reset}")
                    with open("storage_file\\tasks.txt",'w', encoding="UTF-8") as archivo:
                        pass
                else:
                    print("")
            case "3":
                break        
if __name__ == "__main__":
    Eliminar()