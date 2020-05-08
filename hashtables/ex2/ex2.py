class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    route = []

    database = {}

    for ticket in tickets:
        database[ticket.source] = ticket.destination

    # first find the first ticket, add it to route

    route.append(database["NONE"])

    # next loop over the other tickets
    place = database["NONE"]
    while place != "NONE":
        if place == "NONE":
            break
        else:
            route.append(database[place])
            place = database[place]
    return route
