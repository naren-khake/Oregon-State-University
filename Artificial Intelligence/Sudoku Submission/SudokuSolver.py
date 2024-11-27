import itertools
import random
from copy import deepcopy

class SudokuSolver:
    
    def __init__(self, puzzle, step_limit = 1000, cellPickingMethod = "MCV", rules = list(range(1, 7))): #max number of search steps is 1000

        self.rule_mapping = {1: self.naked_singles, 2: self.hidden_singles, 3: self.nakedNum, 4: self.hidden_pairs, 5: self.nakedNum, 6: self.hidden_triples}
        self.puzzle = puzzle
        self.domain_all = self.init_domain(puzzle)
        self.cellPickingMethod = cellPickingMethod
        self.rules = rules
        self.step_limit = step_limit

        self.original_x = 0
        self.original_y = 0
        self.backtrackCount = 0
        self.rule_counter = {x:0 for x in range(1, 7)}
        self.solution = None

    def init_domain(self, puzzle):
        domain_all = []
        for i, row in enumerate(puzzle):
            domain = []
            for j, digit in enumerate(row):
                if(digit == '0'):
                    domain.append([str(x) for x in range(1, 10) if str(x) not in self.neighbor_values((i, j))])
                else:
                    domain.append([digit])
            domain_all.append(domain)
        return domain_all

    def neighbor_values(self, point):
        r, c = point
        values = []
        for (r,c) in self.neighbor_points(point):
            values.append(self.puzzle[r][c])
        return values

    def neighbor_points(self, point):
        r,c = point
        points = set()
        for i in range(len(self.puzzle)):
            points.add((r, i))
            points.add((i, c))
        for p in map(lambda x: (x[0] + ((r//3) * 3), x[1] + ((c//3) * 3)), itertools.product(range(0, 3), repeat=2)):
            points.add(p)
        points.remove(point)
        return points

    def solved_Check(self, domain_all):
        if(domain_all == False):
            return False
        for i in range(len(domain_all)):
            for j in range(len(domain_all[0])):
                if(len(domain_all[i][j]) != 1):
                    return False
        return True

    def hidden_singles(self, domain_all, change_Check):
        for i, row in enumerate(domain_all):
            for j, domain in enumerate(row):
                hidden_single = set(domain) - set(self.neighbor_values((i,j)))
                if(len(hidden_single) == 1 and len(domain) != 1):
                    domain_all[i][j] = list(hidden_single)
                    change_Check = True
        return domain_all, change_Check

    def hidden_pairs(self, domain_all, change_Check):
        for i, row in enumerate(domain_all):
            for j, domain in enumerate(row):
                for (neighbor_x, neighbor_y) in self.neighbor_points((i,j)):
                    neighbor_domain = domain_all[neighbor_x][neighbor_y]
                    hidden_pair = set(domain) - set(neighbor_domain)
                    if(len(hidden_pair) == 2 and (len(domain) > 2 and len(neighbor_domain) > 2)):
                        domain_all[i][j] = list(hidden_pair)
                        domain_all[neighbor_x][neighbor_y] = list(hidden_pair)
                        change_Check = True
                        
        return domain_all, change_Check
	
    def hidden_triples(self, domain_all, change_Check):
        for i, row in enumerate(domain_all):
            for j, domain in enumerate(row):
                for (neighbor_x, neighbor_y) in self.neighbor_points((i,j)):
                    neighbor_domain = domain_all[neighbor_x][neighbor_y]
                    hidden_pair = set(domain) - set(neighbor_domain)
                    if(len(hidden_pair) == 3 and (len(domain) > 3 or len(neighbor_domain) > 3)):
                        domain_all[i][j] = list(hidden_pair)
                        domain_all[neighbor_x][neighbor_y] = list(hidden_pair)
                        change_Check = True
        return domain_all, change_Check

    def naked_singles(self, domain_all, change_Check):
        for i, row in enumerate(domain_all):
            for j, domain in enumerate(row):
                if(len(domain) == 1):
                    for (neighbor_x, neighbor_y) in self.neighbor_points((i,j)):
                        prev_length = len(domain_all[neighbor_x][neighbor_y])
                        domain_all[neighbor_x][neighbor_y] = list(set(domain_all[neighbor_x][neighbor_y]) - set(domain))
                        if(prev_length != len(domain_all[neighbor_x][neighbor_y])):
                            change_Check = True
        return domain_all, change_Check

    def nakedNum(self, domain_all, k, change_Check):
        for i, row in enumerate(domain_all):
            for j, domain in enumerate(row):
                if(len(domain) == k):
                    for (neighbor_x, neighbor_y) in self.neighbor_points((i,j)):
                        prev_length = len(domain_all[neighbor_x][neighbor_y])
                        domain_all[neighbor_x][neighbor_y] = list(set(domain_all[neighbor_x][neighbor_y]) - set(domain))
                        if(prev_length != len(domain_all[neighbor_x][neighbor_y])):
                            change_Check = True
        return domain_all, change_Check

    def solve(self):
        if self.solution:
            return self.solution
        
        self.domain_all = self.recursiveBacktracking(self.domain_all)
        self.solution = {"Solved_Check" : self.solved_Check(self.domain_all), "domain_all": self.domain_all, "backtrackCount": self.backtrackCount, "rule_counter" : self.rule_counter}
    
        return self.solution

    def recursiveBacktracking(self, domain_all):

        if self.solved_Check(domain_all):
            return domain_all
        if(self.step_limit == self.backtrackCount):
            return False
        self.backtrackCount += 1

        cell = self.choose_cell(domain_all)
        if(cell == False):
            return False
        v_x, v_y = cell

        for value in domain_all[v_x][v_y]:
            new_domain_all = deepcopy(domain_all)
            new_domain_all[v_x][v_y] = [value]
            new_domain_all = self.constraintPropagation(new_domain_all)
            if self.rules == []:
                result = self.recursiveBacktracking(new_domain_all)

            if new_domain_all is not False:
                result = self.recursiveBacktracking(new_domain_all)

                if result is not False:
                    return result
        
        return False

    def constraintPropagation(self, domain_all):
        change_Check = True
        steps = 0
        while change_Check:
            change_Check = False
            for r in self.rules:
                rule = self.rule_mapping[r]
                if r in [3, 5]:
                    k = (2 if (r == 3) else 3)
                    (domain_all, change_Check) = rule(domain_all, k, change_Check)
                else: 
                    (domain_all, change_Check) = rule(domain_all, change_Check)

                if change_Check:
                    self.rule_counter[r] += 1
                    break
        return domain_all 
    
    def choose_cell(self, domain_all):
        if self.cellPickingMethod == "baseline":
            return self.fixedBaseline(domain_all)
        else:
            return self.MostConstraintVariable(domain_all)
        
    def MostConstraintVariable(self, domain_all):
        minLength = 10
        mcvs = []
        for i, row in enumerate(domain_all):
            for j, domain in enumerate(row):
                length = len(domain)
                if length < minLength and length > 1:
                    minLength = length

        for i, row in enumerate(domain_all):
            for j, domain in enumerate(row):
                if(len(domain) == minLength):
                    mcvs.append((i,j))

        if(len(mcvs) == 0):
            return False
        mcv = random.choice(mcvs)

        return mcv

    def fixedBaseline(self, domain_all):
        x,y = self.original_x, self.original_y
        self.original_y = (self.original_y + 1) % 9
        if (self.original_y == 0):
            self.original_x = (self.original_x + 1) % 9

        return (x,y)