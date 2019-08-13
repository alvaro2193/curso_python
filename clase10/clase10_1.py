def a(*args):
    return args

print(a(100))

def f(**kwargs):
    return kwargs

print( f(a=1, b=True, h=50, z="Hello, world!"))


def f(*args, **kwargs):
    return args, kwargs

args, kwargs = f(True, False, 3.5, message="Hello, world!", year=2014)
print(args)
print(kwargs)
