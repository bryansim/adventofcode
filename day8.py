#we create a hash of all the coordinates with the height of trees
#take exclude the outside
#then, we go through each view, and mark trees if they are visible, then count the markers

def map_out(input):
    
    map = {}
    for r in range(0,len(input)):
        for c in range(0,len(input[r])):
            try:
                map["{0},{1}".format(r+1,c+1)] += int(input[r][c])
            except KeyError:
                map["{0},{1}".format(r+1,c+1)] = int(input[r][c])

    visible = 0
    visible += len(input)*4 - 4 #assume square ;D

    #loop through inside, through each tree; "is this tree visible from any side?"
    #keys will be 2 to len(input)-1
    
    answer_map = map.copy()
    score_map = map.copy()
    high_score = 0
    
    for row in range(2, len(input)): 
        for column in range(2,len(input)):
            tree_height = map["{0},{1}".format(row,column)]
            #create the row and column
            #get all values for the row
            curr_row_left = [map["{0},{1}".format(row,x)] for x in range(1,len(input)+1)][0:column-1]
            curr_row_right = [map["{0},{1}".format(row,x)] for x in range(1,len(input)+1)][column:][::-1]
            curr_column_top = [map["{0},{1}".format(x,column)] for x in range(1,len(input)+1)][0:row-1]
            curr_column_bottom = [map["{0},{1}".format(x,column)] for x in range(1,len(input)+1)][row:][::-1]
            '''
            still_visible = 1
            for x in curr_row_left:
                if tree_height > int(x):
                    score +=1
                if tree_height <= int(x):
                    still_visible = 0
            if still_visible == 1:
                answer_map["{0},{1}".format(row,column)] = "x"
            
            still_visible = 1
            for x in curr_row_right:
                if tree_height <= int(x):
                    still_visible = 0
            if still_visible == 1:
                answer_map["{0},{1}".format(row,column)] = "x"
            
            still_visible = 1
            for x in curr_column_top:
                if tree_height <= int(x):
                    still_visible = 0
            if still_visible == 1:
                answer_map["{0},{1}".format(row,column)] = "x"
            
            still_visible = 1   
            for x in curr_column_bottom:
                if tree_height <= int(x):
                    still_visible = 0
            if still_visible == 1:
                answer_map["{0},{1}".format(row,column)] = "x"
            '''
            
            view_distance_l = 0
            for x in curr_row_left[::-1]:
                if tree_height > int(x):
                    view_distance_l+=1
                if tree_height <= int(x):
                    view_distance_l+=1
                    break
                
            view_distance_r = 0
            for x in curr_row_right[::-1]:
                if tree_height > int(x):
                    view_distance_r+=1
                if tree_height <= int(x):
                    view_distance_r+=1
                    break
            
            view_distance_u = 0
            for x in curr_column_top[::-1]:
                if tree_height > int(x):
                    view_distance_u+=1
                if tree_height <= int(x):
                    view_distance_u+=1
                    break
                
            view_distance_d = 0
            for x in curr_column_bottom[::-1]:
                if tree_height > int(x):
                    view_distance_d+=1
                if tree_height <= int(x):
                    view_distance_d+=1
                    break
                
            score = view_distance_l*view_distance_r*view_distance_u*view_distance_d
            score_map["{0},{1}".format(row,column)] = score
            if score > high_score:
                high_score = score
            
    visible += list(answer_map.values()).count('x')
            
    return high_score, score_map

