from modules.read_Json.read import readFile

def check_first_time() -> bool:
    """
    return is the user first time using this app
    """

    data = readFile('user/userInfo.json')
    data = data.get('User')

    first_time = data.get('first_time')

    if first_time:
        return True
    else:
        return False

