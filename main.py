# imports from Module/ directory
from modules.Json.read import readFile
from modules.first_time_user.functions import add_user, check_first_time
from data.global_py.variables import menu, json_file
from modules.functions.create_note import create_note
import time
import os 

# main function
def main():
    """
    main function of the program.
    """

    print( menu )

    while True:
        choice: str = input( '=> ' ).replace( ' ', '' ).lower()

        if choice == 'q':
            print( '-> Exiting...' )
            time.sleep( 0.5 )
            break
        elif choice == 'c':
            os.system( 'cls' if os.name == 'nt' else 'clear' )
            print( menu )
        elif choice == '1':
            id: int = 0
            title: str = input( '--> Title: ' )
            text: str = input( '--> Text: ' )

            notes: dict = readFile( json_file )[ 'notes' ]

            keys = notes.keys()
            # max = max( keys )
            print(keys)
            print('still fixing')

            # fixing shit

            create_note( id, title, text )
        elif choice == '2':
            print( 'read note' )
        elif choice == '3':
            print( 'show notes' )
        elif choice == '4':
            print( 'delete note' )
        elif choice == '':
            continue 
        else:
            print( f'!>> ERROR: unknown command [ { choice } ]. Please enter one of the known commands.' )

# the program starts here
if __name__ == '__main__':
    if check_first_time():
        add_user()
        main()
    else:
        main()
