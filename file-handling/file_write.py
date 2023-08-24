
import sys

from file_read import read_file

# reading file

def write_file(filename, content):
    f = None
    try:
        f = open(filename, 'w', encoding='utf-8')
        f.write(content)
    except FileNotFoundError as e:
        print(e)
        raise e
    else:
        print('file opened successfully')
    finally:
        print('finally')
        if f is not None:
            f.close()


def append_file(filename, content):
    f = None
    try:
        f = open(filename, 'a', encoding='utf-8')
        f.write(content)
    except FileNotFoundError as e:
        print(e)
        raise e
    else:
        print('file opened successfully')
    finally:
        print('finally')
        if f is not None:
            f.close()


content = read_file(sys.argv[1])
write_file(sys.argv[2], content)

