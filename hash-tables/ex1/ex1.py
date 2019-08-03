#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

'''
    weights = list of weights
    two weights added together should equal the limit
    length = weights array length
    limit = should be the sum of two weights
'''
def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    #base case:
    if length < 2:
        return None
    
    #create return variable
    output = []

    #add each weight to hashtable
    for value in range(length):
        hash_table_insert(ht, weights[value], value)

    # set package one to be the current weight
    # set package 2 to be the difference between the current weight and the limit
    # see if that node exists in the hash table
    for val in range(length):
        package1 = weights[val]
        package2 = limit - package1
        node = hash_table_retrieve(ht, package2)

    # if the node is not none the value does exist
    # add the largest first
    # add the smaller value second
        if node is not None:
            if node > val:
                output.append(node)
                output.append(val)
            else:
                output.append(val)
                output.append(node)
    return output


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")