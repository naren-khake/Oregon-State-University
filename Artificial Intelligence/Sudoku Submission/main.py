from SudokuSolver import SudokuSolver
from utils import load_puzzle, filled_counter, data_dict
import sys

LEVELS = ["easy", "medium", "hard", "evil"]
filled_average = {}
data_log = data_dict()

def main():
    option, cell_select = menu() #choosing inference rules and cell picking method
    if(option == 1): 
        rules = []
    elif(option == 2):
        rules = [1, 2]
    elif (option == 3):
        rules = [1, 2, 3, 4]
    elif (option == 4):
        rules = [1, 2, 3, 4, 5, 6]

    if(cell_select == 1):
        cell_picking_method = "baseline"
    else:
        cell_picking_method = "mcv"
    
    filled_counts = []
    for level in LEVELS:
        for i, puzzle in enumerate(load_puzzle("sudoku_problems.txt", level = level)):
            print(level, i)
            filled_counts.append(filled_counter(puzzle))
            solver = SudokuSolver(puzzle, cellPickingMethod = cell_picking_method, rules = rules)
            data = solver.solve()

            data_log[cell_picking_method][level]["solved"] += int(data["Solved_Check"])
            if(data["Solved_Check"]):
                data_log[cell_picking_method][level]["backtrack"].append(data["backtrackCount"])
                data_log[cell_picking_method][level]["rules"] = rules
            
        filled_average[level] = sum(filled_counts) / len(filled_counts)

    print(data_log)
    print(filled_average)
        
def menu():
    print("Choose the following options:")
    rules_select = int(input(
        '''
        Select the rules to apply:
        1. No Inference
        2. Naked Singles and Hiddle singles
        3. Naked Singles, Hidden Singles and Pairs
        4. Naked Singles, Hidden Singles, Pairs and Triples
        5. Exit

        Your choice: '''))
    if(1 > rules_select or rules_select > 4):
        sys.exit()
    
    cell_select = int(input(
        '''
        Pick cell selection method:
        1. Fixed Baseline
        2. Most Constrained cell

        Your choice: '''))
    if(cell_select not in [1, 2]):
        sys.exit()
    return rules_select, cell_select

main()