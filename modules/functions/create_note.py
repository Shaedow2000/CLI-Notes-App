from modules.Json.read import readFile
from modules.Json.writeFile import writeFile 
from data.global_py.variables import json_file

def create_note() -> None:
    title: str = input( '--> Title: ' )
    text: str = input( '--> Text: ' )

    notes: dict = readFile( json_file )[ 'notes' ]

    keys_dict = notes.keys()
    keys: list = [ int( number ) for number in keys_dict ]
    keys.sort()

    if not keys:
        max: int = 0
    else:
        max: int = keys[ -1 ]

    id: int = max + 1
            
    data: dict = readFile( json_file )
    notes: dict = data[ 'notes' ]

    if title.replace( ' ', '' ) == '':
        title = f'Untitled #{ id }'

    if text.replace( ' ', '' ) == '':
        text = 'Nothing to see here...'

    notes.update({
        id: {
            "title": title,
            "text": text
        }
    })

    writeFile( json_file, data )

    print( '==> Note created !' )

