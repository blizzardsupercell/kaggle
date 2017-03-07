from random import randint

questioner = 'Ryan:'

inputValue = ''
while inputValue != 'exist':
    randomNumber = randint(1, 100)
    print("%s What's the number?" % questioner)

    inputValue = input()
    while inputValue != randomNumber:
        if inputValue > randomNumber:
            if inputValue > 10 * randomNumber:
                print("%s Your number is too big." % questioner)
            else:
                print("%s The number is big." % questioner)
        else:
            print("%s Your number is small." % questioner)
        inputValue = input()

    print("%s Congratulations you are right!" % questioner)

    print("\n" * 3)
