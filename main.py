# imports from Module/ directory
from modules.first_time_user.functions import add_user, check_first_time
from data.global_py.variables import menu
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
            print( 'create note' )
            notecreation = input( 'Enter note content: ' )
            print( f'Note created: { notecreation }' )
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
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream

#Hello hello
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
