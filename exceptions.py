# create a function with try catch which call b with try catch which call c with try catch which call d with try
# catch which call e with try catch which call f with try catch which call g with try catch which call h with try
# catch which raise an exception
def a():
    try:
        b()
    except Exception as e:
        print("a function", e)


def b():
    try:
        c()
    except Exception as e:
        print("b function", e)
        raise e


def c():
    try:
        d()
    except Exception as e:
        print("c function", e)
        raise e


def d():
    try:
        ea()
    except Exception as e:
        print("d function", e)
        raise e


def ea():
    try:
        f()
    except Exception as e:
        print("e function", e)
        raise e


def f():
    try:
        g()
    except Exception as e:
        print("f function", e)
        raise e


def g():
    try:
        a = 1 / 0
    except Exception as e:
        print("g function", e)
        raise e


a()
