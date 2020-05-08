
def has_negatives(a):
    result = []
    database = {}

    # add all the elements to the database
    for element in a:
        if element != 0:
            database[element] = element
    # check if the negative equivalent is in the database, if so add it to result
    for element in a:
        if -element in database:
            result.append(abs(element))
    # remove duplicates
    result = list(dict.fromkeys(result))
    return result
