from gurobipy import *
from pyomo.environ import *

# Create a model for coal transportation optimization
model = ConcreteModel(name='coal')

# Decision Variables: Hours of operation for each mine
model.x = Var(['M1', 'M2'], domain=NonNegativeReals)

# Objective Function: Minimize total operational cost
model.obj = Objective(expr=200 * model.x['M1'] + 160 * model.x['M2'], sense=minimize)

# Constraints:
# Ensure enough coal is produced to meet demand
model.demand_H = Constraint(expr=6 * model.x['M1'] + 2 * model.x['M2'] >= 12)  # High-grade coal
model.demand_M = Constraint(expr=2 * model.x['M1'] + 2 * model.x['M2'] >= 8)   # Medium-grade coal
model.demand_L = Constraint(expr=4 * model.x['M1'] + 8 * model.x['M2'] >= 24)  # Low-grade coal

# Solve the model
SolverFactory('gurobi').solve(model).write()

# Display solution
print('\nTotal Cost = ', model.obj())
print('Mine 1 hours = ', model.x['M1']())
print('Mine 2 hours = ', model.x['M2']())
