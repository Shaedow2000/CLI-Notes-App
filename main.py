# imports from Module/ directory
from modules.Json.read import readFile
from modules.first_time_user.functions import add_user, check_first_time
from data.global_py.variables import menu, json_file
from modules.functions.create_note import create_note
from modules.functions.delete_note import delete_note
from modules.functions.read_note import read_note
from modules.functions.show_notes import show_all 
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
            create_note()
        elif choice == '2':
            show_all()
            read_id: str | int = input( '--> Number of the note: ' )

            if read_id.isdigit():
                try:
                    read_id = int( read_id )
                    note = read_note( read_id )
                
                    print( note )
                except KeyError:
                    print( f'!> There is no note with the id: { read_id }' )
            else:
                print( f'!> { read_id } is not found. Enter the number of a note.' )
                continue
        elif choice == '3':
            show_all() 
        elif choice == '4':
            delete_note() 
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
