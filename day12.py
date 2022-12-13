def map_grid(input):
    output_grid = []
    acc = []
    start_row = 0
    start_column = 0
    start_position = []
    for char in input:
        if char == 'S':
            start_position = [start_row, start_column]
        if char == 'E':
            end_position = [start_row, start_column]
        if char != '\n':
            start_column +=1
            acc.append(char)
        if char == '\n':
            start_column = 0
            start_row +=1
            output_grid.append(acc)
            acc=[]
    
    grid_distance = {}
    grid_height = {}

    for i in range(0, len(output_grid)):
        for j in range(0,len(output_grid[i])):
            grid_distance['{0},{1}'.format(i,j)] = float('inf')
            
    for i in range(0, len(output_grid)):
        for j in range(0,len(output_grid[i])):
            grid_height['{0},{1}'.format(i,j)] = output_grid[i][j]

    grid_distance['{0}'.format(','.join([str(x) for x in start_position]))] = 0
    grid_height['{0}'.format(','.join([str(x) for x in end_position]))] = 'z'

    return grid_distance, grid_height, start_position, end_position

def num_of(s):
    if s.islower():
        return ord(s)-97
    else:
        return ord(s)-65+26

def traverse(input):
    unvisited , grid_height, start_position, end_position = map_grid(input)
    visited = {}
    x = 0
    
    print(end_position)
    print(start_position)

    while '{0},{1}'.format(end_position[0],end_position[1]) not in visited.keys():
        try:
            current_node = sorted(unvisited.items(), key=lambda x:x[1])[0][0]
        except:
            break
        visited[current_node] = unvisited[current_node]
        unvisited.pop(current_node)
        current_node = [int(x) for x in current_node.split(',')]
        
        possible_paths = []
        possible_paths.append([current_node[0]+1,current_node[1]])
        possible_paths.append([current_node[0]-1,current_node[1]])
        possible_paths.append([current_node[0],current_node[1]+1])
        possible_paths.append([current_node[0],current_node[1]-1])
        
        for path in possible_paths:
            path_str = '{0},{1}'.format(path[0],path[1])
            current_node_str = '{0},{1}'.format(current_node[0],current_node[1])
            try:
                if ((path[0] > -1) and (path[1] > -1)) and (num_of(grid_height[current_node_str]) >= num_of(grid_height[path_str])-1):
                    if unvisited[path_str] > visited[current_node_str]+1:
                        unvisited[path_str] = visited[current_node_str]+1
                    else:
                        pass
            except KeyError:
                pass

    
    answer = {}
    for x in visited.keys():
        if grid_height[x] == 'a':
            answer[x] = visited[x]
    
    return visited['{0},{1}'.format(end_position[0],end_position[1])] #, answer
    
