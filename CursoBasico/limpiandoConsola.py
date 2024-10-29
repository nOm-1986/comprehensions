from os import system, name
def batle_ship_draw():
    return """
    __________           __   .__              _________.__     .__         
    \______   \_____   _/  |_ |  |    ____    /   _____/|  |__  |__|______  
    |    |  _/\__  \  \   __\|  |  _/ __ \   \_____  \ |  |  \ |  |\____ \ 
    |    |   \ / __ \_ |  |  |  |__\  ___/   /        \|   Y  \|  ||  |_> >
    |______  /(____  / |__|  |____/ \___  > /_______  /|___|  /|__||   __/ 
            \/      \/                   \/          \/      \/     |__|    

    """

def option_menu_messages():
    return """
            Welcome to Batle Ship play.
                Please select an option:
                1 - Play.
                5 - To quit
    """

def clearConsole():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def menu():
    running = True
    while running:
        print(batle_ship_draw())
        option = input(option_menu_messages())

        if (option == '1'):
            clearConsole()
            print("Algo esta pasando")
            
        elif option == '5':
            clearConsole()
            print('Thank you to play this game')
            running = False
        
        else:
            clearConsole()
            print('Please choose a correct option')
        

def run():
    menu()


if __name__ == '__main__':
    run()