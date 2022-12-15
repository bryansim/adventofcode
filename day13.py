import functools

f = open("aocday13", "r")
#f = open("13test.txt", "r")

day13_input = f.read().split("\n\n")
day13_input.extend(["[[2]]\n[[6]]"])
print(day13_input)

def compare_ab(a,b):
    if (type(a) == type(b)) and type(b) == int:
        return b-a
    elif type(a) == list and type(b) == int:
        return compare_ab(a, [b])
    elif type(a) == int and type(b) == list:
        return compare_ab([a], b)
    
    for aa, bb in zip(a,b):
        #print(aa,bb)
        if compare_ab(aa,bb) == 0:
            continue
        return compare_ab(aa,bb)
        
    return len(b)-len(a)

def blah(input):
    indices = 0
    answer = 0
    for line in input:
        indices +=1
        a,b = eval(line.split("\n")[0]), eval(line.split("\n")[1])
        print(a,b, compare_ab(a,b), indices)
        if compare_ab(a,b) >= 0:
            answer += indices
        #print(a,b)
        #print(compare_ab(a,b))
        
    return answer
    
#print(blah(day13_input))
       
def sort_input(input):
    input_split = []
    for line in input:
            input_split.extend(line.split('\n'))
        
    input_dict = {x:y for y,x in enumerate(input_split)}
    input_dict_keys = list(input_dict.keys())
    input_dict_keys = (eval(x) for x in input_dict_keys)
    sorted_input_dict_keys = sorted(input_dict_keys, key=functools.cmp_to_key(compare_ab), reverse=True)
    #print(sorted_input_dict_keys)
    return sorted_input_dict_keys.index([[6]])

#109 * 184

print(sort_input(day13_input))     
