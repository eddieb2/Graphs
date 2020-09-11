from room import Room
from player import Player
from world import World
from util import Queue
from util import Stack
from random import random

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


###########################################################################
traversal_path = []
graph = {player.current_room.id: {direction:"?" for direction in player.current_room.get_exits()}}
opp_dir = {'w':'e','e':'w','s':'n','n':'s'}

# Helper Functions
def print_loc():
    print(f'Current Location: {player.current_room.id}')

# Picks a random unexplored direction
def rand_unexplored(cur_room):
    found = False
    while found is False:
        unexplored_move = random.choice(player.current_room.get_exits())
        if unexplored_move in graph[cur_room] and graph[cur_room][unexplored_move] == '?':
            return unexplored_move

# Checks if the graph rooms contain any ?s : returns True if any ?s are found
def contains_qs():
    moves = ['n','s','e','w']
    for move in moves:
        for i in range(len(graph)):
            if graph[i][move] == '?':
                return True

    return False

# Finds all unexplored exits for a room
def unexplored_exits(room):
    unexplored = []

    # Loop through all exits the in room. If exit contains a ? , add to unexplored.
    for exit in graph[room]:
        if graph[room][exit] == "?":
            unexplored.append(exit)

    # Return unexplored exits
    return unexplored

def dft(starting_room):
    # Loop until all exits are explored.
    while len(unexplored_exits(starting_room)) > 0:
        # Choose random direction to travel.
        random_direction = random.choice(unexplored_exits(starting_room))

        # Save previous room.
        prev = player.current_room.id
        # Travel in the chosen random direction.
        player.travel(random_direction)
        # Save current room after travel.
        cur = player.current_room.id
        # Add the direction moved to the traversal path.
        traversal_path.append(random_direction)

        # Initialize the key in the graph so no errors are thrown.
        if cur not in graph:
            graph[cur] = {direction: "?" for direction in player.current_room.get_exits()}

        # For the current room, this will set the opposite direction of what was just traveled, to the previous room
        # I.E - prev = {0: n:1 s:? e:? w:?}  -> cur  = {1: s:0 s:? e:? w:?}
        graph[cur][opp_dir[random_direction]] = prev

        # For the previous room, set the direction moved, to the current room we're on.
        graph[prev][random_direction] = cur

        # Repeat process
        starting_room = cur

def bft(node, starting_room):
    pass

def bfs(starting_room):
    pass


# Main Program - loops until 500 entries in graph
while len(graph) < len(room_graph):
    dft(player.current_room.id)


##########################################w################


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")


'''
There are a few smaller graphs in the file which you can test your traversal method on before committing to the large graph.
You may find these easier to debug.

Start by writing an algorithm that picks a random unexplored direction from the player's current room, 
travels and logs that direction, then loops. This should cause your player to walk a depth-first traversal. 
When you reach a dead-end (i.e. a room with no unexplored paths), walk back to the nearest room that does contain an unexplored path.

You can find the path to the shortest unexplored room by using a breadth-first search for a room with a '?' for an exit. 
If you use the bfs code from the homework, you will need to make a few modifications.

Instead of searching for a target vertex, you are searching for an exit with a '?' as the value. 
If an exit has been explored, you can put it in your BFS queue like normal.

BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w directions 
before you can add it to your traversal path.

If all paths have been explored, you're done!
'''

'''
--------------
  saved code
---------------

visited_exits[player.current_room.id] = []

while len(visited_exits) < len(room_graph):
    # exits for cur room
    exits = player.current_room.get_exits()

    # add all exits to available exits
    available_exits[player.current_room.id] = exits
    print(f'Avail_exits{available_exits}')

    # pick a random exit from the available exits
    # if that exit isn't in visited exits move there
    rand_move = random.choice(available_exits[player.current_room.id])

    if rand_move not in visited_exits[player.current_room.id]:
        traversal_path.append(rand_move)
        visited_exits[player.current_room.id].append(rand_move)
        player.travel(rand_move)

    print(player.current_room.id)
    print(visited_exits)
    
    -----------------------------
    
    # help fxns
def print_visited(string=None):
    print(f'{string} - Visited Exits {visited_exits}')


def print_avail(string=None):
    print(f'{string} - Available Exits {available_exits}')


# visited exits
visited_exits = {}
# available exits
available_exits = {}
# directions to travel
traversal_path = []
opp_dir = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w', }

# loop until all rooms have been visited
while len(visited_exits) < len(room_graph):
    # find all exits
    exits = player.current_room.get_exits()
    # add found exits to the available exits var
    available_exits[player.current_room.id] = exits
    # print_avail('Inside')

    # initialize visited exits with the cur room as it's key with empty arr value

    if player.current_room.id not in visited_exits:
        visited_exits[player.current_room.id] = []

    found_move = False
    # loop and generate random choice until choice isn't in visited exits, then move
    while found_move is False:

        rand_direction = random.choice(available_exits[player.current_room.id])

        if rand_direction not in visited_exits[player.current_room.id]:
            found_move = True
            # add move the traversal path
            traversal_path.append(rand_direction)
            # add exit taken to visited exit

            visited_exits[player.current_room.id].append(rand_direction)
            player.travel(rand_direction)

    print_visited()
    print(f'player loc: {player.current_room.id}')
print(traversal_path)
'''


'''
    # FOR TESTING
    order.append(player.current_room.id)

    cur_room = player.current_room.id

    # Pick random move
    random_move = rand_unexplored(player.current_room.id)

    # Move in that direction
    player.travel(random_move)

    # Adds the next room to the cur room's
    graph[cur_room][random_move] = player.current_room.id

    # Add move to graph
    graph[player.current_room.id] = {direction:"?" for direction in player.current_room.get_exits()}

    # Add the previous room the the opp direction of the random direction chosen
    graph[player.current_room.id][opp_dir[random_move]] = cur_room

    # Add direction to traversal path
    traversal_path.append(random_move)
    
    
    
    -----------------------------------------------------------------
        cur_room = player.current_room.id
    # If current room isn't in the graph, add it.
    if cur_room not in graph:
        graph[cur_room] = {direction: "?" for direction in player.current_room.get_exits()}

    # Choose random direction to travel.
    random_dir = rand_unexplored(cur_room)

    # Travel
    player.travel(random_dir)

    # Add traveled direction to the traversal path.
    traversal_path.append(random_dir)

'''