#!/usr/bin/env python3
import argparse
import os
import sys
__version__ = 0.1
"""This python3 script will recursively create a directory structure as defined from a file. Each directory should be
separated by newlines. Execute the script with -h to see the different options. """

def parse_args():
    description = 'Create a directory structure from file. Directories in the definition file should be separated by ' \
                  'newlines and should follow the UNIX path convention. \n' \
                  'The root directory of the directory structure can be controlled by the --root parameter.'

    epilog = "Example:" \
             "\n" \
             "If the input dirfile contains the following:" \
             "\ndir1/subdir1/" \
             "\ndir2/subdir2/\n" \
             'Then "dirstruct dirfile" will create dir1/subdir1 and dir2/subdir2 in the current directory.'

    call_path = os.getcwd()

    parser = argparse.ArgumentParser(prog='dirstruct', description=description, epilog=epilog,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('dirfile',  type=str, help='the file containing the directory structure.')
    parser.add_argument('--root', '-r', dest='root', action='store', default=call_path,
                        help='the root path where the directory structure should be created. Will be created if it '
                             'does not exist Default: Current directory.')
    parser.add_argument('--verbose', '-v', action='store_true', help='verbose mode', default=False)
    parser.add_argument('--debug', action='store_true', help='print debug information. Will also toggle verbose mode.',
                        default=False)
    parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=__version__))
    parser.add_argument('--remove', action='store_true', help='Inverse - remove directories instead of creating them. '
                                                              'Will not remove recursively. Default false.', default=False)
    return parser.parse_args()


def main(args):

    if args.debug:
        print("Debug mode engaged")
        print("Arguments received:")
        for arg in vars(args):
            print(arg, getattr(args, arg))
        print("")
    dirfile = os.path.realpath(args.dirfile)

    verbose = args.verbose or args.debug
    
    root = os.path.expanduser(args.root)
    if not os.path.exists(root):
        os.mkdir(root)

    os.chdir(root)

    with open(dirfile, 'r') as f:
        for line in f:
            d = line.strip()

            if not args.remove:
                if os.path.exists(d):
                    if verbose:
                        print("%s already exists, skipping" % d)
                    continue
                if verbose:
                    print("mkdir %s" % d)
                if not args.debug:
                    os.makedirs(d)
            else:
                if verbose:
                    print("rm -r %s" % d)
                if not args.debug:
                    os.rmdir(d)

if __name__ == '__main__':
    args = parse_args()
    main(args)

    sys.exit()

else:
    raise ImportError("This python module is not importable. Run as python %s.py." %__name__)
