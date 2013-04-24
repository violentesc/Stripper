Stripper.py is a tool for those pesky password dumps and E-Mail lists.

usage: Stripper.py [-h] [-d DELIMITER] [-i INPUT] [-o OUTPUT [OUTPUT ...]]
                   [-a] [-v] [-e] [-r REPLACE]

Stripper v0.1

optional arguments:
  -h, --help            show this help message and exit
  -d DELIMITER          The char you would like to split the string by.
  -i INPUT              Input file to be parsed
  -o OUTPUT [OUTPUT ...]
                        Output file(s)
  -a                    Append to output file(s). If you do not add this
                        argument files will be over written.
  -v                    Verbose
  -e                    parse username from a E-Mail address.
  -r REPLACE            replace a char or string in the file.
