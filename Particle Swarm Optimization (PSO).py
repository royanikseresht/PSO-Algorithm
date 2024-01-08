import numpy as np

def objective_function(x):
    return sum(x**2) # This is an example

def particle_swarm_optimization(objective_function, num_particles, num_dimensions, num_iterations, inertia_weight, cognitive_param, social_param):

    position = np.random.rand(num_particles, num_dimensions)
    velocity = np.random.rand(num_particles, num_dimensions)

    personal_best_position = position.copy()
    personal_best_value = [objective_function(p) for p in position]

    global_best_position = position[np.argmin(personal_best_value)]
    global_best_value = min(personal_best_value)

    for iteration in range(num_iterations):
        for i in range(num_particles):

            velocity[i] = inertia_weight * velocity[i] + cognitive_param * np.random.rand() * (personal_best_position[i] - position[i]) + social_param * np.random.rand() * (global_best_position - position[i])

            position[i] = position[i] + velocity[i]

            fitness = objective_function(position[i])

            if fitness < personal_best_value[i]:
                personal_best_value[i] = fitness
                personal_best_position[i] = position[i]

                if fitness < global_best_value:
                    global_best_value = fitness
                    global_best_position = position[i]

    return global_best_position

# Example usage
best_solution = particle_swarm_optimization(objective_function, num_particles=30, num_dimensions=2, num_iterations=100, inertia_weight=0.5, cognitive_param=1.5, social_param=1.5)
print("Best solution found:", best_solution)
print("Objective function value:", objective_function(best_solution))
