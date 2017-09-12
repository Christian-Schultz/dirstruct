# Dirstruct - a simple tool to create a directory structure
Dirstruct is a simple python script that takes a file with a list of directories as input and creates the directories in the specified structure

# Help
usage: dirstruct [-h] [--root ROOT] [--verbose] [--debug] [--version]
                 [--remove]
                 dirfile

Create a directory structure from file. Directories in the definition file should be separated by newlines and should follow the UNIX path convention. 
The root directory of the directory structure can be controlled by the --root parameter.

positional arguments:
  dirfile               the file containing the directory structure.

optional arguments:
  -h, --help            show this help message and exit
  --root ROOT, -r ROOT  the root path where the directory structure should be
                        created. Will be created if it does not exist Default:
                        Current directory.
  --verbose, -v         verbose mode
  --debug               print debug information. Will also toggle verbose
                        mode.
  --version             show program's version number and exit
  --remove              Inverse - remove directories instead of creating them.
                        Will not remove recursively. Default false.

Example:
If the input dirfile contains the following:
dir1/subdir1/
dir2/subdir2/
Then "dirstruct dirfile" will create dir1/subdir1 and dir2/subdir2 in the current directory.
