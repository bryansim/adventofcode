def detect_marker(packet):
    
    for pos in range(0,len(packet)):
        substring = packet[pos:pos+4] #14 for part 2
        count = 0
        
        for char in substring:
            if substring.count(char) > 1:
                count+=1
            else:
                pass
            
        if count ==0:
            return pos+4,substring #14 for part 2
