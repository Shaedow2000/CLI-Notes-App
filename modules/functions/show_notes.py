from data.global_py.variables import json_file
from modules.Json.read import readFile

def show_all() -> dict:
    notes: dict = readFile( json_file )[ 'notes' ]
    return notes
