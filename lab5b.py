#!/usr/bin/env python3
# Author ID: dnthakar@myseneca.ca

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    with open(file_name, 'r') as file:
        return file.read()

def read_file_list(file_name):
    # Takes a file_name as string for a file name,
    # returns its entire contents as a list of lines without new-line characters
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    with open(file_name, 'a') as file:
        file.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    with open(file_name, 'w') as file:
        for line in list_of_lines:
            file.write(f"{line}\n")

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Reads data from first file, writes to second file, adds line numbers
    with open(file_name_read, 'r') as infile, open(file_name_write, 'w') as outfile:
        for index, line in enumerate(infile, start=1):
            outfile.write(f"{index}:{line.strip()}\n")

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
