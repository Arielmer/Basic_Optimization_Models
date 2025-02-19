from gurobipy import *
from pyomo.environ import *

# Establish model for recycling process
model = ConcreteModel(name='recycle')

# Decision Variables: How much of each raw material is used to produce different paper types
model.x = Var(['M', 'W', 'C'], ['N', 'P', 'S'], domain=NonNegativeReals)

# Objective Function: Minimize total costs (purchase + processing)
model.obj = Objective(expr=sum(16*model.x['M',j] + 19*model.x['W',j] + 17*model.x['C',j] +
                               9.75*model.x['M','N'] + 12.25*model.x['M','P'] + 9.50*model.x['M','S'] +
                               4.75*model.x['W','N'] + 7.75*model.x['W','P'] + 8.50*model.x['W','S'] +
                               7.50*model.x['C','N'] + 8.50*model.x['C','P'] for j in ['N', 'P', 'S']),
                        sense=minimize)

# Demand Constraints: Ensure production meets demand for each type of paper
model.demand_N = Constraint(expr=0.9*model.x['M','N'] + 0.9*model.x['W','N'] + 0.8*model.x['C','N'] >= 300)
model.demand_P = Constraint(expr=0.8*model.x['M','P'] + 0.85*model.x['W','P'] + 0.7*model.x['C','P'] >= 400)
model.demand_S = Constraint(expr=0.7*model.x['M','S'] + 0.8*model.x['W','S'] >= 200)

# Solve model
SolverFactory('gurobi').solve(model).write()

# Display solution
print('\nTotal Cost = ', model.obj())
print('Decision Variables:', model.x.pprint())
