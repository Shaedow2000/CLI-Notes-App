from modules.Json.read import readFile
from modules.Json.writeFile import writeFile
from modules.functions.show_notes import show_all
from data.global_py.variables import json_file

def delete_note() -> None:
    show_all()

    del_id: str | int = input( '--> Enter the number of the note: ' )

    notes: dict = readFile( json_file )[ 'notes' ]

    if del_id.isdigit():
        del_id = int( del_id )
        if del_id <= notes.__len__():
            del_id = str( del_id )
            new_notes: dict = {}
            
            del notes[ del_id ]
            
            for i in range( notes.__len__() ):
                j: int = i + 1
                if j >= int( del_id ):
                    new_notes[ f'{ j }' ] = notes[ f'{ j + 1 }' ]
                else:
                    new_notes[ f'{ j }' ] = notes[ f'{ j }' ]  
            
            
            data: dict = readFile( json_file )
            data[ 'notes' ] = new_notes

            writeFile( json_file, data )    

            print( '==> Note deleted !' )
        else:
            print( f'!> There is no note with the id: { del_id }' )
    else:
        print( f'!> { del_id } is not found. Enter the number of a note.' )
