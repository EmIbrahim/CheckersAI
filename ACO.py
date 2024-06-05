# ACO.py
import random

class CheckersACO:
    def __init__(self, x, fit, indexOfBestFit):
        self.r = random.Random()

        self.d = 171  # Dimension of problem to be solved.
        self.s = 40   # Number of ants.

        self.x = x[:]  # Positions (solutions).
        self.fitness = fit[:]  # Fitness values.

        self.index = indexOfBestFit

        self.best_solution = self.x[self.index][:]  # Best solution found.
        self.best_fitness = self.fitness[self.index]  # Fitness of best solution.

        self.pheromones = [[1.0 for _ in range(self.d)] for _ in range(self.s)]  # Initial pheromone levels.

        # Parameters for ACO
        self.alpha = 5.0  # Influence of pheromone
        self.beta = 5.0   # Influence of heuristic information
        self.evaporation_rate = 0.9  # Pheromone evaporation rate
        self.Q = 100.0    # Pheromone intensity

    # Update the pheromones based on the fitness values.
    def updatePheromones(self):
        # Evaporate pheromones
        for i in range(self.s):
            for j in range(self.d):
                self.pheromones[i][j] *= (1 - self.evaporation_rate)

        # Deposit new pheromones based on fitness
        for i in range(self.s):
            for j in range(self.d):
                if self.fitness[i] >= self.best_fitness:
                    self.pheromones[i][j] += self.Q / (1.0 + self.fitness[i])

    # Generate new solutions based on pheromones and update positions.
    def updatePositions(self):
        for i in range(self.s):
            for j in range(self.d):
                # Probability calculation using pheromone and heuristic information
                tau = self.pheromones[i][j]
                heuristic_info = 1.0 / (1.0 + self.best_fitness)  # Heuristic information as inverse of best fitness
                numerator = (tau ** self.alpha) * (heuristic_info ** self.beta)
                denominator = sum((self.pheromones[i][k] ** self.alpha) * (heuristic_info ** self.beta) for k in range(self.d))
                if denominator == 0:  # Avoid division by zero
                    probability = 0
                else:
                    probability = numerator / denominator

                prob_exploit = probability
                prob_explore = 1.0 - prob_exploit

                # Determine whether to exploit or explore
                if self.r.random() < prob_exploit:
                    self.x[i][j] = self.best_solution[j]  # Exploit
                else:
                    self.x[i][j] = self.r.random()  # Explore

                # Ensure the values are appropriately rounded
                self.x[i][j] = round(self.x[i][j], 10)
                if self.r.random() < prob_exploit:
                    self.x[i][j] = self.best_solution[j]  # Exploit
                else:
                    self.x[i][j] = self.r.random()  # Explore
                self.x[i][j] = round(self.x[i][j], 10)

    # Update the best solution found so far.
    def updateBestSolution(self):
        print("Length of fitness list:", len(self.fitness))
        for i in range(self.s):
            if self.fitness[i] >= self.best_fitness:
                self.best_fitness = self.fitness[i]
                self.best_solution = self.x[i][:]
