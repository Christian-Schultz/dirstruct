import argparse
import os

description = 'Create a directory structure from file. Directories in the definition file should be separated by ' \
              'newlines and should follow the UNIX path convention. '

epilog = "Example:" \
         "\n" \
         "If the input dirfile contains the following:" \
         "\ndir1/subdir1/" \
         "\ndir2/subdir2/\n" \
         'Then "dirstruct dirfile" will create dir1/subdir1 and dir2/subdir2 in the current path.'

call_path = os.getcwd()

parser = argparse.ArgumentParser(description=description, epilog=epilog, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('dirfile',  type=str, help='the file containing the directory structure')
parser.add_argument('--path', '-p', dest='path', action='store', default=call_path,
                    help='the root path where the directory structure should be created. Default: Current directory')
parser.add_argument('--verbose', '-v', action='store_true', help='verbose mode', default=False)
parser.add_argument('--debug', action='store_true', help='print debug information', default=False)

args = parser.parse_args()

if args.debug:
    print(call_path)

    print(parser.parse_args())

print("Done")