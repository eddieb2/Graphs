"""
Simple graph implementation
"""
from util import Stack, Queue


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph. (neighbors)
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        # Create a queue to hold nodes to visit
        to_visit = Queue()

        # Create a set to hold visited nodes
        visited = set()

        # Initialize: add the starting node to the queue
        to_visit.enqueue(starting_vertex)

        # While queue not empty:
        while to_visit.size() > 0:
            # dequeue first entry
            v = to_visit.dequeue()

            # if not visited:
            if v not in visited:
                # Visit the node (print it out)
                print(v)

                # Add it to the visited set
                visited.add(v)

                # enqueue all its neighbors
                for n in self.get_neighbors(v):
                    # print(f"Adding: {n}")
                    to_visit.enqueue(n)

        '''
        EXAMPLE EXPLAINATION
        bft(4)
            to_visit -> queue -> 4// (6//,7//) (3//) (1//) (5//) (2//) (3//) (3//,4//)
                START -> 4, 
                    NOT IN VISITED
                        print           -> 4,6,7,3,1,5,2
                        add to visited   -> 4,6,7,3,1,5,2
                        enqueue neighbors -> 6,7 -> 3 -> 1 -> 5 -> 2 -> 3 ->3,4
                    IN VISITED
                        skipped ->
            visted   -> set   ->  4,6,7,3,1,5,2
            
            1. choose starting node
            2. dequeue node while to_visited is > 0
            3. is node in visited? 
                NO? then print, add to visited, loop through neighbors and enqueue all neighbors
                YES? dequeue node and continue loop until len 0
        '''

    def dft(self, starting_vertex):
        # Create a stack to hold nodes to visit
        to_visit = Stack()

        # Create a set to hold visited nodes
        visited = set()

        # Initialize: add the starting node to the stack
        to_visit.push(starting_vertex)

        # While STACK not empty:
        while to_visit.size() > 0:
            # remove the last entry
            v = to_visit.pop()

            # if LAST ENTRY of the stack not visited:
            if v not in visited:
                print(v)

                # Add it to visited
                visited.add(v)

                # add all its neighbors to the end of the stack
                for n in self.get_neighbors(v):
                    to_visit.push(n)

    def dft_recursive(self, starting_vertex, visited=None):

        if visited is None:
            visited = set()

        visited.add(starting_vertex)
        print(starting_vertex)

        for n in self.get_neighbors(starting_vertex):
            if n not in visited:
                self.dft_recursive(n,visited)

    def bfs(self, starting_vertex, destination_vertex):

        to_visit = Queue()
        to_visit.enqueue([starting_vertex])

        #
        while to_visit.size() > 0:
            v = to_visit.dequeue()
            last_vert = v[-1]

            if last_vert == destination_vertex:
                return v

            for n in self.get_neighbors(last_vert):
                to_visit.enqueue(v + [n])

    def dfs(self, starting_vertex, destination_vertex):

        to_visit = Stack()
        to_visit.push([starting_vertex])

        while to_visit.size() > 0:
            path = to_visit.pop()
            v = path[-1]

            if v == destination_vertex:
                return path

            for n in self.get_neighbors(v):
                to_visit.push(path + [n])

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[]):
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for n in self.get_neighbors(starting_vertex):
            if n not in path:
                temp_path = self.dfs_recursive(n, destination_vertex, path)
                if temp_path: return temp_path

        return None


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
    # print(graph.vertices)

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
    # print('BFT START')
    # print(graph.bft(4))
    # print('DFT END')
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # print('DFT START')
    graph.dft(4)
    # print('DFT END')
    # graph.dft_recursive(1)

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
