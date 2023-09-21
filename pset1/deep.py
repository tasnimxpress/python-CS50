# Defining data
data = [42, 'forty-two', 'forty two']


# taking user input
user_input = input(str("What is the Answer to the Great Question of Life, the Universe, and Everything? ")).lower().strip()


# print ans according to user_input
if user_input in str(data):
    print ('Yes')
else:
    print('No')