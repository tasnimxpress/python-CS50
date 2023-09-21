# taking user input
user_input = input('Greeting: ').strip().capitalize()


# if else for print different statement
if user_input.startswith('Hello'):
    print('$0')
elif user_input.startswith('H'):
    print('$20')
else:
    print ('$100')