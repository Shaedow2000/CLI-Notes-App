import os
import sys
import platform
import shutil
import time

command: str = 'pynotes'
path: str = os.path.abspath( 'main.py' )

def unix() -> None:
    bin: str = f"/usr/local/bin/{ command }"
    script: str = f"""#!/bin/bash
python3 "{ path }" "$@"
"""

    with open( command, 'w' ) as f:
        f.write( script )

    os.chmod( command, 0o755 )

    print( '==> Creating Executable...' )
    shutil.copy( command, bin )
    os.remove( command )

    print( '|=> Created Executable command !' )
    print( f'==> Write: { command }' )

def windows() -> None:
    sys_path: list[ str ] = os.environ[ 'PATH' ].split( ';' )
    dirs = [ p for p in sys_path if p and os.path.isdir( p ) ]

    for d in dirs:
        if "Windows" in d and os.access( d, os.W_OK ):
            target_dir = d
            break
    else:
        target_dir = os.getcwd()

    target: str = os.path.join( target_dir, f'{ command }.cmd' )

    script = f"""@echo off
python "{ path }" %*
"""
    
    with open(target, "w") as f:
        f.write( script )

    print( '|=> Created Executable command !' )
    print( f'==> Write: { command }' )

if __name__ == '__main__':
    os_name: str = platform.system()
    
    print( f'-> System used: { os_name }' )
    print( '|-> Starting creating executable for the os in use...' )

    time.sleep( 0.85 )

    if os_name in ( 'Linux', 'Darwin' ):
        if os.geteuid() != 0:
            print( '!> Run program as SUDO !' )
            sys.exit( 1 )
        else:
            unix()
    elif os_name == 'Windows':
        windows()
    else:
        print( f'!> Unkown OS: { os_name }' )
