#list of places the tail went
def tail_output(directions): 
    tail_log = []
    tail_relative_position = [0,0]
    tail_position = [0,0]
    
    for x in directions:
        #print (x)
        tail_relative_position = new_tail_relative_position(tail_relative_position, x) 
        y,z = resolve_tail_position(tail_relative_position) 
        #print(y,z)
        tail_relative_position = z
        tail_position = y
        tail_log.append(tail_position.copy())
    
    return tail_log
    
#how the tail moved given it's previous relative position
def resolve_tail_position(relative_tail_position): 
    new_tail_position = [0,0]
    if relative_tail_position[0] == -2: #if tail is 2 positions below,
        new_tail_position = [1,0]
        if (relative_tail_position[1] == -1) or (relative_tail_position[1] == 1): #covers diagonal case
            new_tail_position =[1,relative_tail_position[1]*-1]
        if (relative_tail_position[1] == -2) or (relative_tail_position[1] == 2):
            new_tail_position =[1,int(relative_tail_position[1]/2)*-1]
    if relative_tail_position[0] == 2:
        new_tail_position = [-1,0]
        if (relative_tail_position[1] == -1) or (relative_tail_position[1] == 1):
            new_tail_position = [-1,relative_tail_position[1]*-1]
        if (relative_tail_position[1] == -2) or (relative_tail_position[1] == 2):
            new_tail_position =[-1,int(relative_tail_position[1]/2)*-1]
    if relative_tail_position[1] == -2:
        new_tail_position = [0,1]
        if (relative_tail_position[0] == -1) or (relative_tail_position[0] == 1): 
            new_tail_position = [relative_tail_position[0]*-1,1]
        if (relative_tail_position[0] == -2) or (relative_tail_position[0] == 2): 
            new_tail_position =[int(relative_tail_position[0]/2)*-1,1]
    if relative_tail_position[1] == 2:
        new_tail_position = [0,-1]
        if (relative_tail_position[0] == -1) or (relative_tail_position[0] == 1): 
            new_tail_position = [relative_tail_position[0]*-1,-1]
        if (relative_tail_position[0] == -2) or (relative_tail_position[0] == 2):
            new_tail_position = [int(relative_tail_position[0]/2)*-1,-1]

    return new_tail_position, [relative_tail_position[0]+new_tail_position[0],relative_tail_position[1]+new_tail_position[1]]

#where the tail is given the head moved a certain direction
def new_tail_relative_position(tail_relative_position, direction):
    return [tail_relative_position[0]-direction[0],tail_relative_position[1]-direction[1]]

#given a list of directions, trace where the node went
def retrace(log):
    tail_log = []
    tail_position = [0,0]
    
    for x in log:
        tail_position = [tail_position[0]+x[0],tail_position[1]+x[1]]
        tail_log.append(tail_position)
    
    return tail_log
    
#convert input into a list of directions
def converted_input(directions):
    coord_dir = []
    for line in directions:
        where = line.split(' ')[0]
        how_many_times = int(line.split(' ')[1])
        for i in range(0,how_many_times):
            if where == "U":
                coord_dir.append([1,0])
            if where == "D":
                coord_dir.append([-1,0])
            if where == "L":
                coord_dir.append([0,-1])
            if where == "R":
                coord_dir.append([0,1])
    return coord_dir    
    
def answer(initial_directions, number_of_tails):

    for x in range(0, number_of_tails):
        print("processing tails", x)
        initial_directions = tail_output(initial_directions)

    tail_visited = {'0,0':1}
    retraced = retrace(initial_directions)
    for y in retraced:
        try:
            tail_visited[','.join([str(x) for x in y])] += 1
        except KeyError:
            tail_visited[','.join([str(x) for x in y])] = 1

    return tail_visited, len(tail_visited.keys())
