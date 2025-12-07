from data.global_py.variables import json_file
from modules.Json.read import readFile

def show_all() -> None:
    notes_dict: dict = readFile( json_file )[ 'notes' ]

    for i in range( notes_dict.__len__() ):
        print( f'{ i + 1 }: ', notes_dict[ f'{ i + 1 }' ][ 'title' ] )
