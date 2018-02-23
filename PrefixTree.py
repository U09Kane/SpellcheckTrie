'''
    "Spellchecker via Trie"
    by Kane Maxcy
    02-14-2018

'''


class Node():

    def __init__(self, char):
        '''Initialize new node for a Trie 

        Note: recommend creating root with Node('*')

        Args:
            char (str): character to represent Node

        '''
        self.char = str(char) 
        
        # Dictionary: key = str character, value = Node(character)
        self.children = {}

        self.is_root = False
        self.is_end = False

    def insert_word(self, word, idx=0):
        '''Adds new word to Trie Structure; letter by letter

        Args:
            word:   word being inserted
            idx:    index of the current character in the word (default 0)

        Returns:
            VOID.

        '''
        if idx == len(word):
            self.is_end = True
            return

        if self.is_root and word[idx] not in self.children:
            next_node = Node(word[idx])
            self.children[word[idx]] = next_node

        elif word[idx] in self.children:
            next_node = self.children[word[idx]]

        else:
            self.children[word[idx]] = Node(word[idx])
            next_node = self.children[word[idx]]

        next_node.insert_word(word, idx + 1)

    def is_word(self, word, idx=0):
        ''' 

        '''

        if self.is_root and word[idx] in self.children:
            return self.children[word[idx]].is_word(word, idx + 1)

        if idx == len(word) or word[idx] not in self.children: 
            return False

        elif idx == len(word) - 1 and self.children[word[idx]].is_end is True:
            return True

        else:
            return self.children[word[idx]].is_word(word, idx + 1)


root = Node('*')
root.is_root = True

root.insert_word("do")
root.insert_word("dogs")
root.insert_word("doors")
root.insert_word("dives")

print(root.is_word("apple"))
print(root.is_word("zebra"))
print(root.is_word("ufo"))
print(root.is_word("popsicle"))
print(root.is_word("d"))
print(root.is_word("doo"))
print(root.is_word("dive"))
print(root.is_word("dog"))


print(root.is_word("do"))
print(root.is_word("dogs"))
print(root.is_word("doors"))
print(root.is_word("dives"))
