import math
import random

class NeuralNetwork:

    def __init__(self):
        self.inputSize = 33
        self.hiddenSize = 6

        self.inputNodes = []
        self.hiddenNodes = [-1 for _ in range(self.hiddenSize)]
        self.output = 0

        self.weights_ItoH = [0 for _ in range(self.inputSize)]
        self.weights_HtoO = []

        self._initWeights()  # Call _initWeights method directly without name mangling

    def _initWeights(self):
        rand = random.Random()

        for i in range(self.inputSize):
            self.weights_ItoH[i] = [rand.random() for _ in range(5)]  # Initialize floats

        self.weights_HtoO = [rand.random() for _ in range(self.hiddenSize)]  # Initialize floats

        for i in range(self.inputSize):
            for j in range(5):
                if rand.random() > 0.5:
                    self.weights_ItoH[i][j] = -self.weights_ItoH[i][j]

        for i in range(self.hiddenSize):
            if rand.random() > 0.5:
                self.weights_HtoO[i] = -self.weights_HtoO[i]



    def weightVector(self):
        output = sum(self.weights_ItoH, []) + self.weights_HtoO
        return output


    def updateWeights(self, w_vector):
        i = 0
        for j in range(len(self.weights_ItoH)):
            for k in range(len(self.weights_ItoH[0])):
                self.weights_ItoH[j][k] = float(w_vector[i])  # Convert to float
                i += 1
        for j in range(len(self.weights_HtoO)):
            self.weights_HtoO[j] = float(w_vector[i])  # Convert to float
            i += 1



    def calculateHiddenNodes(self):
        for i in range(1, 6):
            sum = 0.0
            for j in range(33):
                sum += self.inputNodes[j]*self.weights_ItoH[j][i-1]
            sum = round(sum, 10)
            try:
                self.hiddenNodes[i] = self.sigmoid(sum)
            except:
                print(sum)

    def calculateOutputNode(self):
        sum = 0.0
        for i in range(self.hiddenSize):
            sum += self.hiddenNodes[i]*self.weights_HtoO[i]
        sum = round(sum, 10)
        self.output = self.sigmoid(sum)

    def sigmoid(self, val):
        return (1.0 / (1.0 + math.exp(-val)))

    # Coverts the pieces on the board to different values. White player is type 1. Black player is type -1.
    @staticmethod
    def convertBoardValues(board, player_type):
        conversion = [0.5 for i in range(len(board))]
        for i in range(len(board)):
            if player_type == -1:
                conversion[i] = board[i]*-1
            else:
                conversion[i] = board[i]
        return conversion

    # inV is an array of size 32 containing the board positions of the checkers board.
    # Evaluates and Returns the score for a given game board.
    def feedForward(self, inV):
        self.inputNodes = [1.0] + [float(val) for val in inV]  # Convert to floats
        self.calculateHiddenNodes()
        self.calculateOutputNode()
        return self.output
