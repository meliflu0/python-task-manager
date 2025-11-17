import sys

from colors import yellow, blue, cyan, white, reset
from functions_add_view import function_add as fun_add, function_view as fun_view
from function_complete_delete  import function_complete as fun_com, function_delete as fun_del

def Menu():
    while True:
        print(f"\n{blue}=============================={reset}")
        print(f"{white}Welcome! What would you like to do?{reset}")
        print(f"{blue}======={reset}{white}INTERACTIVE MENU{reset}{blue}======={reset}\n")
        
        print(f"{cyan}1.{reset} {white}Add Tasks{reset}")
        print(f"{cyan}2.{reset} {white}View Tasks{reset}")
        print(f"{cyan}3.{reset} {white}Complete Tasks{reset}")
        print(f"{cyan}4.{reset} {white}Delete Tasks{reset}")
        print(f"{cyan}5.{reset} {white}Exit{reset}")
        opcion = input(f"\n{white}Select an option:{reset} ")
        match opcion:
            case "1":
                fun_add.Agregar()
            case "2":
                print(f"\n{blue}=============================={reset}")
                print(f"\n{white}Your current tasks are:{reset} ")
                fun_view.Ver()
            case "3":
                fun_com.Completar()
                
            case "4":
                fun_del.Eliminar()
            case "5": 
                print(f"\n{yellow}See you soon!{reset}\n")
                break
if __name__ == "__main__":
    Menu()  