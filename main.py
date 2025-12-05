# imports from Module/ directory
from modules.first_time_user.functions import add_user, check_first_time

# main function
def main():
    """
    main function of the program.
    """

    while True:
        print( 'later...' )
        break


# the program starts here
if __name__ == '__main__':
    if check_first_time():
        add_user()
        main()
    else:
        main()
