'''
╱╱╱╱╱╱╱╱╱╱╱╭╮
╱╱╱╱╱╱╱╱╱╱╱┃┃
╭━╮╭━━┳━┳━━┫╰━╮
┃╭╮┫╭╮┃╭┫╭━┫╭╮┃
┃┃┃┃╭╮┃┃┃╰━┫┃┃┃
╰╯╰┻╯╰┻╯╰━━┻╯╰╯
'''

import sys

from narchtools import nZip,nRar,nTar

def main() -> None:
    if sys.argv[1] == "create":
        if ".zip" in sys.argv[2]:
            nZip.create(sys.argv[2], sys.argv[3].split(','))
        elif ".rar" in sys.argv[2]:
            print("narch doesn supported create .rar")
        elif "tar" in sys.argv[2]:
            nTar.create(sys.argv[2], sys.argv[3].split(','))
        else:
            print("Please name ur file correct!")

    elif sys.argv[1] == "check":
        if ".zip" in sys.argv[2]:
            nZip.check(sys.argv[2])
        elif ".rar" in sys.argv[2]:
            nRar.check(sys.argv[2])
        elif ".tar" in sys.argv[2]:
            nTar.check(sys.argv[2])
        else:
            print("Please name ur file correct!")

    elif sys.argv[1] == "extract":
        if ".zip" in sys.argv[2]:
            nZip.extract(sys.argv[2],sys.argv[3])
        elif ".rar" in sys.argv[2]:
            nRar.extract(sys.argv[2], sys.argv[3])
        elif ".tar" in sys.argv[2]:
            nTar.extract(sys.argv[2], sys.argv[3])
        else:
            print("Please name ur file correct!")

    elif sys.argv[1] == "add":
        if "zip" in sys.argv[2]:
            nZip.add(sys.argv[2],sys.argv[3].split(','))
        else:
            print("narch supported only .zip for add")

if __name__ == "__main__":
    main()