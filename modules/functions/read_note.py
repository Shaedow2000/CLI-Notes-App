from modules.Json.read import readFile
from data.global_py.variables import json_file

def read_note( id: int ) -> str:
    notes: dict = readFile( json_file )[ 'notes' ]

    return notes[ str( id ) ]

