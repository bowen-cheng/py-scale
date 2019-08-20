import fileinput


def in_place_file_processor(file_name, keyword, replacement):
    """
    Optional in-place filtering (https://docs.python.org/3.7/library/fileinput.html)

    if the keyword argument inplace=True is passed to fileinput.input() or to the FileInput constructor, the file is
    moved to a backup file and standard output is directed to the input file (if a file of the same name as the backup
    file already exists, it will be replaced silently).

    This makes it possible to write a filter that rewrites its input file in place.

    If the backup parameter is given (typically as backup='.<some extension>'), it specifies the extension for the
    backup file, and the backup file remains around; by default, the extension is '.bak' and it is deleted when the
    output file is closed. In-place filtering is disabled when standard input is read.
    """
    print('Replacing keywords in file...')
    with fileinput.FileInput(file_name, inplace=True, backup='.bak') as input_file:
        for line in input_file:
            if keyword in line:
                line = line.replace(keyword, replacement)
            print(line, end='')  # stdout is re-directed to the input file


if __name__ == '__main__':
    in_place_file_processor('file_name', 'keyword', 'replacement')
