import sys

from colors import green, yellow, blue, cyan, white, reset
def Agregar():
    
    while True:  
        print(f"\n{blue}=============================={reset}")
        ask_1 = input(f"\n{white}Do you want to{reset} {yellow}create{reset} {white}a new task? y/n:{reset} ")
        if ask_1 == "y":
            tarea_n = input(f"\n{white}Task name:{reset} ")
            diccionarios = {tarea_n:False}      
            with open("storage_file\\tasks.txt",'a+',encoding="UTF-8") as archivos:
                archivos.write(str(diccionarios) + "\n")
                
            print(f"{white}Task '{tarea_n}' {reset}{green}added{reset} {white}successfully!{reset}")
        elif ask_1 == "n":
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
    Agregar()