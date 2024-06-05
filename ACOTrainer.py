from CheckersV4 import Checkers
from NeuralN import NeuralNetwork
from ACO import CheckersACO
import random
import time

class Train:
    def __init__(self, p=None):
        self.p_size = 50
        self.players = [NeuralNetwork() for _ in range(self.p_size)]
        if p is not None:
            for i in range(len(p)):
                try:
                    self.players[i].updateWeights(p[i])
                except:
                    print("indexissue")
        self.fitness = [0 for _ in range(self.p_size)]
        self.r = random.Random()

    # Calculates the fitness of all players in population by playing a number of games vs random opponents.
    def calculateFitness(self):
        opponents = self.r.sample(range(self.p_size), 15)
        for j in range(self.p_size):
            fit = 0
            for i in opponents:
                game = Checkers(True)
                result = game.gameTestNN(False, self.players[j], self.players[i])
                if result == 'w':
                    fit += 1
                elif result == 'b':
                    fit -= 2
                else:
                    fit += 0
            self.fitness[j] = fit

    # Trains the players and returns the player with the best fitness.
    def obtainBestPlayer(self):
        print("\nInitialising.")
        self.calculateFitness()
        indx_of_Best = Checkers.indxOfMax(self.fitness)
        x = [self.players[j].weightVector() for j in range(self.p_size)]
        aco = CheckersACO(x[:], self.fitness[:], indx_of_Best)
        print("Training")
        for i in range(500):
            print("I" + str(i + 1) + " ", end='', flush=True)

            print("\n--------- Before Updates ---------")
            print("particles", aco.x)
            print("current fitness", self.fitness)
            print("best fitness", aco.best_fitness)
            print("global best", aco.best_solution, "at index", aco.index)

            aco.updatePheromones()
            aco.updatePositions()

            for i in range(self.p_size):
                self.players[i].updateWeights(aco.x[i])

            print("\n--------- After Updates ---------")
            print("particles", aco.x)
            print("current fitness", self.fitness)
            print("best fitness", aco.best_fitness)
            print("global best", aco.best_solution, "at index", aco.index)

            self.calculateFitness()
            aco.updateBestSolution()
        print("\n")
        return aco.best_solution

    # Test the player with the best fitness on its win rate.
    def testPlayerWhite(self, player):
        winw, winb, draw = 0, 0, 0
        for _ in range(10000):
            game = Checkers(True)
            result = game.gameTestNN_White(False, player)
            if result == 'w':
                winw += 1
            elif result == 'b':
                winb += 1
            else:
                draw += 1
        print("white win", winw, "black win", winb, "draw", draw)
        return winw / 100

    # Test the player with the best fitness on its win rate.
    def testPlayerBlack(self, player):
        winw, winb, draw = 0, 0, 0
        for _ in range(10000):
            game = Checkers(True)
            result = game.gameTestNN_Black(False, player)
            if result == 'w':
                winw += 1
            elif result == 'b':
                winb += 1
            else:
                draw += 1
        print("white win", winw, "black win", winb, "draw", draw)
        return winb / 100

    def weightVectorToString(self, arr):
        return ",".join(map(str, arr))

    # Runs the training and checks said players win rate.
    def runner(self):
        start = time.time()

        best_player_weights = self.obtainBestPlayer()
        best_player = NeuralNetwork()
        best_player.updateWeights(best_player_weights)

        win_rate_w = self.testPlayerWhite(best_player)
        win_rate_b = self.testPlayerBlack(best_player)
        end = time.time()
        print("White win percentage", win_rate_w, "Black win percentage", win_rate_b)
        print("Time taken %.2f" % (end - start))
        with open("superPlayer.txt", 'a') as f:
            f.write(f"{win_rate_w},{win_rate_b},{self.weightVectorToString(best_player_weights)}\n")


def getPlayers():
    output = []
    with open("bestPlayers.txt", "r") as fp:
        for line in fp:
            player_weights = line.strip().split(",")[2:]  # Extract player weights
            player_weights = [float(weight) for weight in player_weights if weight]  # Convert to float
            output.append(player_weights)
    return output

for i in range(1):
    print("Iteration", i)
    players = getPlayers()
    tester = Train(players)
    tester.runner()
