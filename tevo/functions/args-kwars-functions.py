# * IN PYTHON MEANS UNPACKING

nums = [1,2,3,4,5]
print(nums)
print(*nums)

# IN A FUNCTION WE HAVE THE POSITION AND KEYWORD ARGUMENT

def test(x, y):
    x += 1
    y += " Test"
    print(x, y)

test(1, y= "John")






# *ARGS WE USE FOR THE POSITION

def test(value, *args):

    nvalue = 0
    print(f"The value are: {value}")
    print(f"The args are: {args}")
    for item in args:
        nvalue += value * item
        print(f"The new value are: {nvalue}")
    print(nvalue)

test(100, 1, 2, 3)




# **KWARS IT'S A 'DICTIONARY'

def test(value, **kwargs):
    value = value
    print(kwargs)
    if 'x' in kwargs:
        value += kwargs['x']
    if 'y' in kwargs:
        value += kwargs['y']
    print(value)


test(100, x=1, y=2, z=3)