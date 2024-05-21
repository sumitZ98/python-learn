import sys


def Add(a,b):
    return (a+b)

def Sub(a,b):
    return (a-b)
    
def Mul(a,b):
    return (a*b)

def Div(a,b):
    return (a/b)

# command line input/Arguments
num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "Add":
    output = Add(num1,num2)
    print(output)


# Enviournment Variables(ENV) is used when using sensitive info
