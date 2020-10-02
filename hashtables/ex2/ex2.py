#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    dic = {}
    for i in tickets:
        dic[i.source] = i.destination
    route = []
    building_route = True
    current = 'NONE'
    while building_route:
        next = dic[current]
        route.append(next)
        current = next
        if dic[current] == 'NONE':
            route.append('NONE')
            building_route = False
    return route
