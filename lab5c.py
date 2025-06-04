#!/usr/bin/env python3
# Author ID: dnthakar@myseneca.ca

def add(number1, number2):
    # Add two numbers together, return the result,
    # if error return string 'error: could not add numbers'
    try:
        # Try to convert both inputs to float, then add
        result = float(number1) + float(number2)
        # Return int if both are integers, else float
        if result.is_integer():
            return int(result)
        return result
    except Exception:
        return 'error: could not add numbers'

def read_file(filename):
    # Read a file, return a list of all lines,
    # if error return string 'error: could not read file'
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except Exception:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception
