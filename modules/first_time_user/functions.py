from modules.read_Json.read import readFile

def check_first_time() -> bool:
    """
    return is the user first time using this app.
    """

    data = readFile( 'user/userInfo.json' )
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
        last_name: str = input( '- last name (optional):' )
    
        if frst_name.replace( ' ', '' ) != '':
            print( f'Hello { frst_name } { last_name }...' )
            break
        else:
            print( '!> Please enter a first name...' )
            continue
