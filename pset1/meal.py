def main():
    user = input('what time is it? ')
    user = convert(user)
    if 7 <= user <= 8:
        print('breakfast time')
    elif 12 <= user <= 13:
        print('lunch time')
    elif 18 <= user <= 19:
        print('dinner time')


def convert(time):
    hours, minutes = time.split(":")
    time = float(hours)+(float(minutes)/60)
    return (time)



if __name__ == "__main__":
    main()