# Checkers AI
#
# Table of Contents
* Project Structure
* How to Run
* Usage of Classes
* Contributions

#

##
# Project Structure
* ACO.py: Initializes values needed for ACO and calculates probabilities.
* ACOTrainer.py: Trains values by playing several thousand matches between NN and NN.
* NeuralNetwork.py: Handles the functionality of the Neural Network, including feed-forward operations and weight calculations.
* CheckersV4.py: The core component of the project, encompassing functions for the main logic, including Minimax implementation, move calculations, gameplay simulation, and more.
* GUI.py: Manages the graphical user interface for AI vs. Human gameplay, allowing users to choose which AI algorithm they want to play against.
* superplayer.txt: Stores weights of the best network after an ACO trainer iteration.

#
# How to Run
* Training the Neural Network:
Run ``` ACOTrainer.py``` to train the neural network using ACO. This will involve playing several thousand (10,000) matches between neural network instances to optimize their weights.

* Simulating AI Matches:
Use ```CheckersV4.py``` to simulate matches between the Neural Network and the Minimax algorithm. This script contains the primary logic and functions for simulating AI gameplay. To find your way to simulate, go to the end of the code and uncomment the last part. Fix n (no. of games) to however much games you want to simulate and run.

* Playing Against the AI:
Execute ```GUI.py``` to start the graphical user interface for human vs. AI gameplay. Choose the AI algorithm (Neural Network(NN) or Minimax (MM)) you wish to compete against from the interface.


##
# Detailed File Descriptions
* ACO.py
>ACO.py is the foundational script for initializing the parameters required for the Ant Colony Optimization (ACO) algorithm. Key aspects include:

Setting the dimension of the problem.
Initializing the number of ants.
Defining alpha, beta, evaporation rate, and pheromone intensity.
Preparing the pheromone matrix and heuristic information.
This file doesn't perform any standalone tasks but serves as the basis for the ACO process used in training the neural network.

* ACOTrainer.py
>ACOTrainer.py is the execution script for training the neural network via ACO. 

It:

Runs multiple iterations of the ACO algorithm.
Simulates games between neural network instances.
Updates the pheromone matrix based on the fitness of the solutions.
Stores the best-performing weights in superplayer.txt.
Running this file repeatedly refines the neural network to improve its performance in gameplay scenarios.

* NeuralNetwork.py
>NeuralNetwork.py encompasses the neural network's architecture and functionalities 

such as:

Initializing network parameters (weights and biases).
Implementing the feed-forward mechanism.
Calculating output values based on input moves.
Updating weights based on training outcomes from ACO.
This script is integral to the AI's decision-making process during gameplay.

* CheckersV4.py
>CheckersV4.py is the core logic file of the project. 

It includes:

Implementation of the Minimax algorithm with Alpha-Beta Pruning for optimal move calculation.
Functions to evaluate game states and calculate possible moves.
Logic for simulating complete games between AI instances (NN vs. MM).
Comprehensive methods for move execution, state updates, and victory condition checks.
This script is vital for simulating AI matches and determining the efficiency of the algorithms.

* GUI.py
>GUI.py provides the graphical user interface for the project. It allows users to:
Play games against the AI (either NN or MM).
Visualize the board and moves.
Choose the preferred AI opponent.
Running this file engages the user in an interactive checkers game against the chosen AI.

* superplayer.txt
>superplayer.txt is a text file that stores the weights of the best-performing neural network after training iterations via ACO. These weights are used to initialize the neural network for subsequent games, ensuring that the AI utilizes the most optimized parameters.



# Contributions:

* https://www.researchgate.net/publication/3418658_Evolving_an_Expert_Checkers_Playing_Program_without_Using_Human_Expertise
* https://link.springer.com/chapter/10.1007/978-3-7908-1833-8_2
* https://www.researchgate.net/publication/342849109_Study_of_Artificial_Intelligence_into_Checkers_Game_using_HTML_and_JavaScript
* https://www.researchgate.net/publication/3302690_Evolving_neural_networks_to_play_checkers_without_expert_knowledge

