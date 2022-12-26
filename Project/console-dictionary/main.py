import os
from tools.dictionary import Dictionary, paint
from tools.forwords import get_transcript

"""Style"""
W = '\x1b[37m'
C = '\x1b[36m'

def menu_dictionary():
    while True:
        os.system('cls||clear')

        main.get_all_word()

        print(f'\n{paint("+", "green")}word for add\t\t    {paint("-", "red")}word for del\n\n')

        select_with_menu_dictionary = input(f'{paint(">>>", "cyan")}')
        
        if select_with_menu_dictionary[0] == "+":
            
            word_on_eng = select_with_menu_dictionary[1:]
            main.set_word(word_on_eng, get_transcript(word_on_eng), )
        elif select_with_menu_dictionary[0] == "-":
            
            index_for_del = int(select_with_menu_dictionary[1:])
            main.remove_row(index_for_del)
            
        if select_with_menu_dictionary.lower() == "exit":
            return

if __name__ == "__main__":
    print(W)

    main = Dictionary("datafiles")

    menu = True
    while menu:
        os.system('cls||clear')
        
        print(f'''{C}
   █▀▄ █ █▀▀ ▀█▀ █ █▀█ █▄░█ ▄▀█ █▀█ █▄█
   █▄▀ █ █▄▄ ░█░ █ █▄█ █░▀█ █▀█ █▀▄ ░█░{W}\n{"_" * 42}''')

        try:
            select_with_main_menu = int(input(f'{paint("1", "green")}-dictionary\t\t{paint("2", "green")}-games\t      {paint(">>>", "cyan")}'))
            
            if select_with_main_menu == 1:
                menu_dictionary()
            elif select_with_main_menu == 2:
                pass
            else:
                raise ValueError()
        except ValueError:
            print(f'\t{paint("Write number: 1 or 2", "red")}\n\t  {paint("(type any key)", "red", "small")}')
            input()

            os.system('cls||clear')
            continue