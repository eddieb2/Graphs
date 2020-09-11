from room import Room
from player import Player
from world import World
from util import Stack
from random import random

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path = []
# ^^ You are responsible for filling traversal_path with directions that
# , when walked in order, will visit every room on the map at least once.

'''
####### Brain Storming #######

MAIN GOAL -  add moves to the traversal_path to walk all the rooms. ** eventually work on efficiency ** 
          -  to start, get player to just move all through all the rooms

What type of traversal method should we use? 
- Breadth first
        -The Breadth First Search (BFS) traversal is an algorithm, which is used to visit all of the nodes of a given graph. 
        In this traversal algorithm one node is selected and then all of the adjacent nodes are visited one by one. 
        After completing all of the adjacent vertices, it moves further to check another vertices and checks its adjacent vertices again.
- ===================> Depth first <===================
        -The Depth First Search (DFS) is a graph traversal algorithm. 
        In this algorithm one starting vertex is given, and when an adjacent vertex is found, 
        it moves to that adjacent vertex first and try to traverse in the same manner.


#########################
'''
###########################################################################
#help fxns
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
opp_dir = {'n': 's', 's': 'n', 'w': 'e' ,'e': 'w',}

# for i in range(len(room_graph)):
#     visited_exits[i] = []

# visited_exits[player.current_room.id] = []

# print_visited('Outside')
# print_avail('Outside')

# loop until all rooms have been visited
while len(visited_exits) < len(room_graph):
    # find all exits
    exits = player.current_room.get_exits()
    # add found exits to the available exits var
    available_exits[player.current_room.id] = exits
    # print_avail('Inside')

    # initialize visited exits with the cur room as it's key with empty arr value

    # visited_exits[player.current_room.id] = []
    if player.current_room.id not in visited_exits:
        visited_exits[player.current_room.id] = []
    prev_move = None
    # randomly select an exit and move there
    # add index + direction moved to visited
    found_move = False
    # loop and generate random choice until choice isn't in visited exits, then move
    while found_move is False:

        rand_direction = random.choice(available_exits[player.current_room.id])

        if rand_direction not in visited_exits:
            found_move = True
            # add move the traversal path
            traversal_path.append(rand_direction)
            # add exit taken to visited exit

            visited_exits[player.current_room.id].append(rand_direction)
            player.travel(rand_direction)


    print_visited()
    print(f'player loc: {player.current_room.id}')
print(traversal_path)


##########################################################


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
'''