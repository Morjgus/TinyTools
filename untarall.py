#!/usr/bin/python3
# untar all tar faile in a given path. Supports compressed tar files.


import os
import argparse
import tarfile
    

def main():
    parser = argparse.ArgumentParser(description='Untar all tar in one dir.')
    parser.add_argument('path', type=str, help='path to dir containing tars')
    args = parser.parse_args()

    if os.access(args.path, (os.R_OK | os.W_OK)):
        path = args.path
        os.chdir(path)
        with os.scandir(path) as entries:
            for entry in entries:
                if tarfile.is_tarfile(entry.name):
                    print("extracting " + entry.name)
                    tf = tarfile.open(name = entry.name, mode = 'r')
                    tf.extractall()



    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                print(entry.name)


if __name__ == "__main__":
   main()            
