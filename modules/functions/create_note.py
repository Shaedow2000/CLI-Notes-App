from modules.Json.read import readFile
from modules.Json.writeFile import writeFile 
from data.global_py.variables import json_file

def create_note( id: int, title: str, text: str ) -> None:
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

