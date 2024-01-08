# Particle Swarm Optimization (PSO) Algorithm

This repository contains a Python implementation of the Particle Swarm Optimization (PSO) algorithm for solving optimization problems. The PSO algorithm is a population-based stochastic optimization technique inspired by the social behavior of birds and fish.

## Overview

The `particle_swarm_optimization.py` file contains a simple implementation of the PSO algorithm for optimizing a user-defined objective function. The algorithm simulates the movement of particles in a swarm through the search space, aiming to find the best solution by updating particle positions and velocities based on their own and global best-known positions.

## Getting Started

To use the PSO algorithm, follow these steps:

1. Install Python 3.x on your machine.
2. Clone this repository to your local machine.
3. Open the `particle_swarm_optimization.py` file and define your objective function under the `objective_function` method.
4. Customize the algorithm parameters such as the number of particles, number of dimensions, number of iterations, inertia weight, cognitive parameter, and social parameter based on your optimization problem.
5. Run the `particle_swarm_optimization.py` file to execute the PSO algorithm and obtain the best solution found.

## Example Usage

Here's an example of how to use the PSO algorithm:

```python
best_solution = particle_swarm_optimization(objective_function, num_particles=30, num_dimensions=2, num_iterations=100, inertia_weight=0.5, cognitive_param=1.5, social_param=1.5)
print("Best solution found:", best_solution)
print("Objective function value:", objective_function(best_solution))
