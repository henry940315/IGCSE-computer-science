character = input("Please enter a character")
if len(character) > 1:
    print('Please just enter a character')
elif len(character) == 1:
    print(ord(character))


