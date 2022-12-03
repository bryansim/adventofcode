def common_item_priority(backpack_string):
    
    pack_a = backpack_string[:(len(backpack_string)//2)]
    pack_b = backpack_string[(len(backpack_string)//2):]
    
    low = zip(range(97,123), range(1,27))
    upp = zip(range(65,93), range(27,53))
    
    alphabet_map = {chr(x):y for x,y in low}
    alphabet_map.update({chr(x):y for x,y in upp})
    
    dict_a = {x:0 for x in pack_a}
    
    for x in pack_b:
        try:
            dict_a[x]+=1
            return alphabet_map[x]
        except:
            pass
    
    return 
    
def scan_packs(arr):
    priority = 0
    for pack in arr:
        priority += common_item_priority(pack)
    return priority

def find_badges(arr):
    
    low = zip(range(97,123), range(1,27))
    upp = zip(range(65,93), range(27,53))
    alphabet_map = {chr(x):y for x,y in low}
    alphabet_map.update({chr(x):y for x,y in upp})
    
    priority = 0
    
    for indices_of_three_packs in range (0,len(arr),3):
        pack_a = set(arr[indices_of_three_packs])
        pack_b = set(arr[indices_of_three_packs+1])
        pack_c = set(arr[indices_of_three_packs+2])
        
        badge_string = "".join(pack_a.intersection(pack_b).intersection(pack_c))
        priority += alphabet_map[badge_string]
        
    return priority
