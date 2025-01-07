'''
╱╱╱╱╱╱╱╱╱╱╱╭╮
╱╱╱╱╱╱╱╱╱╱╱┃┃
╭━╮╭━━┳━┳━━┫╰━╮
┃╭╮┫╭╮┃╭┫╭━┫╭╮┃
┃┃┃┃╭╮┃┃┃╰━┫┃┃┃
╰╯╰┻╯╰┻╯╰━━┻╯╰╯
'''

import os
import tarfile

from zipfile import ZipFile
from rarfile import RarFile


class nZip:
    def create(fname: str, _files: list[str]) -> None:
        if ".zip" in fname:
            with ZipFile(fname, "w") as zipp:
                for files in _files:
                    if os.path.isdir(files):
                        for i in os.listdir(files):
                            zipp.write(files+i)
                    elif os.path.isfile(files) and os.path.exists(files):
                        zipp.write(files)
                    else:
                        print("File doesnt exist or dir doesnt exist")


    def check(fname: str) -> None:
        if ".zip" in fname and os.path.exists(fname):
            with ZipFile(fname,'r') as zipp:
                for i in zipp.namelist():
                    print(i)


    def extract(fname: str, dirr: str) -> None:
        if ".zip" in fname and os.path.exists(fname):
            name = fname[:-4]
            with ZipFile(fname,'r') as zipp:
                if not os.path.exists(name):
                    os.mkdir(name)
                else: pass
                zipp.extractall(path=dirr+name)
            print(f"zip was extract in {dirr+name}")

    
    def add(fname: str, _files: list[str]) -> None:
        if ".zip" in fname and os.path.exists(fname):
            with ZipFile(fname, "a") as zipp:
                for files in _files:
                    if os.path.isdir(files):
                        for i in os.listdir(files):
                            zipp.write(files+i)
                    elif os.path.isfile(files) and os.path.exists(files):
                        zipp.write(files)
                    else:
                        print("File doesnt exist or dir doesnt exist")



class nRar:
    def check(fname: str) -> None:
        if ".rar" in fname and os.path.exists(fname):
            with RarFile(fname) as rar:
                for i in rar.namelist():
                    print(i)


    def extract(fname: str, dirr: str) -> None:
        if ".rar" in fname and os.path.exists(fname):
            name = fname[:-4]
            with RarFile(fname) as rar:
                if not os.path.exists(name):
                    os.mkdir(name)
                else: pass

                rar.extractall(path=dirr+name)


class nTar:

    def _create(_name: str, _files: list[str], _compression: str) -> None:
            with tarfile.open(_name, _compression) as tar:
                for file in _files:
                    if os.path.isdir(file):
                        for i in os.listdir(file):
                            tar.add(file+i)
                    elif os.path.isfile(file) and not os.path.isdir(file):
                        tar.add(file)

    def create(fname: str, _files: list[str]) -> None:
        if ".tar.gz" in fname:
            nTar._create(fname, _files, "w:gz")
        elif "tar.xz" in fname:
            nTar._create(fname, _files, "w:xz")
        elif ".tar" in fname and not ".tar.gz" in fname and not ".tar.hz" in fname:
            nTar._create(fname, _files, "w")

    def check(fname: str) -> None:
        if '.tar' in fname and os.path.exists(fname):
            with tarfile.open(fname) as tar:
                for i in tar:
                    print(i.name)


    def extract(fname: str, dirr: str) -> None:
        if '.tar' in fname and os.path.exists(fname):
            if ".gz" in fname or ".xz" in fname:
                name,_ghz = os.path.splitext(fname)
                name,_tar = os.path.splitext(name)
            else:
                name = fname[:-4]
            with tarfile.open(fname) as tar:
                tar.extractall(path=dirr+name)

