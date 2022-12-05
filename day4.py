def fully_contained_pairs(arr):
    
    count = 0 
    count_overlap_at_all = 0
    
    for pair in arr:

        pair_a, pair_b = pair.split(',')
        
        pair_a = [int(x) for x in pair_a.split('-')]
        pair_b = [int(x) for x in pair_b.split('-')]

        a_area = range(pair_a[0], pair_a[1]+1)
        b_area = range(pair_b[0], pair_b[1]+1)
        
        if (set(a_area)).issubset(set(b_area)) or (set(b_area)).issubset(set(a_area)):
            count +=1
        if (set(a_area)).intersection(set(b_area)) or (set(b_area)).intersection(set(a_area)):
            count_overlap_at_all +=1
        else:
            pass
        
    return count, count_overlap_at_all
    
