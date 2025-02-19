# Basic Optimization Models

This repository contains three optimization models implemented using Pyomo and solved with Gurobi. These models illustrate key problem-solving approaches in management science and operations research, tackling challenges related to resource allocation, supply chain management, and transportation logistics. They demonstrate how mathematical modeling and optimization techniques can aid in decision-making to maximize efficiency, minimize costs, and meet resource constraints.

### Problem Contexts

1. **Resource Allocation Optimization**: A farmer owns 60 acres of land and must decide how to divide it between wheat and corn to maximize profit, given constraints on land, labor, and fertilizer.
2. **Production and Supply Chain Optimization**: A paper recycling company must determine the least costly way of converting mixed paper, office paper, and cardboard into different types of pulp while meeting demand constraints.
3. **Transportation and Logistics Optimization**: A coal mining company operates two mines that produce different coal grades. The company must determine the optimal number of operating hours per mine to fulfill demand at the lowest cost.

These models are valuable for decision-makers in agriculture, manufacturing, supply chain management, and logistics.

## Models

### 1. Resource Allocation Optimization
**Filename:** `resource_allocation_optimization.py`

**Problem Statement:** A farmer has 60 acres of land to allocate between wheat and corn. Each crop has different yields, fertilizer usage, and labor requirements. The goal is to maximize profit while ensuring that total land, labor, and fertilizer constraints are not exceeded.

- **Techniques Used:** Linear Programming (LP)
- **Concepts:** Resource Allocation, Optimization in Agriculture

---

### 2. Production and Supply Chain Optimization
**Filename:** `recycling_optimization.py`

**Problem Statement:** A paper recycling company converts raw materials into different types of pulp. Given the purchase costs, processing costs, and recycling yields, the company must determine the least costly way of meeting the required demand for newsprint, packaging, and print stock quality pulp.

- **Techniques Used:** Mixed-Integer Linear Programming (MILP)
- **Concepts:** Supply Chain Optimization, Production Planning, Cost Minimization

---

### 3. Transportation and Logistics Optimization
**Filename:** `coal_transportation_optimization.py`

**Problem Statement:** A mining company operates two mines that produce different coal grades at different rates. Each mine has an associated operating cost. The company needs to fulfill demand for each grade while minimizing operational costs by determining how many hours each mine should be operated per day.

- **Techniques Used:** Linear Programming (LP), Network Flow Optimization
- **Concepts:** Transportation and Logistics, Supply Chain Management

## Dependencies
Ensure you have the required dependencies installed:
```sh
pip install pyomo gurobipy
```

## Running the Models
Each script can be executed individually using Python. For example:
```sh
python resource_allocation_optimization.py
```