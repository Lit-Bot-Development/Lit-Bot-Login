import pathlib

T = pathlib.Path(__file__).absolute()
print(T)

def A():
    print("Hi")
    A()

A()