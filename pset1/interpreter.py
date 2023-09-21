# taking user input
expression = input("expression: ")
x, y, z = expression.split(" ")

# converting input to integer
int_x = int(x)
int_z = int(z)

# a math interpreter
if y == '+':
    print(float(int_x + int_z))
elif y == '-':
    print(float(int_x - int_z))
elif y == '*':
    print(float(int_x * int_z))
elif y == '/':
    print(float(int_x / int_z))

else:
    print('not found')