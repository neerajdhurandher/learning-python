# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

a = lambda x: x + 10
print(a(5))


def myfunc(n):
    return n*n

b = lambda x: x*myfunc(x)

print(b(5))

c = lambda x, y: x*y
print(c(5, 6))

# can we create for loop inside lambda function?
# Yes, we can create for loop inside lambda function
# Example:
# This will create a list of numbers from 0 to x-1
for_loop = lambda x: [i for i in range(x)]
print(for_loop(5))
