import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents += value * [key]
        # have a copy initialized so that whenever the draw method is called the
        # contents list is refreshed
        self.contents_copy = copy.deepcopy(self.contents)

    def draw(self, num_of_balls):
        selected_balls = []
        # always prefer making a deep copy over shallow copy.
        # whenever the draw method is called we have to draw from
        # the full sample size so update contents to be the original sample size
        self.contents = copy.deepcopy(self.contents_copy)
        if num_of_balls >= len(self.contents):
            return self.contents
        for i in range(num_of_balls):
            random_ball = random.choice(self.contents)
            self.contents.remove(random_ball)
            selected_balls.append(random_ball)
        return selected_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_outcomes = 0
    for i in range(num_experiments):
        drawn_balls = hat.draw(num_balls_drawn)
        # check if at least all the balls in the expected_balls is present
        # in the drawn_balls list.
        if all(
            [
                expected_balls[ball] <= drawn_balls.count(ball)
                for ball in expected_balls.keys()
            ]
        ):
            expected_outcomes += 1
    # return probability
    return expected_outcomes / num_experiments


if __name__ == "__main__":
    # hat = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    # print(hat.draw(9))
    # print(hat.contents)
    # hat = Hat(black=6, red=4, green=3)
    # probability = experiment(
    #     hat=hat,
    #     expected_balls={"red": 2, "green": 1},
    #     num_balls_drawn=5,
    #     num_experiments=2000,
    # )
    # * main tests from freecodecamp
    # hat = Hat(blue=3, red=2, green=6)
    # probability = experiment(
    #     hat=hat,
    #     expected_balls={"blue": 2, "green": 1},
    #     num_balls_drawn=4,
    #     num_experiments=1000,
    # )
    # print(probability)
    # print(hat.draw(4))
    # print(hat.contents)

    hat = Hat(blue=4, red=2, green=6)
    probability = experiment(
        hat=hat,
        expected_balls={"blue": 2, "red": 1},
        num_balls_drawn=4,
        num_experiments=3000,
    )
    print("Probability:", probability)
