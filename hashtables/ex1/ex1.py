def get_indices_of_item_weights(weights, length, limit):

    database = {}

    for i in range(0, length):
        database[weights[i]] = i
    for j in range(0, length):
        needed_weight = limit - weights[j]
        if needed_weight in database:
            return (database[needed_weight], j)

