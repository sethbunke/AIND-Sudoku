assignments = []

rows = 'ABCDEFGHI'
cols = '123456789'

diagonal1 = [a[0]+a[1] for a in zip(rows, cols)]
diagonal2 = [a[0]+a[1] for a in zip(rows, cols[::-1])]

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    no_more_twins = False
    while no_more_twins is False:
        board_before = values.copy()
        #all boxes with length 2
        twins = [box for box in values.keys() if len(values[box]) == 2]
        #for each twin, get peers, and add to list if they match
        n_twins = [[box1, box2] for box1 in twins \
                       for box2 in naked_peers[box1] \
                       if set(values[box1]) == set(values[box2])] #find a match
        for twin1, twin2 in n_twins:
            t1_naked_peers = sorted(naked_peers[twin1])
            t2_naked_peers = sorted(naked_peers[twin2])
            common_peers = sorted(list(set(naked_peers[twin1] & naked_peers[twin2])))
            for peer in common_peers:
                len_values = len(values[peer])
                if len_values > 2:
                    for digit in values[twin1]:
                        #values[peer] = values[peer].replace(digit, '')
                        values = assign_value(values, peer, values[peer].replace(digit, ''))


        # for i in range(len(naked_twins)):
        #     box1 = naked_twins[i][0]
        #     box2 = naked_twins[i][1]
        #     allpeers = set(naked_peers[box1]) & set(naked_peers[box2])
        #     for apeer in allpeers:
        #         if len(set(values[apeer])) > 2:
        #             print('peer: ' + apeer + ' start values: ' +  values[apeer] + ' removing: ' + values[box1])
        #             for num in values[box1]:
        #                 values = assign_value(values, apeer,
        #                                       values[apeer].replace(num, ''))
        #             print('peer: ' + apeer + ' end values: ' +  values[apeer]) 
        if board_before == values: #what is this? 
            no_more_twins = True
    return values


#NOT WORKING
# def naked_twins(values):
#     no_more_twins = False
#     while no_more_twins == False:
#         board_before = values.copy()
#         #all boxes with length 2
#         twins = [box for box in values.keys() if len(values[box]) == 2]
#         #for each twin, get peers, and add to list if they match
#         naked_twins = [[box1,box2] for box1 in twins \
#                        for box2 in naked_peers[box1] \
#                        if set(values[box1]) == set(values[box2]) ] #find a match
#         for i in range(len(naked_twins)):
#             box1 = naked_twins[i][0]
#             box2 = naked_twins[i][1]
#             allpeers = set(naked_peers[box1]) & set(naked_peers[box2])
#             for apeer in allpeers:
#                 if len(set(values[apeer])) > 2:
#                     print('peer: ' + apeer + ' start values: ' +  values[apeer] + ' removing: ' + values[box1])
#                     for num in values[box1]:
#                         values = assign_value(values, apeer,
#                                               values[apeer].replace(num, ''))
#                     print('peer: ' + apeer + ' end values: ' +  values[apeer]) 
#         if board_before == values: #what is this? 
#             no_more_twins = True
#     return values

#initial - passes local unit test, fails server/submission tests
# def naked_twins(values):
#     no_more_twins = False
#     while no_more_twins == False:
#         board_before = values.copy()
#         #all boxes with length 2
#         twins = [box for box in values.keys() if len(values[box]) == 2]
#         #for each twin, get peers, and add to list if they match
#         naked_twins = [[box1,box2] for box1 in twins \
#                        for box2 in peers[box1] \
#                        if set(values[box1]) == set(values[box2]) ] #find a match
#         for i in range(len(naked_twins)):
#             box1 = naked_twins[i][0]
#             box2 = naked_twins[i][1]
#             allpeers = set(peers[box1]) & set(peers[box2])
#             for apeer in allpeers:
#                 if len(set(values[apeer])) > 2:
#                     for num in values[box1]:
#                         values = assign_value(values, apeer,
#                                               values[apeer].replace(num, ''))
#         if board_before == values:
#             no_more_twins = True
#     return values

def naked_twins_ORIG(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

def cross(a, b):
    "Cross product of elements in A and elements in B."
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units

#create peers with no diagonals for use in the naked twins method
naked_units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
naked_peers = dict((s, set(sum(naked_units[s],[]))-set([s])) for s in boxes)

unitlist.append(diagonal1)
unitlist.append(diagonal2)

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

# unitlist_diag = unitlist 
# unitlist_diag.append(diagonal1)
# unitlist_diag.append(diagonal2)

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    output = dict(zip(boxes, grid))
    
    for key in output.keys():
        if output[key] == '.':
            output[key] = '123456789'
    
    return output

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

# def eliminate1(values):
#     solved_values = [box for box in values.keys() if len(values[box]) == 1]
#     for box in solved_values:
#         digit = values[box]
#         for peer in peers[box]:
#             prior_values = values[peer]
#             prior_digit = (digit)
        
#             if len(values[peer]) > 1:
#                 values[peer] = values[peer].replace(digit,'')

def eliminate(values):
    for box in boxes:
        if len(values[box]) == 1:
            for peer in peers[box]:
                #values[peer] = values[peer].replace(values[box], '')
                new_value = values[peer].replace(values[box], '')
                values = assign_value(values, peer, new_value)
    return values

def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                #values[dplaces[0]] = digit
                values = assign_value(values, dplaces[0], digit)
    return values

#def reduce_puzzle(values):
#    pass

def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

# def search(values):
#     pass

def search(values):
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.        
    """
    values_dict = grid_values(grid)
    result = search(values_dict)
    return result



if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
