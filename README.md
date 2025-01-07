# narch

![](https://github.com/user-attachments/assets/55955cb8-b803-40fe-9b8a-2b8201d731b3)

# Description

// documentation written by gpt-4o

// u can build narch (use pyinstaller) instead run python script

The narchtools project provides tools for working with archives in various formats, including ZIP, RAR, and TAR. The command line can be used to create, verify, extract, and add files to archives.

# Need to install

* python3 and pip
* tarfile,zipfile,rarfile (pythons lib)

# Usage

The script is run from the command line and accepts several arguments. The main commands include:

1. create - create an archive

2. check - check the integrity of an archive

3. extract - extract files from an archive

4. add - add files to an existing archive

# Syntax

python narch.py < command > < archive_file > < files >


# Command Parameters

• < command >: The command you want to execute (create, check, extract, add).

• < archive_file >: The name of the archive file with the appropriate extension (.zip, .rar, .tar).

• < files >: A comma-separated list of files to create or add to the archive (only for create and add commands).

# Usage Examples

## Creating an Archive

Creating a ZIP archive:
```
python script.py create archive.zip file1.txt,file2.txt
```

Creating a TAR archive:
```
python script.py create archive.tar file1.txt,file2.txt
```

Creating a RAR archive (not supported):
```
python script.py create archive.rar file1.txt,file2.txt
```
Output: narch doesn't support creating .rar


## Checking an Archive

Checking a ZIP archive:
```
python script.py check archive.zip
```

Checking a RAR archive:
```
python script.py check archive.rar
```

Checking a TAR archive:
```
python script.py check archive.tar
```

## Extracting Files from an Archive

Extracting from a ZIP archive:
```
python script.py extract archive.zip output_directory/
```

Extracting from a RAR archive:
```
python script.py extract archive.rar output_directory/
```

Extracting from a TAR archive:
```
python script.py extract archive.tar output_directory/
```

## Adding Files to an Archive

Adding files to a ZIP archive:
```
python script.py add archive.zip file3.txt,file4.txt
```

Attempting to add files to a RAR archive (not supported):
```
python script.py add archive.rar file3.txt,file4.txt
```
Output: narch supports only .zip for add


# Errors and Messages

The script outputs error messages in case of incorrect file names or unsupported operations. For example:

• "Please name your file correctly!" - if the file name does not match supported formats.

• "narch doesn't support creating .rar" - if you try to create a RAR archive.

# Conclusion

The narchtools project provides a simple interface for working with archives. It allows performing basic operations on archives, such as creating, checking, extracting, and adding files. Please note the supported formats and commands for correct usage.
