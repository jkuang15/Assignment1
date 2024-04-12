Assignment 1: Text Processing - Jamie Kuang - jkuang9

This program uses Python.

Part A:
Contains the functions tokenize(), computeWordFrequencies(), and printFrequencies().

tokenize():
    Runtime: O(n)
    O(n) to read each char 
    O(n) to change each char to lowercase

    Reads in a text file and returns a list of the tokens in that file.
    A token is a sequence of alphanumeric characters, independent of capitalization.

    :param text_file_path: path to the text file to be read
    :return: list of the tokens in the file
computeWordFrequencies():
    Runtime: O(n), iterates over n tokens

    Counts number of occurences of each otken in token list and stores in a dictionary.

    :param tokens: list of tokens
    :return: dict, mapping of each token to number of occurrences.
printFrequencies():
    Runtime: O(nlogn)
    O(n) to iterate through the tokens and print
    O(nlogn) to sort the dictionary

    Prints out word frequency count, ordered by decreasing frequency.

    :param frequencies: dict, mapping each token to number of occurrences

Part B:
Contains the funcion countCommonTokens().

countCommonTokens():
    Runtime: O(n)

    Takes two token lists and performs set operations to filter common tokens from each list.

    :param file1_tokens: list of tokens from file 1
    :param file2_tokens: list of tokens from file 2
    :return: length of resulting set, representative of number of common tokens

How to use:
To use Part A, enter this command to the terminal in the following format:
python3 PartA.py fileName

To use Part B, enter this command to the terminal in the following format:
python3 PartB.py fileName1 fileName2