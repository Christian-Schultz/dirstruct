import argparse
import os
__version__ = 0.1

description = 'Create a directory structure from file. Directories in the definition file should be separated by ' \
              'newlines and should follow the UNIX path convention. '

epilog = "Example:" \
         "\n" \
         "If the input dirfile contains the following:" \
         "\ndir1/subdir1/" \
         "\ndir2/subdir2/\n" \
         'Then "dirstruct dirfile" will create dir1/subdir1 and dir2/subdir2 in the current path.'

call_path = os.getcwd()

parser = argparse.ArgumentParser(prog='dirstruct', description=description, epilog=epilog, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('dirfile',  type=str, help='the file containing the directory structure')
parser.add_argument('--path', '-p', dest='path', action='store', default=call_path,
                    help='the root path where the directory structure should be created. Default: Current directory')
parser.add_argument('--verbose', '-v', action='store_true', help='verbose mode', default=False)
parser.add_argument('--debug', action='store_true', help='print debug information', default=False)
parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=__version__))
parser.add_argument('--relative', action='store_true', help='specifies whether the paths in the input file are '
                                                            'relative or absolute paths. Default true', default=True)
parser.add_argument('--remove', action='store_true', help='Inverse - remove directories instead of creating them. '
                                                          'Will not remove recursively. Default false', default=False)


args = parser.parse_args()

dirfile = os.path.realpath(args.dirfile)

if args.debug:
    print("call_path: %s" % call_path)
    print("dir_file: %s" % dirfile)
    print("parser: %s " % parser.parse_args())

dirs = []
with open(dirfile, 'r') as f:
    for line in f:
        d = line.strip()
        if args.relative:
            d = os.path.realpath(call_path + os.sep + d)
        if not args.remove:
            if os.path.exists(d):
                if args.verbose:
                    "%s already exists, skipping" % d
                continue
            if args.verbose:
                print("mkdir %s" % d)

                    #os.makedirs(d)
        else:
            if args.verbose:
                print("rm -r %d" % d)
            #os.rmdir(d)

print("Done")