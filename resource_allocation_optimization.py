from gurobipy import *
from pyomo.environ import *

# Create a model for land allocation
model = ConcreteModel()

# Decision Variables: Acres allocated to wheat and corn
model.w = Var(domain=NonNegativeReals)  # Acres of wheat
model.c = Var(domain=NonNegativeReals)  # Acres of corn

# Objective Function: Maximize profit
# Wheat generates $200 per acre, Corn generates $300 per acre
model.profit = Objective(expr=200 * model.w + 300 * model.c, sense=maximize)

# Constraints:
# Land Constraint: Total land used cannot exceed 60 acres
model.land = Constraint(expr=model.w + model.c <= 60)

# Labor Constraint: Each acre of wheat requires 3 hours, corn requires 2 hours. Total available: 100 hours
model.time = Constraint(expr=3 * model.w + 2 * model.c <= 100)

# Fertilizer Constraint: Each acre of wheat needs 2 tons, corn needs 4 tons. Total available: 120 tons
model.fertilizer = Constraint(expr=2 * model.w + 4 * model.c <= 120)

# Solve the model
SolverFactory('gurobi').solve(model).write()

# Display solution
print('\nProfit = ', model.profit())
print('Wheat acres = ', model.w())
print('Corn acres = ', model.c())