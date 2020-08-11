
# We are given a dataset that represents an ancestor tree
# Given an individual in the dataset, return their earliest known ancestor
# If the input individual has no parents, return -1
# Each individual is represented by an integer value

# Ancestors is an array of pairs, [(parent, child), ...]
# Each pair can be thought of as two connected vertices

# The input is never None
# There are no cycles
def earliest_ancestor(ancestors, starting_node):
    # Store parents and children in graph where, key=child and value=parent
    graph = {}

    # Add each child as the key in for each entry
    for ancestor in ancestors:
        if ancestor[1] in graph:
            graph[ancestor[1]].append(ancestor[0])
        else:
            graph[ancestor[1]] = [ancestor[0]]

    curr = starting_node
    # If the input individual is not in the graph, it has no parents
    if curr not in graph:
        return -1

    # Set the current individual
    curr = starting_node

    while True:
        # Array to store the current path of ancestors
        path = []
        # Check the array of parents for each child in the graph
        for ancestor in graph[curr]:
            # If the the parent is also a child, add it to the path
            if ancestor in graph:
                path = path + graph[ancestor]
        
        if len(path) == 0:
            return graph[curr][0]
        else:
            graph[curr] = path
    