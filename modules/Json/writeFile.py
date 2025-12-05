import json
from typing import Any

def changeData( data: dict, key: str, value: Any ) -> dict:
    data[ f'{ key }' ] = value
    return data

def writeFile( path: str, data: dict ) -> None:
    """
    write to a json file of a given path.
    """
    with open( f'data/{ path }', 'w' ) as file:
        json.dump( data, file, indent=4 )
        return
    
