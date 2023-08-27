
import sys

# reading file

def read_file(filename):
    f = None
    try:
        f = open(filename, 'r', encoding='utf-8')
    except FileNotFoundError as e:
        print(e)
        raise e
    else:
        return f.read()
    finally:
        print('finally')
        if f is not None:
            f.close()


content = read_file(sys.argv[1])
print(content)

print([ch for ch in content if ch in ['a','e','i','o','u']])

