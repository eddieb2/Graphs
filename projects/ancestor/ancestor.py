from graph import Graph
from util import Stack

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for ancestor in ancestors:
        if ancestor[0] not in graph.vertices:
            graph.add_vertex(ancestor[0])
        if ancestor[1] not in graph.vertices:
            graph.add_vertex(ancestor[1])

        graph.add_edge(ancestor[1], ancestor[0])

    stack = Stack()
    visited = set()
    stack.push([starting_node])
    longest_path = []

    while stack.size() > 0:
        path = stack.pop()
        current_node = path[-1]

        if len(path) > len(longest_path):
            longest_path = path

        if current_node not in visited:
            visited.add(current_node)
            parents = graph.get_neighbors(current_node)

            for parent in parents:
                new_path = path+[parent]
                stack.push(new_path)


    if starting_node == longest_path[-1]:
        return -1
    else:
        print(longest_path[-1])
        return longest_path[-1]

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 1)
    # def test_earliest_ancestor(self):
    #     test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    #     self.assertEqual(earliest_ancestor(test_ancestors, 1), 10)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 2), -1)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 3), 10)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 4), -1)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 5), 4)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 6), 10)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 7), 4)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 8), 4)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 9), 4)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 10), -1)
    #     self.assertEqual(earliest_ancestor(test_ancestors, 11), -1)