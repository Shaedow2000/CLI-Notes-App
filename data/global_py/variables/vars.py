import os

dir: str = os.path.dirname( __file__ )
json_file: str = 'user/userInfo.test.json'
json_file_dir: str = os.path.join( dir, json_file )
json_file_dir = os.path.normpath( json_file_dir )
