
class MyFile:
    def __init__(self, filepath, mode='r'):
        self.filepath = filepath
        self.mode = mode
    def __enter__(self):
        try:
            self.f = open(self.filepath, self.mode)
        except FileNotFoundError as e:
            return None
        print('enter executed')
        return self.f
    def __exit__(self, type, value, traceback):
        if self.f is None:
            return
        print('type = ',type)
        print('value = ', value)
        print('traceback = ', traceback)
        print('exit executed')
        if self.f:
            self.f.close()

# ------------------------


from contextlib import contextmanager

@contextmanager
def open_file(path):
    f = None
    try:
        f = open(path, 'r', encoding='utf-8')
	print('enter executed')
        yield f
    except:
        f.close()
    finally:
        if f is not None:
            print('exit executed')
            f.close()    


with open_file('context_manager.py') as f:
    print(f.read())

print(f.closed)

