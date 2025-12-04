# imports from Module/ directory
from modules.first_time_user.functions import check_first_time
from modules.read_Json.read import readFile

# main function
def main():
    """
    main function of the program.
    :return:
    """

    while True:
        pass


# the program starts here
if __name__ == '__main__':
    if check_first_time():
        pass
    else:
        main()
