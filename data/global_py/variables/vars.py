import os

dir: str = os.path.dirname( __file__ )
json_file: str = os.path.join( 'user', 'userInfo.json' )
json_file_dir: str = os.path.join( dir, json_file )
json_file_dir = os.path.normpath( json_file_dir )

menu: str = """
q: quit | 1: create note | 2: read note | 3: show all | 4: delete note | c: clear screen
""" 
