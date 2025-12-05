from data.global_py.variables import json_file
from modules.Json.read import readFile
import time
import os

def check_first_time() -> bool:
    """
    return is the user first time using this app.
    """

    data = readFile( json_file )
    data = data.get( 'User' )

    first_time = data.get( 'first_time' )

    if first_time:
        return True
    else:
        return False


def add_user():
    """
    add user name and info to the json file.
    """

    print( '>> Welcome to the CLI note taking app !!' )
    
    while True:
        frst_name: str = input( '- enter a first name: ' )
        last_name: str = input( '- last name (optional): ' )
    
        if frst_name.replace( ' ', '' ) != '':
            print( f'Hello { frst_name } { last_name } !' )
            
            time.sleep( 1.5 )
            os.system( 'cls' if os.name == 'nt' else 'clear' ) 

            break
        else:
            print( '!> Please enter a first name...' )
            continue
