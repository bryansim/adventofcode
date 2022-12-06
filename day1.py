def listoffood(elffood):
    
    foodlist = []
    currcount = 0
    
    for x in elffood:

        if x == '':
            foodlist.append(currcount)
            currcount=0
        else:
            x = int(x)
            currcount = x + currcount
        
    return sum(sorted(foodlist)[-3:])
