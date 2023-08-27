

import threading
from threading import Thread

def print_names_list():
    threading.Event().wait(10)
    names = ['name1', 'name2', 'name3']
    for name in names:
        print(name)

t = Thread(target=print_names_list, args=[], kwargs={})
t.start()


class MyThread(Thread):
    def __init__(self, priority):
        super().__init__()
        self.priority = priority
    def run(self):
        print('run method start')
        threading.Event().wait(5)
        print('run method end')
        

m = MyThread(10)
m.start()

m.run()


# Lock

lock = threading.Lock()

def func_exec_with_lock():
    print('lock exec start')
    with lock:
        print('execution of lock')
        threading.Event().wait(5)
    print('lock exec end')

for i in range(5):
    t = Thread(target=func_exec_with_lock, args=[], kwargs={})
    t.start()

# Barrier

barrier = threading.Barrier(2)

def func_exec_barrier():
    print('print barrier start')
    barrier.wait()
    print('print barrier end')


for i in range(2):
    t = Thread(target=func_exec_barrier, args=[], kwargs={})
    t.start()

# Semaphore


semaphore = threading.Semaphore(2)

def func_exec_semaphore():
    print('semaphore start')
    with semaphore:
        threading.Event().wait(5)
        print('end of semaphore')

for i in range(6):
    t = Thread(target=func_exec_semaphore, args=[], kwargs={})
    t.start()



