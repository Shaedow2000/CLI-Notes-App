import json
import os

def readFile( path: str ) -> str:
    dir: str = os.path.dirname( __file__ )

    json_dir: str = os.path.join( dir, f'../../data/{ path }' )
    json_dir = os.path.normpath( json_dir )

    file = open( json_dir )

    data = json.load( file )

    return data
