from data.global_py.variables import json_file
from modules.Json.read import readFile
from modules.Json.writeFile import changeData, writeFile
import time
import os
import sys

def check_first_time() -> bool:
    """
    return is the user first time using this app.
    """

    data = readFile( json_file )

    first_time = data.get( 'first_time' )

    if first_time:
        return True
    else:
        return False


def add_user():
    """
    add user name and info to the json file.
    """

    try:
        print( '>> Welcome to the CLI note taking app !!' )
    
        while True:
            _frst_name: str = input( '-> enter a first name: ' )
            _last_name: str = input( '-> last name (optional): ' )
    
            frst_name: str = _frst_name.replace( ' ', '' ).capitalize()
            last_name: str = _last_name.replace( ' ', '' ).capitalize()

            if frst_name.replace( ' ', '' ) != '':
                data: dict = readFile( json_file )
                data = changeData( data, 'firstname', frst_name )
                data = changeData( data, 'lastname', last_name )
                data = changeData( data, 'first_time', False )
                writeFile( json_file, data )
           
                time.sleep( 0.75 )
                os.system( 'cls' if os.name == 'nt' else 'clear' ) 

                print( f'>> Hello { frst_name } { last_name } !' )
                print( '!> NOTE: write the command in the "=>" !' )
            
                break
            else:
                print( '!> Please enter a first name...' )
                continue
    except KeyboardInterrupt:
        print( '\n-> Exiting...' )
        time.sleep( 0.5 )
        sys.exit( 1 )
        
