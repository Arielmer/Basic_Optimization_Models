# 📌 Basic Optimization Models

Welcome to the **Basic Optimization Models** repository! This project features three mathematical optimization models designed to tackle **resource allocation, supply chain management, and transportation logistics**. These models are implemented using **Pyomo** and solved with **Gurobi**, demonstrating how mathematical programming can be applied to real-world decision-making problems. 🚀

---

## 📊 Problem Contexts

### 1️⃣ Resource Allocation Optimization 🌱
A farmer has **60 acres of land** and must decide how to divide it between wheat and corn to **maximize profit**, considering constraints on **land availability, labor hours, and fertilizer usage**.

### 2️⃣ Production & Supply Chain Optimization ♻️
A **paper recycling company** needs to **minimize costs** while converting **mixed paper, white office paper, and cardboard** into different types of **paper pulp**. The challenge is to efficiently allocate raw materials while ensuring demand is met.

### 3️⃣ Transportation & Logistics Optimization 🚛
A **coal mining company** operates two mines that produce different grades of coal. The company must determine the **optimal number of operating hours per mine** to **meet demand at the lowest cost**.

These models provide practical decision-making insights for **agriculture, manufacturing, supply chain management, and logistics**. 📦

---

## 🏷 Methodology

### 1️⃣ Resource Allocation Optimization
**Filename:** `resource_allocation_optimization.py`
- **Goal:** Maximize profit from wheat and corn production.
- **Constraints:**
  - **Land Usage**: Cannot exceed 60 acres.
  - **Labor Availability**: Wheat requires 3 hours/acre, corn requires 2 hours/acre, total available is 100 hours.
  - **Fertilizer Limitations**: Wheat needs 2 tons/acre, corn needs 4 tons/acre, total available is 120 tons.
- **Techniques Used:** Linear Programming (LP)

### 2️⃣ Production & Supply Chain Optimization
**Filename:** `recycling_optimization.py`
- **Goal:** Minimize total costs while ensuring sufficient production of paper pulp.
- **Constraints:**
  - **Raw Material Processing Costs & Purchase Costs**.
  - **Yield Ratios for Mixed Paper, White Office Paper, and Cardboard**.
  - **Meeting Demand for Newsprint, Packaging Paper, and Print Stock**.
- **Techniques Used:** Mixed-Integer Linear Programming (MILP)

### 3️⃣ Transportation & Logistics Optimization
**Filename:** `coal_transportation_optimization.py`
- **Goal:** Minimize the operational costs of coal mining while meeting demand for different grades of coal.
- **Constraints:**
  - **Mine 1 and Mine 2 Production Rates**.
  - **Hourly Operational Costs** ($200/hour for Mine 1, $160/hour for Mine 2).
  - **Meeting Demand for High, Medium, and Low-Grade Coal**.
- **Techniques Used:** Linear Programming (LP), Network Flow Optimization

---

## 🛠 Technologies Used
- **Python** 🐍
  - `pyomo` for mathematical modeling
  - `gurobipy` as the solver

---

## 📂 Repository Files
- **`resource_allocation_optimization.py`** – Crop selection problem.
- **`recycling_optimization.py`** – Paper recycling cost minimization.
- **`coal_transportation_optimization.py`** – Coal mining operational cost reduction.
- **`README.md`** – Project documentation.

---

## 🚀 Running the Models
Ensure you have the required dependencies installed:
```sh
pip install pyomo gurobipy
```
Run each script individually:
```sh
python resource_allocation_optimization.py
```