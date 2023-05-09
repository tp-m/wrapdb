#!/usr/bin/env python3
#
# libltc get-version.py
#
# Extracts versions for build:
#  - libltc package version based on $srcroot/src/ltc.h
#  - libtool version based on $srcroot/src/ltc.h
#  - macos lib version based on $srcroot/src/ltc.h
#
# Usage:
# get-version.py [--package-version | --libtool-version | --darwin-version]
import argparse
import subprocess
import os
import sys
import shutil

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Extract libltc package version or libtool version')
    group = arg_parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--libtool-version', action='store_true')
    group.add_argument('--package-version', action='store_true')
    group.add_argument('--darwin-version', action='store_true')
    args = arg_parser.parse_args()

    srcroot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

    # package version
    if args.package_version:
        package_version = None

        with open(os.path.join(srcroot, 'src', 'ltc.h'), 'r') as f:
            for line in f:
                if line.startswith('#define LIBLTC_VERSION "'):
                    package_version = line[24:].strip().rstrip('"')
                if package_version:
                    break

        if not package_version:
            print('ERROR: Could not extract package version from src/ltc.h file in', srcroot, file=sys.stderr)
            sys.exit(-1)

        print(package_version)
        sys.exit(0)

    # libtool version + darwin version
    elif args.libtool_version or args.darwin_version:
        libltc_lt_cur = None
        libltc_lt_rev = None
        libltc_lt_age = None

        with open(os.path.join(srcroot, 'src', 'ltc.h'), 'r') as f:
            for line in f:
                if line.strip().startswith('#define LIBLTC_CUR '):
                    libltc_lt_cur = line[19:].strip()
                elif line.strip().startswith('#define LIBLTC_REV '):
                    libltc_lt_rev = line[19:].strip()
                elif line.strip().startswith('#define LIBLTC_AGE '):
                    libltc_lt_age = line[19:].strip()

        if libltc_lt_cur and libltc_lt_rev and libltc_lt_age:
            libltc_lt_cur = int(libltc_lt_cur)
            libltc_lt_rev = int(libltc_lt_rev)
            libltc_lt_age = int(libltc_lt_age)
            if args.libtool_version:
              print('{}.{}.{}'.format(libltc_lt_cur - libltc_lt_age, libltc_lt_age, libltc_lt_rev))
            elif args.darwin_version:
              print('{}.{}.{}'.format(libltc_lt_cur + 1, 0, 0))
            sys.exit(0)
        else:
            print('ERROR: Could not extract libtool version from src/ltc.h file in', srcroot, file=sys.stderr)
            sys.exit(-1)
    else:
        sys.exit(-1)
