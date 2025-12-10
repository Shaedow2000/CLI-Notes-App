# CLI Notes App
A simple yet great CLI app for taking notes made in Python.

## Prerequisites:
- Python 3.10+
- Terminal ( PowerShell / CMD )

## Installation:
1. Clone the repo:
Open your **Terminal** or **CMD**, then type:

```bash
git clone https://github.com/Shaedow2000/CLI-Notes-App.git
```

3. Change directory:
Go to the directory of the cloned repo. It's name is **CLI-Notes-App**:

```bash
cd CLI-Notes-App
```

4. Run the setup script:
Now the final step is to run the setup file. Named **setup.py**:
**Linux / MacOS**:

```bash
sudo python setup.py
```

> [!IMPORTANT]
> RUN THE PROGRAM AS **SUDO** IF YOU USE LINUX OR MACOS.

**Windows**:

```bash
python setup.py
```

4. Run the app:
Now you're all set to go !
- Just type the name of the command in the **Terminal** or **CMD**, and the program will start:

```bash
pynotes
```

## Usage:
- Commands that are in use are:
> q: quit | 1: create note | 2: read note | 3: show all | 4: delete note | c: clear screen

- When you launch the app it will ask you to enter your first name, the last name is optional.
- After that, the app starts and you can write the symbol of the command and start creating notes.
- All the commands should be writen in the **==>***.
## Global Variables:
Global variables are found in *data/global_py/variables/vars.py*.

| Variable      | Description                                 |
|---------------|---------------------------------------------|
| dir           | The absolute directory of the data/ folder. |
| json_file     | The name of the json file in use.           | 
| json_file_dir | The absolute directory of the json file.    |
| menu          | The commands that is shown in the app.      |

## Contribution:
To contribute to the project, just fork a copy of the project, and create your own brach.
### Fork:
Fork the project:

```bash
git clone https://github.com/Shaedow2000/CLI-Notes-App.git
```

### Create your own branch:
Create the branch by using:

```bash
git checkout -b branch-name
```

### Set the environement:
Start the python venv:
**Linux / MacOS**:

```bash
python3 -m venv .venv
```

- then:

```bash
source venv/bin/activate
```

**Windows**:

```bash
python -m venv venv
```

-then:
*CMD*:

```bash
venv\Scripts\activate.bat
```

*PowerShell*:

```bash
venv\Scripts\Activate.ps1
```

### Start:
Now just start coding !

## License:
This project is Licensed under the **Apache-2.0 license**
> See the *LICENSE* file for more Info.
