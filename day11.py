class a_monkey:
    def __init__(self, name, items, operation, test_mod, pass_test, fail_test):
        self.name = name
        self.items = items
        self.operation = operation
        self.test_mod = test_mod
        self.pass_test = pass_test
        self.fail_test = fail_test
        self.inspects = 0
        self.common_mod = 0
        
    def process_worry(self, init_worry):
        old = init_worry
        return eval(self.operation) 
    
    def test(self, number):
        if (number % self.common_mod) % self.test_mod == 0:
            return self.pass_test, (number % self.common_mod)
        elif number % self.test_mod == 0:
            return self.pass_test, number
        else:
            return self.fail_test, number
    
def calc_monkey(input):
    input = input.split('\n')
    monkeys = []
    name = ''
    items = []
    for x in range(0, len(input)):
        if 'Monkey' in input[x]:
            name = [int(s) for s in input[x] if s.isdigit()]
        if 'Starting items' in input[x]:
            items = ([int(x) for x in filter(str.isdigit, input[x].replace(',', ' ').split(' '))])
        if 'Operation' in input[x]:
            operation = input[x].split('= ')[1]
        if 'Test:' in input[x]:
            test_mod = [int(x) for x in filter(str.isdigit, input[x].replace(',', ' ').split(' '))][0] 
            pass_test = [int(x) for x in filter(str.isdigit, input[x+1].replace(',', ' ').split(' '))][0] 
            fail_test = [int(x) for x in filter(str.isdigit, input[x+2].replace(',', ' ').split(' '))][0] 
        if input[x] == '' or x+1 == len(input):
            monkeys.append(a_monkey(name, items, operation, test_mod, pass_test, fail_test))
            continue
            
    #calculate common mod:
    product = 1
    for x in [x.test_mod for x in monkeys]:
        product *= x
    for x in monkeys:
        x.common_mod = product
    
    for round in range(0,10000):
        #print(round)
        for monkey in monkeys:
            #print("Monkey ", monkey.name)
            for item in monkey.items:
                monkey.items = monkey.items[1:]
                #print("Item ", item)
                #print("New worry ", monkey.process_worry(item))
                #print ("Divided worry ", monkey.process_worry(item)//3)
                new_worry = monkey.process_worry(item)
                monkey.inspects +=1
                #print("Test result ", monkey.test(monkey.process_worry(item)//3))
                throw_to, new_worry = monkey.test(new_worry)
                #print(throw_to)
                monkeys[throw_to].items.append(new_worry)
        #print([x.items for x in monkeys])

    sorted_inspects = sorted([x.inspects for x in monkeys])[::-1]
    print(sorted_inspects)
    return sorted_inspects[0]*sorted_inspects[1]
