import sys
import math
import random
import itertools
from gurobipy import *


data=[]

data=[
[0, 67],
[0, 18],
[0, 59],
[0, 92],
[0, 21],
[1, 61],
[1, 85],
[1, 39],
[2, 67],
[2, 22],
[2, 87],
[2, 9],
[2, 12],
[2, 77],
[3, 80],
[3, 65],
[3, 35],
[3, 38],
[3, 95],
[3, 75],
[3, 44],
[3, 63],
[4, 0],
[4, 68],
[4, 40],
[4, 9],
[4, 59],
[5, 64],
[5, 33],
[5, 50],
[5, 40],
[5, 72],
[5, 28],
[6, 40],
[6, 44],
[6, 61],
[6, 95],
[7, 56],
[7, 74],
[7, 83],
[7, 45],
[7, 86],
[8, 64],
[8, 33],
[8, 76],
[8, 61],
[8, 79],
[9, 56],
[9, 41],
[9, 42],
[9, 28],
[10, 81],
[10, 46],
[10, 38],
[10, 77],
[11, 16],
[11, 19],
[11, 20],
[11, 86],
[12, 48],
[12, 2],
[12, 51],
[12, 42],
[13, 1],
[13, 83],
[13, 53],
[13, 89],
[13, 57],
[14, 51],
[14, 26],
[14, 19],
[14, 61],
[14, 95],
[15, 67],
[15, 69],
[15, 93],
[16, 56],
[16, 84],
[16, 93],
[16, 7],
[17, 36],
[17, 14],
[17, 12],
[17, 78],
[17, 46],
[17, 69],
[18, 51],
[18, 76],
[18, 13],
[18, 86],
[18, 45],
[19, 83],
[19, 15],
[20, 65],
[20, 46],
[21, 19],
[21, 84],
[21, 6],
[21, 25],
[21, 95],
[21, 47],
[22, 0],
[22, 33],
[22, 24],
[22, 44],
[22, 29],
[22, 62],
[23, 18],
[23, 36],
[23, 4],
[23, 74],
[23, 77],
[23, 31],
[24, 60],
[24, 67],
[24, 52],
[24, 38],
[24, 31],
[25, 9],
[25, 39],
[26, 32],
[26, 10],
[26, 50],
[26, 87],
[27, 24],
[27, 9],
[27, 83],
[27, 20],
[27, 81],
[28, 84],
[28, 78],
[28, 53],
[28, 30],
[28, 87],
[29, 64],
[29, 83],
[29, 19],
[29, 52],
[29, 25],
[29, 78],
[30, 17],
[30, 66],
[30, 21],
[30, 22],
[30, 49],
[30, 43],
[30, 82],
[30, 69],
[31, 41],
[31, 18],
[31, 67],
[32, 1],
[32, 50],
[32, 92],
[32, 29],
[33, 10],
[33, 67],
[33, 28],
[33, 31],
[34, 77],
[34, 86],
[34, 63],
[35, 66],
[35, 4],
[35, 53],
[35, 10],
[35, 94],
[35, 95],
[36, 52],
[37, 64],
[37, 59],
[37, 71],
[38, 33],
[38, 69],
[38, 73],
[38, 44],
[38, 14],
[38, 95],
[39, 48],
[39, 1],
[39, 51],
[39, 21],
[39, 86],
[39, 46],
[39, 79],
[40, 61],
[40, 87],
[40, 20],
[40, 37],
[40, 53],
[41, 72],
[41, 57],
[41, 18],
[41, 73],
[41, 47],
[42, 4],
[43, 19],
[43, 9],
[43, 11],
[43, 54],
[44, 16],
[44, 24],
[44, 36],
[44, 81],
[45, 65],
[45, 83],
[45, 37],
[45, 54],
[45, 78],
[45, 63],
[46, 49],
[46, 35],
[46, 25],
[46, 9],
[46, 31],
[47, 17],
[47, 19],
[47, 79],
[48, 34],
[48, 5],
[48, 87],
[48, 61],
[49, 48],
[49, 1],
[49, 83],
[49, 36],
[49, 39],
[49, 40],
[49, 80],
[49, 29],
[50, 95],
[51, 2],
[51, 91],
[51, 68],
[51, 88],
[51, 74],
[51, 27],
[51, 93],
[51, 62],
[51, 47],
[52, 0],
[52, 17],
[52, 90],
[52, 36],
[53, 48],
[53, 42],
[53, 87],
[53, 15],
[54, 19],
[55, 60],
[55, 18],
[55, 44],
[55, 85],
[55, 94],
[56, 75],
[56, 67],
[56, 20],
[56, 94],
[56, 7],
[56, 25],
[56, 42],
[56, 71],
[56, 92],
[56, 78],
[57, 0],
[57, 35],
[57, 76],
[58, 52],
[58, 5],
[58, 23],
[59, 84],
[59, 70],
[59, 53],
[59, 46],
[59, 47],
[60, 48],
[60, 26],
[60, 7],
[61, 17],
[61, 43],
[61, 44],
[61, 5],
[61, 55],
[62, 24],
[62, 92],
[62, 4],
[62, 86],
[62, 31],
[63, 34],
[63, 67],
[63, 61],
[63, 95],
[64, 84],
[64, 4],
[64, 54],
[64, 39],
[64, 8],
[64, 52],
[64, 71],
[64, 28],
[65, 17],
[65, 34],
[65, 84],
[65, 71],
[65, 56],
[65, 9],
[65, 44],
[65, 13],
[66, 18],
[66, 95],
[66, 21],
[66, 47],
[67, 56],
[67, 81],
[67, 35],
[67, 60],
[67, 15],
[68, 8],
[68, 49],
[68, 18],
[68, 11],
[68, 62],
[69, 83],
[69, 35],
[69, 8],
[69, 41],
[69, 92],
[69, 29],
[69, 62],
[69, 45],
[70, 17],
[70, 2],
[70, 50],
[70, 46],
[71, 0],
[71, 65],
[71, 66],
[71, 93],
[71, 73],
[71, 29],
[71, 30],
[71, 31],
[72, 32],
[72, 3],
[72, 4],
[72, 37],
[72, 11],
[72, 78],
[72, 53],
[73, 1],
[73, 35],
[73, 5],
[73, 72],
[73, 61],
[73, 77],
[73, 47],
[74, 33],
[74, 95],
[74, 5],
[74, 46],
[74, 39],
[75, 16],
[75, 64],
[75, 80],
[75, 41],
[75, 42],
[75, 74],
[75, 77],
[75, 15],
[76, 42],
[76, 5],
[76, 61],
[77, 50],
[77, 45],
[77, 70],
[78, 64],
[78, 19],
[78, 52],
[78, 53],
[78, 74],
[78, 46],
[78, 15],
[79, 17],
[79, 67],
[79, 21],
[79, 25],
[79, 41],
[79, 93],
[80, 0],
[80, 32],
[80, 35],
[80, 68],
[80, 8],
[80, 89],
[80, 93],
[80, 79],
[81, 88],
[81, 20],
[81, 85],
[81, 71],
[81, 8],
[81, 47],
[81, 28],
[81, 45],
[81, 31],
[82, 90],
[82, 44],
[82, 21],
[83, 88],
[83, 33],
[83, 89],
[84, 73],
[84, 42],
[84, 82],
[84, 22],
[85, 16],
[85, 64],
[85, 50],
[85, 35],
[85, 22],
[85, 58],
[86, 37],
[86, 40],
[86, 25],
[86, 11],
[86, 13],
[86, 62],
[86, 93],
[87, 66],
[87, 44],
[88, 33],
[88, 44],
[88, 70],
[89, 17],
[89, 66],
[89, 5],
[89, 54],
[89, 23],
[89, 26],
[89, 43],
[89, 93],
[89, 31],
[90, 25],
[90, 82],
[90, 35],
[90, 13],
[90, 22],
[91, 74],
[91, 87],
[92, 87],
[92, 13],
[92, 38],
[92, 61],
[93, 1],
[93, 37],
[94, 77],
[94, 30],
[95, 24],
[95, 93],
[95, 47],
[96, 93],
[97, 48],
[97, 53],
[97, 23],
[97, 88],
[97, 71],
[97, 7],
[97, 12],
[98, 56],
[98, 75],
[98, 76],
[99, 2],
[99, 35],
[99, 36],
[99, 66],
[99, 46],
[99, 27],
[99, 21],
[99, 22],
[99, 88],
[99, 59],
[99, 62],
[99, 95]]

#Functions to find cycles of size 2 and 3
def twoCycle(edges):

    twoCycles = {}
    for edge in edges:
        u = edge[0]
        v = edge[1]
        if (u < v and (v,u) in edges):
            twoCycles[(u,v)] = edges[(u,v)] + edges[(v,u)]
    return twoCycles

def threeCycle(nodes, edges):

    threeCycles = {}
    for edge in edges:
        u = edge[0]
        v = edge[1]
        for w in nodes:
            if (w >= u or w >= v ):
                break
            if ( (u,w) in edges and (w,v) in edges ):
                threeCycles[(u,w,v)] = edges[(u,v)] + edges[(u,w)] + edges[(w,v)]
    return threeCycles


## define the two sets of nodes: Patients and deceased donors

patients = list(set([edge[1] for edge in data]))

dead = []
for edge in data:
    if edge[0] not in patients:
        dead.append(edge[0])
dead = list(set(dead))
print(dead)

#create dictionary of edges in the graph
connection = {(data[i][0],data[i][1]) : 1 for i in range(len(data))}




## #############################################################################
# 2-way exchanges
################################################################################

nodes = range(99)
twoCycles = twoCycle(connection)

model = Model("2 way Kidney Exchange")

c = {}

for cycle in twoCycles:
    c[cycle] = model.addVar(vtype=GRB.BINARY, name="c_%s" % str(cycle))


model.update()

for v in nodes:
    constraint = []
    for cycle in c:
        if (v in cycle):
            constraint.append(c[cycle])
    if constraint:
        model.addConstr(quicksum( constraint[i] for i in range(len(constraint)) ) <= 1 , name="v%d" % v)

model.setObjective( quicksum( c[cycle] * twoCycles[cycle] for cycle in twoCycles ),
                GRB.MAXIMIZE )

model.optimize()


#####################################################################
## 2-3-way exchanges
#####################################################################

m = Model('2-3 way kidney exchanges')

threeCycles = threeCycle(nodes, connection)
    
c = {}

for cycle in twoCycles:
    c[cycle] = m.addVar(vtype=GRB.BINARY, name="c_%s" % str(cycle))

for cycle in threeCycles:
    c[cycle] = m.addVar(vtype=GRB.BINARY, name="c_%s" % str(cycle))

m.update()

for v in nodes:
    constraint = []
    for cycle in c:
        if (v in cycle):
            constraint.append(c[cycle])
    if constraint:
        m.addConstr(quicksum(constraint[i] for i in range(len(constraint))) <= 1 , name="v%d" % v)

m.setObjective( quicksum(c[cycle] * twoCycles[cycle] for cycle in twoCycles) +
                quicksum(c[cycle] * threeCycles[cycle] for cycle in threeCycles),
                GRB.MAXIMIZE)

m.optimize()

'''
model.write("D:/Documents/CDO/HW3/LinearProgram.lp")
model.write("D:/Documents/CDO/HW3/LinearProgram.mps")
model.write("D:/Documents/CDO/HW3/LinearProgram.sol")
'''