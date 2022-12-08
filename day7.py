#create a dictionary of a file system
#go through each line
#as you discover directories and files, add them to the file system
#key will be "/ddpgzpc/mlm", with another dictionary of type="dir" or "file", and "size" (0 for dirs)
#doesn't matter if you repeat here
#you have to keep track of where you are at any given time
#anyway, when you come to the end of the input, go through every key in your dictionary
#if it's a file, go back and reference all the dirs it's in to add to the size 
#now you should have a file system with all the sizes for dirs populated
#now you go through once more and add the dirs with <100000 bytes

def retrace(input):
    file_system = {}
    file_system["/"] = {"type":"dir","size":0}
    
    current_place = ""
    for line in input:
        if ("$ cd " in line) and ("$ cd .." not in line): #we moved to a new place
            if line.split(" ")[2]!= "/":
                current_place = current_place + "/" + line.split(" ")[2]

        if "$ cd .." in line: #we went backwards
            current_place= "/".join(current_place.split('/')[0:-1])

        if "dir" in line:
            #found a dir, add to file_system
            file_system[current_place+ "/" + line.split(" ")[1]] = {"type":"dir","size":0}
            
        if line.split(" ")[0].isdigit(): #if file
            bytes = int(line.split(" ")[0])
            file_system[current_place+ "/" + line.split(" ")[1]] = {"type":"file","size":bytes}
    
    for key in file_system:
        current_file = file_system[key]
        subdirs = ""
        if current_file["type"] == "file":
            subdirs = key.split('/')[0:-1]
            #print(key, current_file, subdirs)
            for dir_i in range(0,len(subdirs)+1):
                dir = "/".join(subdirs[0:dir_i])
                try:
                    file_system[dir]["size"]+= current_file["size"]
                except KeyError:
                    pass
    
    answer = 0
    answer2 = 700000000
    for key in file_system:
        current_file = file_system[key]
        if (current_file["type"] == "dir") & (current_file["size"]<100000):
            answer += current_file["size"]
        #constructing size of root because I'm lazy to figure out how to do it programatically
        if (current_file["type"] == "dir") & (len(key.split('/'))==2):
            file_system["/"]["size"]+= current_file["size"]
            
        #find how much we need to delete. total file space of 70000000 and need unused space of 30000000
        #print(70000000-43976281-298050)
        #print(30000000-25725669) # find smallest dir greater than 3976281
        if (current_file["type"] == "dir") & (current_file["size"] > 4274331) & (current_file["size"] < answer2):
            answer2 = current_file["size"]

    return answer2
