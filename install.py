from os import system
from time import sleep
from sys import exit


def inicio():
    system('clear')
    print('''
  _   _   _   _   _   _   _   _   _
 / \ / \ / \ / \ / \ / \ / \ / \ / \ 
( \033[1;32mS\033[m | \033[1;32mi\033[m | \033[1;32mm\033[m | \033[1;32mp\033[m | \033[1;32ml\033[m | \033[1;32me\033[m | \033[1;32mA\033[m | \033[1;32mr\033[m | \033[1;32mc\033[m )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ v1.0
                                     by: ᴎoᴎame''')
    print('''(\033[1;32m1\033[m) Install
(\033[1;32m0\033[m) Exit
    ''')

    def opcao():
        resp = input('(\033[1;32m?\033[m) ')
        if resp == '1':
            system('clear')
            print('''
  _   _   _   _   _   _   _   _   _
 / \ / \ / \ / \ / \ / \ / \ / \ / \ 
( \033[1;32mS\033[m | \033[1;32mi\033[m | \033[1;32mm\033[m | \033[1;32mp\033[m | \033[1;32ml\033[m | \033[1;32me\033[m | \033[1;32mA\033[m | \033[1;32mr\033[m | \033[1;32mc\033[m )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ v1.0
                                     by: ᴎoᴎame            
            ''')
            # Clone from Github
            system('git clone https://github.com/kadu247/SimpleArc.git /tmp/SimpleArc')
            sleep(2)
            print('\033[1;32mOK\033[m\n')
            # Make directory
            sleep(2)
            print('Creating directories...')
            sleep(2)
            system('sudo mkdir /usr/share/icons/SimpleArc')
            sleep(2)
            print('\033[1;32mOK\033[m\n')
            print('Copying files...')
            system('sudo cp -R /tmp/SimpleArc/src/* /usr/share/icons/SimpleArc')
            print('\033[1;32mOK\033[m\n')
            sleep(2)
            print('Successfully installed :)\n\033[1;32mBye...\033[m\n')
            sleep(2)
            exit()
        elif resp == '0':
            print('\n\033[1;32mBye...\033[m\n')
            sleep(2)
            exit()
        else:
            print('\n\033[1;31mError:\033[m Press "\033[1;32m1\033[m" to install or "\033[1;32m0\033[m" to exit\n')
            sleep(2)
            system('clear')
            inicio()

    opcao()


inicio()
