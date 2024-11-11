# Input: ["cheapair", "cheapoair", "peloton", "pelican"]
# Output:
# "cheapair": "pa"  // every other 1-2 length substring overlaps with cheapoair
# "cheapoair": "po" // "oa" would also be acceptable
# "pelican": "ca"   // "li", "ic", or "an" would also be acceptable
# "peloton": "t"    // this single letter doesn't occur in any other string

inputs: list = ["cheapair", "cheapoair", "peloton", "pelican"]
words = {}


class TrieNode:

    def __init__(self):
        # Array for child nodes of each node
        self.child = [None] * 26

        # for end of word
        self.word_end = False

def get_substrings(str) -> dict:
    str_obj = {}
    res = [str[i: j] for i in range(len(str))
           for j in range(i + 1, len(str) + 1)]
    str_obj[str] = res
    return str_obj


# Method to insert a key into the Trie
def insert_key(root, key):
    # Initialize the curr pointer with the root node
    curr = root

    # Iterate across the length of the string
    for c in key:

        # Check if the node exists for the
        # current character in the Trie
        index = ord(c) - ord('a')
        if curr.child[index] is None:
            # If node for current character does
            # not exist then make a new node
            new_node = TrieNode()

            # Keep the reference for the newly
            # created node
            curr.child[index] = new_node

        # Move the curr pointer to the
        # newly created node
        curr = curr.child[index]

    # Mark the end of the word
    curr.word_end = True


# Method to search a key in the Trie
def search_key(root, key):
    # Initialize the curr pointer with the root node
    curr = root

    # Iterate across the length of the string
    for c in key:

        # Check if the node exists for the
        # current character in the Trie
        index = ord(c) - ord('a')
        if curr.child[index] is None:
            return False

        # Move the curr pointer to the
        # already existing node for the
        # current character
        curr = curr.child[index]

    # Return true if the word exists
    # and is marked as ending
    return curr


# Create an example Trie
root = TrieNode()
arr = ["cheapair", "cheapoair", "peloton", "pelican"]
for s in arr:
    insert_key(root, s)

# One by one search strings
search_keys = ["cheapair", "cheapoair", "peloton", "pelican"]


for s in search_keys:
    t = get_substrings(s)
    # print(f"Substrings: {t}")
    for sub in t:
        print(t[sub])
        for subsub in t[sub]:
            if search_key(root,subsub):
                print(subsub)
                print("Present")
            else:
                print(subsub)
                print("Not Present")
