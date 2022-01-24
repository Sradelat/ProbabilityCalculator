# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

# TEST 1  # passed??
# prob_calculator.random.seed(95)
# hat = prob_calculator.Hat(blue=3, red=2, green=6)
# probability = prob_calculator.experiment(
#     hat=hat,
#     expected_balls={"blue": 2,
#                     "green": 1},
#     num_balls_drawn=4,
#     num_experiments=1000)  # 1000
# print("Probability", probability)

# TEST 2
# prob_calculator.random.seed(95)
# hat = prob_calculator.Hat(yellow=5, red=1, green=3, blue=9, test=1)
# probability = prob_calculator.experiment(
#     hat=hat,
#     expected_balls={"yellow": 2, "blue": 3, "test": 1},
#     num_balls_drawn=20,  # testing if balls overdrawn. balls must return to contents
#     num_experiments=10)
# print("Probability", probability)  # should be 1.0

# HAT DRAW TEST
# hat = prob_calculator.Hat(red=5, blue=2)
# hat.draw(2)
# print(len(hat.contents))  # step 1: should be 5   step 2: ????   step 3: profit!

# SETUP
# prob_calculator.random.seed(95)
# hat = prob_calculator.Hat(blue=4, red=2, green=6)
# # hat.draw(4)
# probability = prob_calculator.experiment(
#     hat=hat,
#     expected_balls={"blue": 2,
#                     "red": 1},
#     num_balls_drawn=4,
#     num_experiments=3000)
# print("Probability:", probability)

# Run unit tests automatically
# main(module='test_module', exit=False)
