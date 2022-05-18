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
    words = []

    """ Put the words from that link in some kind of container (the skeleton file suggests adding each word to a
 list and joining the list into a string at the end). Once we have our first link, we can add another to it, 
 and we can repeat the following process to add more:

Make a new key out of the second word in the first key and the random word you pulled out from the 
list of words that followed it.

Look up that new key in the dictionary, and pull a new random word out of the resulting list.

Keep doing that until your program raises a KeyError."""

    

    my_list = list(chains.keys())
         #  print(my_list)

    
    random_key = choice(my_list)

    while True:    
        #  print(random_key)
        random_bridge_word = choice(chains[random_key])
        # print(random_bridge_word)
        # words.append(random_key)
        words.append(random_bridge_word)
        
    
        random_key = (random_key[1], random_bridge_word)
        # next_value = choicemy_list[new_key] 

        if random_key not in my_list:
            return ' '.join(words)
            

        # else:
        # return "".join(words)
        
    
    # print(random_bridge_word)
    
    # when given a word = it is going to access the key with that word at 
    # your code goes here

    


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
