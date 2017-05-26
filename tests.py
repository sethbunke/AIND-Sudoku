import solution
import collections

#c = solution.cross(solution.rows, solution.cols)
"""
print('peers')
print(solution.peers)
"""

input = [1,2,3,2,1,5,6,5,5,5]

result = [item for item, count in collections.Counter(input).items() if count > 1]

#print(result)

#print(solution.peers)

test_diagonal_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
test_grid = solution.grid_values(test_diagonal_grid)

def test():
    test_diagonal_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    test_grid = solution.grid_values(test_diagonal_grid)
    solution.display(test_grid)

    print('******************')

    elim1 = solution.eliminate(test_grid)
    solution.display(elim1)


#print(solution.unitlist)

#if there is a 9 in only one box then set that box to 9
def only_choice(values):
    for unit in solution.unitlist: #go through each unit
        for digit in '123456789': #go through each digit
            #for each box in the unit (row, col, 3x3)
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values


def dia_peers_test():  
    prs = solution.peers

    # print(len(solution.unitlist))
    # print((solution.unitlist))
    test_key = 'B2'
    print(sorted(solution.peers[test_key]))
    print(len(solution.peers[test_key]))

    a1_units_with_diagonal = ['A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D4', 'E1', 'E5', 'F1', 'F6', 'G1', 'G7', 'H1', 'H8', 'I1', 'I9']


    #print(len(solution.unitlist_diag))



test()