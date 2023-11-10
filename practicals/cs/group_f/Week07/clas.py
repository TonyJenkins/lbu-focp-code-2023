import sys

#A demonstration that it is really the python interpreter that is passed the CLAs as [0] is the .py file

if __name__ == '__main__':
    try:
        print(f'The first CLA is {sys.argv[1]}')
        print(f'There are {len(sys.argv) - 1} command line arguments being passed')
    except IndexError:
        print('No CLAs given')