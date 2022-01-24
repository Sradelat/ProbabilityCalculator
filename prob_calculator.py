import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = []  # balls in hat
        for k, v in kwargs.items():  # adding called number of colored balls to hat
            for color in range(v):
                self.contents.append(k)

    def draw(self, num_balls_drawn):
        drawn_balls = []
        if num_balls_drawn > len(self.contents):  # return all balls if draw exceeds contents
            return self.contents
        else:
            for ball in range(num_balls_drawn):
                random_ball = self.contents.pop(random.randrange(len(self.contents)))  # remove rand ball from contents
                drawn_balls.append(str(random_ball))  # add rand ball to new list
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for x in range(num_experiments):
        hat_copy = copy.deepcopy(hat)                         # need new copies every experiment otherwise contents of
        expected_copy = copy.deepcopy(expected_balls)         # the hat will run dry after a few draws
        balls_drawn = hat_copy.draw(num_balls_drawn)  # draw from a new copy every time - not actual
        count = 0
        for color in balls_drawn:
            if color in expected_copy:
                expected_copy[color] += -1  # removing one from expected color if iteration color matches
        for color in expected_copy.values():  # checking each condition in expected balls and counting for later
            if color <= 0:
                count += 1
        if count == len(expected_copy):  # if each condition is met within expected balls
            success += 1

    probability = int(success) / num_experiments  # calculate probability

    return probability
