#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    key = "NONE"

    """
    YOUR CODE HERE
    """
    #add values to hashtable
    for airport in tickets:
        hash_table_insert(hashtable, airport.source, airport.destination)

    #create route by following None -> airport codes -> None
    for val in range(length):
        airport = hash_table_retrieve(hashtable, key)
        route[val] = airport
        key = airport

    return route