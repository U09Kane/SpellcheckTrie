
# ===== Array Rotation  ===================================================== #

def array_left_rotation(a, n, k):
    rotated_array = ['B']*n

    for index, element in enumerate(a):
        new_index = (index - k) % n
        rotated_array[new_index] = element
        
    return rotated_array


# ===== Anagrams ============================================================ 

def number_needed(a, b):

    char_count_first = get_char_counts(a)
    char_count_second = get_char_counts(b)

    return delta(char_count_first, char_count_second)


def get_char_counts(array):  # array of characters
    char_value_array = [0] * 128

    for i in array:
        char_value_array[ord(i)] += 1

    return char_value_array

def delta(first_array, second_array):
    difference = 0
    for i in range(127):
        difference += abs(first_array[i] - second_array[i])

    return difference



# ===== Ransom Note ========================================================= #

# magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
# ransom = ['give', 'one', 'grand', 'today', 'four']

def can_make_ransom(magazine, ransom):

    if len(ransom) > len(magazine):  # sanity check
        return False

    word_dict = {}
    for word in magazine:

        if word not in word_dict:
            word_dict[word] = 1

        else:  # if word already in dict; update count
            word_dict[word] += 1

    for word in ransom:

        if word not in word_dict or word_dict[word] == 0:
            return False
        else:
            word_dict[word] -= 1

    return True


# ===== Linked-List Cycle Detection ========================================= #

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head == None:  # Sanity check
        return False
    
    fast_node = head.next  # Start at different positions to pass next if statement
    slow_node = head
    
    while fast_node is not None and slow_node is not None and fast_node.next is not None:
        if fast_node == slow_node: # If there is a cycle then they must meet at some point
            return True
        fast_node = head.next.next  # fast node will make 2 jumps per iteration
        slow_node = head.next
    
    return False
    



