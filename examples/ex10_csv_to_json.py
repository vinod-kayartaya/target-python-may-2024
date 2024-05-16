import sys
from myutils import csv2json

def main():
    filename = sys.argv[1] if len(sys.argv) >= 2 else input('Enter CSV filename: ')
        
    if filename[-4:].lower() != '.csv':
        print('You must supply a CSV file')
        exit(1)

    csv2json(filename)


if __name__ == '__main__':
    main()

