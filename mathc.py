def helpc():
    print('=== == PYCALC HELP == ===')
    print('Type ADD to perform addition.')
    print('Type SUB to perform subtraction.')
    print('Type MULT to perform multiplication')
    print('Type DIV to perform division.')
    print('Type END to end the instance.')
    print('\nPlease type your command.')

def add(num_a, num_b):
    c = num_a + num_b
    print("The answer to the addition problem is: " + str(c))

def sub(num_a, num_b):
    c = num_a - num_b
    print("The answer to the subtraction problem is: " + str(c))

def mult(num_a, num_b):
    c = num_a * num_b
    print("The answer to the multiplication problem is: " + str(c))

def div(num_a, num_b):
    c = num_a / num_b
    print("The answer to the division problem is: " + str(c))
