# imports from Module/ directory
from modules.Json.read import readFile
from modules.first_time_user.functions import add_user, check_first_time
from data.global_py.variables import menu, json_file
from modules.functions.create_note import create_note
import time
import os

from modules.functions.read_note import read_note 

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
            title: str = input( '--> Title: ' )
            text: str = input( '--> Text: ' )

            notes: dict = readFile( json_file )[ 'notes' ]

            keys_dict = notes.keys()
            keys: list = [ int( number ) for number in keys_dict ]
            keys.sort()

            if not keys:
                max: int = 0
            else:
                max: int = keys[ -1 ]

            id: int = max + 1
            
            create_note( id, title, text )
        elif choice == '2':
            read_id: str = input( '--> id: ' )
            print( read_note( int(read_id) ) ) 
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
