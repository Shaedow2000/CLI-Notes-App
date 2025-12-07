from modules.Json.read import readFile
from data.global_py.variables import json_file
from modules.functions.show_notes import show_all

def read_note() -> None:
    notes: dict = readFile( json_file )[ 'notes' ]

    show_all()

    read_id: str | int = input( '--> Number of the note: ' )

    if read_id.isdigit():
        try:
            read_id = int( read_id )
            print( '\n|-> Title: ', notes[ str( read_id ) ][ 'title' ] )
            print( '|-> Text: ', notes[ str( read_id ) ][ 'text' ], '\n' )
        except KeyError:
            print( f'!> There is no note with the id: { read_id }' )
    else:
        print( f'!> { read_id } is not found. Enter the number of a note.' )

    

