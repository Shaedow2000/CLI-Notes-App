import json
import os

dir: str = os.path.dirname( __file__ )

json_dir: str = os.path.join( dir, '../../data/user/userInfo.json' )
json_dir = os.path.normpath( json_dir )

file = open( json_dir )

data = json.load( file )

print( data )

file.close()
