def tally_of_results(arr):
    combinations = {
        'rockrock':3,
        'rockpaper':6,
        'rockscissors':0,
        'paperrock':0,
        'paperpaper':3,
        'paperscissors':6,
        'scissorsrock':6,
        'scissorspaper':0,
        'scissorsscissors':3,
    }
    abckey = {'A':'rock','B':'paper','C':'scissors'}
    comb1 = {'X':'rock', 'Y':'paper','Z':'scissors'}
    comb1score = {'X':1, 'Y':2,'Z':3}
    comb2 = {'X':'scissors', 'Y':'rock','Z':'paper'}
    comb3 = {'X':'paper', 'Y':'scissors','Z':'rock'}
    
    tally = 0
    for x in arr:
        match = abckey[x[0]]+comb1[x[2]]
        tally += comb1score[x[2]]+combinations[match]
    return tally
    

def simulate_results(arr):
    combinations = { #rock 1, paper, 2, scissors 3
        'rocklose':3, #0+3
        'rockdraw':4, #3+1
        'rockwin':8, #6+2
        'paperlose':1, #0+1
        'paperdraw':5, #3+2
        'paperwin':9, #6+3
        'scissorslose':2, #0+2
        'scissorsdraw':6, #3+3
        'scissorswin':7, #6+1
    }
    abckey = {'A':'rock','B':'paper','C':'scissors'}
    comb1 = {'X':'lose', 'Y':'draw','Z':'win'}
    
    tally = 0
    for x in arr:
        match = abckey[x[0]]+comb1[x[2]]
        tally += combinations[match]
    return tally
