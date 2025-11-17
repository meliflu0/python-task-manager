import sys
from colors import yellow, cyan, white, reset
def Ver():
    print("\n")
    with open("storage_file\\tasks.txt",'r',encoding="UTF-8") as archivos:
                read_1 = archivos.read()
                print(f"{white}{read_1}{reset}")
    print(f"{cyan}1.{reset} {white}Return to the main menu{reset}")
    print(f"{cyan}2.{reset} {white}Exit the application{reset}")
    selection = input(f"\n{white}What would you like to do?:{reset} ")
    match selection:
        case "1":
            return
        case "2":
            print(f"\n{yellow}See you soon!{reset}\n")
            sys.exit()
            
if __name__ == "__main__":
    Ver()