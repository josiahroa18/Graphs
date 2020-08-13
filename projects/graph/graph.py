"""
Simple graph implementation
"""
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            return None

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        queue = Queue()
        queue.enqueue(starting_vertex)

        visited = set()
        while queue.size() > 0:
            curr = queue.dequeue()
            if curr not in visited:
                visited.add(curr)
                print(f"{curr}")

                for neighbor in self.get_neighbors(curr):
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        stack = Stack()
        stack.push(starting_vertex)

        visited = set()

        while stack.size() > 0:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                print(f"{curr}")

                for neighbor in self.get_neighbors(curr):
                    stack.push(neighbor)

    def dft_recursive_helper(self, curr, visited):
        visited.add(curr)
        print(curr)
        for neighbor in self.get_neighbors(curr):
            if neighbor not in visited:
                self.dft_recursive_helper(neighbor, visited)

    def dft_recursive(self, starting_vertex):
        visited = set()
        self.dft_recursive_helper(starting_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        # A queue of paths from the starting vertex in BFS order
        queue = Queue()

        # Enqueue a path starting with the starting index
        queue.enqueue([starting_vertex])
        visited = set()

        while queue.size() > 0:
            # Grab the first path and the last vertex in that path
            curr_path = queue.dequeue()
            curr = curr_path[-1]

            # Check to see if this vertex has been visited
            if curr not in visited:
                # Check to see if this vertex matches our destination vertex
                if curr == destination_vertex: return curr_path
                visited.add(curr)
            
            for neighbor in self.get_neighbors(curr):
                # Add the current vertex's neighbors to the current path
                next_path = curr_path[:]
                next_path.append(neighbor)

                # Check to see if the neighbor matches our destination vertex
                if neighbor == destination_vertex:
                    return next_path
                else:
                    queue.enqueue(next_path)

    # Same alogrithm as bfs but with a queue
    def dfs(self, starting_vertex, destination_vertex):
        stack = Stack()
        stack.push([starting_vertex])

        visited = set()

        while stack.size() > 0:
            curr_path = stack.pop()
            curr = curr_path[-1]

            if curr not in visited:
                visited.add(curr)

            for neighbor in self.get_neighbors(curr):
                next_path = curr_path[:]
                next_path.append(neighbor)

                if neighbor == destination_vertex:
                    return next_path
                else:
                    stack.push(next_path)

    def dfs_recursive_helper(self, curr, destination, visited):
        if curr == destination:
            return [curr]
        
        for neighbor in self.get_neighbors(curr):
            if neighbor not in visited:
                visited.add(neighbor)
                path = self.dfs_recursive_helper(neighbor, destination, visited)

                if path is not None:
                    path.insert(0, curr)
                    return path
        

    def dfs_recursive(self, starting_vertex, destination_vertex):
        visited = set()
        visited.add(starting_vertex)
        return self.dfs_recursive_helper(starting_vertex, destination_vertex, visited)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
