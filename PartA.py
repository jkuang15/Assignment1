import sys

def tokenize(TextFilePath) -> list:
    '''
    Runtime: O(n)
    O(n) to read each char 
    O(n) to change each char to lowercase

    Reads in a text file and returns a list of the tokens in that file.
    A token is a sequence of alphanumeric characters, independent of capitalization.

    :param text_file_path: path to the text file to be read
    :return: list of the tokens in the file
    '''
    # Create empty list 'tokens' to store all tokens in text file.
    tokens = list()
    try:
        # Open the text file via the provided path and read from it byte-by-byte. ('rb')
        with open(TextFilePath, 'rb') as f:
            # Read 1 byte at a time
            text = f.read(1) 
            # Initialize the current token as an empty string.
            current = ''
            # While there are still valid bytes being read, complete the loop.
            while text:
                # Check each character in the byte
                for c in text: 
                    # Check ASCII code of the byte. In between 47 and 57 is a number, in between 65 and 122 is a character. 39 is apostrophe
                    if (47 <= c <= 57) or (65 <= c <= 122) or (c == 39):
                        # If valid ASCII character, append it to current token and convert to lowercase to avoid case-sensitivity.
                        current += chr(c).lower()
                    else:
                        # Otherwise, the program has encountered a non-ASCII character. Stop parsing and add the current token as-is to the
                        # token list.
                        if current:
                            tokens.append(str(current))
                            # Reset token to empty string.
                            current = ''
                # Read the next byte.
                text = f.read(1)
            if current:
                tokens.append(str(current))
    except Exception as e:
        # Error handling for opening file path.
        print(f"Error opening file from {TextFilePath}: {str(e)}")
    
    return tokens

def computeWordFrequencies(tokenList) -> dict:
    '''
    Runtime: O(n), iterates over n tokens

    Counts number of occurences of each otken in token list and stores in a dictionary.

    :param tokens: list of tokens
    :return: dict, mapping of each token to number of occurrences.
    '''
    # Initialize empty dictionary to store word frequencies.
    freq = {}

    # For each token in the provided list, update how many times it appears in the dictionary.
    for token in tokenList:
        if token in freq:
            # Token exists
            freq[token] += 1
        else:
            # Token does not exist yet, add to dict
            freq[token] = 1
    
    return freq
    

def printFrequencies(wordCount):
    '''
    Runtime: O(nlogn)
    O(n) to iterate through the tokens and print
    O(nlogn) to sort the dictionary

    Prints out word frequency count, ordered by decreasing frequency.

    :param frequencies: dict, mapping each token to number of occurrences
    '''
    # Create sorted dictionary, sorted by decreasing order.
    sort_freq = sorted(wordCount.items(), key=lambda x: (-x[1], x[0]), reverse=False)
    # For each token-frequency pair, print out in correct format
    for token, freq in sort_freq:
        print(f"{token} -> {freq}")

if __name__ == "__main__":
    try:
        if len(sys.argv) < 1:
            raise FileNotFoundError("Not enough file names provided.")
        if len(sys.argv) > 2:
            raise FileNotFoundError("Too many file names provided.")
        file_path = sys.argv[1]
        tkns = tokenize(file_path)
        #print(tkns)
        tkn_dict = computeWordFrequencies(tkns)
        #print(tkn_dict)
        printFrequencies(tkn_dict)
    except Exception as e:
        print(f"Error: {e}")
