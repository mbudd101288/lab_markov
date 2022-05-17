"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    
    # your code goes here
    the_file = open(file_path).read()
    
    return the_file
    


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    words = text_string.split()
    
    # print(words)
    chains = {}
    
    for i in range (len(words)-2):
        # put i and i + 1 in a tuple and add that as a key in dict
        my_tuple = (words[i],words[i + 1])
        # print(my_tuple)
        bridge_word = words[i + 2]
        # print(bridge_word)
        
        

        if my_tuple not in chains:
            # chains[my_tuple] = bridge_list.append(bridge_word)
            
            chains[my_tuple] = [bridge_word]
        
        else:
            chains[my_tuple].append(bridge_word)
        

        # every word pair is going to be a key
        # value would be and options that could follow it (could or like would be dicitonary values)
        # the next dictionary key would be you could

    # for key, value in chains.items():
    #      print(f"{key} : {value}")
    return chains


def make_text(chains):
    """Return text from chains."""
    my_list = list(chains.keys())

    random_key = choice(my_list)
    print(random_key)
    words = []
    # when given a word = it is going to access the key with that word at 
    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
