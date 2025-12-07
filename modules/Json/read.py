import json
import os

def readFile( path: str ) -> dict:
    """
    return the data contained inside a given json file.
    """

    dir: str = os.path.join( 'data', path )

    with open( dir, 'r' ) as file:
        return json.load( file )

