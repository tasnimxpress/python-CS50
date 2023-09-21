# convert text emoji to icon emoji
def convert(input):
    input = input.replace(":)" , "🙂")
    input = input.replace(":(" , "🙁")
    return input


# take input from user then convert using convert function
def main():
    user_input = input('write with emoji: ')
    convert_face = convert(user_input)
    print(convert_face)

main() 