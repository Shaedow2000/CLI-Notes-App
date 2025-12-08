import json

def readFile( path: str ) -> dict:
    """
    return the data contained inside a given json file.
    """

    with open( path, 'r' ) as file:
        return json.load( file )

