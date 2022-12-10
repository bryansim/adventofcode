class command:
  def __init__(self, name, execute_time, value):
    self.name = name
    self.execute_time = execute_time
    self.value = value

def go_through_instructions(instructions):
    cycle = 1
    v = 1
    active_instructions = []
    executed_adds = []
    collected_answers = []
    
    while cycle <= 240:
        #when cycle starts, work on latest instruction
        try:
            active_instructions[0].execute_time -=1
        except:
            pass
        for x in active_instructions:
            if x.execute_time == 0:
                v += x.value
                executed_adds.append(x.value)
                active_instructions = active_instructions[1:] #pop executed

        #print("cycle = ", cycle)
        try:
            instruction = instructions[cycle-1]
            if instruction == "noop":
                active_instructions.append(command(instruction, 1, 0))
            if instruction.split(' ')[0] == 'addx':
                active_instructions.append(command(instruction, 2, int(instruction.split(' ')[1])))
        except IndexError:
            pass
        
        #part 1
        #signal_strength = v*cycle
        #print("v =", v, "signal_strength = ", signal_strength)
        #if cycle in [20,60,100,140,180,220]:
        #    collected_answers.append(signal_strength)
        
        #part2 
        sprite = v+2 #in the example, the spirte starts at position 3
        print(cycle, cycle%40+1, sprite)
        if (cycle < 40) & (cycle in [sprite-1,sprite,sprite+1]):
            collected_answers.append('\N{FULL BLOCK}' )
        elif (cycle >= 40) & (cycle%40+1 in [sprite-1,sprite,sprite+1]):
            collected_answers.append('\N{FULL BLOCK}' )
        else:
            collected_answers.append(' ')
        
        cycle+=1
        
    print(''.join(collected_answers[0:39]))
    print(''.join(collected_answers[40:79]))
    print(''.join(collected_answers[80:119]))
    print(''.join(collected_answers[120:159]))
    print(''.join(collected_answers[160:199]))
    print(''.join(collected_answers[200:239]))

    
    return #collected_answers
