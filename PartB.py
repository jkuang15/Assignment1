from PartA import tokenize, computeWordFrequencies
import sys

def countCommonTokens(file1_tokens, file2_tokens) -> int:
    '''
    Runtime: O(n)

    Takes two token lists and performs set operations to filter common tokens from each list.

    :param file1_tokens: list of tokens from file 1
    :param file2_tokens: list of tokens from file 2
    :return: length of resulting set, representative of number of common tokens
    '''
    # Get set union of file 1 and file 2 tokens
    common_tkns = set(file1_tokens) & set(file2_tokens)
    print(f"Common tokens: {common_tkns}")

    # Return length of set union, aka the total amount of common tokens
    return len(common_tkns)

if __name__ == "__main__":
    try:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
    
        tokens1 = tokenize(file1)
        tokens2 = tokenize(file2)
        print(countCommonTokens(tokens1, tokens2))
    except Exception as e:
        print(f"{e}: Incorrect number of files or other error.")
