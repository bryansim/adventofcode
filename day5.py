starting_pos = [
    ['C','Z','N','B','M','W','Q','V'],
    ['H','Z','R','W','C','B'],
    ['F','Q','R','J'],
    ['Z','S','W','H','F','N','M','T'],
    ['G','F','W','L','N','Q','P'],
    ['L','P','W'],
    ['V','B','D','R','G','C','Q','J'],
    ['Z','Q','N','B','W'],
    ['H','L','F','C','G','T','J'],
    ]

def move_crates(starting,instructions):
    for line in instructions:
        
        l = []
        for char in line.split():
            try:
                l.append(float(char))
            except ValueError:
                pass
            
        number,pos1,pos2 = [int(x) for x in l]
        
        to_add = starting[pos1-1][-number:]
        to_add.reverse() #just comment this out for part 2
    
        starting[pos2-1].extend(to_add)
        starting[pos1-1] = starting[pos1-1][:-number]
            
   
    ans = []
    for x in starting:
        ans.append(x[-1])

    return ans
