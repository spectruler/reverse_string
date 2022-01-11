import sys 


def reverse(string):
    return string[::-1]

if len(sys.argv) == 2:
    string = sys.argv[1]
    print(reverse(string))
else:
    string = input('Enter a string: ')
    print(reverse(string))