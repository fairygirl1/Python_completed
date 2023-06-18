from multiprocessing import Process

def func():
    print('dlfkv1')

if __name__ == '__main__':
    print('dkfvj2')
    proc = Process(target=func)
    proc.start()