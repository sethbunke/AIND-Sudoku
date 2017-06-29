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
    #Populate
    test_grid = solution.grid_values(test_diagonal_grid)
    solution.display(test_grid)

    print('******************')

    #If a single value, remove from all peers
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

def show_peers(key):
    print(len(solution.peers[key]))
    print(solution.peers[key])
    print(sorted(solution.peers[key]))


#test()

#peers has diagonals in it

def test_naked(): 
    #fixed
    nt = {"G7": "2345678", "G6": "1236789", "G5": "23456789", "G4": "345678",
    "G3": "1234569", "G2": "12345678", "G1": "23456789", "G9": "24578",
    "G8": "345678", "C9": "124578", "C8": "3456789", "C3": "1234569",
    "C2": "1234568", "C1": "2345689", "C7": "2345678", "C6": "236789",
    "C5": "23456789", "C4": "345678", "E5": "678", "E4": "2", "F1": "1",
    "F2": "24", "F3": "24", "F4": "9", "F5": "37", "F6": "37", "F7": "58",
    "F8": "58", "F9": "6", "B4": "345678", "B5": "23456789", "B6":
    "236789", "B7": "2345678", "B1": "2345689", "B2": "1234568", "B3":
    "1234569", "B8": "3456789", "B9": "124578", "I9": "9", "I8": "345678",
    "I1": "2345678", "I3": "23456", "I2": "2345678", "I5": "2345678",
    "I4": "345678", "I7": "1", "I6": "23678", "A1": "2345689", "A3": "7",
    "A2": "234568", "E9": "3", "A4": "34568", "A7": "234568", "A6":
    "23689", "A9": "2458", "A8": "345689", "E7": "9", "E6": "4", "E1":
    "567", "E3": "56", "E2": "567", "E8": "1", "A5": "1", "H8": "345678",
    "H9": "24578", "H2": "12345678", "H3": "1234569", "H1": "23456789",
    "H6": "1236789", "H7": "2345678", "H4": "345678", "H5": "23456789",
    "D8": "2", "D9": "47", "D6": "5", "D7": "47", "D4": "1", "D5": "36",
    "D2": "9", "D3": "8", "D1": "36"}

    nt1 = {"G7": "1234568", "G6": "9", "G5": "35678", "G4": "23678", "G3":
    "245678", "G2": "123568", "G1": "1234678", "G9": "12345678", "G8":
    "1234567", "C9": "13456", "C8": "13456", "C3": "4678", "C2": "68",
    "C1": "4678", "C7": "13456", "C6": "368", "C5": "2", "A4": "5", "A9":
    "2346", "A8": "2346", "F1": "123689", "F2": "7", "F3": "25689", "F4":
    "23468", "F5": "1345689", "F6": "23568", "F7": "1234568", "F8":
    "1234569", "F9": "1234568", "B4": "46", "B5": "46", "B6": "1", "B7":
    "7", "E9": "12345678", "B1": "5", "B2": "2", "B3": "3", "C4": "9",
    "B8": "8", "B9": "9", "I9": "1235678", "I8": "123567", "I1": "123678",
    "I3": "25678", "I2": "123568", "I5": "35678", "I4": "23678", "I7":
    "9", "I6": "4", "A1": "2468", "A3": "1", "A2": "9", "A5": "3468",
    "E8": "12345679", "A7": "2346", "A6": "7", "E5": "13456789", "E4":
    "234678", "E7": "1234568", "E6": "23568", "E1": "123689", "E3":
    "25689", "E2": "123568", "H8": "234567", "H9": "2345678", "H2":
    "23568", "H3": "2456789", "H1": "2346789", "H6": "23568", "H7":
    "234568", "H4": "1", "H5": "35678", "D8": "1235679", "D9": "1235678",
    "D6": "23568", "D7": "123568", "D4": "23678", "D5": "1356789", "D2":
    "4", "D3": "25689", "D1": "123689"}

    nt2 = {"G7": "1234568", "G6": "9", "G5": "35678", "G4": "23678", "G3":
    "245678", "G2": "123568", "G1": "1234678", "G9": "12345678", "G8":
    "1234567", "C9": "13456", "C8": "13456", "C3": "4678", "C2": "68",
    "C1": "4678", "C7": "13456", "C6": "368", "C5": "2", "A4": "5", "A9":
    "2346", "A8": "2346", "F1": "123689", "F2": "7", "F3": "25689", "F4":
    "23468", "F5": "1345689", "F6": "23568", "F7": "1234568", "F8":
    "1234569", "F9": "1234568", "B4": "46", "B5": "46", "B6": "1", "B7":
    "7", "E9": "12345678", "B1": "5", "B2": "2", "B3": "3", "C4": "9",
    "B8": "8", "B9": "9", "I9": "1235678", "I8": "123567", "I1": "123678",
    "I3": "25678", "I2": "123568", "I5": "35678", "I4": "23678", "I7":
    "9", "I6": "4", "A1": "2468", "A3": "1", "A2": "9", "A5": "3468",
    "E8": "12345679", "A7": "2346", "A6": "7", "E5": "13456789", "E4":
    "234678", "E7": "1234568", "E6": "23568", "E1": "123689", "E3":
    "25689", "E2": "123568", "H8": "234567", "H9": "2345678", "H2":
    "23568", "H3": "2456789", "H1": "2346789", "H6": "23568", "H7":
    "234568", "H4": "1", "H5": "35678", "D8": "1235679", "D9": "1235678",
    "D6": "89", "D7": "123568", "D4": "23678", "D5": "89", "D2":
    "4", "D3": "25689", "D1": "123689"}

    nt3 = {"G7": "2345678", "G6": "1236789", "G5": "23456789", "G4": "345678",
    "G3": "1234569", "G2": "12345678", "G1": "23456789", "G9": "24578",
    "G8": "345678", "C9": "124578", "C8": "3456789", "C3": "1234569",
    "C2": "1234568", "C1": "2345689", "C7": "2345678", "C6": "236789",
    "C5": "23456789", "C4": "345678", "E5": "678", "E4": "2", "F1": "1",
    "F2": "24", "F3": "24", "F4": "9", "F5": "37", "F6": "37", "F7": "58",
    "F8": "58", "F9": "6", "B4": "345678", "B5": "23456789", "B6":
    "236789", "B7": "2345678", "B1": "2345689", "B2": "1234568", "B3":
    "1234569", "B8": "3456789", "B9": "124578", "I9": "9", "I8": "345678",
    "I1": "2345678", "I3": "23456", "I2": "2345678", "I5": "2345678",
    "I4": "345678", "I7": "1", "I6": "23678", "A1": "2345689", "A3": "7",
    "A2": "234568", "E9": "3", "A4": "34568", "A7": "234568", "A6":
    "23689", "A9": "2458", "A8": "345689", "E7": "9", "E6": "4", "E1":
    "567", "E3": "56", "E2": "567", "E8": "1", "A5": "1", "H8": "345678",
    "H9": "24578", "H2": "12345678", "H3": "1234569", "H1": "23456789",
    "H6": "1236789", "H7": "2345678", "H4": "345678", "H5": "23456789",
    "D8": "2", "D9": "47", "D6": "5", "D7": "47", "D4": "1", "D5": "36",
    "D2": "9", "D3": "8", "D1": "36"}

    test_data = nt3

    solution.display(test_data)
    result = solution.naked_twins(test_data)
    print("****************** AFTER *********************************")
    solution.display(result)


test_naked()