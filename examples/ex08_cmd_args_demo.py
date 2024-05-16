import sys
from myutils import is_float

def main():
    args = sys.argv[1:]  # ingore the first one
    s = sum([float(a) for a in args if is_float(a)])
    print(s)

if __name__ == '__main__':
    main()

